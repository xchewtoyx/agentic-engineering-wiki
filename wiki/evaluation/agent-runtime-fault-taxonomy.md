---
type: concept
title: Agent Runtime Fault Taxonomy
description: >
  Runtime faults in agent systems fall into availability, performance,
  control/routing and data/policy classes, and how well a model can diagnose
  them from a trace varies sharply by class.
evidence: weak
sources:
  - title: "When Agentic Executions Fail: AgentChaosBench"
    resource: "Zhang, Li, Tian, Bachras, Jacobsen (University of Toronto), arXiv 2608.14680, 4 Aug 2026 (preprint) — https://arxiv.org/html/2608.14680"
---

Any agent that diagnoses or responds to failures in other agent systems needs
to know two things: what kinds of runtime fault occur, and which of them a
model can actually recognise from telemetry. Without the second, it is easy to
automate responses to diagnoses that are mostly guesses.

The AgentChaosBench preprint injected ten fault types into five agent systems
built on agent-to-agent (A2A) and Model Context Protocol (MCP) links,
instrumented with Langfuse. The faults fall into four classes:

- **Availability**: tool failure, A2A timeout.
- **Performance**: tool or A2A latency.
- **Control and routing**: infinite loop, tool misroute, agent misroute.
- **Data and policy**: context overflow, output corruption, guardrail bypass.

Asked to diagnose from a single trace, a frontier model named the fault type
correctly only 24.8% of the time, the location 31% at best, and both together
22%. The per-class spread was extreme: tool failure was the easiest class,
identified in nearly every case, and guardrail bypass was identified in
about one of 25. Per-class figures depend on the metric and detector model,
so treat "easiest" as relative, not as solved. Pairing each faulty trace with a fault-free
reference raised context-overflow detection by 55 points but did nothing for
guardrail bypass.

The evidence is weak: a single preprint on synthetic injected faults in five
systems. The class split is plausible for any containerised agent deployment
(timeouts, latency, loops, context overflow), but that mapping is an
inference.

For an operations or repair agent, the implication is to treat
diagnosability as uneven by class. This benchmark does not show any class to be
reliably diagnosed. Its per-class table uses a looser ranking metric than
top-1 accuracy, results for some availability faults vary widely across
detector models, and the best overall top-1 fault-type accuracy is low. Use
the class split only to decide what to measure first. Availability faults
such as a dead tool or a timed-out dependency are the likeliest candidates
for bounded automatic action, but admit a class only once your own setting
shows reliable top-1 diagnosis and localisation for it. Policy and corruption
faults should default to escalation. This split fits
[envelope-bounded autonomy](../harness/envelope-bounded-autonomy.md). The
paired-reference result supports
[known-good baseline comparison](known-good-baseline-comparison.md), the low
overall accuracy echoes
[uneven success rates for LLM SRE agents](llm-sre-agents-low-success.md), and the
fault classes give a ready menu for
[practising with fault injection](practise-with-fault-injection.md). For
failures that come from how several agents coordinate rather than from the
runtime, the [MAST taxonomy](mast-multi-agent-failure-taxonomy.md) is the
complementary vocabulary.
