---
name: agentic-wiki
description: Look up agentic engineering knowledge — prompting, context and memory, reasoning techniques, tool/harness design, agent orchestration, evaluation, automated optimization, agent security, and building software with coding agents. Use when designing, debugging, or reviewing an LLM-based agent or application and you want grounded, sourced guidance rather than recall.
---

# Agentic engineering wiki

The wiki is the `wiki/` folder at this plugin's root (two levels up from this
file: `../../wiki/`). It holds ~420 atomic concept notes. Each note has a
`title`, a one-sentence `description`, and `sources:` frontmatter, and
connects to related notes with inline relative links.

**Retrieval model: route → find a seed → follow links.** Load one relevant
note, then pull in only the next note your task actually needs, one hop at a
time. Never load a whole folder.

## 1. Route to a folder

| If the question is…                                                     | Look in          |
| ----------------------------------------------------------------------- | ---------------- |
| What is this, where do I start, how does the model behave (tokens, sampling, logprobs, hallucination, model choice)? | `wiki/` (root)   |
| What text do I write (instructions, examples, format, output structure)? | `prompting/`     |
| What goes in the window, in what order, at what budget?                  | `context/`       |
| What lives outside the window — RAG, retrieval, memory, knowledge bases? | `knowledge/`     |
| What reasoning procedure do I induce (CoT, decomposition, voting, search)? | `reasoning/`   |
| What does the agent see and touch (tools, ACI, observations, approvals)? | `harness/`       |
| How are calls and agents composed (loops, planning, workflows, multi-agent)? | `orchestration/` |
| How do I know it works (graders, eval suites, pass@k, ablations)?        | `evaluation/`    |
| How does it improve automatically (TextGrad, DSPy, harness evolution)?   | `optimization/`  |
| How is it attacked and defended (injection, guardrails)?                 | `security/`      |
| How do humans build software with agents (specs, ambiguity, patches)?    | `development/`   |

Questions often span two folders, such as a tool-use failure, which touches
`harness/` and `orchestration/`. Check each candidate. Each folder's
`index.md` lists its notes with their descriptions, which makes it a cheap
scan when you don't know the vocabulary.

## 2. Find a seed note

**With `okf` available** (the repo's `okf-core.toml` names the bundle
`agentic-engineering`):

```sh
okf search --bundle agentic-engineering "<query>" --limit 10
okf list-concepts --bundle agentic-engineering | jq '.concepts[] | {concept_id, description}'
```

Search is lexical (FTS5/BM25). If the first query misses, try two or three
vocabulary variants before you conclude the wiki has no coverage.

**Without `okf`:** read the routed folder's `index.md`, or grep titles and
descriptions:

```sh
grep -rl -i "<term>" wiki/<folder>/ | head
```

## 3. Load and follow links

```sh
okf context --bundle agentic-engineering --seed <concept-id> --depth 1 --budget-chars 12000
```

Without `okf`, read the seed note's file and open its inline links by hand.
They are relative paths and can cross folders (`../harness/tool-inventory.md`).

## Reading discipline

- **Stay progressive.** Follow a link only when the current note invokes a
  concept your task needs next. Stop once the question is answered.
- **Cite what you use.** When the wiki backs a recommendation, name the
  concept note and its `sources:` entry, not just the conclusion.
- **Report gaps honestly.** If sensible vocabulary variants across the
  likely folders come up empty, say that the wiki doesn't cover the topic.
  Don't fill the gap from recall and present it as wiki content.
- **This content changes fast.** Notes describe techniques as their sources
  reported them. When a claim depends on model capability or a specific
  vendor's API, check the source's date before you treat it as current.
