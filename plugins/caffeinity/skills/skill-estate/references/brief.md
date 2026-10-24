# The brief this skill was built from

The eight requests, condensed, that took the arm-pz skills from a site that disagreed with GitHub
to a self-publishing, self-testing estate (October 2026). Kept as the reference for what a full
run covers; reread one when a phase's scope is unclear.

1. **Reconcile and redesign.** The skills on GitHub and the ones on the site do not match. Go
   through every repo the owner created or contributes to, group them into categories, redesign
   the site, test each skill on real targets (rankings, READMEs), and where a workflow has a gap,
   tune the skill or draft a new one so the workflow is complete.
2. **Make it self-sufficient.** Raise PRs wherever something can improve. Make the tuning skill
   regression-driven so the family keeps improving. Account for repos renamed for
   discoverability. Write a project map. Fix CI/CD so any repo with a SKILL.md that goes live is
   published to the site and listed in the profile README.
3. **Ship it, then deepen.** Merge the open PRs (rollback is the safety net). Run tuning and a
   regression across the family. Create agents for the workflows and an updated plugin; make the
   skills discoverable in Claude and Codex.
4. **No secrets in production.** Hosting credentials are needed only to deploy; they must not be
   stored in CI.
5. **Find the workflow gaps.** Update the project map, design the missing workflow, and implement
   the gaps found.
6. **Connect Git and CI/CD to hosting** so a merge goes live without a manual deploy.
7. **Complete the catalogue.** List every mod that was built, and finish the design reference
   (inspiration) the site was meant to follow.
8. **Prove triggering and get listed.** Automated trigger tests, directory listings, and one
   visual style across every page.
