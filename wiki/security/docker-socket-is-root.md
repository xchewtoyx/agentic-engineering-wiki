---
type: concept
title: The Docker Socket Is Root
description: >
  Mounting the container daemon socket into an agent or sidecar grants
  host-root equivalence, so any prompt injection becomes host compromise;
  restrict it like root access and prefer hardened container flags.
evidence: moderate
sources:
  - title: "Docker Engine security"
    resource: "Docker docs, accessed 3 Oct 2026 — https://docs.docker.com/engine/security/"
  - title: "docker-autoheal README"
    resource: "hasnat/docker-autoheal, accessed 3 Oct 2026 — https://github.com/hasnat/docker-autoheal"
  - title: "Hermes Agent docs: Security"
    resource: "Nous Research official docs as of v0.21.5 (v2026.9.24), retrieved 3 Oct 2026, Docker terminal backend flags — https://hermes-agent.nousresearch.com/docs/user-guide/security"
---

An agent that manages containers needs to restart, inspect and sometimes
recreate them, and the quickest way to give it that power is to mount
`/var/run/docker.sock`. The problem is what else comes with it. Docker's own
security documentation says that access to the daemon effectively grants
host-level control and should be restricted the way root access is: whoever
can talk to the socket can start a privileged container that mounts the host
filesystem.

The pattern is common in self-healing tooling. docker-autoheal, for example,
restarts unhealthy containers through a mounted socket, polling every five
seconds by default, and its README documents no backoff or restart cap. Put
that next to the injection evidence and the risk is plain: a coding or
operations agent run with full permissions (a `--force` or
`danger-full-access` mode, or broad shell access) on a host where the socket is
mounted is root-equivalent, and it reads attacker-influenceable content such as
[logs](logs-are-untrusted-input.md). Any successful
[indirect prompt injection](indirect-prompt-injection.md) is then a host
compromise, the [confused deputy](confused-deputy.md) problem with the largest
possible authority.

The defences follow the general order of
[containing at the environment layer first](contain-environment-first.md).
Don't give the agent the socket. Expose instead a small set of single-purpose
operations ([narrow action verbs](../harness/narrow-action-verb-set.md)) from a
separate component that does hold it, and keep that component's secrets out of
the agent's reach
([credentials stay outside the sandbox](credentials-outside-the-sandbox.md)).
Where an agent must run inside containers, run them hardened: one agent
framework's Docker backend, for example, drops all Linux capabilities and adds
back only a few file-ownership ones, sets `no-new-privileges`, caps process
count and uses size-limited tmpfs. Container namespaces are still weaker than a
VM boundary (see [agent system-level defenses](agent-system-level-defenses.md)).

This is one place where the minimalist case for a few general tools
([minimal, general tool surface](../harness/minimal-general-tool-surface.md))
does not carry over: it is well supported for coding agents in a disposable
sandbox, but a general handle with host-level blast radius is exactly what the
security guidance says to remove.
