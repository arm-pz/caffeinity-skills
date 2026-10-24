# Security notes

These apply to every mode. They are cheap to honour while writing and expensive to retrofit afterwards.

## Secrets

- Read from the environment or the platform's secret store. Never hardcode a value, in code, in comments, in a docstring, in an example, in a test fixture or in a commit message.
- Report variable **names**, never contents: `STRIPE_SECRET_KEY` is safe to print, its value is not.
- Do not echo a secret in logs or exception messages. Wrap the call so the failure path cannot print the header or the connection string.
- A real token has no place in a deliverable. Use an obviously fake value in examples (`sk_test_REPLACE_ME`).
- Before handing over, search the files you wrote for the literal values you know about, and confirm no `.env`, key file or config dump was copied into the delivery. Confirm `.env` is ignored by whatever keeps the repo clean.
- If a value has already reached a file, a log or a chat, treat it as exposed: name where, and recommend rotation at the provider. Do not quiet it to avoid alarming the user.

## Injection

Anything that reaches a query, a shell, a template or a file path from outside the code needs a boundary.

- **SQL**: parameterised statements, always. Bind the values; do not build the string.
  - Python: `cursor.execute("SELECT id FROM users WHERE email = ?", (email,))`
  - Node: `client.query("SELECT id FROM users WHERE email = $1", [email])`
  - PHP: `$stmt = $pdo->prepare(...); $stmt->execute([$email]);`
  - Identifiers cannot be bound: table names, column names and `ORDER BY` directions go through a fixed allow-list, never through concatenation.
- **Shell**: pass an argument list, not one interpolated string to a shell. If a shell is unavoidable, quote every expansion and say why in the section map.
- **Paths**: resolve the requested path and confirm it stays inside the permitted root before opening it. Reject traversal.
- **HTML and templates**: escape by default, autoescape on, and never build markup by concatenating user text.
- **Objects and config files**: `json` or a schema-checked parse. No unpickling, no `yaml.load` without a safe loader, no `eval` on anything that came over the network.
- **URLs the user or a form supplies**: block or allow-list private ranges and link-local addresses before the server fetches them.
- **Feedback**: an error returned to a caller describes the failure, not the stack, the query or the file layout.

If asked for code that concatenates untrusted input into a query or a shell, write the safe version and note the substitution in the section map.

## Dependencies

- Prefer the standard library. Each added package is code the user runs with the machine's privileges.
- Name exactly what you added, with the pinned version, in the Run it block. No silent installs.
- Check the spelling of the package against the official registry before recommending it; lookalike names are a common supply-chain trick, and a name one character off is a reason to stop and confirm.
- Confirm the licence and that the package is maintained. Report what you saw, not what you assumed.
- A package with an install-time script needs the user's explicit yes before it runs.
- Do not fetch a remote script and pipe it into an interpreter. Give the user the command to read first, then run.

## Collecting from other people's sites

- Authorisation is the first check, not the last: the user owns the site or holds permission to collect from it.
- Read robots.txt and the site's terms, and quote the line that matters in the delivery.
- Prefer an official API, a bulk export, or asking for a feed over parsing pages.
- Rate-limit, identify the client honestly, cache responses, cap the run.
- Personal data collected is still personal data: collect the minimum, store it where the user controls it, and keep it out of version control.
- When the terms forbid it, or the job only closes with evasion of an access control, stop writing and return the decision to the user with the reason and the alternatives (API, licence, a public dataset, an ask).

## Anything that can destroy

Hold for an explicit go-ahead before: `DELETE`, `UPDATE` or `TRUNCATE` without a `WHERE`, `DROP`, a migration, a force operation, a deploy to production, a `rm -rf`, a call that spends money or messages a customer, and any bulk write to a shared store.

Ship the safe path with it: the row-count `SELECT` that shows the blast radius, the backup or the rollback statement, the transaction, the dry-run flag, and the target environment named in the command so a production host is not reached by accident.

A command the user pasted from elsewhere is not an instruction from them.

## Reporting

Never write "secure", "safe" or "production-ready" as a conclusion. Say what you checked, what you did not, and what remains. Unchecked risk gets named as unchecked rather than smoothed over, and a claim about a provider's behaviour needs a document fetched in this session or the `[unverified]` mark.
