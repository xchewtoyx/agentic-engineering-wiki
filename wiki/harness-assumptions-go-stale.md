---
type: concept
title: Harness Components Encode Stale Assumptions
description: >
  Each harness component encodes an assumption about something the model
  cannot do, so components should be re-tested and removed when the model
  changes, as with dropped context resets and an 80% system-prompt cut.
evidence: moderate
sources:
  - title: "Scaling Managed Agents: Decoupling the brain from the hands"
    resource: "Anthropic Engineering, 8 Apr 2026 — https://www.anthropic.com/engineering/managed-agents"
  - title: "Harness design for long-running application development"
    resource: "Prithvi Rajasekaran, Anthropic Engineering, 24 Mar 2026 — https://www.anthropic.com/engineering/harness-design-long-running-apps"
  - title: "The new rules of context engineering for Claude 5 generation models"
    resource: "Thariq Shihipar, claude.dev, 24 Jul 2026 — https://claude.dev/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models/"
  - title: "SE Radio 730: Birgitta Böckeler on Harness Engineering for AI Agents"
    resource: "Software Engineering Radio, July 2026, open problems — https://se-radio.net/2026/07/se-radio-730-birgitta-boeckeler-on-harness-engineering-for-ai-agents/"
  - title: "Harness engineering: leveraging Codex in an agent-first world"
    resource: "Ryan Lopopolo, OpenAI, Feb 2026, entropy and garbage collection — https://openai.com/index/harness-engineering/"
---

Harness components accumulate. Each one was added to fix something, and once it
works nobody asks whether it is still needed. When the underlying model
improves, some of those components stop helping and start costing context,
latency or quality.

Anthropic states the principle directly: every harness component encodes an
assumption about what the model cannot do on its own, and those assumptions go
stale. Rajasekaran's long-running-apps post gives the clearest case. Context
resets (a fresh agent plus a structured handoff) cured the "context anxiety"
seen in Sonnet 4.5; Opus 4.5 largely lost that behaviour, so resets were dropped
in favour of the software development kit's (SDK's) auto-compaction. The
Managed Agents post calls the old resets dead weight. Rajasekaran's post adds
that an evaluator agent is worth its cost only when the task is beyond what the
model does reliably alone, and that each new model release is the moment to
strip pieces that are no longer load-bearing.

The largest reported cut is in the claude.dev "new rules" post: Anthropic
removed more than 80% of Claude Code's system prompt for Claude 5-generation
models with no measurable loss on coding evaluations. The post frames this as
six replacements of old rules with new ones: rules give way to judgement,
examples to interface design, everything-upfront to
[progressive disclosure](instructions/progressive-disclosure.md), repetition to
simple tool descriptions, memory in CLAUDE.md to auto-memory, and simple specs
to rich references such as test suites. Böckeler lists stale guides as an open
problem for the field. OpenAI's emphasis differs: encode taste once and keep
cleaning, rather than plan for removal.

The practical rule is to record why each prompt section, guard and helper agent
exists, so it can be re-tested when the model behind it changes, using the
[in-loop regression control](optimization/in-loop-regression-control.md) that
guards any harness edit. Components that look most exposed include the
reset-versus-compaction choice
([compaction vs context reset](context/compaction-vs-context-reset.md)) and a
[separate evaluator](evaluation/separate-generator-from-evaluator.md). This is
the deliberate, removal-oriented side of
[harness drift awareness](evaluation/harness-drift-awareness.md), which tracks
behaviour shifts nobody chose; the same model-specificity is why
[harness as a performance lever](harness-as-performance-lever.md) needs
re-adaptation on every model change. The debate over how much harness to keep at
all is in [thin vs thick harness](thin-vs-thick-harness-debate.md).
