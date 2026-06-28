# SDC.CarrierSplit: Carrier Split: Agent vs Human

> **Trigger:** After decomposition, the same knowledge exists in two forms — if the agent receives the instruction "when in doubt, read the monolith", progressive disclosure loses its meaning
> **Governing patterns:** 
>   → `../fpf-core/references/C.33-carrier-admission.md`
>   → `../fpf-core/references/E.17.EFP-first-entry.md`
>   → `../dpf-fpf-literacy/references/5-agent-context-load.md`
>   → `../dpf-lfw-architecture/references/2-monolith-in-skill.md`
>   → `../dpf-lfw-architecture/references/4-skill-dispatcher.md`

---

#### Always‑Core Fields

| Field | Content |
|---|---|
| **ProblemSignal** | After decomposition, the same knowledge exists in two forms: the monolith (`assets/`) and reference files (`references/`). If the agent receives the instruction "when in doubt, read the monolith", progressive disclosure loses its meaning — the agent loads 60K+ lines instead of 200 |
| **ContextGrounding** | In LFW, each skill has two carriers: `assets/monolith.md` (source of truth for humans) and `references/*.md` (primary source for the agent). It is important to explicitly separate who reads what |
| **ScopeCut** | Rule: the agent always reads references/, never — assets/; the human always edits assets/, rebuilds references/; does not cover the case when references/ are not yet created |
| **NotWishReason** | "The agent is smart, let it decide" — without an explicit rule, the agent may choose the monolith (60K+ lines into context) |

#### Conditional Fields

| Field | Content |
|---|---|
| **EntityOfConcern** | Carrier split — an explicit rule in SKILL.md defining which carrier is for which intended reader |
| **SymptomDetection** | SKILL.md contains the phrase "use assets/... as fallback"; the agent loads the monolith instead of reference |
| **ProblemHypothesis** | The carrier split rule is not explicitly formulated. Solution: SKILL.md contains a section "Source for Agent vs Human" with the imperative: "Agent: always use references/. Do NOT read assets/" |
| **ImprovementCheck** | SKILL.md unambiguously separates: agent → references/, human → assets/. The agent never loads the monolith |
| **AcceptanceCriterion** | SKILL.md contains: (1) "Agent: always use references/. Do NOT read assets/". (2) "Human: read and edit assets/. After edits — rebuild references/". (3) Not a single phrase allowing the agent to read the monolith |
| **MandatoryConstraints** | The phrase "use assets/ as fallback" or equivalent is forbidden; mentioning the monolith in the routing table is forbidden; "pending" status is only acceptable when references/ are truly empty — and then the monolith is not mentioned, the agent simply reports "references/ are not yet created" |
| **CharacterizationRelation** | Carrier split clarity (unambiguousness of the rule), agent compliance (does the agent read references/ and not assets/) |
| **ValidationBoundary** | Verification: give the agent a task in a bounded DPF context → the agent loads the reference, not the monolith |
| **FreshnessOrExpiry** | `stale` when the LFW carrier split architecture changes |
| **ReadinessDisposition** | `P2W-ready` for every skill |

#### Governing‑Pattern Cues

| Cue | Governing Pattern |
|---|---|
| Carrier admission for different intended readers | `C.33`, `E.17.EFP` |
| Agent context load (multi-level memory) | `FPFLIT.AgentContextLoad` |
| Monolith in skill (source of truth placement) | `EWA.MonolithInSkill` |
| Skill dispatcher (routing-only) | `EWA.SkillDispatcher` |

---

> **Source:** `assets/SpecDecomposer-dpf.md` lines L363-L397
