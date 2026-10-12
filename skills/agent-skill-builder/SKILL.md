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

# Agent Skill Builder (DPF)

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

| Situation | Load |
|---|---|
| Is a skill even the right layer (vs `AGENTS.md`, MCP, Memory)? Should I create one at all? | `references/ASB.LayerRouting.md` |
| The skill never triggers, or triggers on the wrong prompts (drafting the `description`) | `references/ASB.TriggerDesign.md` |
| The skill triggers only sometimes; tuning the `description` empirically (near-miss negatives, held-out test) | `references/ASB.DescriptionOptimization.md` |
| Keeping `SKILL.md` small yet complete; where heavy content goes | `references/ASB.ProgressiveDisclosure.md` |
| Which files a skill folder must/may contain; frontmatter; bundled resources | `references/ASB.SkillAnatomy.md` |
| Whether to split one fat skill into several; the mega-skill anti-pattern | `references/ASB.Atomicity.md` |
| Several skills must cooperate; chaining vs orchestrating (pointer-not-call, acyclicity) | `references/ASB.InterSkillComposition.md` |
| Evaluating a skill end-to-end before relying on it (baselines, assertions, iteration, self-eval) | `references/ASB.EvaluationLoop.md` |
| Whether the skill works on a weaker model (the weak-model admission test) | `references/ASB.QualityGate.md` |
| Where the skill should live (global / project-local / symlink) | `references/ASB.Placement.md` |
| Keeping the skill current; the "offer to update" rule; deprecation | `references/ASB.Evolution.md` |
| Trust, scripts as attack surface, third-party / awesome-list skills | `references/ASB.SecurityAndTrust.md` |
| Compacting a skill's materials to minimal size (**opt-in**; only on explicit owner request + accepted trade-offs) | `references/ASB.Compaction.md` |

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
refresh triggers, provenance, and the intra-DPF dependency graph. Frontmatter
`dependencies` (`builds_on` / `coordinates_with`) carries FPF codes only — and
they appear nowhere else (no body cue block, no `:12` edge list, no routing-table
cues column). Each card's `:12 Relations` is a one-line pointer, not an edge list.

## references/ status

**First seed** — 13 pattern cards + INDEX + relations, all `status: seed`, readiness
mode `source-faithful` (faithful to the merged AS-DPF `AS.1`–`AS.12` and the
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
`ASB.Evolution`). The evolution of the DPF content itself follows
`pattern-language-as-agent-skill` (`PLAS.QualityAndRefresh`).
