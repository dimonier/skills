---
id: ECPF.TG
title: "Transformation Governance"
status: source-faithful
keywords: [round-trip, drift, idempotence, boundary, governance]
dependencies:
  builds_on:
    - A.6.3
  coordinates_with:
    - A.6.3.CR
    - A.6.3.CSC
---

# ECPF.TG — Transformation Governance

> **Trigger:** When compact episteme blocks and prose are transformed back and forth across multiple passes, and round-trip idempotence (sourceClaims/fpfMetadata stability) must hold structurally.
>
> **Governing FPF patterns:**
>   → A.6.3 (Epistemic Viewing — umbrella for the representation-scheme transitions)
>   → A.6.3.CR / A.6.3.CSC (the fidelity disciplines the two directions are held to)
> **Type:** DPF pattern body (cross-cutting: governs the composition of `ECPF.2` and `ECPF.7`)
> **Status:** source-faithful
> **Normativity:** Normative

> **Primary EntityOfConcern:** `RoundTripGovernance@Context`, the boundary rule that keeps the episteme↔prose round-trip idempotent across multiple passes by different agents.

### ECPF.TG:1 - Problem frame

Use this pattern when episteme blocks and prose are transformed back and forth across multiple passes — by the same or different agents, separated in time — and semantic drift must be prevented structurally, not by relying on any single agent remembering the text's provenance.

First useful move: enforce the block-structure boundary (TG-1) and delegate the two directions to `ECPF.2` (forward) and `ECPF.7` (reverse), so the round-trip is idempotent without agent-side provenance knowledge.

What goes wrong if missed: each pass adds interpretive detail that displaces the original meaning, and the drift compounds across agents (the mechanism observed in `samples/`).

What this buys: `Episteme₁.sourceClaims ≈ Episteme₂.sourceClaims` and `Episteme₁.fpfMetadata ≈ Episteme₂.fpfMetadata` hold across any number of passes, with no agent tracking provenance.

Not this pattern when there is no round-trip — a single forward render (`ECPF.2`) or a single reconstruction (`ECPF.7`) needs only its own pattern. This pattern governs their **composition** across passes.

### ECPF.TG:2 - Problem

When episteme blocks and prose are transformed back and forth across multiple passes, semantic drift occurs unless the transformation boundary is structurally disciplined. The mechanism observed in `samples/`:

1. An ````episteme```` code fence is produced from source text. It contains both source claims (non-bracketed content) and FPF-computed metadata (`[aggregation]`, `[assurance]`, `[reasoning]`, `[evidence]`).
2. The episteme block is reconstructed into prose. The reconstruction mistakenly includes the computed metadata as content — F_eff values, R_eff values, Quintet invariants, emergence descriptions.
3. A second agent receives this prose and compacts it again. It treats the leaked metadata as new source claims — reinterprets them, recalculates metrics from them, adds new Assurance blocks.
4. The cycle compounds: each pass adds interpretive detail that displaces the original meaning.

This is not a bug in individual agents. It is a missing boundary constraint: the episteme↔prose transformation lacked a rule about what crosses the boundary.

### ECPF.TG:3 - Forces

| Force | Settlement |
|---|---|
| Structural vs remembered | The boundary must hold structurally (TG-1), not by any agent remembering provenance. |
| Two directions vs one rule | The forward and reverse renders are governed by their own patterns (`ECPF.2`/`ECPF.7`); this pattern owns only the composition boundary. |
| Content vs metadata | sourceClaims cross the boundary unchanged; fpfMetadata is dropped on reconstruction — the split is the whole discipline. |

### ECPF.TG:4 - Solution

**TG-1 (block structure — the boundary).** An Episteme block is delimited by an ````episteme id="..." context="..."```` code fence. `id` and `context` are required attributes on the opening fence line. The body contains non-bracketed source claims and optional `[bracketed]` fpfMetadata sections. All `[bracketed]` sections (`[aggregation]`, `[assurance]`, `[reasoning]`, `[evidence]`) are structurally separated from source claims and omitted in reconstruction (ECPF.2:4.0).

**TG-2 (round-trip discipline — delegation).** The two directions are governed by their own patterns, not re-specified here:

| Direction | Pattern | Transformation type | Fidelity discipline |
|---|---|---|---|
| Forward (prose → notation) | `ECPF.2` | `A.6.3.RT` | `A.6.3.CR` (conservative) or `A.6.3.CSC` (controlled loss, `structural-analysis` mode only) |
| Reverse (notation → prose) | `ECPF.7` | `A.6.3.RT` | `A.6.3.CR` only, plus `A.6.3.NAR` for form restoration |

**Consequence (idempotence).** When TG-1 holds, ECPF.2 and ECPF.7 are each applied, and compaction is deterministic over sourceClaims, round-trip is idempotent: `Episteme₁.sourceClaims ≈ Episteme₂.sourceClaims` and `Episteme₁.fpfMetadata ≈ Episteme₂.fpfMetadata`. No agent-side knowledge of text provenance is required — the boundary rules make the property hold structurally.

### ECPF.TG:5 - Archetypal Grounding

**Correct (round-trip idempotent over a composing source):**

```
Source (0-src.txt):
 "The auth pipeline has three stages: rate limiting, JWT verification, and
  user lookup. Rate limiting is the weakest stage; its reliability is 0.6 and
  the concurrent-load path is not yet validated."

Episteme₁ (sourceClaims):
 parts:
  RateLimit
  JWTVerify
  UserLookup
 weakest:
  RateLimit

Episteme₁ (fpfMetadata — legitimate: the source composes into a pipeline):
 [aggregation]:
  F_eff = min(F_i) = F0
  R_raw = min(R_i) = 0.6 (RateLimit)
  R_eff = max(0, 0.6 − Φ(CL1))
  G_eff = SpanUnion({G_i})
  invariants: IDEM ✓ COMM ✓ LOC ✓ WLNK enforced MONO holds

Prose₁ (reconstruction from Episteme₁ — sourceClaims only):
 "The auth pipeline has three stages: rate limiting, JWT verification, and
  user lookup. Rate limiting is the weakest stage."
 ↑ No F_eff, no R_raw, no invariants, no CL — fpfMetadata omitted.

Episteme₂ (from Prose₁):
 sourceClaims ≈ Episteme₁.sourceClaims
 fpfMetadata ≈ Episteme₁.fpfMetadata (recomputed from same claims → same values)
```

**Incorrect (the `samples/` drift mechanism — metadata leaks into prose):**

```
Prose₁ includes "All five invariants (idempotency, commutativity, locality,
weakest link, monotonicity) hold. Reliability is limited to 0.6 due to the
unvalidated concurrent-load path."

Episteme₂ reads invariants and R_raw=0.6 as new source claims →
 - [aggregation] recomputed on inflated claims
 - New [assurance] block with CL_min, ED, valid_until added
 - Metric values drift: F_eff: F0 → F2, R_raw: 0.6 → 0.5
```

A non-composing source (e.g. the checklist definition in `ECPF.2:5`) carries no
`[aggregation]` at all — computing one would itself be an `ECPF.2` rule-11
violation. The drift mechanism is only demonstrated on a source that legitimately
carries fpfMetadata.

### ECPF.TG:6 - Bias-Annotation

The first bias is attributing drift to individual agents: teams patch the "bad" agent instead of the missing boundary. The repair is TG-1 — a structural rule, not a behavioural instruction.

The second bias is over-governing: adding extra governance rules that re-specify the directions instead of delegating to `ECPF.2`/`ECPF.7`. The repair is TG-2 — this pattern owns the boundary and the composition, nothing more.

### ECPF.TG:7 - Conformance Checklist

| Check | Passing condition |
|---|---|
| CC-ECPFTG.1 Boundary declared | Every Episteme block is a ````episteme id="..." context="..."```` fence with `id` and `context` required. |
| CC-ECPFTG.2 sourceClaims/fpfMetadata split structural | Non-bracketed = sourceClaims; `[bracketed]` = fpfMetadata, omitted on reconstruction. |
| CC-ECPFTG.3 Directions delegated | Forward render cites `ECPF.2`; reverse render cites `ECPF.7`; neither is re-specified here. |
| CC-ECPFTG.4 Idempotence claimed | Round-trip is idempotent over sourceClaims and fpfMetadata, structurally, not by provenance memory. |
| CC-ECPFTG.5 No leaked metadata in prose | Reconstructed prose contains no F_eff/R_eff/Quintet/emergence/Assurance content. |

### ECPF.TG:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
|---|---|---|
| Agent-blame | Drift treated as one agent's error, not a missing boundary. | Enforce TG-1 structurally. |
| Boundary unspecified | No rule states what crosses the episteme↔prose boundary. | Declare the sourceClaims/fpfMetadata split as the boundary. |
| Direction re-specified | TG rules re-implement the forward/reverse render instead of delegating. | Delegate to `ECPF.2`/`ECPF.7`; keep only the composition boundary. |
| Provenance memory | Idempotence relies on an agent remembering the text's history. | Make idempotence hold structurally from the boundary rules. |

### ECPF.TG:9 - Consequences

When TG-1/TG-2 hold, the round-trip is idempotent across any number of passes and any number of agents, with no shared state and no provenance memory. The cost: the boundary discipline must be applied on every render and reconstruction — a small per-pass overhead that buys compounding-drift elimination. The property is structural, so it survives agent substitution, time separation, and interleaving with other tasks.

### ECPF.TG:10 - Rationale

The drift mechanism is a boundary failure, not an agent failure, so the governance must be a boundary rule. Two design choices follow: (1) make the sourceClaims/fpfMetadata split the single structural boundary, because every leak observed in `samples/` is a `[bracketed]` section crossing into prose; (2) delegate the directions to `ECPF.2`/`ECPF.7` rather than re-specifying them, so the transformation types (`A.6.3.RT`) and fidelity disciplines (`A.6.3.CR`/`A.6.3.CSC`) have a single home. A cross-cutting pattern that owned the render logic itself would fork it from the directional patterns and reintroduce exactly the drift it exists to prevent.

### ECPF.TG:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| W3C PROV — provenance as a distinct layer from content | Adopt | sourceClaims vs fpfMetadata split (TG-1) as the content/provenance boundary | Reopen when the provenance/content distinction in FPF changes |
| FPF `A.6.3` — representation-scheme transition umbrella | Adopt | Both directions typed as `A.6.3.RT`, with CR/CSC as fidelity discipline (TG-2) | Reopen on FPF `A.6.3` revision |
| Idempotence as a structural round-trip property (information theory) | Adapt | Round-trip idempotence stated as a structural consequence, not a remembered invariant | Reopen when the Episteme fence format changes |

### ECPF.TG:12 - Relations

- **Builds on (FPF):** `A.6.3` (Epistemic Viewing — umbrella), `A.6.3.CR` / `A.6.3.CSC` (fidelity disciplines).
- **Coordinates with:** `ECPF.2` (forward render) and `ECPF.7` (reverse render) — this pattern governs their composition across passes, delegating the directions to them.
- **Precedes:** nothing — it is loaded last in the round-trip chain, when the two directions are already composed.

### ECPF.TG:End
