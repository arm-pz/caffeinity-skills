export const meta = { name: 'unlisted-phase', description: 'uses a phase meta does not list', phases: [{ title: 'Scan' }] }
phase('Scan')
await agent('scan', { model: 'sonnet' })
phase('Fix')
await agent('fix', { model: 'sonnet' })
return 'done'
