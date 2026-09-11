# Agent Skill Builder — Relation Records

> **Canonical home.** This file is the canonical home for the source/edition/
> dependency citation and the dependency graph. The same graph appears in three
> views — each card's frontmatter `dependencies` (machine-readable), each card's
> `:12 Relations` (human-readable), and this file (the global map). All three must
> agree in membership and edge direction; change one → change all three.
>
> **Edge direction.** Relation functions follow `E.4.PFR:3.3`; two are used here:
> - **`builds_on` (dependency):** `dependent → prerequisite`. The left card loads
>   the right card before applying its own move.
> - **`coordinates_with` (peer, non-directional):** the two cards cross-reference each
>   other; neither builds on the other.
> A child-narrows-parent relation is **Specialization** (`E.4.PFR:3.3`) — recorded in
> the "DPF-specialization edges" table below, not as `builds_on`. There is no generic
> "governs / applies-to" edge (`E.4.PFR:1.1`); a rule stated in every card is content,
> not a relation, and is noted in prose rather than drawn as an edge.
> This file holds the intra-LPF graph and the parent-DPF specialization edges — never
> FPF edges (those live in each card's frontmatter `dependencies`). SKILL.md carries
> only a one-line pointer here.

## Source / edition citation

- **Skill:** `agent-skill-builder` (LPF — Local Practices Framework; alias
  `create-agent-skill`).
- **Authoring scenario (PLAS.EntryRoute):** outcome (a) "revise framework";
  axes — `FPF-grounded` (relies on FPF Core through the AS-DPF) and
  `language-from-scratch` (the skill directory is the access-facing carrier; the
  edition lives in this skill's own `references/*.md`; no externally published
  projection document exists).
- **Field / field boundary:** authoring, reviewing, and evolving **agent skills** —
  layer routing, trigger design, progressive disclosure, anatomy, atomicity,
  quality gate, placement, evolution, security, and material compaction. Not the
  agent runtime/platform (owned by AAPE-DPF), not facts/preferences (Memory).
- **Parent DPF:** `Agent Skills DPF` (`../Agent-Skills-DPF.md`), pattern codes
  `AS.1`–`AS.12`.
- **Dependency chain (unidirectional, `E.5.3`):** `agent-skill-builder` → `AS-DPF`
  → `FPF Core` → (nothing).
- **Skill dependencies:** `episteme-compaction` (the `ASB.Compaction` notation and
  forward/reverse render, ECPF.1–ECPF.7); `skill-creator` / `create-agent-skill`
  (carrier mechanics).
- **Readiness:** all 10 patterns are `status: seed`, readiness mode
  `source-faithful` (faithful to the AS-DPF `AS.1`–`AS.11` + the
  `agent-skill-builder` skill payload + the episteme-notation report); not
  `case-validated`.
- **Entry-route record:** outcome (a) "revise framework", the two authoring-scenario
  axes, the coverage map (specialized vs omitted `AS.*` patterns), and the honest
  omissions are maintainer evidence in the project vault (`DEC-0002`).
- **Publication-form checks:** `E.11.PFP` `PFM1`–`PFM12` are N/A — there is no
  reader-facing publication form for this skill carrier.

## Naming settlement (`F.18`)

- **Governed value:** a locally-groundable practice "build, review, and evolve an
  agent skill — the procedural guidance layer loaded on demand by an LLM agent".
- **Candidates compared:** `agent-skill-builder` (chosen — names the actor's job,
  matches the AS-DPF SOURCEPACK alias `create-agent-skill`), `skill-creator` (taken:
  a distinct base-utility skill for the technical packaging process),
  `skill-authoring` (rejected — domain-flavored, less action-oriented),
  `skill-builder` (rejected — drops the "agent" bounded context).
- **Decision:** `agent-skill-builder`, PatternID prefix `ASB.`.
- **Reopen condition:** the scope grows beyond skill authoring/review/evolution, or
  `create-agent-skill` is renamed and the alias collision must be resolved.

## Refresh triggers (G.11)

Revisit this skill (reopen → refresh) on any of the following:

1. **AS-DPF change:** a revision of the parent DPF patterns (`AS.1`–`AS.11`) the
   cards specialize.
2. **FPF change:** a revision of the governing FPF patterns (`E.4`, `E.5.3`,
   `E.11`, `C.33`, `F.18`, `E.10`, `E.21`, `E.19`, `E.23`, `G.11`, `E.4.PFR`,
   `A.6.3`, `C.2.3`).
3. **Skill-payload change:** a new edition of the `agent-skill-builder` /
   `create-agent-skill` payload.
4. **Notation change:** an `episteme-compaction` (ECPF) edition change affecting
   `ASB.Compaction`.
5. **PLAS change:** `pattern-language-as-agent-skill` conformance requirements
   change (E.8 sections, EntryRoute, carrier mechanics).
6. **Local-use telemetry (G.11 `TelemetryDelta`):** the owner reports a misfire, or
   a weak model (`ASB.QualityGate`) fails to follow a card.

Minimal revisit route: the `ASB.QualityGate` weak-model run + `E.21` for the
affected cards + a frontmatter parse check — without a full rebuild.

## Dependency graph

### Intra-LPF edges

| Kind | From | To | Relation function |
|---|---|---|---|
| builds_on | `ASB.Atomicity` | `ASB.LayerRouting` | Routing decides whether to split into atomic skills |
| builds_on | `ASB.Placement` | `ASB.LayerRouting` | Routing decides global vs project-local |
| builds_on | `ASB.Placement` | `ASB.SkillAnatomy` | The folder is the thing placed |
| builds_on | `ASB.ProgressiveDisclosure` | `ASB.TriggerDesign` | The `description` is level 1 of progressive disclosure |
| builds_on | `ASB.ProgressiveDisclosure` | `ASB.SkillAnatomy` | Resource roles implement the three levels |
| builds_on | `ASB.Atomicity` | `ASB.ProgressiveDisclosure` | Externalize shared heavy content rather than duplicate |
| builds_on | `ASB.Compaction` | `ASB.ProgressiveDisclosure` | Move 1 (delete/externalize) is the first half of compaction; disclosure is the **default** when owner consent is absent (opt-in gate) |
| builds_on | `ASB.Evolution` | `ASB.QualityGate` | The weak-model gate re-runs on every revision |

### Intra-LPF cross-reference (symmetric, non-directional)

- `ASB.Placement` ⇔ `ASB.SecurityAndTrust` — "be selective with global skills" is
  stated in both; neither builds on the other, each points to the other for its
  placement/security side.

### Cross-cutting content (not relation edges)

Two rules are stated in every card's body and are **content, not relations**
(`E.4.PFR:1.1`), so they are not drawn as edges:

- the "offer to update" rule (`ASB.Evolution:4`);
- the weak-model admission gate (`ASB.QualityGate:4`).

### DPF-specialization edges (parent AS-DPF)

| From (→) | To | Relation function |
|---|---|---|
| `ASB.LayerRouting` | `AS.1` | Specializes layer routing |
| `ASB.TriggerDesign` | `AS.2` | Specializes trigger design |
| `ASB.Atomicity` | `AS.3` | Specializes atomicity & decomposition |
| `ASB.ProgressiveDisclosure` | `AS.4` | Specializes progressive disclosure |
| `ASB.SkillAnatomy` | `AS.5` | Specializes skill anatomy & bundled resources |
| `ASB.QualityGate` | `AS.8` | Specializes the weak-model quality gate |
| `ASB.Placement` | `AS.9` | Specializes placement & portability |
| `ASB.Evolution` | `AS.10` | Specializes skill evolution & currentness |
| `ASB.SecurityAndTrust` | `AS.11` | Specializes security & trust |
| `ASB.Compaction` | `AS.4` | Adds material compaction (F3 hybrid) on top of disclosure |

The dependency chain is unidirectional (`E.5.3`): `agent-skill-builder` → `AS-DPF`
→ `FPF Core` → (nothing). `episteme-compaction` and `skill-creator` are skill
dependencies for carrier mechanics/notation, not DPF patterns.
