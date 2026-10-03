---
type: concept
title: Harness Memory Strategy Spectrum
description: >
  Harness memory ranges from linear unbounded history through recursive
  summarisation, pluggable condensers and threshold compaction to persistent
  agent-authored memory files, and knowing which design is in play is the
  first step in debugging a memory problem.
evidence: moderate
sources:
  - title: "Harness Engineering"
    resource: "Barbaste et al. (Wavestone AI Lab), arXiv 2609.00006, July 2026 preprint, §9 and Table 5 — https://arxiv.org/html/2609.00006v1"
  - title: "Hermes Agent docs: Memory"
    resource: "Nous Research — https://hermes-agent.nousresearch.com/docs/user-guide/features/memory"
  - title: "OpenClaw docs: Memory"
    resource: "OpenClaw — https://docs.openclaw.ai/concepts/memory"
  - title: "OpenClaw docs: Agent workspace"
    resource: "OpenClaw — https://docs.openclaw.ai/concepts/agent-workspace"
  - title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
    resource: "Lin, Liu, Pan et al., arXiv 2604.25850, 28 Apr 2026 preprint, §4.4.1 — https://arxiv.org/html/2604.25850v1"
---

"Memory" covers very different designs across agent harnesses. A harness that
keeps everything behaves differently under load from one that summarises, and
both differ from one where the agent writes its own notes. The conceptual
vocabulary ([agent memory tiers](agent-memory-tiers.md),
[memory management](memory-management.md),
[OS-inspired agent memory](os-inspired-agent-memory.md)) says what a memory
system must do; this note is about where shipped harnesses actually sit.

The Wavestone study of eleven harnesses (a July 2026 preprint) sorts memory
strategies into five types:

1. linear unbounded history (Mini-SWE-Agent);
2. recursive summarisation (Aider), a direct use of
   [memory summarization](memory-summarization.md);
3. pluggable condensers (OpenHands);
4. threshold compaction (Gemini CLI, Mistral Vibe, Hermes, Pi, OpenCode);
5. persistent cross-session memory files authored by the agent (Codex), a form
   of [self-directed memory management](self-directed-memory-management.md).

The taxonomy is a preprint's, so treat it as a useful vocabulary rather than an
established classification. The Agentic Harness Engineering ablation (also a
preprint) found long-term memory to be the single largest isolated component
gain, at 5.6 points on Terminal-Bench 2.

Two documented harnesses show how much the details matter even within one type.
**Hermes** compacts by threshold and keeps a deliberately bounded memory:
MEMORY.md is capped at 2,200 characters and USER.md at 1,375. Both are injected
as a frozen snapshot at session start, so the prompt cache is preserved and
writes appear only in the next session. Memory does not auto-compact; an
over-limit write errors and the agent must consolidate. The docs warn against
pointing two agent processes at one memory home. **OpenClaw** keeps memory as
plain Markdown in the workspace with no hidden state: daily logs, a curated
MEMORY.md loaded only in the main private session, and an optional summary file.
Memory is unbounded on disk, injection is capped by bootstrap budgets (20,000
characters per file, 60,000 in total), and notes are flushed to memory before
each compaction.

Those details turn into diagnostic questions. An agent that "ignores" a fact it
just saved may be running on a frozen snapshot until the next session; a failing
memory write may be a size-cap error rather than corruption; an agent missing
context may be hitting injection truncation limits rather than losing data.
Compaction-based designs need [safeguarded compaction](../context/safeguarded-compaction.md);
designs where the model rewrites its own memory risk
[context collapse](../optimization/context-collapse.md); and the more structured
designs converge on the storage-versus-presentation split in
[context as a compiled view](../context/context-as-compiled-view.md).
