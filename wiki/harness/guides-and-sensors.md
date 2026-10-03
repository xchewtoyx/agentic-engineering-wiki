---
type: concept
title: Guides and Sensors
description: >
  Harness controls are feedforward guides (rules, docs) or feedback sensors
  (tests, analysis, reviewers), each computational or inferential; sensors
  are placed by cost, cheap ones locally and fuller ones later.
evidence: moderate
sources:
  - title: "SE Radio 730: Birgitta Böckeler on Harness Engineering for AI Agents"
    resource: "Software Engineering Radio, July 2026 — https://se-radio.net/2026/07/se-radio-730-birgitta-boeckeler-on-harness-engineering-for-ai-agents/"
  - title: "Harness engineering (martinfowler.com, Exploring Gen AI)"
    resource: "Birgitta Böckeler, Feb 2026, read via secondary summary — https://github.com/robyscar/ML_LLM_CLAUDE_SKILLS_Jamie-BitFlight_claude_skills/blob/main/research/evaluation-testing/harness-engineering-martin-fowler.md"
---

A harness accumulates many kinds of control: instruction files, linters, tests,
review agents, scheduled checks. Without a way to classify them it is hard to
see what is missing, what duplicates what, or where an expensive check is
running too often.

Birgitta Böckeler's framing, from her martinfowler.com article (read through a
secondary summary) and confirmed in her own words on SE Radio 730, sorts every
control along two axes. A **guide** acts before the agent does: AGENTS.md
files, rules, and computational guides such as codemods and OpenRewrite
recipes. A **sensor** acts after: tests, static analysis, and large language
model (LLM) reviewers. Each guide or sensor is either **computational**
(deterministic code) or **inferential** (judged by a model). Sensors are then
placed by cost, with cheap ones run locally, fuller ones at pre-commit, and
maintenance sensors on a weekly schedule. She also introduces
"harnessability", the observation that some codebases are easier to harness
than others, and advises assessing risk as probability times impact times
detectability while keeping humans accountable.

Böckeler is candid about open problems: measuring how effective sensors are,
conflicting constraints, guides going stale as models improve, and the sprawl
of dozens of markdown files.

The frame explains several neighbouring practices. Deterministic sensors are
what [back-pressure](back-pressure.md) means in practice, a short
[steering file that points rather than explains](../instructions/steering-files-as-navigation-pointers.md)
is a guide, and
[fix the environment, not the output](../instructions/fix-the-environment-not-the-output.md)
amounts to adding a guide or sensor after every failure. An LLM reviewer is an
inferential sensor in the role of a
[separate evaluator](../evaluation/separate-generator-from-evaluator.md).

For an agent that diagnoses or operates live systems, the frame suggests an
ordering, offered as an implication rather than a sourced claim: health checks,
status commands, logs and diagnostic tools are computational sensors and should
run before any LLM is involved. That is the same ordering argued in
[deterministic scores gate LLM diagnosis](../orchestration/deterministic-score-gates-llm-diagnosis.md).
