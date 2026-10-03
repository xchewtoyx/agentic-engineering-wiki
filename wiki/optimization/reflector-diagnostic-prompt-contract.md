---
type: concept
title: Reflector Diagnostic Prompt Contract
description: >
  Prompt a dedicated Reflector to diagnose one attempt against ground truth and
  environment feedback (plus unit-test reports in the AppWorld variant),
  returning JSON diagnostic fields and, in the FINER variant, per-bullet
  helpful/harmful/neutral tags.
sources:
  - title: "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models"
    resource: "ACE (Zhang et al.), App. F, Figs. 10, 13; App. A.4, A.6"
---

In the [generator–reflector–curator loop](generator-reflector-curator-loop.md)
the Reflector is the only role that judges. Its prompt is designed to produce
a lesson specific enough for a separate Curator to turn into a playbook bullet.

ACE publishes two Reflector prompts, and they differ in persona, inputs, and
output. Don't merge them into one contract.

**Persona and task.**

- **AppWorld (Fig. 10).** An "expert AppWorld coding agent and educator" who
  must "diagnose the current trajectory": what went wrong (or could be
  better), grounded in execution feedback, API usage, the unit-test report,
  and ground truth when applicable.
- **FINER (Fig. 13).** An "expert analyst and educator" who diagnoses why the
  reasoning went wrong from the gap between the predicted answer and the
  ground truth. It gets the same diagnostic instructions minus the
  API-specific items, plus "focus on the root cause, not just surface-level
  errors".

**Inputs.**

| | AppWorld (Fig. 10) | FINER (Fig. 13) |
|---|---|---|
| Attempt | Full agent–environment trajectory | Question, reasoning trace, predicted answer |
| Ground truth | Ground-truth code | Ground-truth answer |
| Test report | Unit-test report | None |
| Environment feedback | Inside the trajectory (execution output) | Separate environment-feedback field |
| Playbook | The ACE playbook; the tagging instruction refers to the bullets the Generator used | Only the playbook portion the Generator used |

**Output schema (JSON).** Every variant returns five diagnostic fields:
`reasoning`, `error_identification`, `root_cause_analysis`,
`correct_approach`, `key_insight`. The `bullet_tags` field is
variant-specific. The FINER Reflector (Fig. 13) adds it as a list of
`{id, tag}` with tag ∈ {helpful, harmful, neutral}. The AppWorld Reflector
(Fig. 10) is told to tag the bullets it was given, but its listed output
schema has only the five diagnostic fields. Where present, the tags feed the
usage counters of the
[itemized bullet context](itemized-bullet-context.md). Treat the field as
optional and add it explicitly if your merge step needs per-bullet
attribution.

**Steering the diagnosis (AppWorld prompt only).** The AppWorld prompt names
the root-cause categories to look for: wrong source of truth, bad filters
(timeframe, direction, identity), formatting issues, missing authentication.
It also tells the Reflector to record API output schemas whenever observed
output didn't match expectations (e.g. "returns a list of IDs, not
objects"). Two worked examples in that prompt show the expected grain of
insight:

- Identity resolved by keyword-matching transaction descriptions instead of
  the authoritative contacts API. Insight: always resolve entities from the
  authoritative source app, never from indirect heuristics.
- Pagination capped with `for i in range(10)`, which ran cleanly but silently
  truncated results. Insight: loop until the API returns empty.

The second example matters because the code raised no error. The failure
was caught only by the unit test against ground truth. A plausible inference
(not a result the paper isolates) is that such silent failures are one reason
label-free adaptation can trail labeled adaptation. See
[feedback-signal dependence of context adaptation](context-adaptation-feedback-dependence.md)
for the measured gaps.
The same per-trajectory root-cause unit appears in harness-evolution
pipelines ([agent debugger trajectory distillation](agent-debugger-trajectory-distillation.md)).

**Privileged signal at update time only.** When ground truth (and, for
AppWorld, test reports) is available, the Reflector sees it only while
updating the playbook. That holds offline, and in labeled online runs where the label
arrives after the prediction. The Generator never sees them when it uses the
playbook. The
Reflector's lesson has to be phrased so that it helps a future Generator that
will never see them. The
[curator contract](curator-delta-operation-contract.md) restates this
constraint.

**Refinement rounds are a tuning knob.** Letting the Reflector iterate on
its own diagnosis trades insight extraction against "overthinking" that adds
noisy updates. AppWorld average by number of rounds: none 53.3; 1 → 61.3
(under-extracts); 3 → 65.8; 5 → 67.6 (best); 10 → 65.2 (degrades). Start at
3–5 rounds; this sweep covers AppWorld only. On FiNER, a weaker Reflector
model cost some gain but still helped (see
[context adaptation noise robustness](context-adaptation-noise-robustness.md)).
