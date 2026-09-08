---
id: ECPF.6
title: "Episteme Compaction Quality Evaluation and Admission"
status: source-faithful
keywords: [quality, evaluation, admission, compactness, verdict]
dependencies:
  builds_on: []
  coordinates_with:
    - E.21
    - E.22
    - E.23
---

# ECPF.6 — Episteme Compaction Quality Evaluation and Admission

> **Trigger:** When a compact-episteme rendering must be evaluated for quality before admission, against structural dimensions (not fluency), and proceeding without evaluation would admit hidden defects.
>
> **Governing FPF patterns:**
>   → E.21 (Pattern Quality Evaluation)
>   → E.22 (Quality Evaluation Framing)
>   → E.23 (Repeated Improvement)
> **Type:** DPF evaluation pattern
> **Status:** source-faithful
> **Normativity:** Normative

> **Primary EntityOfConcern:** `EpistemeCompactionQualityResultRow@Context`, a DPF-local evaluation record for one episteme compaction version evaluated for one declared use.

### ECPF.6:1 - Problem frame

Use this pattern when a generated episteme compaction must be evaluated for quality before admission — and the evaluation must check structural correctness, not fluency — and proceeding without evaluation would admit output with hidden type errors, missing evidence, or category violations.

First useful move: evaluate the rendering against six dimensions, produce `EpistemeCompactionQualityResultRow@Context` with values and repair actions, and assign a quality verdict: admitted, requires-repair, or rejected.

What goes wrong if missed: generated episteme notation is accepted based on fluency or "looks right" heuristics. Hidden structural defects — untyped slots, missing evidence anchors, category errors — propagate to downstream consumers.

What this buys: every episteme compaction has a quality verdict based on explicit, checkable dimensions. Defects are named and assigned repair actions before admission.

Not this pattern when evaluating general prose quality (fluency, style, readability). Use the upstream Narrativization DPF (`NSTD.6`) for general narrative quality evaluation.

### ECPF.6:2 - Problem

Generated episteme notation is structurally complex — typed slots, aggregation operators, evidence graphs, reasoning chains, strict distinctions — and quality cannot be judged by fluency. "Looks like episteme notation" is not a quality standard. A rendering may be syntactically valid episteme notation but carry type errors, incomplete evidence, missing cutset analysis, or hidden category violations.

### ECPF.6:3 - Forces

| Force | Tension |
|---|---|
| Evaluation depth vs evaluation speed | Full dimensional evaluation takes time; fast "looks right" checks miss defects. |
| Dimension independence vs cross-dimension coupling | A type error in one slot may cascade to evidence and reasoning defects. |
| Admission threshold vs use-case variance | "Good enough" depends on the consumer and audit requirements. |

### ECPF.6:4 - Solution

Evaluate one admitted episteme compaction version for one declared use against six dimensions. Each dimension produces a value, an evidence basis, and, if below threshold, a lowering reason, a repair action, and a reopen condition.

**Six evaluation dimensions:**

| Dimension | What is evaluated | Threshold for admission |
|---|---|---|
| **Compactness** | Token ratio vs equivalent F0 prose | < 50% of F0 token count (i.e., ≥ 50% savings) |
| **Slot completeness** | All required template slots filled | 100% required slots filled; optional slots marked [pending] if not available |
| **Type correctness** | Every slot value has valid U.-type or marker | 100% typed/marked; no untyped prose in slots |
| **Evidence traceability** | Every claim has evidence anchor or [pending] | 100% of claims have verifiedBy, validatedBy, or [pending] |
| **Strict-distinction compliance** | No A.7 category errors | 0 violations of the mandatory A.7 distinctions |
| **Hybrid-mode appropriateness** | In hybrid mode, episteme blocks self-contained; no contradiction with plain text | episteme blocks parseable independently; plain text does not broaden or contradict |

**Quality verdict:**

| Verdict | Condition |
|---|---|
| `admitted` | All six dimensions at or above threshold. |
| `requires-repair` | One or more dimensions below threshold; specific repair actions named. |
| `rejected` | Critical failure: type errors make output unparseable; evidence anchors absent on safety claims; category errors on load-bearing distinctions. |

**Evaluation result record:**

```episteme id="EpistemeCompactionQualityResultRow" context="FPF.Rendering"
Evaluation:
 evaluatedRenderingRef: <rendering version id>
 declaredUse: <consumer type and task type>
 evaluatedDimensionRows:
  Compactness: <value> (F0-equiv: <tokens>, FPF: <tokens>)
  SlotCompleteness: <value> (<missing slots>)
  TypeCorrectness: <value> (<untyped slots>)
  EvidenceTraceability: <value> (<unanchored claims>)
  StrictDistinctionCompliance: <value> (<violations>)
  HybridModeAppropriateness: <value> (<issues>)
 evidenceBasis: [<check method or tool reference>]
 overallVerdict: admitted | requires-repair | rejected
 loweringReasons: [<per-dimension reasons for below-threshold values>]
 repairActions: [<per-dimension repair actions>]
 reopenCondition: <what triggers re-evaluation>
```

**Compactness calculation:**

```
Compactness = episteme_token_count / F0_equivalent_token_count
Threshold for admission: Compactness ≤ 0.50 (i.e., ≥ 50% savings)
```

**Improvement loop:**

For repeated improvement, package evaluation rows as `EpistemeCompactionQualityEvaluationResult@Context` and prepare `EpistemeCompactionImprovementLoopInput@Context` for `E.22`/`E.23`. Do not count a style pass, prompt retry, or cosmetic edit as improvement until the changed rendering version is re-evaluated through ECPF.6.

### ECPF.6:5 - Archetypal Grounding

**Tell:** A generated `Diag(AuthService crashes)` block is evaluated. Compactness: 0.32 (68% savings) — admitted. Slot completeness: Evidence block present, valid_until filled — admitted. Type correctness: all slots typed — admitted. Evidence traceability: SCR references present — admitted. Strict distinctions: 1 violation (H₃ says "the spec requires" without acting system) — requires-repair. Verdict: requires-repair; repair action: apply canonical reformulation to H₃.

**Show — evaluation result row:**

```episteme id="EpistemeCompactionQualityResultRow" context="AuthDiag-v1"
Evaluation:
 evaluatedRenderingRef: Diag(AuthService crashes)@2025-07-04T14:00
 declaredUse: agent-to-agent diagnostic
 evaluatedDimensionRows:
  Compactness: 0.32 (F0-equiv: 250, FPF: 80) — admitted
  SlotCompleteness: 100% — admitted
  TypeCorrectness: 100% — admitted
  EvidenceTraceability: 100% (SCR refs present) — admitted
  StrictDistinctionCompliance: 0.86 (1 violation: H₃ "spec requires" Episteme-agency) — requires-repair
  HybridModeAppropriateness: N/A (not hybrid) — admitted
 evidenceBasis: manual check against CC-ECPF2-5 checklists
 overallVerdict: requires-repair
 loweringReasons:
  - StrictDistinctionCompliance: H₃ uses "spec requires" without acting System#Role:Context
 repairActions:
  - Rewrite H₃: DesignService#TransformerRole:SpecCtx updated spec carrier → new req added
 reopenCondition: after repair action applied, re-evaluate all dimensions
```

### ECPF.6:6 - Bias-Annotation

The first bias is fluency-as-quality: accepting output because it "looks like FPF" without dimensional checking. The repair is the six-dimension checklist — every rendering is evaluated against explicit criteria.

The second bias is dimension-shopping: an evaluator picks the dimensions that pass and ignores the ones that fail. The repair is the all-dimensions rule — every dimension must be evaluated; N/A is permitted only for inapplicable dimensions (e.g., HybridModeAppropriateness when output is F4-F5 only).

### ECPF.6:7 - Conformance Checklist

| Check | Passing condition |
|---|---|
| CC-ECPF6.1 Rendering version identified | The evaluated rendering has a version identifier or timestamp. |
| CC-ECPF6.2 Declared use stated | The consumer type and task type are named. |
| CC-ECPF6.3 All six dimensions evaluated | Every applicable dimension has a value (N/A only for inapplicable). |
| CC-ECPF6.4 Evidence basis present | The evaluation method or check tool is named. |
| CC-ECPF6.5 Verdict assigned | admitted, requires-repair, or rejected is stated. |
| CC-ECPF6.6 Repair actions specific | Each below-threshold dimension has a specific repair action. |
| CC-ECPF6.7 Reopen condition stated | What triggers re-evaluation is named. |

### ECPF.6:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
|---|---|---|
| Fluency eval | Evaluating "does it read well?" instead of the six dimensions. | Use the six-dimension checklist; fluency is not a dimension. |
| Self-eval without checklist | Agent evaluates its own output without mechanical checking. | Run CC-ECPF2 through CC-ECPF5 checklists before assigning verdict. |
| Threshold creep | Lowering admission threshold to admit borderline output. | Record threshold and evidence basis; do not adjust threshold post-hoc. |
| Repair without re-eval | Repair applied but rendering not re-evaluated. | After any repair, re-run all six dimensions. |
| Missing reopen condition | No condition stated for when to re-evaluate. | Always state a reopen condition: rendering change, use change, evidence decay, or schedule. |

### ECPF.6:9 - Consequences

Applying ECPF.6 adds evaluation overhead (~3-5 minutes per rendering) but prevents admission of structurally defective episteme notation. The six-dimension framework is deliberately simple — it covers the minimum viable quality checks for episteme notation without requiring full FPF Core pattern-quality evaluation (which belongs in `E.21`).

The improvement loop connects to `E.22`/`E.23` for repeated quality cycles, making the evaluation results actionable for continuous improvement rather than one-time admission gating.

### ECPF.6:10 - Rationale

Quality evaluation is the last rendering step because it gates admission. Without it, all other patterns (ECPF.1-5) produce output that may be syntactically valid but structurally defective. The six dimensions were selected to cover the failure modes that ECPF.1-5 are designed to prevent — compactness (ECPF.1), slot completeness and type correctness (ECPF.2), evidence traceability (ECPF.3-4), strict distinctions (ECPF.5), and hybrid appropriateness (ECPF.1).

### ECPF.6:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| ISO/IEC 25010:2023 — quality model with characteristics, sub-characteristics, measures | Adopt | Six-dimension evaluation table + verdict thresholds | Reopen when a rendering defect class is found that no dimension covers |
| Deming, "Out of the Crisis," 1986 — Plan-Do-Check-Act cycle | Adopt | Improvement loop + reopenCondition field | Reopen on FPF `E.22`/`E.23` revision |

### ECPF.6:12 - Relations

- **Specializes:** `NSTD.6` (Declared-Use Narrative Rendering Quality Evaluation) — ECPF.6 adds FPF-specific quality dimensions.
- **Uses:** `ECPF.1`, `ECPF.2`, `ECPF.3`, `ECPF.4`, `ECPF.5` — dimensions correspond to pattern compliance.
- **Coordinates with:** `E.22` (Quality Evaluation Framing) and `E.23` (Repeated Improvement) — for improvement loop.
- **Coordinates with:** `E.21` (Pattern Quality Evaluation) — for full pattern-quality evaluation when needed.
- **Exits to:** `NSTD.6` when evaluating general narrative quality rather than FPF structural quality.

### ECPF.6:End
