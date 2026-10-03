---
type: concept
title: Doom-Loop Detection
description: >
  Harness middleware should detect repetitive actions, such as repeated edits
  to the same file, and push the agent to change approach, much as a circuit
  breaker or retry budget does.
evidence: weak
sources:
  - title: "Improving Deep Agents with harness engineering"
    resource: "Viv Trivedy, LangChain, 17 Feb 2026, LoopDetectionMiddleware — https://www.langchain.com/blog/improving-deep-agents-with-harness-engineering"
  - title: "Basic agent loop"
    resource: "Meta Model API cookbook, Agent Patterns, undated (retrieved 3 Oct 2026) — https://dev.meta.ai/docs/cookbook/basic-agent-loop"
---

Agents get stuck. A model that has settled on a wrong idea will edit the same
file again and again, re-run the same failing command, or re-read the same log,
each time expecting a different result. Left alone, such a loop burns tokens
and time and can leave the environment worse than it found it.

LangChain's Terminal-Bench work added a `LoopDetectionMiddleware` that flags
repeated edits to the same file, which it calls doom loops, and prompts the
agent to change approach. It sat alongside other harness-only changes (a
pre-completion checklist, environment mapping at start-up, time-budget
warnings) that together moved one agent from 52.8% to 66.5% on Terminal-Bench
2.0. Meta's basic agent-loop recipe lists stuck detection on repeated identical
tool calls among its standard guards, alongside iteration caps and token
budgets, and its goal-tracking recipe queues a nudge after about ten model
calls with no reported progress. LangChain's post does not isolate how much of
its gain came from loop detection, which is why the evidence here is rated
weak: one vendor post, one middleware, no separate measurement.

This is the agent-harness form of a familiar operations pattern, in the same
family as circuit breakers and retry budgets. That mapping is an inference, but
it suggests how to design one. A detector needs a signature for "the same
action" (same file, same command, same arguments), a threshold, and a response
that changes the situation rather than just stopping it, such as a nudge to
re-plan, an escalation, or a hand-off to a different worker. Browser agents
show a specific case, the [blind scroll loop](blind-scroll-loop.md), and
workflows that cycle between generation and repair have their own version in
[cyclic workflow repair loops](../orchestration/cyclic-workflow-repair-loops.md).

Loops are often a symptom of poor feedback: if a failure comes back as silence
or an opaque code, retrying is the agent's only move. Better
[failure feedback](failures-returned-as-actionable-feedback.md) reduces loops,
and detection catches the rest. Long contexts make it worse through the
distraction mode in
[four ways long contexts fail](../context/four-context-failure-modes.md), where
the agent repeats its own history instead of planning.

For an agent that takes operational actions, the same restart or the same fix
applied repeatedly to one component is a doom loop with real side effects, and
its limits belong with the bounded-restart rules of
[supervision tree escalation](../orchestration/supervision-tree-escalation.md).
Completion checks such as [verify before done](verify-before-done.md) are the
complementary guard against stopping too early rather than too late.
