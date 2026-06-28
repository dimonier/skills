# SDC.SyncDiscipline: Monolith → References Sync Discipline

> **Trigger:** A human edits the monolith, references/ are not updated — "source of truth" and "primary source for agent" have diverged
> **Governing patterns:** 
>   → `../dpf-lfw-architecture/references/2-monolith-in-skill.md`
>   → `../fpf-core/references/G.11-currentness.md`
>   → `../fpf-core/references/C.33-carrier-admission.md`
>   → `../fpf-core/references/C.35-carrier-update.md`
>   → `../fpf-core/references/E.17-description-vs-described.md`

---

#### Always‑Core Fields

| Field | Content |
|---|---|
| **ProblemSignal** | A human edits the monolith (`assets/dpf.md`) — adds a problem card, changes AcceptanceCriterion, fixes a governing cue. References/ are not updated. The agent continues to read old reference files. A divergence arises: "source of truth" and "primary source for agent" have diverged |
| **ContextGrounding** | The monolith is the source of truth. References/ are derived views for the agent. Synchronization is always unidirectional: monolith → references. Never the other way around |
| **ScopeCut** | The sync process: detecting changes in the monolith → rebuilding affected reference files → updating INDEX.md → updating SKILL.md; does not cover version control (git) |
| **NotWishReason** | "I'll edit the reference file directly, bypassing the monolith" — violates unidirectionality and creates divergence |

#### Conditional Fields

| Field | Content |
|---|---|
| **EntityOfConcern** | The sync process: detecting divergence and rebuilding references/ from the updated monolith |
| **SymptomDetection** | A reference file contains a problem card absent from the monolith (reference was edited directly); the monolith contains a new problem card absent from references/ (monolith was updated, references/ were not) |
| **ProblemHypothesis** | The sync process is not defined. Rule: (1) all edits — only in the monolith, (2) after edits — re-run decomposition (full rebuild of references/), (3) reference files are never edited manually (except for agent-specific annotations) |
| **ImprovementCheck** | After monolith edit and rebuild: all reference files are up-to-date, INDEX.md is updated, SKILL.md routing table is current |
| **AcceptanceCriterion** | Sync process: (1) monolith is changed, (2) decomposition is run (manual or scripted), (3) references/ are rebuilt, (4) INDEX.md is updated, (5) SKILL.md routing table is verified, (6) "Done" status is confirmed |
| **MandatoryConstraints** | Sync is always unidirectional (monolith → references); editing reference files directly is prohibited; references/ is rebuilt on every monolith change affecting problem cards; adding/removing a problem card → full rebuild |
| **CharacterizationRelation** | Sync latency (time between monolith edit and references/ update), fidelity (references/ matching the monolith), direction compliance (no reverse edits) |
| **ValidationBoundary** | Verification: comparison of problem cards in the monolith and in references/ — full correspondence |
| **FreshnessOrExpiry** | The sync process activates on every monolith change |
| **ReadinessDisposition** | `P2W-ready` after the first successful rebuild |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Monolith as source of truth | `EWA.MonolithInSkill` |
| Framework currentness and refresh | `G.11` |
| Carrier update discipline | `C.33`, `C.35` |
| Derived artifact vs source | `E.17` (description vs described thing) |

---

> **Source:** `assets/SpecDecomposer-dpf.md` lines L400-L434
