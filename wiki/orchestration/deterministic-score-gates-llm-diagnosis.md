---
type: concept
title: A Deterministic Score Gates LLM Diagnosis
description: >
  A fixed, formula-based score built from a few observable variables should
  decide when to wake an LLM diagnostician, so the LLM is never the component
  that decides whether there is a problem.
evidence: weak
sources:
  - title: "Thinking, Fast and Slow"
    resource: "Kahneman, ch. 22, on formulas versus expert judgement"
  - title: "SE Radio 730: Birgitta Böckeler on Harness Engineering for AI Agents"
    resource: "Software Engineering Radio, July 2026 — https://se-radio.net/2026/07/se-radio-730-birgitta-boeckeler-on-harness-engineering-for-ai-agents/"
---

An agent that monitors and diagnoses other systems faces a design choice before
any diagnosis happens: who decides that there is a problem at all? If a large
language model (LLM) makes that call, every health check costs inference, the
judgement varies from run to run, and a degraded or manipulated model can talk
itself into or out of an incident.

Kahneman reports that, in low-validity settings, a few observable variables
scored on a simple scale and combined by formula beat holistic expert judgement
on both accuracy and consistency. The Apgar score for newborns is the worked
example, and overrides are reserved for rare decisive facts. By analogy, a
fixed health score built from a handful of observable system variables should
decide when to wake the LLM diagnostician. Because the transfer is from
research on human decision-making, the evidence is weak.

It does agree with harness-engineering practice. Birgitta Böckeler classifies
harness controls as computational or inferential and places cheap sensors first
([guides and sensors](../harness/guides-and-sensors.md)). Health checks,
process status, logs and vendor doctor commands are computational sensors, so
they should run before an LLM is involved. It is also an instance of
[non-LLM task implementation](non-llm-task-implementation.md): detection is a
classification task that a formula does more dependably than a model.

The result is a two-stage pipeline. Deterministic probes produce the inputs:
process and container state, readiness probes, doctor exit codes and
structured findings, and basic resource checks. A transparent formula combines
them. Only when the score crosses an agreed level does the agent spend
inference on diagnosis, and even then it [diagnoses by default and acts by
exception](../harness/diagnose-by-default-act-by-exception.md). Writing the
formula while calm, and versioning it with the runbooks, makes the decision to
investigate reproducible and auditable, even though the diagnosis that follows
is not. The gate sits naturally at the front of a [level-triggered reconcile
loop](level-triggered-reconcile-loop.md).
