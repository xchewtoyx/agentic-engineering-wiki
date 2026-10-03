---
type: concept
title: Generator–Reflector–Curator Loop
description: >
  ACE's three-role architecture for self-improving contexts — a Generator solves
  tasks, a Reflector distills lessons from its trajectories, and a Curator
  turns them into delta updates that deterministic code merges into an
  evolving playbook.
sources:
  - title: "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models"
    resource: "ACE (Zhang et al.), Figs. 3–4, §3–3.2, §4, App. A.1–A.2, App. F"
---

Agentic Context Engineering (ACE) treats the agent's context as an evolving
**playbook** that improves from the agent's own experience, without updating
model weights. It splits the work into three specialized roles, extending the
single-role memory loop of Dynamic Cheatsheet. The rationale is to avoid
overloading one model call with every responsibility (acting, judging, and
editing the context at once):

1. **Generator** — answers the query or runs the task using the current
   playbook and produces a **trajectory**. Per §3.1 it also highlights which
   bullets were useful or misleading. The two published prompts differ:
   - **AppWorld (Fig. 9):** injects the playbook between delimiters
     (`PLAYBOOK_BEGIN … PLAYBOOK_END`) and says to read it first. It also says
     "treat the cheatsheet as a tool": use only the parts relevant to the task
     and otherwise use your own judgement, a hedge against stale or misleading
     bullets. The reproduced prompt has no explicit used-bullet output field.
   - **FINER (Fig. 12):** gets both the playbook and a reflection on previous
     mistakes. It outputs JSON with `reasoning`, `bullet_ids` (the bullets it
     used), and `final_answer`.
2. **Reflector** — critiques the trajectory (optionally over several
   **iterative refinement** rounds) and extracts concrete **insights**:
   what went wrong, why, and what to do instead. Contract:
   [reflector diagnostic prompt](reflector-diagnostic-prompt-contract.md).
3. **Curator** — turns insights into ADD-only **delta context items**. It
   does not edit the playbook itself: deterministic, non-LLM system code
   merges the deltas into the playbook, which feeds back to the Generator on
   the next query.
   Contract: [curator delta operations](curator-delta-operation-contract.md).

Data flow: Query → Generator → trajectory → Reflector → insights → Curator →
delta items → deterministic merge → playbook → Generator.

The same loop serves two settings:

- **Offline** — optimizing a system prompt over a training split before
  deployment (the playbook becomes the shipped prompt).
- **Online** — test-time memory adaptation, where the playbook keeps updating
  as the deployed agent processes a stream of queries.

Instead of condensing what was learned into terse summaries or static
instructions (the [brevity bias](brevity-bias.md) failure), the playbook is
meant to accumulate detailed, domain-specific strategies, tool usage notes,
and even ready-to-use code.

Key design choices that make the loop work:

- The playbook is an [itemized bullet context](itemized-bullet-context.md),
  not a monolithic prompt.
- Updates are [incremental deltas](incremental-delta-context-updates.md)
  merged deterministically, kept compact by
  [grow-and-refine maintenance](grow-and-refine-context-maintenance.md).
- Separating evaluation/insight extraction (Reflector) from curation (Curator)
  is the first of ACE's claimed innovations and is credited with higher
  context quality; it mirrors the [critique–optimizer separation](critique-optimizer-separation.md)
  found in textual-optimization systems: one role diagnoses, another edits.
- The Curator's output is merged by **lightweight, non-LLM logic**: the merge
  is deterministic, never an LLM rewrite of the whole playbook. Because deltas
  are itemized and localized, the authors argue that many can be **merged in
  parallel** for batched adaptation. The reported runs use batch size 1, so
  that benefit is claimed rather than measured.
- **Multi-epoch adaptation**: offline, the same training queries can be
  revisited for several passes so the playbook is progressively strengthened.

**Model-agnostic (per App. A.1).** The loop operates only on execution
traces and deltas. All three roles were switched to GPT-OSS-120B, GPT-5.1,
and Llama-3.3-70B with no algorithm change, and ACE beat base and GEPA on
every backbone tested. The margins were "often" 5–12 points on AppWorld and
finance. They were much smaller on Llama-3.3-70B (FiNER only: +2.4 offline
with labels). The authors attribute the smaller Llama gains to noisier
reflections from weaker models (see
[feedback dependence](context-adaptation-feedback-dependence.md)). Offline,
with DeepSeek-V3.1, the loop also improved DDXPlus medical diagnosis (+15.0 vs
GEPA +1.2) and BIRD-SQL Text-to-SQL (+5.1 vs +4.4; ACE gained most on the
Simple subset, GEPA more on Moderate and Challenging). These are single
benchmarks per domain, not broad domain coverage.
For where the token budget goes, see the
[cost profile](context-adaptation-cost-profile.md).

**Offline warmup, then online.** On AppWorld, the best online configuration
first builds the playbook offline on the training split, then keeps adapting
at test time. This added about +3.4 average over cold-start online adaptation
(59.5 vs 56.1, DeepSeek-V3.1, no labels). For context, the top AppWorld
leaderboard entry (IBM CUGA, GPT-4.1, 60.3 average) is a reference point,
not a controlled baseline. Offline ACE (59.4) roughly matched its average.
The warmed-up online run beat it on test-challenge by 8.4 TGC and 0.7 SGC. Reference configuration: batch
size 1 (one delta per sample), up to 5 Reflector rounds, up to 5 offline
epochs. For evaluation controls, see
[self-adapting context evaluation protocol](self-adapting-context-evaluation-protocol.md).
