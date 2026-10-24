# Verification

The prompt may only list checks that were run against a real build in a real browser. A prompt that claims a clean console when nobody opened the console is worse than one that says "not verified", because the reader stops looking.

## 1. Build the site before writing the prompt

Create a scratch folder outside the repo, write the site there, and run it. This is the source of truth for every file section.

    npm install        # no lockfile commit unless the prompt includes it
    npm run lint       # tsc --noEmit
    npm run build      # production build, zero warnings that matter

Record the resolved versions from `node_modules` or `npm ls --depth=0`, not only the ranges in `package.json`.

## 2. Serve it and read the banner

    npm run dev -- --port=<free-port>
    npm run preview -- --port=<free-port>

Read the port from the server's own banner. Do not assume: port 3000 and 127.0.0.1:3000 can belong to someone else's process, and a bare HTTP 200 is not proof it is yours. Check the title or a known string in the response.

If Vite binds `[::1]`, `curl http://127.0.0.1:<port>` fails with exit 7; use `http://localhost:<port>`. Use user-level tooling (Playwright MCP or equivalent) to load the page.

## 3. Console and network

- No console errors after full page load and scroll. A missing favicon is a real 404; either add the favicon or list it as not verified.
- No failed network requests for assets the prompt lists.
- Every image resolves: scroll the whole page once so lazy images load, then count `img` elements with `naturalWidth === 0`. Expect zero.

## 4. Layout at four widths

Check 390×844, 768×1024, 1280×800, 1920×1080. At each width:

- `document.documentElement.scrollWidth <= document.documentElement.clientWidth` (no horizontal scroll).
- Nav, hero, the signature scene and the final CTA are on screen and readable.
- Mobile menu (if any) opens, navigates to its target, and closes.

Screenshots are useful but do not replace the measurements; some environments do not paint. Read the DOM and computed styles when a screenshot is blank.

## 5. The behaviours the prompt claims

For each load-bearing behaviour in "How the page works", measure it rather than eyeballing it:

- **Scroll scenes.** Sample progress `p` through the scene and read the computed transforms/opacities. Confirm the start state, the end state, and that the middle is monotonic where the prompt says it is.
- **Horizontal reel or pinned section.** Confirm the nearest card to the focus point has the highest opacity and the counter matches it. Confirm the section releases afterwards.
- **Drawn routes or counters.** Confirm the final value equals the data in `content.ts`, not a hard-coded duplicate.
- **Forms.** Submit empty: the invalid message appears and focus moves to the field. Submit valid: the success state appears. Confirm the mailto or endpoint the prompt describes.
- **Countdowns and clocks.** Let one tick and confirm the value changed in the expected direction.

If the prompt makes a claim about order ("dust clears before the Earth rises"), verify the order from the sampled values. If the source does not match the claim, either change the source or change the claim; do not ship the mismatch. Minor mismatches that are part of the design's feel can stay if they are reported honestly.

## 6. Reduced motion

Emulate `prefers-reduced-motion: reduce` and reload. The smooth scroll loop is off, decorative bounce loops are off, and every scene still resolves to a readable state (no section stuck at opacity 0, no transform at its start value forever). Scroll-triggered reveals must still fire, immediately.

## 7. Accessibility smoke

- One `h1`; heading levels in order.
- Every image has `alt`, including empty `alt=""` for decorative ones.
- Buttons and links have discernible names; icon-only controls have `aria-label`.
- Focus is visible on the primary CTA and form fields.
- Colour contrast of body text against its background passes 4.5:1 (and 3:1 for large display text).

## 8. Replay the prompt

This is the check specific to this skill. Run

    node scripts/replay-prompt.mjs <prompt.md> --out <fresh-dir>
    node scripts/replay-prompt.mjs <prompt.md> --check <scratch-dir>

`--check` compares every file section against the scratch build, line-endings normalized. Any drift means the prompt does not reproduce the site it claims to reproduce. Then build the replay folder and confirm lint/build pass there too; a byte-identical tree can still fail if the prompt omitted an asset instruction.

## What to write in the prompt

Under "Checks already run" list the checks with results, e.g.:

- `npm run lint` and `npm run build` pass on the versions listed above.
- No horizontal overflow at 390, 768, 1280, 1920.
- All scenes sampled and end states confirmed.
- Reduced motion: loop off, scenes resolve.
- Replay from the file sections produces a byte-identical tree and builds.

Under "Not verified" be specific: a first-run install today, a browser you did not open, an asset not downloaded, a claim in the design notes that is descriptive rather than tested. Honesty here is what makes the rest of the prompt credible.
