---
type: concept
title: External Supervisor over Self-Diagnosis
description: >
  A degraded agent cannot be trusted to diagnose or repair the process and
  store it runs in, so supervision and repair belong to a separate process
  with its own identity, credentials and failure domain.
evidence: moderate
sources:
  - title: "Scaling Managed Agents: Decoupling the brain from the hands"
    resource: "Anthropic Engineering, 8 April 2026, section 'Don't adopt a pet' — https://www.anthropic.com/engineering/managed-agents"
  - title: "Hermes Agent docs: Security"
    resource: "Nous Research official docs as of v0.21.5 (v2026.9.24), retrieved 3 Oct 2026 — https://hermes-agent.nousresearch.com/docs/user-guide/security"
  - title: "Hermes Agent docs: Session storage recovery"
    resource: "Nous Research official docs, retrieved 3 Oct 2026 — https://hermes-agent.nousresearch.com/docs/user-guide/session-storage-recovery"
  - title: "OpenClaw docs: Triage"
    resource: "OpenClaw official docs as of 2026.9.x, retrieved 3 Oct 2026 — https://docs.openclaw.ai/cli/triage"
  - title: "Neurodiversity For Dummies"
    resource: "Marble, Chabria and Jayaraman, ch. 9, on a designated external state monitor"
  - title: "Reliable Machine Learning"
    resource: "Chen et al., ch. 15, on corrupted validation masking incidents"
---

When an agent degrades, the faculties it would use to notice the problem are
often the ones that have broken. A planner stuck in a loop, a corrupted context
or a session store refusing writes all impair the agent's reading of its own
health, and a self-check running inside that agent inherits the same fault.
Anthropic's Managed Agents post describes the operational version: when
harness, session and sandbox shared one container, a stuck session looked the
same whether the cause was a harness bug, a dropped event or a dead container,
and debugging meant opening a shell inside a "pet" that held user data. Its fix
was the cattle-not-pet split described in [brain, hands and session
decoupling](../harness/brain-hands-session-decoupling.md).

## Self-repair has hard limits

Asking an agent to fix its own stack is natural: it is already running, it has
a shell, and it can read its own logs. Two kinds of repair defeat that
approach, because the agent is standing inside what it would be repairing.
Restarting its gateway kills the process executing the restart, and repairing
its session store means rewriting the database that holds its current session.

Vendors enforce this. Hermes Agent (docs as of v0.21.5) has a non-overridable
guard in its terminal tool against stopping or restarting the gateway from
inside its own supervised process, including `pkill python`-style kills;
neither user approval nor its YOLO mode can override it, because a self-restart
can kill the tool mid-call and set off a supervisor loop. Its session-storage
recovery docs advise against asking the agent to fix a write-ahead-log refusal,
because its own session lives in the same store. OpenClaw (2026.9.x) reaches a
similar position through its repair prompt, which forbids starting or stopping
services and deleting state or databases; the one exception is an owned, atomic
gateway restart during the automatic repair after a failed update, while manual
triage never owns service lifecycle changes. These are primary vendor
statements.

## Watch from outside

The case for a separate supervisor that watches and repairs is partly an
analogy from human self-monitoring: the state being watched for frequently
degrades self-monitoring, so a trusted third party should watch for agreed
signs, and their flag should be treated as credible rather than argued with. A
software-native argument points the same way. *Reliable Machine Learning*
shows that a check sharing a broken upstream dependency can certify a broken
change as healthy, and a diagnostician calling the same LLM provider as the
agent it repairs shares exactly that kind of dependency. This is the
operational form of [separating the generator from the
evaluator](../evaluation/separate-generator-from-evaluator.md).

So the supervisor should run as its own process or container, with its own
identity and credentials and, where practical, its own model provider, and it
should own process restarts and store recovery rather than delegating them to
the agent being repaired. It must also avoid becoming a second writer on the
stores it repairs ([single-threaded writes](single-threaded-writes.md)).

The vendor refusals are well documented, but the stronger claims rest on
inference: no source studies an LLM agent supervising another, and whether the
supervisor must avoid sharing the provider, network or credentials is untested.
A supervisor also cannot repair the layer it depends on: one hosted on the same
container daemon or host cannot survive the failure of that daemon or host, so
a small watchdog outside it may be needed at the top of a [supervision
tree](supervision-tree-escalation.md). What the supervisor watches is best
reduced to a [deterministic score](deterministic-score-gates-llm-diagnosis.md)
before any LLM is woken.
