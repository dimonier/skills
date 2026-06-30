---
id: SDC.CarrierSplit
title: "Carrier split: agent vs human"
---

# SDC.CarrierSplit: Carrier split: agent vs human

> **Trigger:** [TODO: trigger condition — human review required]
> **Governing patterns:**
>   → [TODO: extract governing-pattern cues from body and convert to reference paths]

---

### 6.8 `SDC.CarrierSplit` — Carrier split: agent vs human

#### Always‑Core Fields

| Field | Content |
|---|---|
| **ProblemSignal** | After decomposition the same knowledge exists in two forms: monolith (`assets/`) and reference files (`references/`). If the agent receives an instruction "when in doubt read the monolith", progressive disclosure loses its purpose — the agent loads 60K+ lines instead of 200 |
| **ContextGrounding** | In LFW each skill has two carriers: `assets/monolith.md` (source of truth for the human) and `references/*.md` (primary source for the agent). It is essential to explicitly separate who reads what |
| **ScopeCut** | Rule: the agent always reads references/, never — assets/; the human always edits assets/, reassembles references/; does not cover the case when references/ have not yet been created |
| **NotWishReason** | "The agent is smart, let it decide" — without an explicit rule the agent may choose the monolith (60K+ lines into context) |

#### Conditional Fields

| Field | Content |
|---|---|
| **EntityOfConcern** | Carrier split — an explicit rule in SKILL.md defining which carrier is for which intended reader |
| **SymptomDetection** | SKILL.md contains the phrase "use assets/... as fallback"; the agent loads the monolith instead of references |
| **ProblemHypothesis** | The carrier split rule is not explicitly formulated. Solution: SKILL.md contains an "Source for agent vs human" section with an imperative: "Agent: always use references/. DO NOT read assets/" |
| **ImprovementCheck** | SKILL.md unambiguously separates: agent → references/, human → assets/. The agent never loads the monolith |
| **AcceptanceCriterion** | SKILL.md contains: (1) "Agent: always use references/. DO NOT read assets/". (2) "Human: read and edit assets/. After edits — rebuild references/". (3) No phrase allowing the agent to read the monolith |
| **MandatoryConstraints** | The phrase "use assets/ as fallback" or equivalent is prohibited; mentioning the monolith in the routing table is prohibited; "pending" status is only allowed when references/ are genuinely empty — and then the monolith is not mentioned, the agent simply reports "references/ have not yet been created" |
| **CharacterizationRelation** | Carrier split clarity (unambiguity of the rule), agent compliance (does the agent read references/ and not assets/) |
| **ValidationBoundary** | Verification: give the agent a task in the DPF bounded context → the agent loads the reference, not the monolith |
| **FreshnessOrExpiry** | `stale` when the LFW architecture carrier split changes |
| **ReadinessDisposition** | `P2W-ready` for every skill |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Carrier admission for different intended readers | `C.33`, `E.17.EFP` |
| Agent context load (multi-level memory) | `FPFLIT.AgentContextLoad` |
| Monolith in skill (source of truth placement) | `EWA.MonolithInSkill` |
| Skill dispatcher (routing-only) | `EWA.SkillDispatcher` |
