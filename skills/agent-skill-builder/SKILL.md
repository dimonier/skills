---
name: agent-skill-builder
description: |
  Guide for deciding when to create agent skills, how to design them well,
  and what anti-patterns to avoid. Use when: (1) creating a new skill,
  (2) deciding between skills vs AGENTS.md vs MCP vs Memory,
  (3) reviewing an existing skill for quality,
  (4) unsure if a skill is needed at all,
  (5) compacting a skill's materials to a minimal size — only on explicit
  request and acceptance of the trade-offs (discarding the unnecessary,
  rendering what remains as episteme blocks).
---

# Agent Skill Builder (LPF)

**Bounded context:** authoring, reviewing, and evolving **agent skills** — the
procedural guidance layer an LLM agent loads on demand. The skill is one of four
guidance layers (`AGENTS.md` rules / **skills** / MCP / memory); this framework
covers the skill artifact and its authoring discipline, not the agent runtime.

**Carrier:** this skill directory is the access-facing carrier bearing the
`AgentSkillBuilder` edition; the edition is recoverable from `references/*.md`.
There is no monolith. For the technical packaging process (init, package, iterate)
see the `skill-creator` skill; for FPF-grounded DPF/LPF-as-skill authoring see
`pattern-language-as-agent-skill`.

## When to load which pattern

| Situation | Load | Governing cues |
|---|---|---|
| Is a skill even the right layer (vs `AGENTS.md`, MCP, Memory)? Should I create one at all? | `references/ASB.LayerRouting.md` | `AS.1`, `E.4`, `E.5.3`, `E.11` |
| The skill never triggers, or triggers on the wrong prompts (drafting the `description`) | `references/ASB.TriggerDesign.md` | `AS.2`, `E.11` |
| Keeping `SKILL.md` small yet complete; where heavy content goes | `references/ASB.ProgressiveDisclosure.md` | `AS.4`, `E.11`, `C.33` |
| Which files a skill folder must/may contain; frontmatter; bundled resources | `references/ASB.SkillAnatomy.md` | `AS.5`, `C.33`, `F.18`, `E.10` |
| Whether to split one fat skill into several; the mega-skill anti-pattern | `references/ASB.Atomicity.md` | `AS.3`, `E.4`, `E.5.3` |
| Whether the skill actually works before relying on it (weak-model test) | `references/ASB.QualityGate.md` | `AS.8`, `E.21`, `E.19` |
| Where the skill should live (global / project-local / symlink) | `references/ASB.Placement.md` | `AS.9`, `E.4`, `E.5.3`, `C.33` |
| Keeping the skill current; the "offer to update" rule; deprecation | `references/ASB.Evolution.md` | `AS.10`, `E.23`, `G.11`, `E.4.PFR` |
| Trust, scripts as attack surface, third-party / awesome-list skills | `references/ASB.SecurityAndTrust.md` | `AS.11`, `E.5.3`, `C.33` |
| Compacting a skill's materials to minimal size (**opt-in**; only on explicit owner request + accepted trade-offs) | `references/ASB.Compaction.md` | `AS.4`, `A.6.3`, `C.2.3` |

## Navigation rule

There is no single linear chain; enter per use-case:

- **Decide / cold start** → `ASB.LayerRouting` first (a skill is only one of four
  layers), then `ASB.TriggerDesign` to draft the `description`. Do not start by
  writing the body.
- **Author** → `ASB.SkillAnatomy` → `ASB.ProgressiveDisclosure` → `ASB.Atomicity`
  → `ASB.TriggerDesign`.
- **Review an existing skill** → run every `CC-*` across the cards;
  `ASB.QualityGate` is the admission gate.
- **Place / publish** → `ASB.Placement` → `ASB.SecurityAndTrust`.
- **Maintain** → `ASB.Evolution`.
- **Compact materials** → `ASB.Compaction` is **opt-in**: require explicit owner
  confirmation of the minimal-size goal and acceptance of the trade-offs; otherwise
  default to `ASB.ProgressiveDisclosure` (delete the unnecessary first, in prose).

## Single surface

`references/*.md` IS the canonical source — the agent and the human author read
and edit those files directly. `SKILL.md` (this file) is routing-only: no pattern
body content lives here. `references/INDEX.md` lists every card once;
`references/relations.md` is the canonical home for the source/edition citation,
the dependency graph, and refresh triggers. Frontmatter `dependencies`
(`builds_on` / `coordinates_with`) carries FPF codes only; each card names its
parent AS-DPF pattern in `:12 "Builds on (DPF)"`, and `relations.md` holds the
intra-LPF graph and the DPF-specialization edges.

## references/ status

**First seed** — 10 pattern cards + INDEX + relations, all `status: seed`, readiness
mode `source-faithful` (faithful to the AS-DPF `AS.1`–`AS.11` and the
`agent-skill-builder` skill payload), not `case-validated`. Before reliance, run the
`ASB.QualityGate` weak-model test.

## Guardrails

When a judgment is ambiguous — dropping source content, choosing a name, splitting
a card, or any choice that could diverge from the owner's intent — **ask the owner,
do not decide silently**. Deployment to the user-level skills directory is
owner-owned; edit only the repo carrier.

## Evolution

If the owner is dissatisfied or refines the process, offer to update this skill —
its `description`, the routing table, or a `references/*.md` body (see
`ASB.Evolution`). The evolution of the LPF content itself follows
`pattern-language-as-agent-skill` (`PLAS.QualityAndRefresh`).
