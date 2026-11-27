export const meta = { name: 'branch', description: 'second step only when the first says blocking', phases: [{ title: 'One' }, { title: 'Two' }] }
if (!args) return { status: 'needs_input', missing: ['pr'] }
const S = { type: 'object', required: ['verdict'], properties: { verdict: { type: 'string' } } }
const a = await agent('one', { model: 'opus', phase: 'One', schema: S })
if (a.verdict === 'blocking') await agent('two', { model: 'sonnet', phase: 'Two' })
return a
