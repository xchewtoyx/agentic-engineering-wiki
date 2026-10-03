---
type: concept
title: Level-Triggered Reconcile Loop
description: >
  An agent that repeatedly compares desired with actual state, and acts to
  close the gap, tolerates missed events and crash-uncertain outcomes better
  than one reacting to individual alerts.
evidence: moderate
sources:
  - title: "Controllers"
    resource: "Kubernetes documentation, Concepts > Architecture — https://kubernetes.io/docs/concepts/architecture/controller/"
  - title: "The Practice of Cloud System Administration"
    resource: "Limoncelli, Chalup and Hogan, ch. 10, on convergent versus direct orchestration"
  - title: "Hacker News discussion of Pi Durable"
    resource: "HN thread 49925969, practitioner comments — https://news.ycombinator.com/item?id=49925969"
---

An event-driven agent reacts to each alert or message as it arrives. That
breaks in exactly the conditions an operations agent exists for. Alerts get
dropped, arrive out of order or repeat; the agent itself may crash mid-action
and come back unsure whether its last action happened. An agent that remembers
"I was handling alert 42" has to reconstruct a sequence it may never have seen
fully.

The Kubernetes controller pattern avoids this. A controller is a
non-terminating loop that compares the desired state with the current state and
acts to close the gap. Controllers are level-triggered and simple, and they
tolerate missed events because the next pass re-reconciles from what is
actually there. *The Practice of Cloud System Administration* names the
trade-off. Convergent orchestration declares an end state and self-corrects
drift. Direct orchestration runs an ordered sequence and is needed when
invariants must hold mid-flight, as in a live database migration.
Practitioners discussing Pi Durable reach a similar answer from the
durable-execution side, recommending declarative, idempotent interaction with
the environment in the style of Ansible.

For an agent that takes operational actions, the core loop reads the desired
state of each system it owns (services up, readiness passing, intake open,
expected versions), observes the actual state, and chooses the smallest
pre-approved action that closes the gap. A [deterministic
score](deterministic-score-gates-llm-diagnosis.md) can decide when a gap is
worth LLM attention at all. The loop fits the crash-uncertainty problem well,
because after a restart the agent simply observes again rather than trusting
its journal about what it last did ([unknown state on
resurrection](../harness/unknown-state-on-resurrection.md)), which softens the
gap the [effect sandwich](effect-sandwich.md) leaves. Every action must be safe
to re-run, since the next pass may repeat it, and each loop must be
rate-bounded by [supervision-tree escalation](supervision-tree-escalation.md)
so it cannot thrash. Procedures with mid-flight invariants, such as an upgrade
with a one-way state migration, stay as direct, ordered runbooks. The LLM's
place in the loop is to propose the action, not apply it ([the LLM proposes,
code applies](../harness/llm-proposes-code-applies.md)), and the actions it may
propose come from a [narrow action verb
set](../harness/narrow-action-verb-set.md).
