---
id: ECPF.5
title: "Strict-Distinction Compliance in Generated Compact Episteme"
status: source-faithful
keywords: [strict-distinction, category-error, A.7, reflexive-split, mereology]
dependencies:
  builds_on:
    - A.7
    - A.12
    - A.14
  coordinates_with: []
---

# ECPF.5 — Strict-Distinction Compliance in Generated Compact Episteme

> **Trigger:** When generated compact-episteme output may contain category errors (Role=Function, MethodDescription=Method=Work, Episteme acting, Role in partOf) and must be verified against the mandatory A.7 distinctions.
>
> **Governing FPF patterns:**
>   → A.7 (Strict Distinction)
>   → A.12 (External Transformer and Reflexive Split)
>   → A.14 (Advanced Mereology — PhaseOf)
> **Type:** DPF pattern body
> **Status:** source-faithful
> **Normativity:** Normative

> **Primary EntityOfConcern:** `StrictDistinctionCompliance@Context`, the act of verifying that generated episteme notation respects the mandatory A.7 distinctions and applying canonical reformulations where violations are found.

### ECPF.5:1 - Problem frame

Use this pattern when generated episteme notation may contain category errors — Role confused with Function, MethodDescription confused with Method confused with Work, U.Episteme assigned an action, or Role appearing in a partOf chain — and these errors would make the output structurally invalid for downstream FPF-literate consumers.

First useful move: run the mandatory A.7 distinctions against every claim in the output. For each violation, apply the canonical reformulation.

What goes wrong if missed: generated episteme notation looks structurally correct but carries category errors that downstream FPF processing would reject or misinterpret. An Episteme "performing" an action, a Role appearing in a structural composition chain, or a MethodDescription confused with its execution — each is a silent semantic corruption.

What this buys: every claim in the output respects FPF type discipline, preventing silent propagation of category errors through multi-agent reasoning chains.

Not this pattern when the output is at F0-F2 and not claiming FPF type discipline. Use `ECPF.1` to verify formality level first.

### ECPF.5:2 - Problem

LLM-generated episteme notation is prone to recurring category errors because natural language routinely blurs the distinctions that FPF type discipline requires. "The specification decided to tighten limits" — a U.Episteme (specification) cannot decide. "The process executed the rule" — a process is not a U.System. "The holon bearing TransformerRole" — only U.System can bear roles. These errors are invisible to non-FPF readers but structurally invalid for FPF-literate consumers.

### ECPF.5:3 - Forces

| Force | Tension |
|---|---|
| Detection thoroughness vs rendering speed | Full distinction check adds ~10-15 seconds of verification; skipped checks risk silent errors. |
| Natural language fluency vs FPF strictness | LLMs are trained on prose that blurs distinctions; FPF output requires explicit repair. |
| Fix completeness vs output brevity | Canonical reformulations are longer than the original sloppy phrasing. |

### ECPF.5:4 - Solution

Apply the mandatory A.7 distinctions as verification rules. For each violation, apply the canonical reformulation.

**The mandatory A.7 distinctions:**

| # | Distinction | Rule |
|---|---|---|
| 1 | **Role ≠ Function** | Role is a mask; Function = Method/Work under a Role. Role does not execute. |
| 2 | **MethodDescription ≠ Method ≠ Work** | Description ≠ capability ≠ execution. Separate slots: Tᴰ for description, Tᴿ for Work. |
| 3 | **Holon ≠ System ≠ Episteme** | Only U.System can act. U.Episteme is passive. U.Holon is the compositional root. |
| 4 | **Episteme ≠ Carrier** | Knowledge ≠ its material carrier (file). Episteme is content; carrier is an accessible file/record. |
| 5 | **Collective ≠ Set** | Acting group = collective system, not a MemberOf-set. Collective has behavior; set is mathematical. |

**Canonical reformulations:**

| Wrong (natural language pattern) | Correct (FPF-compliant) |
|---|---|
| "The process executed the rule" | `System#TransformerRole:Ctx` executed `Method`; `Work` anchored to SCR |
| "The specification decided to tighten limits" | `DesignService#TransformerRole:Ctx` updated carriers of specification (SCR ids) |
| "Holon bearing TransformerRole" | `System bearing TransformerRole` |
| "The document updated itself" | `System#TransformerRole:Ctx` executed Work on carrier of document |
| "The team is a set of members" | Team = collective `System`; members are `ComponentOf` team, not `MemberOf` set |
| "Roles are parts of the system" | Roles are masks assigned to systems; system parts are holons. Roles never appear in `partOf` chains. |

**Strict distinction verification rules (normative):**

1. **No action verbs for U.Episteme** — scan for Episteme-type entities (specification, document, model, proof, requirement) followed by action verbs (decided, executed, performed, changed, updated). Replace with: System → Work on carrier.
2. **No Role in partOf chains** — scan for Role-typed entities in composition/aggregation slots. Roles belong in RoleAssignment slots only.
3. **No Method without System** — scan for Method/Work claims without a performing System#Role:Context. Add the performer.
4. **No MethodDescription as Work** — scan for MethodDescription in run-time (Tᴿ) slots. MethodDescription is design-time (Tᴰ) only.
5. **No MemberOf for acting groups** — scan for MemberOf used to describe team/collective composition. Use ComponentOf for collective systems.

**External Transformer rule (A.12):**

```
Rule: holder(Agent) ≠ Target
 Agent and Target are different holons.
 No "self-magic."

Reflexive Split (for self-action):
 System = {Regulator, Regulated}
 Regulator#TransformerRole:InternalCtx → Target: Regulated
 HolonDelimitation: <relation between Regulator and Regulated inside containing holon>
 HolonBoundaryCrossing: <relation crossing the delimitation (signal, control, flow)>
```

**Reflexive split rendering template:**

```
ReflexiveSplit(System: <ID>):
 Regulator: <Subsystem₁>#TransformerRole:<InternalCtx>
 Regulated: <Subsystem₂>
 HolonDelimitation: <relation between Regulator and Regulated inside containing holon>
 HolonBoundaryCrossing: <relation crossing the delimitation (signal, control, flow)>
 Method: <U.Method>
 MethodDescription: <U.MethodDescription> [src: scr://…]
 Work: <U.Work> @ <time>, resources: <Γ_work>
 Evidence:
  externalObserver: <System#ObserverRole:Ctx>
  verifiedBy: [<proof-ids>]
```

**Mereological relations (for composition slots):**

| Relation | Use for | Applies to |
|---|---|---|
| `ComponentOf` | Structural part (mechanical) | U.System |
| `ConstituentOf` | Logical/content part | U.Episteme |
| `PortionOf` | Quantitative portion (preserves extensive properties) | Matter/resources |
| `PhaseOf` | Temporal part/state | Continuous identity over time |
| `MemberOf` | Set membership (no behavior) | Mathematical sets |
| `RoleBearerOf` | System bears Role | U.System ↔ U.Role |

**Critical rule:** Roles never appear in `partOf` chains. Holarchies are built from substantive holons only.

### ECPF.5:5 - Archetypal Grounding

**Tell:** An agent generates: "The specification decided to require additional thermal testing." The distinction check catches: U.Episteme (specification) cannot decide. Canonical reformulation: `DesignService#TransformerRole:SpecUpdateCtx` executed `Method(updateSpecCarrier)`; `Work` anchored to `scr://spec/thermal-req/v2`.

**Tell:** An agent generates: "The battery pack consists of 72 cells and a MonitoringRole." The distinction check catches: Role in partOf chain. Canonical reformulation: `Cell₁…Cell₇₂` as parts; `MonitoringRole` assigned to `BMSSystem#MonitorRole:PackCtx` via `RoleAssignment`.

**Show — Violation detection and repair:**

```
# BEFORE (violation — Episteme acting):
The safety analysis concluded that margins are insufficient.

# AFTER (FPF-compliant):
SafetyAnalyst#TransformerRole:AnalysisCtx executed Method(safetyMarginAnalysis);
Work anchored to scr://analysis/safety-2025-07;
Conclusion recorded in U.Episteme(SafetyAnalysisReport#42):
 finding: margins insufficient
 Evidence: [src: scr://analysis/safety-2025-07]
```

### ECPF.5:6 - Bias-Annotation

The first bias is false-negative acceptance: the agent accepts output that "sounds FPF-like" but carries hidden category errors. The repair is mechanical scanning — the listed rules are applied to every claim, not only "suspicious" ones.

The second bias is over-correction: the agent rewrites acceptable episteme notation because it worries about edge cases. The repair is the declared scope — only the listed distinctions are mandatory. Do not invent additional distinctions.

### ECPF.5:7 - Conformance Checklist

| Check | Passing condition |
|---|---|
| CC-ECPF5.1 Episteme-action scan clean | No U.Episteme-type entity is followed by an action verb. |
| CC-ECPF5.2 Role-in-composition scan clean | No Role appears in a parts list, aggregation, or composition slot. |
| CC-ECPF5.3 Method performer present | Every Method/Work claim names a System#Role:Context performer. |
| CC-ECPF5.4 MethodDescription/Method/Work separated | No MethodDescription in run-time slots; no Work in design-time slots. |
| CC-ECPF5.5 Collective/Set distinction correct | Acting groups use ComponentOf; MemberOf reserved for mathematical sets. |
| CC-ECPF5.6 Violations repaired | Every detected violation has a canonical reformulation applied. |

### ECPF.5:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
|---|---|---|
| "Sounds FPF" acceptance | Output uses FPF vocabulary but carries category errors. | Run mechanical distinction scan, not "does it sound right?" |
| Self-magic | A system is described as acting on itself without reflexive split. | Apply ReflexiveSplit template. |
| Role-as-part | A role is listed as a component of a system. | Move role to RoleAssignment; parts are holons only. |
| Episteme-agency | "The report says", "the spec requires", "the model predicts." | Add the acting system; Episteme is the content, not the actor. |
| Method confusion | "The method was executed" mixing description, capability, and execution. | Split into MethodDescription, Method, Work in separate slots. |

### ECPF.5:9 - Consequences

Applying ECPF.5 adds verification overhead but prevents silent propagation of category errors through multi-agent chains. A category error in one agent's output, if consumed by another FPF-literate agent, can cause compound errors — the downstream agent reasons about an Episteme as if it were an acting System, or includes a Role in a structural composition.

The listed distinctions are deliberately minimal — they cover the most common category errors in LLM-generated episteme notation. Additional distinctions belong in FPF Core (A.7), not in this DPF.

### ECPF.5:10 - Rationale

Strict distinctions are the most fragile part of episteme notation generation because natural language training data systematically blurs them. An LLM trained on "the report concluded" will naturally generate "the specification decided." Three alternative enforcement approaches were considered and rejected: (1) training-time mitigation — infeasible because the rendering agent is a fixed pretrained model, not a fine-tuned one; (2) prompt-embedded rules — unreliable for 30B-35B models because natural-language rules compete with natural-language generation priors; (3) human review — contradicts the machine-for-machine use case where output must be structurally valid before agent consumption. Mechanical checking — scanning for Episteme-type nouns followed by action verbs, scanning parts lists for Role-typed entries, scanning Tᴿ slots for MethodDescription — is the only approach that works at inference time without model retraining and without human in the loop. It is also the approach that aligns with the skill's self-check architecture: each scan maps to a YES/NO question in the self-check.

### ECPF.5:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| Guarino & Welty, "Evaluating Ontological Decisions with OntoClean," 2002 — identity, rigidity, unity | Adopt | Mandatory A.7 distinctions + canonical reformulations | Reopen on FPF `A.7` distinction revision |
| Bender et al., "On the Dangers of Stochastic Parrots," 2021 — LLMs reflect training distribution | Adopt | Mechanical scan rules (Episteme-agency, Role-in-partOf, Method confusion) | Reopen when a new category-error class is observed in field use |

### ECPF.5:12 - Relations

- **Specializes:** `NSTD.4` (Voice, Focalization, and Agency) — ECPF.5 adds FPF-specific strict distinction rules.
- **Uses:** `A.7` (Strict Distinction) — for the mandatory A.7 distinctions.
- **Uses:** `A.12` (External Transformer and Reflexive Split) — for external transformer and reflexive split patterns.
- **Uses:** `A.14` (Advanced Mereology) — for PhaseOf temporal part/state.
- **Uses:** `ECPF.2` (Typed Slot Rendering) — for typed slot discipline.
- **Follows:** `ECPF.2` — slots must be typed before distinctions are checked.
- **Precedes:** `ECPF.6` — distinction compliance is an evaluation dimension.

### ECPF.5:End
