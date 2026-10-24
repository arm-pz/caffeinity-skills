# Stack presets

Pick the smallest stack that can carry the page's load-bearing mechanic. A page that scrolls one pinned scene does not need a router; a single-page brochure does not need a build step. Bigger stacks cost the reader more tokens and add failure points the prompt has to describe.

## Static preset

Use when the page is genuinely static: no shared component state, no client routing, no build-time data. One `index.html`, one `styles.css`, one `main.js`. No package manager, no install step.

    ## Tech stack
    Plain HTML, CSS and JavaScript. No framework, no build step, no dependencies.
    Files: index.html, styles.css, main.js.
    Open index.html directly, or serve with `python -m http.server 8080`.

Rules:
- CSS custom properties for the palette and type scale; no preprocessor.
- `requestAnimationFrame` + scroll listeners for motion; no animation library.
- ES modules via `<script type="module" src="main.js">`.
- No CDN scripts and no library links. A Google Fonts stylesheet (with `preconnect`) is the one allowed external request; otherwise use a system stack.

Do not use the static preset for scroll-pinned multi-scene pages, canvas work, or anything that needs component reuse. The hand-written scene state gets unreadable and the "exactly" promise stops meaning anything.

## Vite preset (tested)

Use for a one-page site with several scroll scenes, shared state, or reusable components. These are the versions that were installed and built in the SELENE run, not the ranges that happen to be latest:

| Package | Version |
| --- | --- |
| react | 19.3.1 |
| react-dom | 19.3.1 |
| typescript | 5.8.3 |
| vite | 6.4.4 |
| @vitejs/plugin-react | 5.2.0 |
| tailwindcss | 4.3.3 |
| @tailwindcss/vite | 4.3.3 |
| @types/react | 19.3.0 |
| @types/react-dom | 19.3.0 |
| lenis | 1.3.27 (only when smooth scroll is part of the mechanic) |

In `package.json`, pin with carets for minors and a tilde for TypeScript, as the SELENE prompt does (`^19.1.0`, `~5.8.2`, `^6.2.3`, …). The prompt must state the versions that were actually resolved, because a reader installing today gets whatever the carets allow.

Scripts:

    "dev": "vite --port=3006 --host=0.0.0.0",
    "build": "vite build",
    "preview": "vite preview --port=3006",
    "lint": "tsc --noEmit"

Rules:
- Tailwind v4 through `@tailwindcss/vite`; theme tokens in `@theme` inside `src/index.css`. No `tailwind.config.js` unless a plugin needs one.
- TypeScript strict. `npm run lint` is the type check; there is no ESLint layer unless the prompt includes one.
- One rAF loop owns scroll-driven style writes. Do not mix `useEffect` scroll listeners with the loop for the same elements; that is how two writers fight over one transform.
- `lenis` only if the page needs smooth scrolling for a pinned scene. If it is in `package.json`, it is used.
- No animation library, no icon set, no component library unless the mechanic needs it. SVG drawn inline, icons drawn as SVG.
- Code-split below-the-fold scenes with `React.lazy` only when the build makes the initial bundle genuinely heavy. The SELENE prompt splits six components; a smaller page should not.

## Asset rule for both presets

Every visual is code-native (CSS gradients, SVG, canvas) or a real asset the user supplied. The prompt lists each supplied asset with its path and role. It never contains a hotlink, a signed download URL, or an instruction to fetch from a storage bucket: those expire and the prompt stops building. The single exception is the Google Fonts stylesheet above, which is stable and named in the stack section.
