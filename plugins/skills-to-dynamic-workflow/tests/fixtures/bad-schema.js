export const meta = { name: 'bad-schema', description: 'a required key the schema cannot satisfy' }
const r = await agent('x', { model: 'sonnet', schema: { type: 'object', additionalProperties: false, required: ['a'], properties: { b: { type: 'string' } } } })
return r
