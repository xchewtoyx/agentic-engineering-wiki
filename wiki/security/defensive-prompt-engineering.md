---
type: concept
title: Defensive Prompt Engineering
description: >
  Design system prompts and input handling so untrusted user content cannot
  override developer instructions or exfiltrate privileged context.
sources:
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 5"
  - title: "SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering"
    resource: "SWE-agent (Yang et al.), pp. 106–118 (Appendix E)"
---

Once an application is live it faces intended users and attackers. Three attack
families matter for harness design:

1. [Prompt extraction](prompt-extraction.md) — stealing system prompts or
   privileged context.
2. [Jailbreaking and prompt injection](jailbreaking-and-prompt-injection.md) —
   getting the model to violate policy or follow attacker instructions.
3. Information extraction — eliciting training data or sensitive context.

Impact includes remote tool/code execution, data leaks, social harm,
misinformation, service subversion, and brand damage. Risk grows with
capability: better instruction-following also means better malicious-instruction
following, and models struggle to distinguish privileged
[system prompts](../harness/system-prompt-architecture.md) from user text once concatenated.

**Why there is no single structural fix.** SQL injection is closed by
parameterized queries because SQL has a rigid, machine-checkable boundary
between query and bound values. Natural language has none: the model decides
what counts as an instruction by inference over meaning, and instructions can
be encoded implicitly (a roleplay framing, a directive buried in retrieved
text) in ways no parser can reject outright. Prompt injection is the same root
cause — untrusted content interpreted as instruction — on an interface that
cannot enforce the separation, so defense is necessarily layered. Indirect
injection additionally turns the agent into a
[confused deputy](confused-deputy.md): its tool authority is real, and the
attacker's goal is to get that authority spent on their instruction.

Defense is layered — model ([instruction hierarchy](instruction-hierarchy.md)),
prompt ([prompt-level attack defenses](prompt-level-attack-defenses.md), which
raise the cost of an injection but are mitigations, not boundaries), and system
([agent system-level defenses](agent-system-level-defenses.md): isolation,
[human approval gates](../harness/human-approval-gates.md), least-privilege tool
scoping, [input/output guardrails](input-output-guardrails.md)). The system
layer matters most because it does not assume the model resisted the attempt —
it bounds what a successful injection can accomplish, even against a novel
technique that defeats every layer above. Size that layer against the adversary
actually in scope: a container sandbox contains accidental damage from
untrusted-but-benign code, but is not equivalent to VM isolation against input
engineered for a container escape.

ChatML-style reserved delimiters help only if untrusted content stays out of
the system role ([system prompt architecture](../harness/system-prompt-architecture.md)).
Treat anything the system did not itself author — a retrieved document, a tool
return value, a user-typed field — as equally untrusted, because to the model
they are indistinguishable sources of "things in my context." Prompt-hack risk
cannot be fully eliminated while the system retains impactful capabilities;
measure both attack success and false refusals when tightening defenses.
