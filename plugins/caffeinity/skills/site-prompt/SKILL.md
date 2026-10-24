---
name: site-prompt
description: Writes one self-contained, paste-and-build prompt for a website from a topic. Narrows the topic to a concrete subject, derives the concept from that subject's world, builds and verifies the site in a scratch folder, then embeds every file verbatim with a pinned stack, final copy, code-native visuals and the checks that were actually run. Use when the user asks for a website prompt, one-shot build prompt, mega-prompt or SELENE-style prompt for a new site, landing page or one-pager. Not for building, hosting or reviewing the site itself, not for redesigning an existing page, and not for authoring skills.
---

# Site Prompt

Produce one markdown file that a code generator can paste into an empty directory to rebuild a website exactly. The prompt is the deliverable; the site built along the way is scaffolding. Every claim in the prompt must have been run.

## Own the prompt, not the site

- **In:** a topic, optionally with a brand, name, domain, audience, must-have content or stack constraints.
- **Out:** `site-prompts/<slug>.md` in the current project, or the path the user names. One file.
- **Stop at the prompt.** An actual build goes to `sites-building`; hosting to `sites-hosting`; critique of an existing page to `impeccable` or `frontend-design`; skill authoring to `draft-skill`.

## The subject is the concept

A topic is not a theme. "Ship" is a category, and a site about "ships" is a template with nautical nouns. Narrow it to one concrete subject, one audience and one job, then derive the page from that subject's world. SELENE is not a reusable template: its Earthrise, trajectory and mission reel exist because the subject is a lunar voyage. A cargo ship site must earn its own sections, vocabulary and signature interaction.

Before designing, fill in the brief in `references/subject-brief.md`:

- one concrete subject, not a category;
- audience, and the job the page does for them;
- the single job of the page;
- at least eight terms a practitioner actually uses, plus the artifact world;
- one signature mechanic only this subject would earn;
- the tension the page dramatizes;
- what can be claimed honestly.

One ambiguous word ("ship") is not a brief. Pick the most commercial reading, state the assumption in the prompt, and proceed. Ask only when the fork changes a claim, such as a real operator versus a concept or a regulated service.

Run the swap test before building: replace the subject with something unrelated. If the sections, motion and copy still work, the concept is templated; redesign. `references/subject-brief.md` has worked SELENE and cargo-ship derivations and the template-smell list.

## Workflow

1. Fill the subject brief. Do not design yet.
2. Choose the smallest stack that serves the concept; read `references/stack-presets.md`.
   - Static HTML, CSS and JS when content plus light interaction is all the page needs.
   - Vite + React + TS + Tailwind only when scroll choreography, shared state or a component system is load-bearing.
   - If the site needs auth, payments, a database or a live AI backend, stop: this skill writes marketing and concept sites, not products.
3. Build the real site in a temp directory outside the project. Write final copy first, then layout, then motion. No lorem ipsum, placeholder images or hotlinked stock.
4. Swap-test again. Cut every section that would survive a topic change.
5. Verify with `references/verification.md`. Record which checks ran, at which viewports, and which did not run.
6. Write the prompt using `references/prompt-format.md`. Every file appears in full under a `## File:` heading. No ellipses, no "same as above", no scratch paths, no localhost.
7. Replay-test the prompt:

       node scripts/replay-prompt.mjs <prompt.md> --out <clean-dir>
       node scripts/replay-prompt.mjs <prompt.md> --check <built-dir>

   Then build the replay directory. Every file must match and the build must pass. If not, the prompt is not done.
8. Report the prompt path, narrowed subject, stack, file count, checks run and not run, replay result, and any prompt inconsistency left in the source.

Trigger cases for this skill live in `tests/trigger-cases.md`; the verifier's own cases are in `tests/replay-cases.md`. The trigger cases are specification until they are run.

## Keep the prompt honest

- The receiver has never seen this conversation. Any sentence pointing at the scratch build, the design discussion or the generator breaks it.
- Never write a check into the prompt that was not run. The "Checks already run" section lists commands, viewports, results and the unverified remainder.
- Visuals are code-native: SVG, CSS, canvas, gradients, inline data URIs. No remote images or asset hotlinks. Google Fonts links are allowed; other third-party URLs are not. User-supplied images are external inputs; say exactly where they must be placed.
- Do not carry SELENE's layer stack, mission reel, trajectory or countdown into another topic. Reuse a mechanic only when the subject earns it.
- Mark invented operators, lines and missions as concepts. Do not invent customers, logos, certifications, ratings or performance metrics.
- Keep comments that record why a number has its value; the receiver will otherwise "fix" it.
- The negative rules in the prompt ("do not improve", "do not substitute", "do not add files") are part of the contract, not decoration.

## Hand off

- Actual build or hosting of the generated site: `sites-building`, then `sites-hosting`.
- Critique or redesign of an existing page: `impeccable` or `frontend-design`.
- A batch of prompts to turn into a skill: `prompts-to-skill`.
- Repo naming, description and listing for a published prompt library: `findable`.
