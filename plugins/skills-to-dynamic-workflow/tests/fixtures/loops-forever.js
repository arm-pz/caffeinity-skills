export const meta = { name: 'loops-forever', description: 'reviews until the verdict is pass, which a stub never gives' }
const S = { type: 'object', required: ['verdict'], properties: { verdict: { type: 'string', enum: ['fail', 'pass'] } } }
let r = { verdict: 'fail' }
while (r.verdict !== 'pass') r = await agent('review', { model: 'sonnet', schema: S })
return r
