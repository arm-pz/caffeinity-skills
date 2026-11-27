// node --test plugins/skills-to-dynamic-workflow/tests/test_check_workflow.mjs
import { test } from 'node:test'
import assert from 'node:assert/strict'
import { execFileSync } from 'node:child_process'
import { copyFileSync, mkdtempSync, readFileSync, symlinkSync, writeFileSync } from 'node:fs'
import { tmpdir } from 'node:os'
import { join, dirname } from 'node:path'
import { fileURLToPath } from 'node:url'

const HERE = dirname(fileURLToPath(import.meta.url))
const SKILL = join(HERE, '..', 'skills', 'skills-to-dynamic-workflow')
const CHECK = join(SKILL, 'scripts', 'check_workflow.mjs')

const { dryRun, braceSpan } = await import(CHECK)

function run(...argv) {
  return runAt(CHECK, ...argv)
}
function runAt(script, ...argv) {
  const env = { ...process.env, CHECK_WORKFLOW_TIMEOUT_MS: '500' }
  try {
    return { code: 0, out: execFileSync('node', [script, ...argv], { encoding: 'utf8', env, stdio: 'pipe' }) }
  } catch (e) {
    return { code: e.status, out: `${e.stdout}${e.stderr}` }
  }
}
// The body of a workflow file: everything after its meta literal.
function body(file) {
  const src = readFileSync(file, 'utf8')
  const at = src.indexOf('{', src.indexOf('export const meta'))
  return src.slice(at + braceSpan(src, at).length)
}
const EXAMPLE = join(SKILL, 'references', 'examples', 'review-a-pull-request.js')
const fixture = name => join(HERE, 'fixtures', `${name}.js`)

test('the template passes and walks both steps with args', () => {
  const r = run(join(SKILL, 'assets', 'workflow-template.js'), '--args', '{"idea":"x"}')
  assert.equal(r.code, 0, r.out)
  assert.match(r.out, /2 agents when every step finishes \(1 opus, 1 sonnet\)/)
})

test('the worked example passes, and --stub walks its second step', () => {
  const ex = join(SKILL, 'references', 'examples', 'review-a-pull-request.js')
  const plain = run(ex, '--args', '{"pr": 12}')
  assert.equal(plain.code, 0, plain.out)
  assert.match(plain.out, /never reached in the dry runs: Fix/)
  const walked = run(ex, '--args', '{"pr": 12}', '--stub', '{"verdict":"fail"}')
  assert.equal(walked.code, 0, walked.out)
  assert.match(walked.out, /2 agents when every step finishes \(1 opus, 1 sonnet\)/)
  assert.doesNotMatch(walked.out, /warn/)
})

for (const [name, why] of [
  ['meta-not-literal', /first statement must be `export const meta/],
  ['meta-variable', /pure literal/],
  ['uses-date-now', /Date\.now\(\) is not allowed/],
  ['wrong-name', /meta\.name is "another-name" but the file is wrong-name\.js/],
  ['unlisted-phase', /phase titles missing from meta\.phases: Fix/],
  ['bad-schema', /required key "a" is ruled out by additionalProperties: false/],
  ['no-return', /returned nothing/],
  ['escape', /dry run threw: Cannot read properties of undefined/],
  ['loops-forever', /more than 1000 agent\(\) calls/],
  ['spins', /still running after/],
]) {
  test(`fails: ${name}`, () => {
    const r = run(fixture(name))
    assert.equal(r.code, 1, r.out)
    assert.match(r.out, why)
  })
}

test('a comment that mentions Date.now() is not a violation on its own', () => {
  const r = run(fixture('uses-date-now'))
  assert.equal((r.out.match(/Date\.now/g) || []).length, 1, r.out)
})

test('a folder checks every script and reports the count', () => {
  const r = run(join(HERE, 'fixtures'))
  assert.equal(r.code, 1)
  assert.match(r.out, /10 of 11 workflows failed/)
})

test('a branch that depends on an agent result is walked only with --stub', () => {
  assert.match(run(fixture('branch'), '--args', '{}').out, /1 agents/)
  assert.match(run(fixture('branch'), '--args', '{}', '--stub', '{"verdict":"blocking"}').out, /2 agents/)
})

test('the dry run cannot reach the host process', () => {
  const r = run(fixture('escape'))
  assert.doesNotMatch(r.out, /HOST CODE RAN/)
})

test('the checker runs from a folder whose path has a space', () => {
  const dir = mkdtempSync(join(tmpdir(), 'check workflow '))
  const copy = join(dir, 'check_workflow.mjs')
  copyFileSync(CHECK, copy)
  const r = runAt(copy, EXAMPLE, '--args', '{"pr": 12}')
  assert.equal(r.code, 0, r.out)
  assert.match(r.out, /ok   review-a-pull-request/)
})

test('the checker runs when reached through a symlinked folder', () => {
  const real = mkdtempSync(join(tmpdir(), 'check-real-'))
  copyFileSync(CHECK, join(real, 'check_workflow.mjs'))
  const link = `${real}-link`
  symlinkSync(real, link, 'dir')
  const r = runAt(join(link, 'check_workflow.mjs'), EXAMPLE, '--args', '{"pr": 12}')
  assert.equal(r.code, 0, r.out)
  assert.match(r.out, /ok   review-a-pull-request/)
})

test('a fractional round is read as a whole round', async () => {
  const r = await dryRun(body(EXAMPLE), { pr: 12, round: 2.5 }, 'done', {})
  assert.equal(r.calls.length, 1)
  assert.match(r.calls[0].prompt, /\.reviews\/pr-12\/round-2\. /)
  assert.match(r.calls[0].prompt, /Round: 2\n/)
})

test('a malformed --args-file gives the usage line, not a stack trace', () => {
  const file = join(mkdtempSync(join(tmpdir(), 'args-')), 'args.json')
  writeFileSync(file, 'not json')
  const r = run(EXAMPLE, '--args-file', file)
  assert.equal(r.code, 2, r.out)
  assert.match(r.out, /--args-file .*args\.json/)
})

test('a step whose skill is missing ends the run as needs_input, not done', async () => {
  const r = await dryRun(body(EXAMPLE), { pr: 12 }, 'done', { status: 'skipped', stopReason: 'not installed' })
  assert.equal(r.calls.length, 1)
  assert.equal(r.result.status, 'needs_input')
  assert.equal(r.result.resume.from, 1)
})

test('round 4 reviews in its own folder and fixes nothing', async () => {
  const r = await dryRun(body(EXAMPLE), { pr: 12, round: 4 }, 'done', { verdict: 'fail' })
  assert.equal(r.calls.length, 1)
  assert.equal(r.result.status, 'done')
  assert.match(r.result.steps[1].why, /round 4 is the last review/)
  assert.match(r.calls[0].prompt, /\.reviews\/pr-12\/round-4\. /)
})

test('a PR number that is not a whole number asks for one before any agent starts', async () => {
  const r = await dryRun(body(EXAMPLE), { pr: 'abc' }, 'done', {})
  assert.equal(r.calls.length, 0)
  assert.equal(r.result.status, 'needs_input')
})
