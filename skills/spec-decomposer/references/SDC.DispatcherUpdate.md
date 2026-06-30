---
id: SDC.DispatcherUpdate
title: Updating the SKILL.md dispatcher
---

# SDC.DispatcherUpdate: Updating the SKILL.md dispatcher

> **Trigger:** [TODO: trigger condition — human review required]
> **Governing patterns:**
>   → [TODO: extract governing-pattern cues from body and convert to reference paths]

---

### 6.7 `SDC.DispatcherUpdate` — Updating the SKILL.md dispatcher

#### Always‑Core Fields

| Field | Content |
|---|---|
| **ProblemSignal** | After decomposition, new files appear in `references/`, but the SKILL.md dispatcher still contains a routing table with "pending" status and/or an incomplete list of reference files. The agent does not know about new references or cannot find them |
| **ContextGrounding** | SKILL.md — the skill dispatcher: routing table (situation → reference). After decomposition the routing table must be updated: status → "Done", reference file list → complete |
| **ScopeCut** | Updating the routing table and status in SKILL.md after decomposition; does not cover creating SKILL.md from scratch |
| **NotWishReason** | "Leave pending, the agent will read INDEX.md" — the routing table in SKILL.md is the primary agent interface, INDEX is secondary |

#### Conditional Fields

| Field | Content |
|---|---|
| **EntityOfConcern** | SKILL.md dispatcher — a routing table that directs the agent to the right reference based on the situation |
| **SymptomDetection** | Routing table contains "pending" status when references/ are populated; routing table references non-existent reference files; routing table does not mention new references |
| **ProblemHypothesis** | SKILL.md was created before decomposition and was not updated after. A "post-decomposition dispatcher update" step is needed |
| **ImprovementCheck** | SKILL.md: routing table is complete (all references listed), status "Done", the "Source for agent vs human" section points to references/ as primary |
| **AcceptanceCriterion** | SKILL.md after update: (1) routing table lists all reference files, (2) each routing table row contains trigger condition and governing cues, (3) status changed from "pending" to "Done", (4) no mention of the monolith as a fallback for the agent |
| **MandatoryConstraints** | Prohibited to leave "pending" status when references/ are populated; routing table must be synchronized with actual references/ content; prohibited to direct the agent to the monolith |
| **CharacterizationRelation** | Routing completeness (all references in the table), trigger accuracy (does trigger match ProblemSignal), status honesty |
| **ValidationBoundary** | Verification: the agent uses the routing table to find a reference for each of 3 typical situations |
| **FreshnessOrExpiry** | `stale` on every change to references/ contents |
| **ReadinessDisposition** | `P2W-ready` as the concluding step of decomposition |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Skill dispatcher (routing-only) | `EWA.SkillDispatcher` |
| Agent context load | `FPFLIT.AgentContextLoad` |
| Carrier first entry | `FPFLIT.CarrierFirstEntry` |
| SKILL.md as dispatcher | skill-creator SKILL.md |
