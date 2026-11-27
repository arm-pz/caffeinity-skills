// node --test plugins/skills-to-dynamic-workflow/tests/test_check_workflow.mjs
import { test } from 'node:test'
import assert from 'node:assert/strict'
import { execFileSync } from 'node:child_process'
import { join, dirname } from 'node:path'
import { fileURLToPath } from 'node:url'

const HERE = dirname(fileURLToPath(import.meta.url))
const SKILL = join(HERE, '..', 'skills', 'skills-to-dynamic-workflow')
const CHECK = join(SKILL, 'scripts', 'check_workflow.mjs')

function run(...argv) {
  try {
    return { code: 0, out: execFileSync('node', [CHECK, ...argv], { encoding: 'utf8' }) }
  } catch (e) {
    return { code: e.status, out: `${e.stdout}${e.stderr}` }
  }
}
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
  assert.match(r.out, /7 of 8 workflows failed/)
})

test('a branch that depends on an agent result is walked only with --stub', () => {
  assert.match(run(fixture('branch'), '--args', '{}').out, /1 agents/)
  assert.match(run(fixture('branch'), '--args', '{}', '--stub', '{"verdict":"blocking"}').out, /2 agents/)
})
