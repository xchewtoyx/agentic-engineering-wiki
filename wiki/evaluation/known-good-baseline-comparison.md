---
type: concept
title: Compare Against a Known-Good Baseline
description: >
  Diagnose an agent system by diffing it against a known-good reference, such
  as a fault-free trace of the same workflow or a recorded healthy
  fingerprint calibrated for normal noise.
evidence: weak
sources:
  - title: "When Agentic Executions Fail: AgentChaosBench"
    resource: "Zhang, Li, Tian, Bachras, Jacobsen, arXiv 2608.14680, August 2026 (preprint), Fig. 3 — https://arxiv.org/html/2608.14680"
  - title: "Software Engineering at Google"
    resource: "Winters, Manshreck and Wright, ch. 16 (A-A comparison to calibrate noise before trusting a diff, via a secondary summary)"
---

A diagnostician looking at one failing trace, or one snapshot of current
metrics, cannot easily tell abnormal from normal. Token rates, latencies and
tool-error rates vary from run to run, and each agent deployment's healthy
profile depends on its models, channels and workload.

The most direct evidence is a 2026 preprint, AgentChaosBench. A frontier model
diagnosing injected faults from a single trace named the fault type correctly
only 24.8% of the time. Pairing each faulty trace with a fault-free reference
trace of the same workflow raised context-overflow detection by 55 points. The
pairing did not help with guardrail bypass, so a baseline is not a universal
remedy (see the [agent runtime fault taxonomy](agent-runtime-fault-taxonomy.md)).

Two adjacent practices extend the idea. A deviation can only be read as signal
if a resting state was deliberately recorded first, so each system gets a
healthy fingerprint of token rate, tool-error rate, latency and memory. And
release engineering supplies the calibration step: run a system against
itself under identical inputs (an A-A comparison) to measure nondeterminism
and infrastructure noise before trusting any diff. Overall the evidence is
weak, resting on one preprint result and reasoning from adjacent practice.

For an agent that diagnoses other systems, the implication is to capture
references while those systems are healthy: reference traces for the
workflows that matter, and a fingerprint of key gauges together with how much
they vary under normal load. Diagnosis then becomes a diff against that
reference, which gives thresholds to any scoring step and gives the model
richer material than a summary would
([raw traces over summaries](../optimization/raw-traces-over-summaries.md)).
A clean trace from the same harness is also the comparison point when
[localising the root-cause step](root-cause-step-localisation.md). Because a
baseline describes one combination of image, model and configuration, it needs
recapturing whenever those change. Labelled faulty and fault-free traces come
cheaply from [fault-injection practice](practise-with-fault-injection.md).
