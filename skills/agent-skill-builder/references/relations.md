# Agent Skill Builder — Relation Records

> **Canonical home of the intra-DPF graph and provenance.** This file is the single
> authored home for the source/edition citation, the intra-DPF dependency graph,
> provenance, sibling-DPF relations, compatibility/deprecation, and refresh triggers.
> FPF governing edges are **not** here — their single home is each card's frontmatter
> `dependencies`, and they are repeated nowhere (no body cue block, no `:12` edge
> list, no `SKILL.md` cues column). One home per edge: `:12 Relations` is a one-line
> pointer to the frontmatter, not an edge list.
>
> **Edge direction.** Relation functions follow `E.4.PFR:3.3`; two are used here:
> - **`builds_on` (dependency):** `dependent → prerequisite`. The left card loads
>   the right card before applying its own move.
> - **`coordinates_with` (peer, non-directional):** the two cards cross-reference each
>   other; neither builds on the other.
> A child-narrows-parent relation (former **Specialization** to the AS-DPF) is now
> recorded as **provenance** (the "Provenance" table below), not as a live edge. There
> is no generic "governs / applies-to" edge (`E.4.PFR:3.3` — the relation-function
> list closes with "no `Subject-pattern relation`"); a rule stated in every card is
> content, not a relation, and it is noted in prose rather than drawn as an edge.
> `SKILL.md` carries only a one-line pointer here.

## Source / edition citation

- **Skill:** `agent-skill-builder` (DPF — Domain Principle Framework; alias
  `create-agent-skill`).
- **Authoring scenario (PLAS.EntryRoute):** outcome (a) "revise framework";
  axes — `FPF-grounded` (relies on FPF Core directly) and
  `language-from-scratch` (the skill directory is the access-facing carrier; the
  edition lives in this skill's own `references/*.md`; no externally published
  projection document exists).
- **Field / field boundary:** authoring, reviewing, and evolving **agent skills** —
  layer routing, trigger design, progressive disclosure, anatomy, atomicity,
  quality gate, placement, evolution, security, and material compaction. Not the
  agent runtime/platform (owned by AAPE-DPF), not facts/preferences (Memory).
- **Provenance:** absorbed the former AS-DPF monolith (`../Agent-Skills-DPF.md`,
  pattern codes `AS.1`–`AS.12`) on 2026-10-04 (`DEC-0005`).
- **Dependency chain (unidirectional, `E.5.3`):** `agent-skill-builder` (ASB-DPF)
  → `FPF Core` → (nothing).
- **Skill dependencies:** `episteme-compaction` (the `ASB.Compaction` notation and
  forward/reverse render, ECPF.1–ECPF.7); `skill-creator` / `create-agent-skill`
  (carrier mechanics).
- **Readiness:** all 13 patterns are `status: seed`, readiness mode
  `source-faithful` (faithful to the merged AS-DPF `AS.1`–`AS.12` + the
  `agent-skill-builder` skill payload + the episteme-notation report); not
  `case-validated`.
- **Entry-route record:** outcome (a) "revise framework" → later collapsed into a
  single DPF (`DEC-0005`); the original coverage map (which `AS.*` patterns were
  synthesized into cards) and honest omissions remain maintainer evidence (`DEC-0002`).
- **Publication-form checks:** `E.11.PFP` `PFM1`–`PFM12` are N/A — there is no
  reader-facing publication form for this skill carrier.
- **Source pack (`G.2`, adopted):** `anthropics/skills` + `skill-creator` (folder
  structure, frontmatter schema, validation, eval loop, description optimization);
  `agent-skill-builder` / `create-agent-skill` (four-layer model, when-to-create,
  atomicity, anti-patterns, placement, weak-model gate); Anthropic "Building effective
  agents" (workflow vs agent loop, conceptual only); opencode skills format (`SKILL.md`
  portability); ISO/IEC/IEEE 42010:2022 (viewpoint/view analog). All `verified /
  current`.

## Naming settlement (`F.18`)

- **Governed value:** the domain practice "build, review, and evolve an
  agent skill — the procedural guidance layer loaded on demand by an LLM agent".
- **Candidates compared:** `agent-skill-builder` (chosen — names the actor's job,
  matches the former AS-DPF SOURCEPACK alias `create-agent-skill`), `skill-creator` (taken:
  a distinct base-utility skill for the technical packaging process),
  `skill-authoring` (rejected — domain-flavored, less action-oriented),
  `skill-builder` (rejected — drops the "agent" bounded context).
- **Decision:** `agent-skill-builder`, PatternID prefix `ASB.`.
- **Reopen condition:** the scope grows beyond skill authoring/review/evolution, or
  `create-agent-skill` is renamed and the alias collision must be resolved.

## Refresh triggers (G.11)

Revisit this skill (reopen → refresh) on any of the following:

1. **FPF change:** a revision of the governing FPF patterns (`E.4`, `E.5.3`,
   `E.11`, `C.33`, `F.18`, `E.10`, `E.21`, `E.19`, `E.23`, `G.11`, `E.4.PFR`,
   `A.6.3`, `C.2.3`).
2. **Skill-payload change:** a new edition of the `agent-skill-builder` /
   `create-agent-skill` payload.
3. **Notation change:** an `episteme-compaction` (ECPF) edition change affecting
   `ASB.Compaction`.
4. **PLAS change:** `pattern-language-as-agent-skill` conformance requirements
   change (E.8 sections, EntryRoute, carrier mechanics).
5. **Local-use telemetry (G.11 `TelemetryDelta`):** the owner reports a misfire, or
   a weak model (`ASB.QualityGate`) fails to follow a card.

Minimal revisit route: the `ASB.QualityGate` weak-model run + `E.21` for the
affected cards + a frontmatter parse check — without a full rebuild.

## Dependency graph

### Intra-DPF edges

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
| builds_on | `ASB.DescriptionOptimization` | `ASB.TriggerDesign` | The `description` is the optimization input |
| builds_on | `ASB.InterSkillComposition` | `ASB.Atomicity` | Decomposition precedes composition |
| builds_on | `ASB.InterSkillComposition` | `ASB.TriggerDesign` | Chaining happens by `description` |
| coordinates_with | `ASB.EvaluationLoop` | `ASB.QualityGate` | The weak-model gate is the admission test inside the loop |
| coordinates_with | `ASB.EvaluationLoop` | `ASB.DescriptionOptimization` | Optimization runs after the body is stable |
| coordinates_with | `ASB.SkillAnatomy` | `ASB.TriggerDesign` | The `description` field is written per the trigger card |
| coordinates_with | `ASB.Atomicity` | `ASB.DescriptionOptimization` | Atomicity improves trigger accuracy |
| coordinates_with | `ASB.QualityGate` | `ASB.DescriptionOptimization` | The gate and the tuning loop share description quality |
| coordinates_with | `ASB.Compaction` | `ASB.Atomicity` | Where shared content goes (Move 1 routing) |

### Intra-DPF cross-reference (symmetric, non-directional)

- `ASB.Placement` ⇔ `ASB.SecurityAndTrust` — "be selective with global skills" is
  stated in both; neither builds on the other, each points to the other for its
  placement/security side.

### Cross-cutting content (not relation edges)

Two rules are stated in every card's body and are **content, not relations**
(`E.4.PFR:3.3`), so they are not drawn as edges:

- the "offer to update" rule (`ASB.Evolution:4`);
- the weak-model admission gate (`ASB.QualityGate:4`).

### Provenance (former AS-DPF patterns absorbed 2026-10-04)

| ASB card | Former AS-DPF source |
|---|---|
| `ASB.LayerRouting` | `AS.1` Layer Routing |
| `ASB.TriggerDesign` | `AS.2` Trigger Design |
| `ASB.DescriptionOptimization` | `AS.7` Description Optimization |
| `ASB.ProgressiveDisclosure` | `AS.4` Progressive Disclosure |
| `ASB.SkillAnatomy` | `AS.5` Skill Anatomy & Bundled Resources |
| `ASB.Atomicity` | `AS.3` Atomicity & Decomposition |
| `ASB.InterSkillComposition` | `AS.12` Inter-Skill Composition |
| `ASB.EvaluationLoop` | `AS.6` Evaluation Loop |
| `ASB.QualityGate` | `AS.8` Quality Gate |
| `ASB.Placement` | `AS.9` Placement & Portability |
| `ASB.Evolution` | `AS.10` Skill Evolution & Currentness |
| `ASB.SecurityAndTrust` | `AS.11` Security & Trust |
| `ASB.Compaction` | `AS.4` (extension: material compaction, F3 hybrid) |

### Sibling-DPF relations (prose, not graph edges)

- `AAPE-DPF` — sibling artisan: ASB-DPF covers the skill artifact; AAPE-DPF covers
  the agent runtime/platform.
- `Python-Dev-DPF` — sibling: a Python-Dev skill is authored under ASB-DPF.
- `SpecDecomposer-LPF` — concretizes carrier decomposition for ASB-DPF. The
  `specialized_by` direction is a derived reading, stated in prose (never authored
  as an edge — `E.4.PFR:3.3`).

### Cross-framework coordination

`ASB.Compaction` coordinates with `pattern-language-as-agent-skill`'s
`PLAS.CompactedProjection`: the compacted-carrier card depends on this pattern's
Move 1/Move 2 and fixes the projection's runtime allow-list, the no-frontmatter
rule, and the in-block `Grounding (FPF)` slot; this card points back to it (the
projection always names its canonical source). Opt-in gate and delete-list locus:
`DEC-0001` / `DEC-0003` (vault).

### Compatibility boundary

Compatible with any skill-loading agent that reads the Anthropic `SKILL.md` format
(`name` + `description` frontmatter, optional bundled resources, `ALLOWED_PROPERTIES`
per `quick_validate.py`). Product-specific extensions (e.g. `allowed-tools`) are
admitted but reduce portability.

### Deprecation / supersession

None yet (first ASB-DPF edition).

The dependency chain is unidirectional (`E.5.3`): `agent-skill-builder` (ASB-DPF) →
`FPF Core` → (nothing). `episteme-compaction` and `skill-creator` are skill
dependencies for carrier mechanics/notation, not DPF patterns.
