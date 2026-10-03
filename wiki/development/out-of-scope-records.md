---
type: concept
title: Out-of-Scope Records
description: >
  A repository folder of short decision records for rejected feature requests,
  each with the decision, reason and prior requests, gives agents and triagers
  durable memory of what the project has deliberately declined.
evidence: moderate
sources:
  - title: "mattpocock/ts-reset and mattpocock/sandcastle, .out-of-scope folders"
    resource: "https://github.com/mattpocock/ts-reset, https://github.com/mattpocock/sandcastle (read 2 Oct 2026)"
  - title: "mattpocock/skills, triage skill (OUT-OF-SCOPE.md)"
    resource: "https://github.com/mattpocock/skills/tree/main/skills/engineering/triage (read 2 Oct 2026)"
---

Matt Pocock's recent repositories carry a `.out-of-scope/` folder of one-file records, one per declined idea. Each states the decision, the reasoning, and the prior requests that asked for it, by issue number. `ts-reset` has six (for example, typing a Promise rejection as `Error`, declined because it contradicts the library's own `unknown` catch typing and is better enforced by a lint rule). `sandcastle` has eight, mostly about features that would bloat the core.

The records are the negative counterpart to architecture decision records. Those say why the system is the way it is; out-of-scope records say why it is not some other way. For an agent doing triage, they turn "has this been asked before, and why was it refused?" from a search through closed issues into a file read, which is the case where a [cache](../instructions/single-source-of-truth-and-cache.md) is worth paying for. The `triage` skill in his skills repository carries its own guidance file for the convention, naming two purposes: institutional memory of why something was rejected, and deduplication so a repeat request surfaces the earlier decision instead of re-litigating it.

It fits his broader pattern of memento-driven development: write the repository for a colleague who wakes with no memory every morning, which is the agent's permanent condition and the reason [tacit knowledge](tacit-knowledge-erosion-under-ai-assisted-work.md) has to be made explicit.

Boundary: a record only helps if triage checks it; without a pointer from the triage workflow it becomes [sediment](../instructions/sediment.md).
