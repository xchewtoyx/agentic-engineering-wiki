---
type: concept
title: Budget-Matched Agent Ablation
description: >
  Hold total queries or model calls constant when ablating an orchestration
  component so quality gains are not confused with extra compute.
sources:
  - title: "Assisting in Writing Wikipedia-like Articles From Scratch with Large Language Models"
    resource: "Shao et al. (2024), full paper, pp. 1–27"
---

Removing a planning or orchestration component often changes the number of
queries, turns, or references gathered. Compare variants under a fixed total
question or call budget to isolate the component's structure from the benefit
of simply spending more inference compute.

For iterative research, replace adaptive follow-ups with the same number of
batch questions rather than with fewer questions. A large quality and source-
diversity loss under equal budget is evidence for the conversational control
flow itself. Use this alongside
[component-level harness ablation](component-level-harness-ablation.md) when
architecture components also interact non-additively.
