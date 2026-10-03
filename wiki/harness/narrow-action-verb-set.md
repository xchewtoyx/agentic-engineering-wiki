---
type: concept
title: Narrow Action Verb Set
description: >
  Give an agent that changes real systems a small set of named, single-purpose,
  parameterised action verbs instead of a shell or a root-equivalent API, so
  least privilege can be expressed, audited and approved per action.
evidence: moderate
sources:
  - title: "Building Secure and Reliable Systems"
    resource: "Adkins et al., ch. 5 (small functional APIs)"
  - title: "Infrastructure as Code, 3rd edition"
    resource: "Kief Morris, ch. 12"
  - title: "AI Engineering: Building Applications With Foundation Models"
    resource: "AI Engineering (Chip Huyen), ch. 6 (write actions)"
  - title: "LLM06:2025 Excessive Agency"
    resource: "OWASP GenAI Security Project — https://genai.owasp.org/llmrisk/llm062025-excessive-agency/"
---

The simplest way to let an agent act on a system is to hand it a shell, or an
API credential that can do anything. Everything is then possible, which is the
problem: no permission can be narrower than "anything", no audit log of a
shell session says reliably what was done, and an approver shown a long
command string cannot tell what they are approving.

Security engineering's answer is the small functional API. Adkins and
colleagues argue that least privilege can only be expressed if each permitted
action exists as a distinct, nameable endpoint. A shell exposing the whole
POSIX interface is nearly impossible to constrain or audit, while a small API
produces granular logs that support firm statements about what was and was not
done. [Agent tool categories](agent-tool-categories.md) adds that risk rises
sharply for write actions that change the environment. The Open Worldwide
Application Security Project (OWASP) entry on excessive agency names excessive
functionality, permissions and autonomy as root causes, and recommends
minimising extensions, requiring approval for high-impact actions, and complete
mediation in downstream systems rather than trusting the model.

Applied to agents, the write surface becomes a handful of verbs, each with
typed parameters, its own permission, its own audit event and its own approval
level. For an operations agent that might be "restart service X", "roll back
the image tag of Y", "pause queue Z"; for an email assistant, `send_reply(thread_id, body)`
rather than a general `send_email(to, …)`, the scoping that defends against a
[confused deputy](../security/confused-deputy.md). Each verb is easy to
[gate](human-approval-gates.md), to mark
[replay-safe or not](replay-safe-tool-annotation.md), and to record in a
[full-trace audit](full-trace-remediation-audit.md); the model chooses among
them and code applies them ([the LLM proposes, code applies](llm-proposes-code-applies.md)).
Targets that must never be touched stay outside the set entirely
([hardline command floor](../security/hardline-command-floor.md)), and raw
root-equivalent handles such as a container daemon socket are never handed to
the agent ([the Docker socket is root](../security/docker-socket-is-root.md)).

**The tension with minimal general tools.** This position runs directly against
a well-supported practitioner finding. Coding-agent minimalists such as Mario
Zechner, Armin Ronacher and Simon Willison argue that a few general tools
(read, write, edit, bash) plus command-line tools beat large bespoke tool sets,
because each bespoke tool spends context and confuses selection
([minimal, general tool surface](minimal-general-tool-surface.md)). Both are
right for their setting. The minimalists' agent writes code inside a sandbox
where the worst case is a discarded container; the security guidance addresses
an agent with privileged access to live systems, where the worst case is an
outage or a breach. The usual resolution is to split by effect: general,
read-only tools for investigation, where flexibility and context economy pay
off, and narrow verbs for anything that changes state. The verb set should
still be small, for the minimalists' reason; "narrow" means each verb does one
bounded thing, not that there are many of them.
