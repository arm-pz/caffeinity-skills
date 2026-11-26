#!/usr/bin/env node
// Checks the dynamic workflow scripts in plugins/caffeinity/workflows/ without spending a token.
//
//   node scripts/check_workflows.mjs            check every workflow
//   node scripts/check_workflows.mjs launch-safely
//
// For each script it checks the rules Claude Code applies when it loads one (meta first and a pure
// literal with name and description, meta.name matching the file, phase titles matching meta.phases,
// no import(), Date.now(), Math.random() or argless new Date()), then dry-runs the body twice with
// stub agents: once where every step finishes, once where every step stops at its gate. It prints the
// agents each run would start, with their model, so a change that adds Opus calls shows up here.
// A dry run proves the control flow, not the skills: the first real run is still the test of those.

import { readFileSync, readdirSync } from 'node:fs'
import { join, dirname, basename } from 'node:path'
import { fileURLToPath } from 'node:url'

const ROOT = join(dirname(fileURLToPath(import.meta.url)), '..')
const DIR = join(ROOT, 'plugins', 'caffeinity', 'workflows')

// Arguments for the "every step finishes" dry run. A workflow with no entry runs with {}.
const DRY_ARGS = {
  'launch-safely': { url: 'https://staging.example.com', source: '.', isolatedEnv: 'http://localhost:3000' },
  'build-a-skill': { idea: 'a skill that drafts release notes', confirmed: { purpose: 'x', triggers: ['y'] } },
  'get-found': { repo: 'arm-pz/example', what: 'an example skill', site: 'https://skillsmith.tech' },
  'grow-search-traffic': { site: 'https://example.com', queries: ['example query'] },
  'land-a-job': { resume: 'resume.pdf', jobDescription: 'jd.md' },
  'decision-memo': { question: 'Should we build or buy?' },
  'learn-any-topic': { topic: 'Rust ownership', level: 'beginner' },
  'run-cold-outbound': { leadList: 'leads.csv', icp: 'small agencies', monthlySends: 3000, offer: 'audit', audience: 'agency owners' },
  'launch-a-product': { skills: 'backend dev', time: '10h a week', budget: '$200' },
  'maintain-skills': { clones: '~/skills' },
  'audit-agent-skills': { owner: 'arm-pz', clones: '~/skills' },
  'set-up-a-coding-agent': { repo: '.' },
}

function fail(name, msg) {
  console.log(`FAIL ${name}: ${msg}`)
  return false
}

// Returns the text of the object literal that starts at `start` (an opening brace).
function braceSpan(src, start) {
  let depth = 0
  let quote = null
  for (let i = start; i < src.length; i++) {
    const c = src[i]
    if (quote) {
      if (c === '\\') i++
      else if (c === quote) quote = null
      continue
    }
    if (c === "'" || c === '"' || c === '`') quote = c
    else if (c === '{') depth++
    else if (c === '}' && --depth === 0) return src.slice(start, i + 1)
  }
  return null
}

// A fake value shaped like the JSON schema an agent() call asked for.
function fake(schema, mode) {
  if (!schema) return 'stub output'
  if (schema.enum) {
    if (mode === 'stop' && schema.enum.includes('stopped')) return 'stopped'
    if (mode === 'stop' && schema.enum.includes('HOLD')) return 'HOLD'
    return schema.enum[0]
  }
  switch (schema.type) {
    case 'object': {
      const o = {}
      for (const [k, v] of Object.entries(schema.properties || {})) o[k] = fake(v, mode)
      return o
    }
    case 'array': return []
    case 'number': case 'integer': return 0
    case 'boolean': return mode === 'stop'
    default: return 'stub'
  }
}

async function dryRun(body, args, mode) {
  const calls = []
  const phases = []
  const agent = async (prompt, opts = {}) => {
    if (typeof prompt !== 'string' || !prompt.trim()) throw new Error('agent() called with an empty prompt')
    calls.push({ label: opts.label || prompt.slice(0, 40), model: opts.model || 'inherit', effort: opts.effort || 'inherit' })
    return fake(opts.schema, mode)
  }
  const parallel = async thunks => Promise.all(thunks.map(t => t().catch(() => null)))
  const pipeline = async (items, ...stages) => Promise.all(items.map(async (item, i) => {
    let v = item
    try { for (const s of stages) v = await s(v, item, i) } catch { return null }
    return v
  }))
  const workflow = async name => ({ workflow: name, status: 'stub child run' })
  const budget = { total: null, spent: () => 0, remaining: () => Infinity }
  const AsyncFunction = (async () => {}).constructor
  const fn = new AsyncFunction('agent', 'parallel', 'pipeline', 'phase', 'log', 'args', 'budget', 'workflow', body)
  const result = await fn(agent, parallel, pipeline, t => phases.push(t), () => {}, args, budget, workflow)
  return { calls, phases, result }
}

async function check(file) {
  const name = basename(file, '.js')
  const src = readFileSync(file, 'utf8')
  const m = /^\s*export const meta\s*=\s*/.exec(src)
  if (!m) return fail(name, 'the first statement must be `export const meta = {...}`')
  const metaText = braceSpan(src, m[0].length)
  if (!metaText) return fail(name, 'meta object is not closed')
  const metaCode = metaText.replace(/'(?:\\.|[^'\\])*'|"(?:\\.|[^"\\])*"/g, "''")
  if (/\.\.\.|`|\(/.test(metaCode)) return fail(name, 'meta must be a pure literal: no spreads, templates or calls')
  let meta
  try { meta = Function(`"use strict"; return (${metaText})`)() } catch (e) { return fail(name, `meta does not parse: ${e.message}`) }
  if (!meta.name || !meta.description) return fail(name, 'meta needs a name and a description')
  if (meta.name !== name) return fail(name, `meta.name is "${meta.name}" but the file is ${name}.js`)

  const body = src.slice(m[0].length + metaText.length)
  for (const [re, what] of [[/\bimport\s*\(/, 'import()'], [/Date\.now\s*\(/, 'Date.now()'],
    [/Math\.random\s*\(/, 'Math.random()'], [/new Date\(\s*\)/, 'argless new Date()']]) {
    if (re.test(body)) return fail(name, `${what} is not allowed in a workflow script`)
  }

  const metaPhases = (meta.phases || []).map(p => p.title)
  const called = [...body.matchAll(/phase\(\s*'([^']+)'\s*\)/g)].map(x => x[1])
  const unlisted = called.filter(t => !metaPhases.includes(t))
  if (unlisted.length) return fail(name, `phase() titles missing from meta.phases: ${unlisted.join(', ')}`)
  const unused = metaPhases.filter(t => !called.includes(t))
  if (unused.length) return fail(name, `meta.phases titles never passed to phase(): ${unused.join(', ')}`)

  let ok
  let empty
  let stopped
  try {
    ok = await dryRun(body, DRY_ARGS[name] || {}, 'done')
    empty = await dryRun(body, undefined, 'done')
    stopped = await dryRun(body, DRY_ARGS[name] || {}, 'stop')
  } catch (e) {
    return fail(name, `dry run threw: ${e.message}`)
  }
  for (const [label, run] of [['finishes', ok], ['no args', empty], ['stops at a gate', stopped]]) {
    if (run.result === undefined) return fail(name, `dry run (${label}) returned nothing`)
  }
  if (empty.calls.length) return fail(name, 'with no args it should ask for input before starting any agent')

  const models = ok.calls.reduce((acc, c) => ({ ...acc, [c.model]: (acc[c.model] || 0) + 1 }), {})
  const mix = Object.entries(models).map(([k, v]) => `${v} ${k}`).join(', ')
  console.log(`ok   ${name}: ${ok.calls.length} agents when every step finishes (${mix}); ${stopped.calls.length} when steps stop at their gates`)
  return true
}

const only = process.argv[2]
const files = readdirSync(DIR).filter(f => f.endsWith('.js') && (!only || f === `${only}.js`)).map(f => join(DIR, f))
if (!files.length) {
  console.log(only ? `no workflow named ${only}` : 'no workflows found')
  process.exit(1)
}
let failed = 0
for (const f of files) if (!(await check(f))) failed++
console.log(failed ? `${failed} of ${files.length} workflows failed` : `${files.length} workflows ok`)
process.exit(failed ? 1 : 0)
