---
type: concept
title: Sediment
description: >
  Without a pruning discipline, agent documents accumulate stale layers
  because adding feels safe and removing feels risky; checking each line for
  relevance, and deleting no-ops by testing against the model's default,
  keeps them live.
evidence: moderate
sources:
  - title: "mattpocock/skills, writing-for-agents skill"
    resource: "https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md (read 2 Oct 2026, v1.2.3)"
  - title: "mattpocock/skills, retro skill"
    resource: "https://github.com/mattpocock/skills/blob/main/skills/engineering/retro/SKILL.md (read 2 Oct 2026)"
---

Sediment is Matt Pocock's name for the default fate of an unpruned agent document: stale layers settle because adding a line feels safe and removing one feels risky, until you have to core down through them to find what is still live. The pressure to add is real and healthy, since each mistake should [become a change to the environment](fix-the-environment-not-the-output.md); sediment is what happens when nothing pushes the other way.

The counter is a relevance check on every line. A line loses relevance either by never bearing on the task (exposition, or a branch that should have been [disclosed](information-hierarchy.md)) or by going stale as the behaviour it describes changes. Shorter documents are easier to keep relevant.

No-op hunting, from [lean skill instructions](lean-skill-instructions.md), is sharpened in two ways. The test is model-relative, not reader-relative: whether a sentence changes behaviour versus the model's default is settled by running the document, not by debate. When a sentence fails, delete the whole sentence rather than trimming words. The same test grades [leading words](leading-words-in-agent-instructions.md): a word too weak to beat the default ("be thorough") is a no-op, and the fix is a stronger word ("relentless"), not a different technique.

His `retro` skill operationalises this, with "no-ops" and an oversized `AGENTS.md` as standing categories to inspect after a session. At repository scale the same job can be handed to a scheduled agent, as in [entropy garbage collection](../development/entropy-garbage-collection-agents.md), and when the agent writes its own skills an automatic stale-and-archive lifecycle is one defence, as in [self-authored skill drift](self-authored-skill-drift.md).

Boundary: a line can look like a no-op to a reader yet change model behaviour; only a run decides.
