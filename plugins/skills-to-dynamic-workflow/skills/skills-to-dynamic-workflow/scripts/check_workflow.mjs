#!/usr/bin/env node
// Checks Claude Code dynamic workflow scripts without spending a token.
//
//   node check_workflow.mjs path/to/workflow.js
//   node check_workflow.mjs plugins/my-plugin/workflows            every .js in a folder
//   node check_workflow.mjs review-a-pr.js --args '{"pr": 12}'      args for the "finishes" dry run
//   node check_workflow.mjs workflows --args-file dry-args.json     {"<meta.name>": {...args}, ...}
//   node check_workflow.mjs review-a-pr.js --stub '{"verdict": "blocking"}'
//                                   force a field in every stub result, to walk a branch that
//                                   depends on what an agent returned (the stubs return "stub")
//
// For each script it checks the rules Claude Code applies when it loads one: meta is the first
// statement, a pure literal with a name and a description, meta.name is lowercase-hyphenated and
// matches the file name, and the body has no import(), Date.now(), Math.random() or argless
// new Date(). Then it dry-runs the body three times with stub agents: once where every step
// finishes, once with no args, once where every step stops at its gate. Every schema handed to
// agent() is checked the way the runtime checks it, every phase is checked against meta.phases,
// and it prints how many agents each run would start and on which model, so a change that adds
// Opus calls or crosses the 25-agent "Large workflow" warning shows up here.
//
// A dry run proves the control flow, not the skills. The first real run is still the test of those.
// Exit code: 0 when every script passes (warnings allowed), 1 otherwise.

import { readFileSync, readdirSync, statSync } from 'node:fs'
import { join, basename, resolve } from 'node:path'

const LARGE = 25

function usage(msg) {
  if (msg) console.error(msg)
  console.error('usage: node check_workflow.mjs <file.js|dir>... [--args JSON] [--args-file FILE] [--stub JSON]')
  process.exit(2)
}

// Returns the text of the object literal that starts at `start` (an opening brace).
export function braceSpan(src, start) {
  let depth = 0
  let quote = null
  for (let i = start; i < src.length; i++) {
    const c = src[i]
    if (quote) {
      if (c === '\\') i++
      else if (c === quote) quote = null
      continue
    }
    if (c === '/' && src[i + 1] === '/') { i = src.indexOf('\n', i); if (i < 0) return null; continue }
    if (c === '/' && src[i + 1] === '*') { i = src.indexOf('*/', i + 2) + 1; if (i <= 0) return null; continue }
    if (c === "'" || c === '"' || c === '`') quote = c
    else if (c === '{') depth++
    else if (c === '}' && --depth === 0) return src.slice(start, i + 1)
  }
  return null
}

// Strips comments and string contents so the rule checks only see code.
function codeOnly(src) {
  let out = ''
  let quote = null
  for (let i = 0; i < src.length; i++) {
    const c = src[i]
    if (quote) {
      if (c === '\\') { i++; continue }
      if (c === quote) { quote = null; out += c }
      continue
    }
    if (c === '/' && src[i + 1] === '/') { const j = src.indexOf('\n', i); i = j < 0 ? src.length : j - 1; continue }
    if (c === '/' && src[i + 1] === '*') { const j = src.indexOf('*/', i + 2); i = j < 0 ? src.length : j + 1; continue }
    if (c === "'" || c === '"' || c === '`') quote = c
    out += c
  }
  return out
}

// The checks the runtime makes on an agent() schema before it starts the agent.
export function schemaProblem(schema, path = 'schema') {
  if (schema === undefined) return null
  if (!schema || typeof schema !== 'object') return `${path} is not an object`
  if (path === 'schema' && (schema.type !== 'object' || !schema.properties)) {
    return 'schema needs {type: "object", properties: {...}} at its root'
  }
  if (schema.type === 'object' && schema.properties) {
    const props = Object.keys(schema.properties)
    for (const r of schema.required || []) {
      if (!props.includes(r)) {
        return schema.additionalProperties === false
          ? `${path}: required key "${r}" is ruled out by additionalProperties: false`
          : `${path}: required key "${r}" is not in properties`
      }
    }
    for (const [k, v] of Object.entries(schema.properties)) {
      const p = schemaProblem(v, `${path}.${k}`)
      if (p) return p
    }
  }
  if (schema.type === 'array' && schema.items) return schemaProblem(schema.items, `${path}[]`)
  return null
}

// A fake value shaped like the JSON schema an agent() call asked for.
let STUB = {}

function fake(schema, mode, top = true) {
  if (!schema) return 'stub output'
  if (schema.enum) {
    for (const stop of ['stopped', 'HOLD', 'blocked', 'fail']) {
      if (mode === 'stop' && schema.enum.includes(stop)) return stop
    }
    return schema.enum[0]
  }
  switch (schema.type) {
    case 'object': {
      const o = {}
      // Outward actions would stop every chain at its first step, so the stubs never propose any.
      for (const [k, v] of Object.entries(schema.properties || {})) {
        o[k] = k === 'proposedActions' ? [] : top && k in STUB ? STUB[k] : fake(v, mode, false)
      }
      return o
    }
    case 'array': return mode === 'done' ? [fake(schema.items, mode, false)] : []
    case 'number': case 'integer': return 0
    case 'boolean': return mode === 'stop'
    default: return 'stub'
  }
}

async function dryRun(body, args, mode) {
  const calls = []
  const phases = []
  const problems = []
  const agent = async (prompt, opts = {}) => {
    if (typeof prompt !== 'string' || !prompt.trim()) throw new Error('agent() called with an empty prompt')
    const p = schemaProblem(opts.schema)
    if (p) problems.push(`${opts.label || prompt.slice(0, 40)}: ${p}`)
    if (opts.isolation !== undefined && opts.isolation !== 'worktree') problems.push(`isolation must be 'worktree', got ${JSON.stringify(opts.isolation)}`)
    if (opts.phase) phases.push(opts.phase)
    calls.push({ label: opts.label || prompt.slice(0, 40), model: opts.model || 'session model', effort: opts.effort || 'default' })
    return fake(opts.schema, mode)
  }
  const parallel = async thunks => {
    if (!Array.isArray(thunks)) throw new Error('parallel() takes an array of () => Promise thunks')
    if (thunks.some(t => typeof t !== 'function')) throw new Error('parallel() items must be functions, not promises')
    return Promise.all(thunks.map(t => Promise.resolve().then(t).catch(() => null)))
  }
  const pipeline = async (items, ...stages) => {
    if (!Array.isArray(items)) throw new Error('pipeline() takes an array of items first')
    if (stages.some(s => typeof s !== 'function')) throw new Error('pipeline() stages must be functions')
    return Promise.all(items.map(async (item, i) => {
      let v = item
      try { for (const s of stages) v = await s(v, item, i) } catch { return null }
      return v
    }))
  }
  const workflow = async name => ({ workflow: typeof name === 'string' ? name : 'script', status: mode === 'stop' ? 'stopped_at_gate' : 'done' })
  const budget = { total: null, spent: () => 0, remaining: () => Infinity }
  const AsyncFunction = (async () => {}).constructor
  const fn = new AsyncFunction('agent', 'parallel', 'pipeline', 'phase', 'log', 'args', 'budget', 'workflow', body)
  const result = await fn(agent, parallel, pipeline, t => phases.push(t), () => {}, args, budget, workflow)
  return { calls, phases, problems, result }
}

function mix(calls) {
  const by = {}
  for (const c of calls) by[c.model] = (by[c.model] || 0) + 1
  return Object.entries(by).map(([k, v]) => `${v} ${k}`).join(', ') || 'none'
}

export async function check(file, dryArgs) {
  const name = basename(file, '.js')
  const errors = []
  const warnings = []
  const out = { name, file, errors, warnings, summary: '' }
  const src = readFileSync(file, 'utf8')

  const m = /^(?:\s|\/\/[^\n]*\n|\/\*[\s\S]*?\*\/)*export const meta\s*=\s*/.exec(src)
  if (!m) { errors.push('the first statement must be `export const meta = {...}`'); return out }
  const metaText = braceSpan(src, m[0].length)
  if (!metaText) { errors.push('meta object is not closed'); return out }
  const metaCode = codeOnly(metaText)
  if (/\.\.\.|`|\(|\b[A-Za-z_$][\w$]*\s*[,}\n]/.test(metaCode.replace(/\b(true|false|null)\b/g, '').replace(/[\w$]+\s*:/g, ':'))) {
    errors.push('meta must be a pure literal: no variables, spreads, templates or calls')
    return out
  }
  let meta
  try { meta = Function(`"use strict"; return (${metaText})`)() } catch (e) { errors.push(`meta does not parse: ${e.message}`); return out }
  if (!meta.name || !meta.description) errors.push('meta needs a name and a description')
  if (meta.name && !/^[a-z0-9]+(-[a-z0-9]+)*$/.test(meta.name)) errors.push(`meta.name "${meta.name}" should be lowercase words joined by hyphens`)
  if (meta.name && meta.name !== name) errors.push(`meta.name is "${meta.name}" but the file is ${name}.js`)
  if (meta.description && /\n/.test(meta.description)) warnings.push('meta.description should be one line: the permission dialog shows it')
  if (meta.phases && !(Array.isArray(meta.phases) && meta.phases.every(p => p && typeof p.title === 'string'))) {
    errors.push('meta.phases must be a list of {title, detail?}')
  }
  if (errors.length) return out

  const body = src.slice(m[0].length + metaText.length)
  const code = codeOnly(body)
  for (const [re, what] of [[/\bimport\s*\(/, 'import()'], [/\bimport\s+[\w{*]/, 'an import statement'],
    [/\brequire\s*\(/, 'require()'], [/Date\.now\s*\(/, 'Date.now()'],
    [/Math\.random\s*\(/, 'Math.random()'], [/new\s+Date\s*\(\s*\)/, 'argless new Date()'],
    [/\bprocess\./, 'process (no shell or environment access in a script)']]) {
    if (re.test(code)) errors.push(`${what} is not allowed in a workflow script`)
  }
  if (/:\s*(string|number|boolean|any)(\[\])?\s*[,)=]/.test(code) || /\binterface\s+\w+\s*{/.test(code)) {
    warnings.push('looks like TypeScript; workflow scripts are plain JavaScript')
  }
  if (errors.length) return out

  const metaPhases = (meta.phases || []).map(p => p.title)
  let ok, empty, stopped
  try {
    ok = await dryRun(body, dryArgs, 'done')
    empty = await dryRun(body, undefined, 'done')
    stopped = await dryRun(body, dryArgs, 'stop')
  } catch (e) {
    errors.push(`dry run threw: ${e.message}`)
    return out
  }
  for (const [label, run] of [['finishes', ok], ['no args', empty], ['stops at a gate', stopped]]) {
    if (run.result === undefined) errors.push(`dry run (${label}) returned nothing: end the body with a return`)
    for (const p of run.problems) if (!errors.includes(p)) errors.push(p)
  }
  if (empty.calls.length) {
    warnings.push(`with no args it starts ${empty.calls.length} agent(s); if it needs input, return needs_input with an example first`)
  }
  if (dryArgs === undefined && ok.calls.length === 0) {
    warnings.push('the "finishes" dry run started no agents: pass real-looking args with --args')
  }
  const used = new Set([...ok.phases, ...stopped.phases, ...empty.phases])
  const unlisted = [...used].filter(t => !metaPhases.includes(t))
  if (unlisted.length) errors.push(`phase titles missing from meta.phases: ${unlisted.join(', ')}`)
  const unused = metaPhases.filter(t => !used.has(t))
  if (unused.length) warnings.push(`meta.phases never reached in the dry runs: ${unused.join(', ')}`)
  if (ok.calls.length > LARGE) warnings.push(`${ok.calls.length} agents: over ${LARGE}, Claude Code will flag it as a Large workflow`)
  const unpinned = ok.calls.filter(c => c.model === 'session model').length
  if (unpinned) warnings.push(`${unpinned} agent(s) name no model and will run on the session's model`)

  out.summary = `${ok.calls.length} agents when every step finishes (${mix(ok.calls)}); ${stopped.calls.length} when steps stop at their gates`
  return out
}

async function main() {
  const argv = process.argv.slice(2)
  const targets = []
  let argsJson
  let argsFile
  for (let i = 0; i < argv.length; i++) {
    if (argv[i] === '--args') argsJson = argv[++i]
    else if (argv[i] === '--args-file') argsFile = argv[++i]
    else if (argv[i] === '--stub') {
      try { STUB = JSON.parse(argv[++i]) } catch (e) { usage(`--stub is not JSON: ${e.message}`) }
    }
    else if (argv[i] === '-h' || argv[i] === '--help') usage()
    else targets.push(argv[i])
  }
  if (!targets.length) usage('no workflow file or folder given')

  const files = []
  for (const t of targets) {
    const p = resolve(t)
    let st
    try { st = statSync(p) } catch { usage(`not found: ${t}`) }
    if (st.isDirectory()) files.push(...readdirSync(p).filter(f => f.endsWith('.js')).sort().map(f => join(p, f)))
    else files.push(p)
  }
  if (!files.length) usage('no .js workflow files found')

  let byName = {}
  if (argsFile) byName = JSON.parse(readFileSync(argsFile, 'utf8'))
  let shared
  if (argsJson !== undefined) {
    try { shared = JSON.parse(argsJson) } catch (e) { usage(`--args is not JSON: ${e.message}`) }
    if (files.length > 1) usage('--args applies to one file; use --args-file for a folder')
  }

  let failed = 0
  for (const f of files) {
    const name = basename(f, '.js')
    const r = await check(f, shared !== undefined ? shared : byName[name])
    if (r.errors.length) {
      failed++
      for (const e of r.errors) console.log(`FAIL ${r.name}: ${e}`)
    } else {
      console.log(`ok   ${r.name}: ${r.summary}`)
    }
    for (const w of r.warnings) console.log(`warn ${r.name}: ${w}`)
  }
  console.log(failed ? `${failed} of ${files.length} workflows failed` : `${files.length} workflow${files.length > 1 ? 's' : ''} ok`)
  process.exit(failed ? 1 : 0)
}

if (process.argv[1] && resolve(process.argv[1]) === resolve(new URL(import.meta.url).pathname)) main()
