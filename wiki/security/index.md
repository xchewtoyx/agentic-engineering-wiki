# Concept

* [Agent System-Level Defenses](agent-system-level-defenses.md) - Isolation, approval gates, scope filters, and input/output guardrails that contain damage when prompt defenses fail on a tool-using agent.
* [ChatML Injection Resistance](chatml-injection-resistance.md) - Reserved role-marker tokens can't be produced by ordinary user text, so an API caller is structurally confined to the user role and cannot fake turns.
* [Confused Deputy](confused-deputy.md) - An agent holding legitimate tool authority is steered by untrusted content into spending that authority on an attacker's instruction instead of its user's — the authority is real, only its source of direction is hijacked.
* [Defensive Prompt Engineering](defensive-prompt-engineering.md) - Design system prompts and input handling so untrusted user content cannot override developer instructions or exfiltrate privileged context.
* [Indirect Prompt Injection](indirect-prompt-injection.md) - Malicious instructions planted in tool outputs or retrieved documents that the agent treats as trusted commands once they enter context.
* [Input Output Guardrails](input-output-guardrails.md) - Harness checks on prompts and generations that block leaks, attacks, and bad outputs — with explicit policies per failure mode and false-refusal awareness.
* [Instruction Hierarchy](instruction-hierarchy.md) - Train and design so conflicting instructions resolve toward higher-privilege layers — system over user over model output over tool output.
* [Jailbreaking and Prompt Injection](jailbreaking-and-prompt-injection.md) - Subverting safety features or injecting malicious instructions so the model follows attacker goals instead of developer policy.
* [Memory Hacking](memory-hacking.md) - Adversarial conversation that implants false past events into an agent’s durable memory — a retrieval/reflection risk beyond ordinary prompt injection.
* [Prompt Extraction](prompt-extraction.md) - Attacks that trick a model into revealing its system prompt or privileged context so an application can be replicated or exploited.
* [Prompt-Level Attack Defenses](prompt-level-attack-defenses.md) - Explicit refuse rules, reinforced system instructions, and known-attack preemption inside the prompt — useful layers that never guarantee obedience.
* [Publish-State Protection Guard](publish-state-protection-guard.md) - Once an agent's own end-state check passes, intercept later destructive commands against that verified output at the tool level so a "tidy up" pass cannot erase what was just proven correct.
* [Safe Search Argument Passing](safe-search-argument-passing.md) - Wrap agent search queries so strings that look like CLI flags (e.g. --notes) are never parsed as options by underlying grep/find tools.
