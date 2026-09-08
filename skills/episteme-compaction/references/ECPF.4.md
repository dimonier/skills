---
id: ECPF.4
title: "Evidence Chain and ADI Reasoning Rendering"
status: source-faithful
keywords: [evidence, ADI, EPV-DAG, SCR, epistemic-debt, reasoning]
dependencies:
  builds_on:
    - A.10
    - B.3.4
    - B.5
  coordinates_with: []
---

# ECPF.4 — Evidence Chain and ADI Reasoning Rendering

> **Trigger:** When a claim must carry evidence provenance and a multi-hypothesis reasoning trace, and the output would otherwise present conclusions without showing support, alternatives, or falsifications.
>
> **Governing FPF patterns:**
>   → A.10 (Evidence Graph Referring — EPV-DAG, SCR/RSCR, verifiedBy/validatedBy)
>   → B.3.4 (Evidence Decay and Epistemic Debt — ED calculation, Refresh/Deprecate/Waive)
>   → B.5 (Canonical Reasoning Cycle — ADI)
> **Type:** DPF pattern body
> **Status:** source-faithful
> **Normativity:** Normative

> **Primary EntityOfConcern:** `EvidenceAndReasoningRendering@Context`, the act of rendering EPV-DAG evidence provenance and ADI multi-hypothesis reasoning in compact episteme output.

### ECPF.4:1 - Problem frame

Use this pattern when an FPF claim must carry evidence provenance and reasoning trace, and the output would otherwise present conclusions without showing which evidence supports them, which hypotheses were considered, and which were falsified.

First useful move: render the Evidence block with verifiedBy/validatedBy anchors, SCR references, and ED calculation. Render the Reasoning block with Abduction→Deduction→Induction cycle and at least 3 hypotheses.

What goes wrong if missed: claims appear as bare assertions. Downstream consumers cannot distinguish verified claims from guesses, cannot trace evidence to carriers, and cannot see which alternative explanations were considered and rejected.

What this buys: every conclusion is traceable to evidence carriers and specific reasoning steps. Alternative hypotheses are visible, making the reasoning auditable.

Not this pattern when the claim is a definition, axiom, or convention that does not require empirical evidence. Use `ECPF.2` for typed definitional claims.

### ECPF.4:2 - Problem

Free-form prose often presents conclusions without evidence provenance and single-cause reasoning without alternative exploration. "The service crashed because of a race condition" hides: what tests confirmed this, which evidence carriers hold the test results, what other causes were considered, and why they were rejected. FPF evidence graph and ADI notation make these dimensions explicit.

### ECPF.4:3 - Forces

| Force | Tension |
|---|---|
| Evidence completeness vs rendering brevity | Full EPV-DAG rendering with all nodes and edges is verbose; selective rendering may hide gaps. |
| Hypothesis count vs analysis depth | 5+ hypotheses provide coverage but require domain knowledge for generation. |
| ED calculation vs freshness tracking | Epistemic Debt requires valid_until dates; perpetual evidence (axioms) needs explicit null marking. |

### ECPF.4:4 - Solution

Apply two rendering subsystems: Evidence Graph rendering for provenance, and ADI cycle rendering for reasoning.

**Evidence Graph Rendering:**

EPV-DAG is a typed acyclic graph separate from mereology. Nodes:
- `SymbolCarrier` — U.System in CarrierRole (file, dataset, log)
- `TransformerRole` — external transformer performing observation
- `MethodDescription` — method blueprint (design-time)
- `Observation` — dated assertion/result
- `U.Episteme` — knowledge holon

Edges: `evidences`, `derivedFrom`, `measuredBy`, `interpretedBy`, `usedCarrier`, `happenedBefore`

**Evidence anchors:**

| Anchor | Type | Use |
|---|---|---|
| `verifiedBy` | Formal | Proofs, static guarantees, model-checking |
| `validatedBy` | Empirical | Tests, measurements, experiments, observations |

**SCR / RSCR:**
- SCR (Symbol Carrier Register) — exhaustive carrier registry
- RSCR (Release SCR) — SCR adapted to bounded context

**Evidence Decay (ED):**

```
valid_until: ISO-8601-date | null    // null = perpetual (axioms/physical laws only)
ED_t(i) = k * max(0, t - valid_until_i)
ED_t(A) = Σ_i ED_t(evidence_i)
```

Actions when ED exceeds budget: `Refresh` | `Deprecate` | `Waive`

**Evidence rendering template:**

```
Evidence:
 claim: "<claim text>"
 verifiedBy: [<proof-id>, src: <scr-ref>]
 validatedBy: [<test-id>, src: <scr-ref>]
 valid_until: <ISO-8601-date | null>
 ED: <value>
 externalTransformer: <System#ObserverRole:Context>
```

**ADI Reasoning Rendering:**

The ADI cycle: Abduction (generate hypotheses) → Deduction (derive testable predictions) → Induction (test against reality).

| Phase | Name | Question |
|---|---|---|
| **A** | Abduction | What is the most plausible new explanation? |
| **D** | Deduction | If hypothesis is true, what logically follows? |
| **I** | Induction | Do predictions match reality? |

**ADI rendering template:**

```
Reasoning(issue: <ID>):
 Abduction:
  H₁: <hypothesis 1>
  H₂: <hypothesis 2>
  H₃: <hypothesis 3>
  …    (minimum 3, recommend 5)
 Deduction:
  H₁ → <prediction 1>
  H₁ → <prediction 2>
  H₃ → <prediction 3>
  …
 Induction:
  test(H₁): <method> → <result> ✓/✗
  test(H₃): <method> → <result> ✓/✗
  src: <scr-ref>
 Conclusion: <selected hypothesis> confirmed; R = <high/medium/low>; <falsified hypotheses> rejected
```

**ADI rules (normative):**

1. Minimum 3 hypotheses in Abduction; recommend 5 for diagnostic or safety cases.
2. Each hypothesis must have at least one testable prediction in Deduction.
3. Induction must show test method and result (✓ confirmed / ✗ falsified) for at least two hypotheses.
4. Falsified hypotheses must remain visible — do not delete rejected alternatives.
5. Conclusion must name which hypothesis is selected and at what confidence.

### ECPF.4:5 - Archetypal Grounding

**Tell:** A diagnostic claim "the service crashes because of a race condition" is rendered with 5 hypotheses, testable predictions, and induction results showing H₁ confirmed, H₃ falsified, and the remaining hypotheses still under investigation.

**Show — complete Evidence + Reasoning block:**

```
Evidence:
 claim: "Service S handles load L with p99 latency ≤ δ"
 verifiedBy: [proof: invariant-check.sc, src: scr://proof/inv-042]
 validatedBy: [test: load-test-2025-07, src: scr://test/lt-789]
 valid_until: 2026-01-01
 ED: 0
 externalTransformer: TestTeam#ObserverRole:LoadTestContext

Reasoning(issue: NPE@UserService.java:42):
 Abduction:
  H₁: user=null when session.expired → tokenRefresh.race → null return
  H₂: getUserProfile() called before user initialization
  H₃: race condition in concurrent token refresh
  H₄: session timeout config not synced with refresh interval
  H₅: null returned from cache on cache-miss without fallback
 Deduction:
  H₁ → NPE occurs only after 30min inactivity
  H₁ → logs show failed refresh before NPE
  H₃ → NPE reproduces under load (concurrent requests)
 Induction:
  test(H₁): reproduce after 30min idle → NPE ✓
  test(H₃): load test 1000 req/s → NPE not reproduced ✗
  src: scr://test/repro-2025-07-03
 Conclusion: H₁ confirmed; R = high; H₃ falsified
```

### ECPF.4:6 - Bias-Annotation

The first bias is single-hypothesis reasoning: Abduction lists only one hypothesis, collapsing ADI into a linear assertion. The repair is the minimum-3 rule.

The second bias is survivorship: falsified hypotheses are deleted from the output, making the reasoning look infallible. The repair is the visibility rule — falsified hypotheses must stay.

### ECPF.4:7 - Conformance Checklist

| Check | Passing condition |
|---|---|
| CC-ECPF4.1 Evidence anchors present | At least one of verifiedBy or validatedBy is present with SCR reference. |
| CC-ECPF4.2 valid_until explicit | Every evidence block has a valid_until date or null (with justification). |
| CC-ECPF4.3 ED calculated | Epistemic Debt value is stated. |
| CC-ECPF4.4 Minimum 3 hypotheses | Abduction lists at least 3 hypotheses. |
| CC-ECPF4.5 Testable predictions | Each hypothesis has at least one testable prediction in Deduction. |
| CC-ECPF4.6 At least 2 tests in Induction | Induction shows test results for at least two hypotheses. |
| CC-ECPF4.7 Falsified hypotheses visible | Rejected hypotheses are not deleted. |
| CC-ECPF4.8 Conclusion explicit | Selected hypothesis, confidence, and rejected hypotheses are named. |

### ECPF.4:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
|---|---|---|
| Bare conclusion | Output has no Evidence or Reasoning block. | Add Evidence block (at least [pending]) and ADI Reasoning block. |
| Single hypothesis | Only one hypothesis listed, no alternatives explored. | Generate at least 3 hypotheses; force alternative generation. |
| Deleted falsification | Falsified hypotheses removed to make reasoning look clean. | Keep falsified hypotheses visible with ✗ markers. |
| Untestable predictions | Deduction lists vague predictions ("it will fail sometimes"). | Make predictions specific: conditions, thresholds, observable outcomes. |
| Stale evidence | valid_until in the past, no ED flag. | Calculate ED; flag if > 0; trigger Refresh/Deprecate/Waive decision. |

### ECPF.4:9 - Consequences

Applying ECPF.4 adds significant rendering overhead (Evidence + Reasoning blocks add ~40-80 tokens) but transforms conclusions from assertions into auditable reasoning chains. Downstream agents can verify evidence freshness, reproduce reasoning steps, and identify which alternatives remain unexplored.

The ADI cycle is deliberately visible — it does not hide the reasoning process behind a single conclusion. This makes the output suitable for safety-case analysis, compliance documentation, and multi-agent reasoning chains.

### ECPF.4:10 - Rationale

Evidence and reasoning rendering are the most trust-sensitive episteme notation operations. A conclusion without evidence provenance is indistinguishable from a guess. A conclusion without alternative hypotheses is indistinguishable from confirmation bias. Making both dimensions explicit is the minimum requirement for agent-to-agent communication where downstream decisions depend on upstream claims.

### ECPF.4:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| Peirce, "Collected Papers," 1931-1958 — abduction distinct from deduction and induction | Adopt | ADI reasoning template (A→D→I phases) | Reopen on FPF `B.5` ADI revision |
| W3C PROV — provenance data model tracing assertions to sources | Adopt | Evidence Graph rendering: EPV-DAG, SCR/RSCR, verifiedBy/validatedBy | Reopen on FPF `A.10` evidence-graph revision |
| FPF `B.3.4` — ED as function of time since valid_until | Adopt | Evidence Decay (ED) rendering + Refresh/Deprecate/Waive | Reopen on FPF `B.3.4` revision |

### ECPF.4:12 - Relations

- **Specializes:** `NSTD.3` (Source Mechanism, Event Model, and Coherence) — ECPF.4 adds evidence and reasoning chain rendering.
- **Uses:** `A.10` (Evidence Graph Referring) — for EPV-DAG, SCR/RSCR, verifiedBy/validatedBy.
- **Uses:** `B.3.4` (Evidence Decay and Epistemic Debt) — for ED calculation and Refresh/Deprecate/Waive.
- **Uses:** `B.5` (Canonical Reasoning Cycle) — for ADI cycle structure.
- **Follows:** `ECPF.3` — trust metrics reference evidence chains.
- **Precedes:** `ECPF.6` — evidence completeness is an evaluation dimension.

### ECPF.4:End
