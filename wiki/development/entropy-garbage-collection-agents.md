---
type: concept
title: Entropy Garbage Collection
description: >
  Agents copy existing patterns, bad ones included, so scheduled background
  agents should scan for drift from encoded "golden principles" and stale docs,
  then open small clean-up pull requests.
evidence: moderate
sources:
  - title: "Harness engineering: leveraging Codex in an agent-first world"
    resource: "Ryan Lopopolo, OpenAI, Feb 2026, 'Entropy and garbage collection' — https://openai.com/index/harness-engineering/"
  - title: "SE Radio 730: Birgitta Böckeler on Harness Engineering for AI Agents"
    resource: "Software Engineering Radio, July 2026, scheduled maintenance sensors — https://se-radio.net/2026/07/se-radio-730-birgitta-boeckeler-on-harness-engineering-for-ai-agents/"
---

A codebase or knowledge base that agents work in drifts. OpenAI's harness-engineering team observed that agents copy whatever patterns already exist, including bad ones, so a single shortcut can spread across a codebase. Documentation goes stale in the same way, and once stale docs are part of the agent's context they actively mislead it.

OpenAI's first response was manual: a weekly clean-up consuming about a fifth of the team's time. They replaced it with "golden principles" encoded in the repository plus recurring background Codex tasks that scan for deviations, update quality grades and open small refactor pull requests, most of which are merged automatically. A separate recurring doc-gardening agent opens fix-up pull requests against the documentation, supported by linters that check freshness and cross-links. Birgitta Böckeler's equivalent is the scheduled maintenance sensor, run weekly, at the slow end of her cost-ordered sensor placement in [guides and sensors](../harness/guides-and-sensors.md). The pattern resembles the toil-reduction jobs of site reliability engineering.

It depends on two things being in place: principles written down where an agent can check against them (the repository-as-system-of-record idea in [steering files as navigation pointers](../instructions/steering-files-as-navigation-pointers.md)), and changes small enough to review or auto-merge safely. Without the first, the clean-up agent has nothing to enforce; without the second, clean-up becomes a risky rewrite.

The agent's own instructions need the same treatment. Runbooks, skills and steering files rot as the tools and systems they describe change, so a scheduled pass that checks them against current documentation and command output is the doc-gardening equivalent for [sediment](../instructions/sediment.md). Where agents author and edit their own skills and memory, that is a live source of entropy in its own right, with its own controls, described in [self-authored skill drift](../instructions/self-authored-skill-drift.md). In every case the output of a clean-up pass is a small proposed change rather than an in-place rewrite, which keeps it consistent with [fixing the environment, not the output](../instructions/fix-the-environment-not-the-output.md).
