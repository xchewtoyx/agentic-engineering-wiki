---
type: concept
title: Prompt Evolution vs Playbook Accumulation
description: >
  Choose between evolving whole candidate prompts (GEPA-style) and accumulating
  itemized insights by delta updates (ACE-style) based on how many granular,
  long-lived rules the task needs to retain.
sources:
  - title: "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models"
    resource: "ACE (Zhang et al.), §2.2, §4.2–4.4, §5, App. B–C, App. F (Figs. 6–9)"
---

Both families are [context adaptation](context-adaptation.md): they improve
behaviour by editing inputs, not weights. They differ in what is optimized and
how it is updated, and so suit different tasks.

| | Prompt evolution (e.g. GEPA) | Full-rewrite memory (e.g. Dynamic Cheatsheet) | Playbook accumulation (e.g. ACE) |
|---|---|---|---|
| Artifact | One instruction prompt | One cheatsheet document | [Itemized bullet context](itemized-bullet-context.md) |
| Update | Propose whole-prompt variants from rollouts + reflective feedback; select by evaluator score under a rollout budget | Regenerate the whole cheatsheet each step, or write a fresh summary from retrieved examples | Curator writes only new insights; [deterministic delta merge](incremental-delta-context-updates.md) |
| Typical win | Short, transferable instructions | Short reusable heuristics and code snippets on independent single-turn queries | Many granular rules, procedures, edge cases retained over long horizons |
| Characteristic risk | [Brevity bias](brevity-bias.md) | [Context collapse](context-collapse.md) | Unbounded growth; needs [grow-and-refine](grow-and-refine-context-maintenance.md) |

Selection heuristics:

- **Independent, single-turn reasoning** (the AIME, Game-of-24, and GPQA
  setting where Dynamic Cheatsheet was mainly evaluated): reported gains there
  came from short reusable heuristics and code snippets. A compact evolved
  prompt or short cheatsheet may be enough. ACE did not test this setting
  head-to-head.
- **Multi-turn agents** with step-by-step procedures and tool-use rules, and
  **knowledge-intensive domains** with many specific rules and edge cases,
  favour accumulation. The evidence is AppWorld, FiNER, and Formula, plus
  single extra benchmarks for medical diagnosis and Text-to-SQL. The authors
  argue such knowledge is hard to compress into one instruction without
  losing detail.
- Need **per-rule bookkeeping** (which entry helped or hurt, targeted
  refinement, de-dup, stable earlier rules across a long run)? An itemized
  representation supports this directly. Whole-prompt candidates are
  optimized end to end, so there is no built-in per-rule attribution.

Agent-memory systems sit near the accumulation end with different units:
reusable workflows induced from trajectories (Agent Workflow Memory), cached
plan templates for cheap re-execution (agentic plan caching), linked
Zettelkasten-style notes ([Zettelkasten agent memory notes](../knowledge/zettelkasten-agent-memory-notes.md)),
and composed skills ([skill library](../orchestration/skill-library.md)). Playbook accumulation
generalizes the idea beyond memory to system prompts and evidence.

Mechanics of the prompt-evolution side. GEPA (Genetic-Pareto) collects
execution traces, uses natural-language reflection to diagnose errors and
assign credit, and proposes prompt updates. A genetic search keeps a
**Pareto frontier** of high-scoring prompts to avoid local optima. MIPROv2
instead jointly optimizes instructions and demonstrations by Bayesian
optimization (see
[instruction vs demonstration optimization](instruction-vs-demonstration-optimization.md)).

Measured gap (DeepSeek-V3.1, offline, labels available). On AppWorld, ACE
beat ICL by 12.3 and GEPA by 11.9 average points; MIPROv2 was not run there.
On FiNER and Formula, it beat ICL, MIPROv2, and GEPA by 10.9 points on
average. The authors attribute the gap to tasks that need precise domain
knowledge and tool rules beyond what fixed demonstrations or one optimized
prompt hold. On BIRD-SQL the gap was small (+5.1 vs GEPA +4.4), and GEPA
gained more on harder queries.

When a detailed playbook is *not* worth it:

- Multi-hop QA such as HotPotQA often benefits more from concise, high-level
  instructions (how to retrieve and synthesize evidence) than from a long
  context.
- Fixed-strategy tasks such as Game of 24 may need a single reusable rule.
  Extra context there is just redundancy.

Accumulation pays off when a task needs detailed domain knowledge, complex
tool use, or environment-specific strategies beyond what the model's weights
or a simple system prompt already provide.

What the artifacts look like in practice (AppWorld). All three methods
share one agent scaffold: a supervisor framing, a Python REPL, API-discovery
calls, and standing rules such as "read the API spec before calling",
"verify before irreversible changes", and "loop over page_index". They differ
in what gets added:

- **Evolved prompt (GEPA):** the scaffold followed by hard-coded
  "Domain-Specific Strategy for … Tasks" sections (bill splitting, file
  organization, playlists, alarms). These are task-family procedures baked
  into one static prompt, with no per-rule identity. Presumably, covering a
  new task family would take another whole-prompt evolution round.
- **Cheatsheet (Dynamic Cheatsheet):** the scaffold plus a delimited
  `CHEATSHEET` block and fixed guidance on using it (analyze and pick
  strategies, explain before concluding, write self-contained code without
  hard-coded local paths). The cheatsheet content is regenerated wholesale.
- **Playbook (ACE):** the scaffold plus a delimited playbook of
  [ID-tagged bullets](itemized-bullet-context.md), with an instruction to use
  only the relevant parts. It grows by delta.
