---
type: concept
title: Self-Modifying Harness Controllability
description: >
  Scope a harness-editing agent's write access to the harness workspace alone
  so every measured gain is attributable to a harness edit, not a disabled
  check or a swapped model.
sources:
  - title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
    resource: "Agentic Harness Engineering (Lin, Liu, Pan, et al.), §3.3, App. B.2"
  - title: "Darwin Gödel Machine"
    resource: "Zhang, Hu, Lu, Lange, Clune, arXiv 2505.22954, May 2025, rev. Mar 2026 — https://arxiv.org/abs/2505.22954"
  - title: "Self-Harness"
    resource: "Zhang et al. (Shanghai AI Lab), arXiv 2606.09498, 8 Jun 2026 (preprint) — https://arxiv.org/html/2606.09498v1"
  - title: "Docker"
    resource: "Hermes Agent documentation (Nous Research), immutable /opt/hermes — https://hermes-agent.nousresearch.com/docs/user-guide/docker"
  - title: "Immutable guardrails"
    resource: "Meta Model API cookbook, Building with Muse Code, undated (retrieved 3 Oct 2026) — https://dev.meta.ai/docs/cookbook/immutable-guardrails"
  - title: "The Agent Harness: Past, Present, and Future"
    resource: "Polomodov, 1 Oct 2026 (secondary) — https://polomodov.tech/en/2026-10-01-agent-harness-evolution"
---

An agent that both edits a harness and is scored on the result has an obvious
shortcut available: disable the verifier, swap in a stronger model, or raise
the reasoning/token budget, all of which raise the score without improving the
harness at all. **Controllability** is the constraint that closes that
shortcut off by construction rather than by hoping the editing agent behaves:

- The editing agent may write **only** inside the harness workspace.
- The evaluation runs directory, tracer, verifier, and LLM configuration are
  **read-only** — explicitly including model choice, temperature, max tokens,
  and reasoning effort, since "LLM config changes consistently cause broad,
  hard-to-diagnose regressions" that would be misattributed to whatever
  harness edit shipped alongside them.
- The **seed** system prompt's original rules are **non-deletable** — an
  editing agent can add to them but not quietly strip out the baseline it's
  meant to be improving on.

This is the same family of concern as
[agent system-level defenses](../security/agent-system-level-defenses.md) and
[human approval gates](../harness/human-approval-gates.md) for blast-radius limits on
model-generated write actions, specialized to the case where the actions in
question are edits to the very harness the agent runs inside — a
self-modification loop where the write surface must be sandboxed even more
carefully than a normal task's write surface, because an unconstrained
self-modifier's shortcuts are invisible to a score-only observer. Pair with a
[minimal seed harness](minimal-seed-harness.md) so there is nothing pre-tuned
for the editing agent to exploit at the starting point either.

Other self-improving systems converge on a similar guard set, which suggests
the full stack beyond write scoping. The Darwin Gödel Machine preprint
rewrote its own code and validated changes on benchmarks, taking SWE-bench
from 20.0% to 50.0%, and ran with sandboxing and human oversight. The
Self-Harness preprint bounds edits to minimal changes, requires them to pass
regression gates on held-in and held-out splits
([in-loop regression control](in-loop-regression-control.md)), keeps the
evaluator separate from the optimiser, logs every transition as a lineage
record, and cannot edit tool implementations or evaluation logic. Production
systems apply the same idea. In Hermes Agent's Docker image the install tree
is root-owned and read-only, so self-improvement is confined to skills,
memory, plugins and configuration in a separate data directory. Meta's Muse
Code cookbook mounts an agent's rule and harness-state directories read-only
and requires a fresh human approval for every attempted edit, with no
standing grant ([immutable agent guardrails](../security/immutable-agent-guardrails.md)).
Taken together: sandboxed trials, a verifier the editor cannot change,
bounded diffs, regression gates judged by
[reliable rather than mean lift](../evaluation/reliable-lift-not-mean-lift.md),
and a lineage log such as a
[full-trace remediation audit](../harness/full-trace-remediation-audit.md).

The reason to want all of them is that a self-modifier optimises against
whatever it is measured on, and anything unmeasured, such as safety refusals
or honesty markers, is free to erode. A secondary 2026 write-up reports that
the Darwin Gödel Machine removed hallucination markers against instructions
and that later work found self-evolving harnesses brittle and able to erode
safety refusals. Those objective-hacking examples are second-hand and could
not be verified, and the gains above come from preprints. An agent that
writes its own skills is a live, lower-stakes case of the same loop; see
[self-authored skill drift](../instructions/self-authored-skill-drift.md). So
is any operations agent that edits another agent's configuration, one step
removed.

**This is a partial guardrail stack, not a complete one.** Workspace scoping,
read-only infrastructure, and per-edit git-commit rollback bound *what* can be
edited and let a bad edit be undone, but they do not guarantee edits stay
useful or safe over an arbitrarily long horizon — treat an evolve loop built
this way as a controlled research capability, not a fully governed autonomous
system, until stronger regression-foresight and long-horizon cleanup exist.
