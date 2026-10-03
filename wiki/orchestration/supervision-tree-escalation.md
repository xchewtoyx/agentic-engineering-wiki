---
type: concept
title: Supervision-Tree Escalation
description: >
  Every automated restart or retry loop in an agent system needs an OTP-style
  intensity and period cap that turns repeated failure into escalation up a
  supervision tree, with restart strategies that encode how components depend
  on each other.
evidence: moderate
sources:
  - title: "Supervisor Behaviour"
    resource: "Erlang/OTP 29 documentation — https://www.erlang.org/doc/system/sup_princ.html"
  - title: "Supervisor Trees and Fault Tolerance Patterns for AI Agent Systems"
    resource: "Zylos Research, 16 March 2026 (vendor research blog) — https://zylos.ai/research/2026-03-16-supervisor-trees-fault-tolerance-ai-agent-systems/"
  - title: "The Practice of Cloud System Administration"
    resource: "Limoncelli, Chalup and Hogan, ch. 6, on crash-loop escalation thresholds"
---

A watcher that restarts a failing component forever hides the real problem. A
service that crashes on every start because of bad configuration or a
corrupted data file will loop indefinitely, burning resources and looking busy,
unless something counts the restarts. *The Practice of Cloud System
Administration* makes the general case: the restart action itself needs a rate
limit that converts repeated restarts into human escalation. The same holds for
an agent retrying a failing step, which is why [cyclic repair
loops](cyclic-workflow-repair-loops.md) need an attempt counter.

Erlang/OTP supervisors are the established model. Each supervisor has a restart
intensity and period, by default one restart in five seconds; if that is
exceeded, the supervisor terminates its children and itself, passing the
failure to its parent. The total restarts tolerated before the whole system
fails is the product of the intensities up the tree. Restart strategies encode
dependencies. Under one_for_one only the failed child restarts; one_for_all
restarts all siblings; rest_for_one restarts the failed child and those started
after it. A 2026 Zylos write-up maps this onto agent runtimes, for example
using one_for_all for a vector store and session store that must stay
consistent, and notes that LLM nondeterminism and non-idempotent tool calls
complicate recovery. That mapping comes from a vendor research blog, so it is
hedged; the OTP facts are primary.

The open problem is that real agent deployments already contain several loops.
Container restart policies, process supervisors inside the image, a vendor's
own channel or session restart logic, any autoheal sidecar, an operations
agent and human or coding-agent responders can all act on the same component,
and no source designs their ordering or damping. Interacting control loops
with no agreed ordering can amplify each other.

The remedy is to draw the tree explicitly. Vendor-provided inner loops sit at
the leaves. An [external supervisor](external-supervisor-over-self-diagnosis.md)
watches components with a bounded intensity, typically driven by a
[level-triggered reconcile loop](level-triggered-reconcile-loop.md). Humans sit
at the root, reached when the supervisor's own intensity is exceeded or the
failure leaves its [autonomy envelope](../harness/envelope-bounded-autonomy.md);
stepping down a [degradation ladder](degradation-ladder.md) is often the right
action on the way up. Strategy choice follows the system's real dependencies,
such as gateway, agent loop and state store. The same parent-child shape
appears in durable runtimes as [task ownership
trees](task-ownership-tree-abort-propagation.md). Finally, a supervisor cannot
supervise the host it runs on, so the top of the tree may need a small
watchdog outside it.
