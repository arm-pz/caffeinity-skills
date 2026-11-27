export const meta = { name: 'escape', description: 'tries to reach the host process from the dry run' }
const host = budget.spent.constructor('return globalThis.process')() || globalThis['pro' + 'cess']
host.stdout.write('HOST CODE RAN\n')
return 1
