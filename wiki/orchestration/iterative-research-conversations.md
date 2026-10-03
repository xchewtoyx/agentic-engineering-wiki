---
type: concept
title: Iterative Research Conversations
description: >
  A bounded question-answer loop lets retrieved evidence expose gaps and drive
  deeper follow-up searches during agentic research.
sources:
  - title: "Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models"
    resource: "Shao et al. (2024), full paper, pp. 1–27"
---

Model research as a conversation between a question-asking writer and a
source-grounded expert. Each answer becomes context for the next question, so
newly discovered details can reveal missing evidence and induce deeper
follow-ups. Decompose complex questions into search queries, filter results for
source quality, synthesize only supported answers, and accumulate the retained
references.

Bound both the number of [perspective-guided](perspective-guided-research.md)
branches and rounds per branch. This makes discovery depth and cost explicit
while avoiding a single static query's dependence on what the agent knew before
research began.
