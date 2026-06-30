---
id: SDC.SyncDiscipline
title: "Synchronization discipline: monolith → references"
---

# SDC.SyncDiscipline: Synchronization discipline: monolith → references

> **Trigger:** [TODO: trigger condition — human review required]
> **Governing patterns:**
>   → [TODO: extract governing-pattern cues from body and convert to reference paths]

---

### 6.9 `SDC.SyncDiscipline` — Synchronization discipline: monolith → references

#### Always‑Core Fields

| Field | Content |
|---|---|
| **ProblemSignal** | The human edits the monolith (`assets/dpf.md`) — adds a problem card, changes an AcceptanceCriterion, corrects a governing cue. References/ are not updated. The agent continues reading old reference files. A divergence arises: "source of truth" and "primary source for agent" have diverged |
| **ContextGrounding** | The monolith is the source of truth. References/ are derived views for the agent. Synchronization is always unidirectional: monolith → references. Never the reverse |
| **ScopeCut** | Synchronization process: detecting changes in the monolith → rebuilding affected reference files → updating INDEX.md → updating SKILL.md; does not cover version control (git) |
| **NotWishReason** | "I'll edit the reference file directly, bypassing the monolith" — violates unidirectionality and creates divergence |

#### Conditional Fields

| Field | Content |
|---|---|
| **EntityOfConcern** | Synchronization process: detecting divergence and rebuilding references/ from the updated monolith |
| **SymptomDetection** | Reference file contains a problem card absent from the monolith (reference was edited directly); monolith contains a new problem card absent from references/ (monolith was updated, references/ were not) |
| **ProblemHypothesis** | The synchronization process is not defined. Rule: (1) all edits — only in the monolith, (2) after edits — re-run decomposition (full rebuild of references/), (3) reference files are never edited manually (except agent-specific annotations) |
| **ImprovementCheck** | After editing the monolith and rebuilding: all reference files are current, INDEX.md is updated, SKILL.md routing table is current |
| **AcceptanceCriterion** | Synchronization process: (1) monolith changed, (2) decomposition run (manual or scripted), (3) references/ rebuilt, (4) INDEX.md updated, (5) SKILL.md routing table verified, (6) "Done" status confirmed |
| **MandatoryConstraints** | Synchronization is always unidirectional (monolith → references); prohibited to edit reference files directly; rebuild references/ on every monolith change affecting problem cards; when adding/removing a problem card — full rebuild |
| **CharacterizationRelation** | Sync latency (time between monolith edit and references/ update), fidelity (references/ match monolith), direction compliance (no reverse edits) |
| **ValidationBoundary** | Verification: comparison of problem cards in the monolith and in references/ — full match |
| **FreshnessOrExpiry** | The synchronization process is triggered on every monolith change |
| **ReadinessDisposition** | `P2W-ready` after the first successful rebuild |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Monolith as source of truth | `EWA.MonolithInSkill` |
| Framework currentness and refresh | `G.11` |
| Carrier update discipline | `C.33`, `C.35` |
| Derived artifact vs source | `E.17` (description vs described thing) |
