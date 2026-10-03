---
type: concept
title: Single Source of Truth and Cache
description: >
  Each meaning in agent documentation should live in one authoritative place,
  and any document restating what the environment already says (scripts,
  config, layout, --help) is a cache that only earns its load when the lookup
  is expensive or the knowledge is unwritten.
evidence: moderate
sources:
  - title: "mattpocock/skills, writing-for-agents skill"
    resource: "https://github.com/mattpocock/skills/blob/main/skills/productivity/writing-for-agents/SKILL.md (read 2 Oct 2026, v1.2.3)"
  - title: "mattpocock/evalite and mattpocock/sandcastle, CLAUDE.md"
    resource: "https://github.com/mattpocock/evalite, https://github.com/mattpocock/sandcastle (read 2 Oct 2026)"
---

Duplication, the same meaning in more than one place, costs maintenance and tokens, and it inflates that meaning's prominence beyond its real rank. A [leading word](leading-words-in-agent-instructions.md) is the deliberate inverse: it repeats a token on purpose, never the meaning.

Matt Pocock's `writing-for-agents` skill extends single source of truth to the environment. `package.json` scripts, config files, directory layout and `--help` output are sources of truth, and a document that restates them is a cache of a lookup. A cache goes stale and only earns its load when the lookup is expensive. What deserves writing down is what the agent cannot find by looking: the unwritten convention, the reason behind a choice, the gotcha no config confesses.

His repositories show the shift. `evalite`'s `CLAUDE.md` is a long `/init`-style file that restates build commands, pnpm filter syntax and architecture. `sandcastle`'s, the newest, is a few lines: the typecheck command, a pointer to the glossary for terminology, the changeset convention, and pointers to agent docs. `ts-reset`'s is three lines, each a convention or gotcha. That short, pointer-heavy shape is the one described in [steering files as navigation pointers](steering-files-as-navigation-pointers.md).

Boundary: a cache is justified when the source is slow or scattered, such as pulling decisions out of years of upstream issue threads, which is what [out-of-scope records](../development/out-of-scope-records.md) do for declined requests.
