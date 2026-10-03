---
type: concept
title: Context Adaptation Feedback Dependence
description: >
  A self-adapting context's gain depends on what feedback its reflection step
  sees (ground-truth labels, execution signals, or neither), and weak or absent
  signals can make adaptation worse than none.
sources:
  - title: "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models"
    resource: "ACE (Zhang et al.), §4.3–4.4, §5, App. A.1, App. F"
---

[Context adaptation](context-adaptation.md) learns only from what its
reflection step can observe. A [Reflector](reflector-diagnostic-prompt-contract.md)
can be grounded in any of these:

- **Ground-truth labels** (reference code plus unit-test reports in the
  AppWorld prompts; reference answers in the FINER prompts). This is the strongest signal. It can feed offline or online
  adaptation; in online runs the label is revealed only after the prediction
  (for example, in ACE's online runs with labels). Real deployments usually
  lack labels, so in practice labels tend to be limited to an offline
  training split. That is a deployment constraint, not a limit of online
  mode.
- **Natural execution feedback** (errors, API responses, task-completion
  checks from the environment). This needs no labels, so it is what a
  deployed online system usually has.
- **Nothing reliable**. The Reflector must judge correctness by itself.

What App. A.1 shows across model families (results cover only AppWorld,
FiNER, and Formula):

- **AppWorld**, an agent benchmark with rich execution feedback: label-free
  adaptation was competitive. Offline ACE without GT nearly matched or
  exceeded the with-GT variant (39.4 vs 40.5 on GPT-OSS-120B; 61.3 vs 60.2 on
  GPT-5.1, Test-Normal only). Online, label-free adaptation from execution
  feedback gave the largest AppWorld gains (+7.6 and +11.6 over the ReAct
  base).
- **Finance (FiNER, Formula)**: labels mattered more. Offline with GT reached
  +12.1 (GPT-OSS-120B) and +9.5 (GPT-5.1) over base. Without GT it was about
  4–5 points lower, and online ACE did not match offline-with-GT.
- **Dynamic Cheatsheet (cumulative, online)** fell *below* the unadapted base
  on finance with both of those backbones (−8.2 and −3.8). The authors
  attribute such regressions to unreliable feedback polluting the context.
  Full-rewrite updates prone to [context collapse](context-collapse.md) are a
  plausible contributing factor.
- Gains were smaller on Llama-3.3-70B (FiNER only). The authors attribute
  this to noisier reflections from weaker models.

Design implications:

- Before enabling online self-adaptation, check that the environment returns
  a signal that distinguishes success from failure. If it doesn't, and labels
  exist only for a training split, adapt offline against them and ship the
  frozen context.
- Silent-correctness failures (code runs and the answer is wrong) can't be
  seen from execution success alone. If you want them learned without labels,
  add test-style checks to the environment (a design inference, not a
  measured result).
- Keep a no-adaptation baseline in the offline regression suite. Adaptation
  that regresses below it is a real, observed outcome.

Headline backbone (DeepSeek-V3.1):

- **AppWorld, offline:** with labels +17.0, without labels +14.8. The
  authors credit naturally available signals, such as code execution success
  or failure, for the label-free result.
- **Financial tagging, online without labels:** ACE scored 67.3 against a
  70.7 base, and Dynamic Cheatsheet fell below base on both finance tasks. The
  context "can be polluted by spurious or misleading signals". Offline,
  Formula held up much better without labels (83.0 vs 85.5) than FiNER did
  (71.1 vs 78.3). The authors list formula correctness among the "rich
  feedback" signals.

The underlying limitation is that the method needs a reasonably strong
Reflector. If the Reflector can't extract meaningful insights from the traces
and outcomes, the context becomes noisy or even harmful. In a domain where no
available model can produce useful insights, the context will lack them. Full
rewrite memories have the same dependency on how well the model curates.
