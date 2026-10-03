# Wiki authoring rules

These rules govern every note in the `wiki/` bundle. Read them before you
create or edit a note.

## Purpose

`wiki/` is a zettelkasten-style wiki of agentic engineering knowledge: prompt
and context engineering, harness and tool design, agent orchestration,
evaluation and the surrounding practice. It is read in two ways from the same
files:

- **By agents**, as external memory retrieved with `okf search` / `okf
  context` and followed one link at a time.
- **By people**, as a browsable docs site.

Both readers are served by the same principle, **progressive disclosure**: a
reader should be able to load exactly the notes they need, one link-hop at a
time. Nothing should force irrelevant material into context because a note was
scoped too broadly.

This repo holds curated notes only. Ingest material (fleeting notes,
literature notes, scoring caches) lives elsewhere and never lands here.

## Layout

One OKF bundle, `wiki/`, with one level of pillar folders:

| Folder           | Routing question                                                          |
| ---------------- | ------------------------------------------------------------------------- |
| _(root)_         | What is this field, where do I start, how does the model itself behave?   |
| `prompting/`     | What text do you write?                                                   |
| `context/`       | What goes in the window, in what order, at what budget?                   |
| `knowledge/`     | What lives outside the window, and how does it get back in?               |
| `reasoning/`     | What reasoning procedure do you induce or run within a call?              |
| `harness/`       | What does the agent see and touch?                                        |
| `orchestration/` | How are calls and agents composed over time?                              |
| `evaluation/`    | How do you know it works?                                                 |
| `optimization/`  | How does the system get improved automatically or improve itself?         |
| `security/`      | How are agents attacked and defended?                                     |
| `development/`   | How do humans build software with agents?                                 |

- A note's folder is chosen by the **routing question it answers**, not by
  its source or by topic keywords. Folders are a routing aid for readers.
  They are not a taxonomy: a note belongs to exactly one folder, and the
  link graph carries every other relationship.
- No nested subfolders. Adding or renaming a folder is a deliberate layout
  change, not something a single note does.
- Each folder has a `_directory.yml` with its title and routing question,
  and an `index.md` that `okf index --recurse` generates. Never hand-edit
  `index.md`. It is reserved in OKF, so retrieval doesn't see it.
- Filename = a descriptive kebab-case slug of the concept. The concept ID is
  the path without `.md` (for example `harness/tool-inventory`).

### Placement rule: prompting vs reasoning vs orchestration

> If the note is about **what text you write** (instruction wording, anatomy,
> examples as format or task signal, output structure), it goes in
> `prompting/`. If it is about **what reasoning procedure you induce or run**
> (step-by-step, decomposition, search, sampling and voting, self-critique,
> test-time compute), it goes in `reasoning/`, even when the procedure is
> triggered purely by prompt text. Few-shot exemplars whose job is to
> demonstrate a procedure go in `reasoning/`. A note about a multi-step
> _pipeline_ rather than a single call goes in `orchestration/`.

### Root notes

The root holds orientation concepts (`llm-agent`, `context-engineering`,
`prompt-engineering`, …) and model fundamentals (tokens, sampling,
logprobs, hallucination, model selection). These are entry points that the
pillars build on. Don't add pillar-specific material at the root.

## The atomicity rule

Each note captures exactly one concept, claim or technique: small enough to
state precisely, large enough to be useful on its own. If you find yourself
writing "and" between two ideas that could stand alone, split them. A note
should make sense on its own once the notes it links to (or that link to it)
have been read, without loading the whole wiki.

Before writing a new note, search the whole bundle (every folder) for an
existing note on the same concept. If one exists, extend it in place. Keep one
canonical note per concept across the whole bundle.

## Frontmatter (YAML, OKF-conformant)

```yaml
---
type: concept
title: Tool Inventory
description: >
  One sentence stating what this concept is and why it matters.
sources:
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), §3"
---
```

- `type: concept` for everything.
- `title`: a precise human-readable name.
- `description`: exactly one sentence. It is the search snippet and the docs
  site's lede, not a summary of the whole note.
- `sources`: the papers, books or posts the note draws on. Put a locator in
  `resource` (section, chapter or page range).
- No other fields. In particular, no `tags` (categorisation emerges from
  links) and no lifecycle fields (`generated`, `verified`, `status`,
  `stale_after`). This repo curates information, not lifecycle. When content
  goes out of date, revise or remove the note.

## Linking rule

Link concepts inline with CommonMark links, at the exact point in the prose
where the related concept comes up, never as a "See also" list at the end.
Use relative paths: `[tool inventory](tool-inventory.md)` within a folder, and
`[tool inventory](../harness/tool-inventory.md)` across folders.

- Links stay inside `wiki/`. Never link to another repository or bundle.
  Citations go in `sources:`, not in inline links.
- The bundle must never _depend_ on outside material to complete a thought.
  If a concept from a neighbouring field (security, requirements,
  observability, …) is genuinely the next hop, write it here at the depth
  agentic-engineering readers need.
- Choose outbound links by asking: once a reader has understood this note
  and wants to make progress on their task, which concept do they need next?
  Link forward towards utility and application. Don't link backwards towards
  citation or taxonomy. Zero links or several are both fine, so don't force
  links to meet a quota.

## No hub notes

Don't create overview, "map of content" or category notes, or any note that
exists to link out to everything. The generated folder `index.md` pages
provide browsing for the docs site. Everything else comes from inline links
between atomic notes. If part of the graph feels disconnected, add more
precise links between existing notes.
