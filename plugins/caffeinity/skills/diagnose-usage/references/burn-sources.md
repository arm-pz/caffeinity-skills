# Burn sources

Open this at step 3 of the workflow, once you have the user's `/usage` paste.

**Provenance.** The first five suspects come from Boris Cherny's (Claude Code) X post of 29 Oct 2026 on usage draining faster than expected. The effort-setting mechanics under "How effort is set" come from third-party write-ups of the Claude Code docs, checked 29 Oct 2026. Both can be out of date: confirm against the user's `/effort` slider and the current docs before stating a level or flag as fact.

## Suspects

| Suspect | Why it is heavy | Evidence to look for in the paste | One change |
|---|---|---|---|
| High effort (xhigh, max) | Deeper reasoning per turn, more tokens per turn | One long session at a raised level | Lower the level for routine work; `/effort auto` returns to the model default |
| Subagents inheriting effort | Anthropic says subagents inherit the session's effort by default, so a raised level multiplies across every subagent | Many short agent runs under one session | Lower the session effort before fan-out. Whether a per-subagent effort setting is honoured has been reported both ways; test it, do not assume |
| Goal mode (`/goal`) | Keeps working until a condition is met, so one prompt can mean many turns | A single session far larger than the rest | Bound the goal, and check `/usage` partway |
| Workflows and Agent Teams | Fan out many agents at once | A burst of agent activity in one session | Use only when the work parallelises; check `/usage` after the first stage |
| Long SDK jobs | Headless loops run unattended and accumulate | A job session far above interactive ones | Set a turn or budget cap if the SDK version offers one; look up the option name in the docs, do not invent it |
| Environment override | A `CLAUDE_CODE_EFFORT_LEVEL` variable is reported to override every other effort setting | User says they set a low level but usage did not change | Ask the user to check that variable in their shell and CI |
| Heavier model | Model and effort are set separately and cost combines both | `/model` shows a larger model than the work needs | Ask whether the task needs it; `/model` changes it |

## How effort is set

Per the third-party summaries, not verified against the live docs:

- `/effort` opens a slider; `/effort <level>` sets directly; `/effort auto` resets to the model default.
- `claude --effort <level>` sets it for one launched session.
- Levels run low, medium, high, xhigh, max, and a Claude Code setting called ultracode. Which levels exist depends on the model, and an unsupported level falls back to a lower one without telling you.
- Max applies to the current session only.

## Reading the paste

Pick the one or two sessions or categories holding the most tokens. If the top one is not a suspect above, say so and go to step 5 (`/feedback`) rather than forcing a match.
