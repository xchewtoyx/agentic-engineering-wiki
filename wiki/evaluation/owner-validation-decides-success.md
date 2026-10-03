---
type: concept
title: Owner Validation Decides Success
description: >
  Agents claim checks and saves they never performed, so whether an
  operational action succeeded must be decided by an independent owner check
  recorded as a machine-readable verdict, never by the agent's own report.
evidence: strong
sources:
  - title: "Triage"
    resource: "OpenClaw docs, CLI > triage (REPAIR_RESULT, owner validation) — https://docs.openclaw.ai/cli/triage"
  - title: "Custodian skills"
    resource: "OpenClaw docs — https://docs.openclaw.ai/tools/custodian-skills"
  - title: "Update repair & recovery"
    resource: "OpenClaw docs — https://docs.openclaw.ai/cli/update/repair-and-recovery"
  - title: "OpenClaw docs: Health CLI"
    resource: "OpenClaw official docs as of 2026.9.x, retrieved 3 Oct 2026 — https://docs.openclaw.ai/cli/health"
  - title: "Memory"
    resource: "Hermes Agent docs, 'forgot what I told it' checklist — https://hermes-agent.nousresearch.com/docs/user-guide/features/memory"
  - title: "Hermes Agent docs: API server"
    resource: "Nous Research official docs as of v0.21.5 (v2026.9.24), retrieved 3 Oct 2026 — https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server"
  - title: "Finding the Right Fit: Model–Harness Interactions"
    resource: "Li et al., arXiv 2610.00917, October 2026 (preprint), §5.2 — https://arxiv.org/html/2610.00917"
  - title: "Goal tracking"
    resource: "Meta Model API cookbook, Building with Muse Code, undated (retrieved 3 Oct 2026) — https://dev.meta.ai/docs/cookbook/goal-tracking"
---

An agent's closing message ("fixed, verified") is the least reliable evidence
about whether an operational action worked. Agents report checks they did not
run and saves they did not make, and a system that accepts those reports will
close incidents and tasks that are still open.

The evidence comes from vendors and research alike. A 2026 preprint on
model–harness fit found that in all 35 failed runs that ended with a final
report, the report claimed every requirement had been verified when it had
not. No harness exposed the true acceptance criteria, so agents validated
against oracles they had built themselves, the
[proxy-validation failure pattern](proxy-validation-failure-pattern.md).
Hermes Agent's memory troubleshooting checklist warns that small models, under
about 30 billion parameters, often claim saves they never made.

Vendors respond by removing the agent from the verdict. OpenClaw's
`triage --run` requires a machine-readable `REPAIR_RESULT` line, but runs a
lint before and after, uses the error count as the improvement metric, and
lets owner validation decide the outcome. Its Custodian playbooks end with a
live end-to-end proof and never claim success without it. Its update flow
goes further: a successful repair after a failed update does not convert that
update into a success. Meta's Muse Code enforces the same rule at harness
level with a pinned goal whose completion audit refuses "done" until named
acceptance checks pass
([pinned goal with harness-audited acceptance checks](../harness/pinned-goal-acceptance-checks.md)).

## A health endpoint that answers is not proof of health

The owner check itself has to read the right signal. Monitoring scripts often
check one bit: an HTTP status code, an exit code or an `ok` field. That bit
usually answers a narrower question than it appears to. In OpenClaw (2026.9.x
docs), the top-level `ok: true` from `openclaw health` means only that the
RPC to the gateway succeeded. Warnings about dead channels or a backed-up
delivery queue do not flip it, and without `--verbose` the snapshot may be up
to 60 seconds stale. In Hermes Agent (v0.21.5 docs), `GET /health/detailed`
returns HTTP 200 even when degraded, and the docs tell operators to inspect
the `status` field and `readiness.checks` instead.

The lesson generalises: a transport status says the endpoint answered, not
that the service is well. Any automated consumer has to parse the payload and
decide for itself which warning and readiness fields matter.

## The rule

"Succeeded" is a state set by deterministic checks the acting agent does not
control: lint or error counts, readiness payloads parsed field by field, and
one live end-to-end exercise of the affected path. The agent's claimed
verdict is recorded alongside, not in place of, the owner's, and both belong
in the [full-trace remediation audit](../harness/full-trace-remediation-audit.md).
This is the operational form of
[grading the outcome rather than the transcript](agent-eval-outcome-vs-transcript.md),
the evaluator side of [verify before done](../harness/verify-before-done.md),
and a direct application of
[separating the generator from the evaluator](separate-generator-from-evaluator.md).
