# Prompt format

The output is one markdown document the user can paste into a fresh agent session. It has to be enough on its own: no links to this skill, no reference to the scratch folder, no "see the files I made".

## Section order

Use these headings in this order. Skip none of them; a prompt without the file sections is a brief, not a one-shot prompt.

1. **Title** — the subject, then a line stating it is a single self-contained prompt and the agent must build the whole site from it.
2. **What this project is** — two or three sentences: product, audience, the page's one job, the setting. Say it is a landing page and what it must make the visitor do (reserve, request a quote, book).
3. **How the page works** — the 3–5 load-bearing behaviours (scroll model, signature mechanic, what the page must show rather than claim), with the contract each one has to satisfy.
4. **Build this exactly** — a short list of hard constraints. For a rebuild of an existing site this says "Reproduce this exactly"; for an original this says "Build this exactly". Either way it rules out substitutes, lookalike assets, added dependencies, and omissions.
5. **Tech stack** — the pinned stack from `references/stack-presets.md`, with exact versions and the commands that were run.
6. **Assets** — either "everything is code-native, generate it in CSS/SVG" or the user-supplied asset list with how each is produced or placed. No hotlinks, no stock-photo placeholders, no referenced URL that will disappear.
7. **Steps to build** — the order to create files, install, and run; the verify commands; what "done" looks like.
8. **File sections** — one `## File: \`path\`` heading per file, each containing exactly one fenced code block with the complete file. This is the part that makes the prompt work.
9. **Design notes** — why the page looks the way it does: palette intent, type pairing, the subject-native details. This is judgement, not a second implementation; no file content should change to "improve" it.
10. **Checks already run** — the checks from `references/verification.md` that were actually run, with their results. Anything not run goes in a short "not verified" list.

## File heading contract

The file sections are parsed by `scripts/replay-prompt.mjs`. They must be exactly:

    ## File: `src/App.tsx`

- Path relative to the project root, forward slashes only, no leading `./`.
- One fenced code block directly under the heading, labelled with the language.
- The block holds the complete file. No `...`, no `// rest of file`, no elisions, no patch hunks.
- No duplicate paths.
- Order: config and entry first (`package.json`, `vite.config.ts`, `tsconfig.json`, `index.html`), then app entry and styles, then data/content, then lib and hooks, then components. That order makes the replay diff readable and the code block sane to read in one pass.
- Images go in the Assets section as instructions. Binary files never appear in a code block.

## The skeleton

    # {Subject} — one-shot build prompt

    This is a single, self-contained prompt. Build the whole site from it. Do not ask questions, do not substitute assets, do not stop until `npm run build` passes.

    ## What this project is
    ...

    ## How the page works
    ...

    ## Build this exactly
    - ...

    ## Tech stack
    ...

    ## Assets
    ...

    ## Steps to build
    ...

    ## File: `package.json`
    ```json
    ...
    ```

    ## File: `index.html`
    ```html
    ...
    ```

    ## Design notes
    ...

    ## Checks already run
    ...

## Things that break a one-shot prompt

- **Placeholders.** "Style this section" or "add your copy here" guarantees an agent will invent generic copy. Write the final copy in the files.
- **Scratch references.** `localhost:4317`, absolute paths from your machine, "the version I tested" without the version number. The prompt travels; those do not.
- **A file list without file bodies.** A file inventory is a brief. Every listed path gets a section, or the path does not get listed.
- **Unverifiable checks.** Listing `npm run lint` as "passing" when it was never run. If you did not run it, move it to "not verified".
- **Commented-out code and TODOs.** They read as unfinished and agents act on them.
- **Leftover subject matter.** A mission-control string in a freight page is a bug in the concept. Run the swap test before you write the sections.
- **An explanation of the skill.** The prompt is for the builder, not a note to the user about how it was made.
