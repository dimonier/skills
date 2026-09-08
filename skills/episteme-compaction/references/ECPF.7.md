---
id: ECPF.7
title: "Reconstruction from Episteme Notation to Prose"
status: source-faithful
keywords: [reconstruction, reverse-render, source-return, style, round-trip]
dependencies:
  builds_on:
    - A.6.3.RT
    - A.6.3.CR
    - A.6.3.CSC
    - A.6.3.NAR
  coordinates_with:
    - E.17.EFP
---

# ECPF.7 — Reconstruction from Episteme Notation to Prose

> **Trigger:** When a compact episteme block (```episteme id="..." context="..."``` code fence) must be reconstructed into prose, and the result must recover the source's claims without leaking FPF-computed metadata or FPF-internal terminology.
>
> **Governing FPF patterns:**
>   → A.6.3.RT (Representation-Scheme Transition — the reverse render: notation → prose)
>   → A.6.3.CR (Conservative Retextualization discipline — entity-of-concern-preserving, no claim widening)
>   → A.6.3.CSC (Controlled Semantic Coarsening — source-return, loss visibility)
>   → A.6.3.NAR (Structure-to-Narrative Rendering — restoring connected narrative form: genre/voice, `[style]`)
>   → E.17.EFP (SourcePinnedExplanation — source-return classification)
> **Type:** DPF pattern body
> **Status:** source-faithful
> **Normativity:** Normative

> **Primary EntityOfConcern:** `ReconstructionFromNotationToProse@Context`, the reverse render that maps a compact episteme (typed-slot notation) back into source-genre prose.

### ECPF.7:1 - Problem frame

Use this pattern when a compact episteme block must be reconstructed into prose — the reverse direction of ECPF.2 — and the reconstruction must recover the source's claims and, where the source is narrative, its form, without leaking FPF-computed metadata or FPF-internal terminology into the prose.

First useful move: apply the reconstruction rules — reverse render (`A.6.3.RT`) with `A.6.3.CR` discipline applied **only** to sourceClaims; omit all fpfMetadata; translate FPF-internal terms back to plain domain language; restore connected narrative form via `A.6.3.NAR` / `[style]`.

What goes wrong if missed: computed metadata and FPF terminology leak into the prose and are re-read by the next agent as source claims, triggering compounding semantic drift (see `ECPF.TG`).

What this buys: an idempotent round-trip — reconstructed prose is indistinguishable in form from fresh original text, and re-compaction reproduces the same sourceClaims and fpfMetadata.

Not this pattern when the task is forward compaction only (use `ECPF.2`) or when no notation is involved (use the upstream `NSTD` patterns for general prose rendering).

### ECPF.7:2 - Problem

Reconstruction has three distinct failure channels, each a leak across the notation→prose boundary:

1. **Metadata leakage.** The computed `[bracketed]` sections (`[aggregation]`, `[assurance]`, `[reasoning]`, `[evidence]`) are rendered as prose content — F_eff, R_eff, Quintet invariants, emergence descriptions. The next agent reads them as source and recalculates metrics from them.
2. **Terminology retention.** FPF-internal terms (`U.*` prefixes, `Tᴰ`/`Tᴿ`, `[confidence: ...]`, `[src: ...]`, `[pending]`, `Γ_*`, `ComponentOf`/`ConstituentOf`/`PortionOf`/`PhaseOf`) are left verbatim in prose, where they read as domain content rather than structural scaffolding.
3. **Form flattening.** Episteme section names are emitted as headings, and pattern-compressed repetition is left as a summary description instead of being re-expanded into concrete instances. The result is a labelled dump, not connected prose.

### ECPF.7:3 - Forces

| Force | Tension |
|---|---|
| Fidelity vs form | `A.6.3.CR` forbids claim widening; `A.6.3.NAR` demands genre/voice restoration. They are orthogonal and must not be conflated — form is restored, claims are not invented. |
| Omission vs translation | fpfMetadata is **omitted**; FPF-internal terms are **translated**, not omitted. Confusing the two leaks content or leaves jargon. |
| Source-return vs independence | The reconstruction is orientation-only (`SourcePinnedExplanation`); operative claims must return to the source, never to the reconstruction. |

### ECPF.7:4 - Solution

Apply the reverse render: `A.6.3.RT` (notation → prose) with `A.6.3.CR` conservative discipline applied **only to sourceClaims**. fpfMetadata is omitted entirely. The type of transformation is RT (a representation-scheme change, not same-regime rewording); CR is the fidelity discipline layered on top of it, not the transformation type.

**Rule 1 — Source-claims only.** Reconstructed prose carries only sourceClaims. fpfMetadata is omitted. The prose MUST NOT contain: F_eff, R_eff, G_eff, R_raw values; Quintet invariant names or assessments; emergence descriptions (MHT, etc.); Assurance blocks; aggregation formulas; graph dependency descriptions; cutset names; SCR references that were computed rather than sourced.

**Rule 2 — Term translation.** FPF-internal terminology must be translated back to plain domain language:

| FPF term in source claim | Must become in prose |
|---|---|
| `U.MethodDescription(X)` | "X", "description of X", "X as a method" — no `U.` prefix |
| `U.Work`, `U.Method` | "work", "method", "execution" — no `U.` prefix |
| `Tᴰ` / `Tᴿ` | Omit entirely unless equivalent domain concept exists ("design", "execution") |
| `[confidence: high/medium/low]` | Omit; if needed, use ordinary qualifiers ("likely", "confirmed") — never bracket form |
| `[src: scr://...]` | Omit; source tracking is FPF-internal |
| `[pending]` | Omit; do not render "unverified" or "pending evidence" in prose |
| `ComponentOf`, `ConstituentOf`, `PortionOf`, `PhaseOf`, etc. | "part of", "belongs to", or restructure sentence — no mereological term |
| `PhaseOf` | "during", "at time", or restructure sentence |
| `PortionOf` | "part of", "amount of" |
| `Γ_epist`, `Γ_sys`, etc. | Never appear in prose |
| `valid_until: null`, `ED: 0`, Evidence block content | Never appear in prose — Evidence is fpfMetadata |

**Rule 3 — Form restoration (`A.6.3.NAR`).** Reconstruction MUST be connected narrative in the **genre and voice of the source** (a tale reads as a tale, a diagnostic as a diagnostic), not a labelled dump of Episteme sections. This form-restoration slice is governed by `A.6.3.NAR`, with `[style]` (genre/register/voice/devices/signature) as its parameter carrier.

| FPF in source | Reconstruction must |
|---|---|
| `Setup:` / `Encounters:` section labels | Dissolve into narrative flow; no heading |
| `pattern: Predator threatens → sings → rolls away` | Re-expand each encounter as its own passage |
| `each encounter extends escaped-from list by one` | Actually list the growing sequence per encounter |

Section names of the Episteme are **scaffolding, not prose headings.** Do NOT emit them as titles/labels. Pattern-compressed repetition — `pattern: X → Y → Z`, `each encounter extends … by one` — MUST be re-expanded into concrete instances matching the source's own unfolding.

**Rule 4 — `[style]` consumption.** If `[style]` is present, the reconstruction MUST adopt its genre, register, voice, and devices, and reproduce any `signature` verbatim. `[style]` is read as a form instruction (the one `[bracketed]` section consumed-not-dropped); its lines never appear as labelled claims. All other `[bracketed]` sections remain omitted.

**Rule 5 — Source-return.** Reconstruction is classified as `SourcePinnedExplanation` (`E.17.EFP`) with bounded use = orientation only. Operative claims return to the FPF form or the original source, never to the reconstruction (`E.17:5.1c`).

### ECPF.7:5 - Archetypal Grounding

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

### ECPF.7:6 - Bias-Annotation

The first bias is over-inclusion: the reconstructor renders fpfMetadata as prose content, treating computed metrics as claims. The repair is the omit-all-brackets rule — sourceClaims only.

The second bias is terminology retention: the reconstructor leaves `U.*`, `Tᴰ`/`Tᴿ`, `[confidence]`, `[src]` verbatim, treating structural scaffolding as content. The repair is the term-translation table (Rule 2).

The third bias is form flattening: the reconstructor emits a labelled dump of sections instead of connected prose. The repair is Rule 3 — dissolve scaffolding, re-expand pattern-compression.

### ECPF.7:7 - Conformance Checklist

| Check | Passing condition |
|---|---|
| CC-ECPF7.1 Source-claims only | Reconstructed prose contains only sourceClaims; no fpfMetadata content (F_eff, R_eff, Quintet, emergence, Assurance, cutset). |
| CC-ECPF7.2 Terms translated | No `U.*`, `Tᴰ`/`Tᴿ`, `[confidence]`, `[src]`, `[pending]`, `Γ_*`, or mereological terms remain in prose. |
| CC-ECPF7.3 Scaffolding dissolved | Episteme section names are not emitted as headings or labels. |
| CC-ECPF7.4 Pattern re-expanded | Pattern-compressed repetition is re-expanded into concrete instances. |
| CC-ECPF7.5 Connected narrative | Reconstruction reads as connected prose in the source's genre/voice, not a labelled dump. |
| CC-ECPF7.6 `[style]` consumed | If `[style]` present, its genre/register/voice/devices are adopted and `signature` reproduced verbatim. |
| CC-ECPF7.7 Source-return stated | Reconstruction is classified `SourcePinnedExplanation` (orientation only). |

### ECPF.7:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
|---|---|---|
| Metadata-as-content | fpfMetadata rendered as prose claims | Omit all `[bracketed]` sections except `[style]` |
| Jargon retention | FPF-internal terms left in prose | Apply the term-translation table (Rule 2) |
| Scaffolding-as-headings | Section names emitted as titles | Dissolve into narrative flow (Rule 3) |
| Summary-of-pattern | Pattern-compression left as a description | Re-expand each instance |
| Self-sufficient reconstruction | Reconstruction treated as operative | Source-return (Rule 5) |

### ECPF.7:9 - Consequences

Applying ECPF.7 makes the round-trip idempotent when combined with ECPF.2 and the block-structure boundary: `Episteme₁.sourceClaims ≈ Episteme₂.sourceClaims` and `Episteme₁.fpfMetadata ≈ Episteme₂.fpfMetadata`. No agent-side knowledge of text provenance is required — the boundary rules make the property hold structurally. The cost: reconstruction is orientation-only and cannot be relied upon for operative claims.

### ECPF.7:10 - Rationale

The reverse render is a distinct pattern from the forward render (ECPF.2) because its failure modes are the mirror image: forward compaction risks *under*-marking (losing type/evidence), while reconstruction risks *over*-inclusion (leaking metadata and jargon). The governing discipline also differs: forward `structural-analysis` may admit controlled loss (`A.6.3.CSC`), while reconstruction never widens claims (`A.6.3.CR` conservative only). Separating it from ECPF.2 — and from the round-trip governance pattern `ECPF.TG` — makes each direction independently loadable and testable, and keeps the transformation type (RT) explicit rather than mislabeled as CR.

### ECPF.7:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| W3C PROV — provenance as a distinct layer from content | Adopt | Rule 1 sourceClaims-only + fpfMetadata omission | Reopen when the sourceClaims/fpfMetadata split changes |
| Narratology / FPF `A.6.3.NAR` — structure-to-narrative rendering | Adopt | Rule 3 form restoration + `[style]` as parameter carrier | Reopen on FPF `A.6.3.NAR` revision |

### ECPF.7:12 - Relations

- **Builds on (FPF):** `A.6.3.RT` (reverse render), `A.6.3.CR` (conservative discipline), `A.6.3.CSC` (source-return), `A.6.3.NAR` (form restoration).
- **Uses (FPF):** `E.17.EFP` (SourcePinnedExplanation — source-return classification).
- **Inverse of:** `ECPF.2` — the forward render; ECPF.7 is its reverse operation.
- **Coordinates with:** `ECPF.TG` — the round-trip governance pattern that constrains the composition of ECPF.2 and ECPF.7 across passes.

### ECPF.7:End
