# SDC.DispatcherUpdate: Updating the SKILL.md Dispatcher

> **Trigger:** After decomposition, new files appear in `references/`, but the SKILL.md dispatcher still contains a routing table with "pending" status
> **Governing patterns:** 
>   → `../dpf-lfw-architecture/references/4-skill-dispatcher.md`
>   → `../dpf-fpf-literacy/references/5-agent-context-load.md`
>   → `../dpf-fpf-literacy/references/8-carrier-first-entry.md`

---

#### Always‑Core Fields

| Field | Content |
|---|---|
| **ProblemSignal** | After decomposition, new files appear in `references/`, but the SKILL.md dispatcher still contains a routing table with "pending" status and/or an incomplete list of reference files. The agent does not know about new references or cannot find them |
| **ContextGrounding** | SKILL.md is the skill dispatcher: routing table (situation → reference). After decomposition, the routing table must be updated: status → "ready", reference file list → complete |
| **ScopeCut** | Updating the routing table and status in SKILL.md after decomposition; does not cover creating SKILL.md from scratch |
| **NotWishReason** | "I'll leave it as pending, the agent will read INDEX.md" — the routing table in SKILL.md is the agent's primary interface, INDEX is secondary |

#### Conditional Fields

| Field | Content |
|---|---|
| **EntityOfConcern** | SKILL.md dispatcher — routing table that directs the agent to the appropriate reference by situation |
| **SymptomDetection** | The routing table contains "pending" status when references/ are populated; the routing table references non-existent reference files; the routing table does not mention new references |
| **ProblemHypothesis** | SKILL.md was created before decomposition and was not updated after. A "post-decomposition dispatcher update" step is needed |
| **ImprovementCheck** | SKILL.md: routing table is complete (all references listed), status is "Ready", the "Source for Agent vs Human" section points to references/ as primary |
| **AcceptanceCriterion** | SKILL.md after update: (1) routing table lists all reference files, (2) each routing table row contains a trigger condition and governing cues, (3) status changed from "pending" to "Ready", (4) no mention of the monolith as a fallback for the agent |
| **MandatoryConstraints** | It is forbidden to leave "pending" status when references/ are populated; the routing table must be synchronized with the actual contents of references/; it is forbidden to direct the agent to the monolith |
| **CharacterizationRelation** | Routing completeness (all references in table), trigger accuracy (does the trigger match the ProblemSignal), status honesty |
| **ValidationBoundary** | Verification: the agent uses the routing table to find the reference for each of 3 typical situations |
| **FreshnessOrExpiry** | `stale` every time the composition of references/ changes |
| **ReadinessDisposition** | `P2W-ready` as the final step of decomposition |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Skill dispatcher (routing-only) | `EWA.SkillDispatcher` |
| Agent context load | `FPFLIT.AgentContextLoad` |
| Carrier first entry | `FPFLIT.CarrierFirstEntry` |
| SKILL.md as dispatcher | skill-creator SKILL.md |

---

> **Source:** `assets/SpecDecomposer-dpf.md` lines L326-L360
