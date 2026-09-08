---
id: ECPF.2
title: "Typed Slot Rendering for Episteme Claims"
status: source-faithful
keywords: [typed-slot, episteme-fence, U.-types, sourceClaims, fpfMetadata]
dependencies:
  builds_on:
    - A.6.3.RT
    - A.6.3
    - E.10.D2
    - C.2.1
    - A.6.5
    - A.1
    - A.2
    - A.3.4
    - A.15
  coordinates_with: []
---

# ECPF.2 — Typed Slot Rendering for Episteme Claims

> **Trigger:** When a claim currently expressed as free-form prose (F0) must be rendered as a typed, named, bounded slot in a compact episteme block (```episteme id="..." context="..."``` code fence).
>
> **Governing FPF patterns:**
>   → A.6.3.RT (Representation-Scheme Transition — the forward render: prose → typed slots)
>   → A.6.3 (Epistemic Viewing umbrella)
>   → E.10.D2 (Describe_EoC_DescEp morphism)
>   → C.2.1 (U.Episteme slot relation / EpistemeSlotRelation)
>   → A.6.5 (U.RelationSlotDiscipline)
>   → A.1 / A.2 / A.3.4 / A.15 (U.-type vocabulary and role-method-work alignment)
> **Type:** DPF pattern body
> **Status:** source-faithful
> **Normativity:** Normative

> **Primary EntityOfConcern:** `TypedSlotRendering@Context`, the act of replacing a free-form prose claim with a U.-typed slot in an compact episteme output block.

### ECPF.2:1 - Problem frame

Use this pattern when a claim currently expressed as free-form prose (F0) must be rendered as a typed, named, bounded slot in an compact episteme output (F4-F5), and the claim's type, scope, and boundary would otherwise remain implicit.

First useful move: render source claims as an ````episteme id="..." context="..."```` code fence block.

What goes wrong if missed: claims remain as untyped prose sentences. Downstream agents cannot parse claim types, cannot distinguish a diagnostic claim from a trust claim from a work record, and cannot compose claims into larger reasoning chains.

What this buys: every claim becomes machine-parseable — typed, named, and bounded by its slot.

Not this pattern when the output is at F0-F2 formality (teaching, casual, non-technical). Use `ECPF.1` to decide formality first.

### ECPF.2:2 - Problem

Free-form prose (F0) carries claims as sentences without explicit type, scope, or boundary metadata. An agent reading "the service is probably crashing because of a race condition" cannot tell: is this a diagnostic claim or a hypothesis? What is the confidence? What evidence supports it? What system performed the diagnosis? episteme typed-slot rendering makes these dimensions explicit.

### ECPF.2:3 - Forces

| Force | Tension |
|---|---|
| Typing completeness vs rendering speed | Every slot adds overhead; missing slots hide information. |
| Template rigidity vs domain flexibility | Fixed templates ensure parsability; domain-specific slots may be needed. |
| U.-prefix precision vs agent training | U.-prefixes require FPF literacy; 30B-35B models may need explicit vocabulary. |

### ECPF.2:4 - Solution

Render ALL source text as an `Episteme` block — the single universal template. Source claims become indented values under source-derived sections. FPF-computed or attributed metadata goes into optional `[bracketed]` sections.

#### ECPF.2:4.0 — Episteme Block Structure and the Episteme Template

Every episteme block consists of two layers:

| Layer | Contents | Purpose | Survives round-trip? |
|---|---|---|---|
| sourceClaims | All non-bracketed content: section names, claim values, claim-level markers | Substantive claims from source | Yes — unchanged across episteme↔prose |
| fpfMetadata | `[bracketed]` sections: `[aggregation]`, `[assurance]`, `[reasoning]`, `[evidence]` | Computed or attributed description | No — omitted in reconstruction |

**The Episteme code fence (universal):**

Every Episteme block is delimited by a markdown code fence with language identifier `episteme` and two required attributes on the opening fence line. The `Episteme(id, context)` header line is removed — `id` and `context` are now fence attributes. This is a breaking format change; no backward compatibility with the old inline `Episteme(id, context)` format is preserved.

````
```episteme id="<id>" context="<BoundedContext>"
section:
  claim-value [confidence: high/medium/low] [src: scr-ref]
  claim-value
  claim-value:
   sub-value
   sub-value
 section:
  claim-value [src: scr-ref]

 [aggregation]:                        # fpfMetadata, optional
  F_eff = min(F_i)
  R_raw = min(R_i) along cutset
  R_eff = max(0, R_raw − Φ(CL_min))
  G_eff = SpanUnion({G_i})
  invariants:
   IDEM: ✓/✗  COMM: ✓/✗  LOC: ✓/✗  WLNK: enforced/cutset  MONO: holds/conditional

 [assurance]:                          # fpfMetadata, optional
  F_eff = value
  G_eff = coverage
  R_eff = value
  CL_min = CLk (edge description)
  Cutset: bottleneck path

 [reasoning]:                          # fpfMetadata, optional
  Abduction:
   H₁: hypothesis
   ...
  Deduction:
   H₁ → prediction
   ...
  Induction:
   test(H₁): method → result ✓/✗
   ...

  [evidence]:                           # fpfMetadata, optional
   verifiedBy: [proof-ids | pending]
   validatedBy: [test-ids | pending]
   valid_until: ISO-date | null
   ED: number

  [style]:                              # fpfMetadata, optional; form descriptor for reconstruction
   genre: <required if [style] present — e.g. Russian folk tale / diagnostic report / ADR>
   register: <required if [style] present — e.g. oral-colloquial, archaic / technical-neutral>
   voice: <optional; e.g. 3rd-person narrator, formulaic>
   devices: <optional; e.g. repetition-with-increment, rhyming refrain, epithets>
   signature: <optional; verbatim recurring surface, if load-bearing — e.g. song, catchphrase>
```
````

**Structural rules (normative):**

1. `id` and `context` — required attributes on the opening fence line (` ```episteme id="..." context="..." `). `context` is a `U.BoundedContext` scoping the Episteme's claims.
2. `section` names — free-form, source-derived. Use dotted-notation for hierarchy (`Solution.Quartet`, `Solution.RoleAssignment`). No FPF-internal prefixes (`Γ_`, `U.`).
3. Claims — indented values under a section. No `claim:` prefix; indentation carries structure. Deeper indent = sub-claim.
4. `[confidence: h/m/l]` — only when source expresses uncertainty.
5. `[src: scr-ref]` — only when source provides an explicit reference.
6. At least one section with at least one claim.
7. `[aggregation]` — optional. All-or-nothing: if present, all five Quintet invariants and all aggregation fields must be present. Only when claims compose into a system/episteme/process.
8. `[assurance]` — optional. Only when a trust/confidence assessment is load-bearing.
9. `[reasoning]` — optional. Only when diagnostic/analytical reasoning is performed (ADI cycle).
10. `[evidence]` — optional. Only when source provides evidence provenance.
11. **No fabricated metadata.** Source has no evidence → no `[evidence]`. No trust claim → no `[assurance]`. No hypothesis generation → no `[reasoning]`. No composition → no `[aggregation]`.

**`[style]` — form descriptor (normative):**

`[style]` is an optional fpfMetadata section that captures the source's **form** (genre, register, voice, devices, signature) for use during reconstruction. Unlike other `[bracketed]` sections, `[style]` is **read as a form instruction** by the reconstructor — it guides the shape of generated prose without its lines ever becoming labelled claims.

12. `[style]` is optional. Fill it when reconstruction target must reproduce a **recognizable source form** (narrative, marketing, legal, etc.). Skip for form-neutral technical output.
13. If `[style]` present, `genre` and `register` are required; `voice`, `devices`, `signature` are optional.
14. `[style]` is fpfMetadata: its contents do NOT emit as claim values into prose.
15. **Exception to the omit-all-brackets rule:** reconstruction MUST read `[style]` and conform the generated prose to its genre, register, voice, and devices. It is the one bracketed section consumed-not-dropped.
16. `signature` may hold verbatim recurring surface (refrain, catchphrase) **only when it is load-bearing form**, not general content. `signature` is optional within optional `[style]`: fill only when a recognizable recurring signature is present; otherwise omit.

**Normative rule (sourceClaims/fpfMetadata split):**

Non-bracketed content = sourceClaims. `[bracketed]` sections = fpfMetadata. Reconstruction: sourceClaims → prose; fpfMetadata → omitted. This split is structural and prevents the semantic drift mechanism demonstrated in `samples/`.

sourceClaims MUST contain **only propositions present in or directly recoverable from the source**. Interpretation, strategy analysis, method-step labelling, cross-episode generalization, and conclusions the source does not state are **fpfMetadata**, not sourceClaims. They go into a `[bracketed]` section (`[reasoning]`, `[analysis]`, or `[assurance]` as appropriate) so they are **omitted on reconstruction**.

Litmus test: *"Is this claim asserted by the source, or inferred by the renderer?"* Inferred → bracket it.

**Common rendering patterns (illustrative, not normative):**

| Source type | Typical claims | Typical `[bracketed]` |
|---|---|---|
| Diagnostic (crash, bug) | RootCause, Trigger, Path, Fix | `[reasoning]` + `[evidence]` |
| Architecture decision | Decision, Context, Rationale, Tradeoffs | `[assurance]` + `[evidence]` |
| Code/design review | Issue, Current, Problem, Fix | usually none |
| Project status | Progress, Done, InProgress, Blocked | usually none |
| System composition | parts as claims | `[aggregation]` |
| Trust assessment | claim being assessed | `[assurance]` |
| Pattern body, summary, explanation | source-derived sections | none by default |
| Self-action | Regulator, Regulated, Boundary | usually none |

These are not separate templates — they are natural claim-structuring patterns that emerge from using the single Episteme template. An agent does not choose a template; it always renders as Episteme and adds `[bracketed]` sections only as needed.

**U.-type quick reference (types required for ECPF.2 rendering):**

| U.-type | Use for |
|---|---|
| `U.Entity` | Anything individuable and referable under bounded context |
| `U.Holon` | Whole-with-parts; part of larger wholes |
| `U.System` | Acting physical/operational holon; bears roles, executes Work |
| `U.Episteme` | Knowledge holon (spec, proof, model, narrative output); non-agentive |
| `U.Role` | Context-bound work-facing role value (mask, not behaviour) |
| `U.RoleAssignment` | Holder#Role:Context binding |
| `U.Capability` | System ability/envelope to enact a Method under conditions |
| `U.Method` | Abstract order-sensitive way-of-doing (design-time) |
| `U.MethodDescription` | Description episteme of a Method (recipe/SOP) |
| `U.Work` | Dated execution (run-time, immutable) |
| `U.Transformation` | Bounded change of a holon under conditions |
| `U.BoundedContext` | Context where terms have meaning |
| `U.ClaimGraph` | Claim body of an Episteme (nodes=claims, edges=relations) |
| `U.ReferenceScheme` | How claims are read as statements about EntityOfConcern |

**Markers and modifiers (normative):**

| Marker | Meaning | Example |
|---|---|---|
| `[confidence: high/medium/low]` | Claim certainty | `race condition [confidence: high]` |
| `[pending]` | Unverified information | `adjust pool [pending]` |
| `[src: <id>]` | Source reference | `[src: scr://test/lt-789]` |
| `→` | Causality/sequence | `expired → race → null` |
| `@` | Time window | `@2025-07-03T10:00..10:45` |
| `#` | RoleAssignment | `DevTeam#DeployerRole:ProdCtx` |
| `⊑` | Subtype | `U.System ⊑ U.Holon` |
| `Tᴰ` / `Tᴿ` | Design-time / Run-time | `MethodDescription ∈ Tᴰ; Work ∈ Tᴿ` |

**Formatting rules (normative):**

````
```episteme id="<id>" context="<context>"
section:
 claim-value [markers]
 claim-value:
  sub-value
```
````

**Formatting prohibitions (normative):**

- No `claim:` prefix — indentation carries structure
- No preambles ("I've reviewed…", "After analyzing…", "Here is my analysis…")
- No closing pleasantries ("Hope this helps!", "Let me know if…")
- No unmarked uncertainty ("probably", "likely", "maybe" → use `[confidence: ...]`)
- No mixed design-time and run-time in one claim
- No actions assigned to U.Episteme (only U.System can act)
- No non-English claim values (exceptions: proper names, domain terms, wordplay, quoted material)
- No fpfMetadata in reconstructed prose (omit all `[bracketed]` content; translate FPF markers to plain language)
- No fabricated `[bracketed]` sections not supported by source content

#### ECPF.2:4.0a — Ontology: EpistemeSlotRelation in Rendered Output

Rendering is not a format conversion — it is the `Describe_EoC_DescEp` morphism (A.7:5.9, E.10.D2). The agent receives an EntityOfConcern (source text, system, event, or problem) and produces a `U.Episteme` that describes it.

**Core transform:**

```
Describe_EoC_DescEp(EntityOfConcern) → U.Episteme
  entityOfConcernRef: ref to described entity
  boundedContextRef: context scoping the claims
  viewpointRef: narrative perspective
  content: U.ClaimGraph (the output text — sections, claims, relations)
  referenceScheme: interpretation frame (how claims bind to entities)
```

**Every rendered Episteme block fills these slots:**

| Slot | Filled by | Mandatory? |
|---|---|---|
| `EntityOfConcernSlot` | What is this narrative about? (source topic, system, event) | Yes |
| `GroundingHolonSlot` | Where are claims grounded? (optional for narrative) | No |
| `ClaimGraphSlot` | The output body — sections, indented claims, bracketed metadata | Yes |
| `ViewpointSlot` | Who is this narrative for? (consumer type from ECPF.1) | Yes |
| `ReferenceSchemeSlot` | How are claims interpreted as statements about EntityOfConcern? | Implicit |

**The Episteme code fence as carrier:**

The `episteme id="..." context="..."` code fence is the publication carrier (C.2.1:4.2.3, E.17). The fence:

- `id` — maps to episteme identity
- `context` — maps to `BoundedContextRef` in `DescriptionContext`
- Non-bracketed content — `ClaimGraph` body
- `[bracketed]` sections — FPF-computed metadata, separate from ClaimGraph

**Agent self-check (ontology):**
After rendering, the agent verifies:

1. `EntityOfConcernSlot` filled — what is being described?
2. `ViewpointSlot` implied — who is the consumer? (from ECPF.1 decision)
3. `ClaimGraphSlot` filled — at least one section with ≥1 claim
4. `content` carries typed claims with FPF markers where justified
5. `[bracketed]` sections present only when source justifies them

**`[style]` ontology mapping:** `[style]` is a form descriptor that targets `ViewpointSlot` and `ReferenceSchemeSlot` — it tells the reconstructor *how to read claims into prose*, not *what the claims are*. Genre, register, voice, and devices inform `ReferenceSchemeSlot` (interpretation frame for binding claims to entities). The style is part of the description's viewpoint, not part of the described entity.

### ECPF.2:5 - Archetypal Grounding

**Tell — checklist explanation (no fabricated metadata):** Source text about checklists (7 lines, ~50 tokens) is rendered as Episteme with source-derived sections and claim-level `[src]` markers from wiki-links. No `[bracketed]` sections — source has no evidence, no aggregation, no reasoning.

````
```episteme id="Checklist" context="WorkMethodology"
Definition:
 tool improving work results without requiring skill improvement
[src: scr://vault/ControlList]
 most useful description for a method [src: scr://vault/Checklist]
Relation:
 complement instructions/regulations, do not replace
 daily reminder how to apply method + verify execution
Structure:
 items within one section — no order, any order or parallel
 if order matters → split into sequential sections
```
````

**Tell — diagnostic with reasoning and evidence:** Source describes AuthService crashes (~250 tokens). Rendered as Episteme with `[reasoning]` and `[evidence]` `[bracketed]` sections because source contains diagnostic reasoning and test evidence.

````
```episteme id="AuthService crashes" context="ProductionOps"
RootCause:
 JWTVerify executes after RateLimit [confidence: high]
Trigger:
 unauth req → RL exhaustion → legit lockout → cascade fail
Path:
 RateLimit → JWTVerify → null user → NPE → crash
Fix:
 reorder: JWTVerify → RateLimit [confidence: high]
 add null-check before user.* [confidence: medium]
 
 [reasoning]:
  Abduction:
   H₁: middleware order incorrect (JWT after RL)
   H₂: RL pool exhaustion under unauth flood
   H₃: missing null-check on user object
   H₄: race in token refresh under load
   H₅: config mismatch session timeout vs refresh interval
  Deduction:
   H₁ → unauth reqs counted against RL → legit users blocked
   H₂ → cascade: RL full → 429 → retry storm → crash
  Induction:
   test(H₁): reorder middleware → crashes stop ✓
   test(H₄): load test 1000 req/s → no race ✗
   src: scr://test/repro-2025-07-03
 
 [evidence]:
  verifiedBy: [proof: middleware-order.sc, src: scr://proof/mw-042]
  validatedBy: [test: auth-load-2025-07, src: scr://test/alt-789]
  valid_until: 2026-01-01
  ED: 0
```
````

Token savings: ~68% vs F0 prose, sourceClaims lossless, `[bracketed]` sections omitted in reconstruction.

**Tell — pattern body (no fabricated metadata):** Source: A.3 Transformer Constitution (~1384 tokens). Rendered with source-derived sections, no `[bracketed]` sections.

````
```episteme id="A.3.TransformerConstitution" context="FPF.Kernel"
Intent:
 substrate-neutral way to state who acts, under which role
 fixes Transformer Quartet for all kernel & Γ reuse
 builds on A.2 Holon-Role, A.4 Temporal Duality
 guarded by A.7 Strict Distinction, A.10 Evidence Graph
Problem:
 5 recurrent failures (self-magic, plan=event, capability=result,
episteme-as-doer, scope-leak) [confidence: high]
Solution.Quartet:
 ActingSide — System bearing TransformerRole [confidence: high]
 MethodDescription — Tᴰ recipe/algorithm/SOP via carrier [confidence: high]
 Method — Tᴰ order-sensitive composition, mask-of-work [confidence: high]
 Work — Tᴿ dated execution; isExecutionOf MethodDescription [confidence: high]
```
````

Token ratio: ~290 tokens vs ~1384 source (~79% savings, lossless over source claims).

### ECPF.2:6 - Bias-Annotation

The first drift is over-marking: an agent adds `[confidence: high]` or `[src: ...]` to every claim regardless of source. The repair: use markers only when the source justifies them — uncertainty or explicit references.

The second drift is fabricated metadata: an agent adds `[evidence]` or `[reasoning]` blocks the source does not contain. The repair: check each `[bracketed]` section against the source; remove any unsupported.

The third drift is **interpretation-in-sourceClaims**: the agent places derived analysis (strategy, method-step labels, outcome generalization, cross-episode pattern) in non-bracketed sections, so it leaks into the reconstruction as if it were source text. The repair: apply the litmus test per claim ("asserted by source, or inferred by renderer?"); move inferred content to a `[bracketed]` metadata section.

### ECPF.2:7 - Conformance Checklist

| Check | Passing condition |
|---|---|
| CC-ECPF2.1 Episteme rendered | Output is an ````episteme id="..." context="..."```` code fence block. |
| CC-ECPF2.2 At least one section with claims | Minimum one section with at least one indented claim value. |
| CC-ECPF2.3 Markers source-justified | `[confidence]` only when source has uncertainty; `[src]` only when source has explicit reference. |
| CC-ECPF2.4 No untyped prose claims | No free-form prose sentences as claim values. |
| CC-ECPF2.5 Uncertainty marked | Every intrinsically uncertain value carries `[confidence: ...]` or `[pending]`. |
| CC-ECPF2.6 Design/run-time separated | Tᴰ and Tᴿ never mixed in one claim. |
| CC-ECPF2.7 No prohibited content | No preambles, pleasantries, `claim:` prefix, or unmarked uncertainty. |
| CC-ECPF2.8 Output language is English | All claim values in English (exceptions: proper names, domain terms, wordplay, quoted material). |
| CC-ECPF2.9 No fabricated metadata | No `[bracketed]` section present without source justification. |
| CC-ECPF2.10 `[aggregation]` all-or-nothing | If present → all five Quintet invariants and aggregation fields present. |

### ECPF.2:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What fails | Repair |
|---|---|---|
| Prose-as-claim | A claim value is a full English sentence instead of a compact typed value. | Extract key proposition; drop prose wrapping. |
| Over-marking | `[confidence: high]` on every claim or `[src: ...]` without source reference. | Only mark where source justifies — explicit uncertainty or references. |
| Fabricated metadata | `[evidence]`, `[reasoning]`, `[assurance]` blocks not in source. | Remove any `[bracketed]` section source does not contain. |
| Incomplete aggregation | `[aggregation]` present but invariants or fields missing. | All-or-nothing: fill all fields or remove `[aggregation]`. |
| Type-invention | Non-existent U.-type used. | Restrict to the U.-type quick reference. |

### ECPF.2:9 - Consequences

Applying ECPF.2 adds typing overhead — each claim must be classified and slotted. The payoff is machine-parseable, composable, auditable output.

The Episteme template eliminates template-selection errors (agents no longer choose Diag vs ADR vs Note) and template-specific slot discipline (no memorizing which slots belong to which template). Structure emerges from the source's own organization.

### ECPF.2:10 - Rationale

Typed slot rendering is the core episteme compaction pattern. The single Episteme template was chosen over multiple task-specific templates for three reasons:

1. **Ontological truth.** All rendered text is `U.Episteme` — knowledge claims. The source never says "I am a diagnosis" or "I am an architecture decision." These are downstream agent interpretations that should not constrain the rendering.

2. **Eliminating template-selection failure.** With multiple templates, agents had to choose before rendering. Wrong choice caused structural loss (take4: ADR for pattern body). With one template, there is no choice to get wrong.

3. **Bracketed metadata boundary.** `[aggregation]`, `[assurance]`, `[reasoning]`, `[evidence]` are structurally separated from source claims. This makes the sourceClaims/fpfMetadata split transparent: non-bracketed = source, bracketed = FPF-computed. A simpler, mechanical boundary than the prior approach of template-specific split rules.

### ECPF.2:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| Protocol Buffers, Apache Avro, JSON Schema — schema-driven data interchange | Adopt | :4.0 Episteme template as the single typed-slot schema | Reopen when the Episteme fence/template format changes |
| Shannon entropy preservation under bijective encoding (information theory) | Adopt | sourceClaims/fpfMetadata split + lossless forward render | Reopen when the U.-type vocabulary or markers change |

### ECPF.2:12 - Relations

- **Specializes:** `NSTD.2` (Structure-to-Sequence Ordering) — ECPF.2 adds FPF-specific slot ordering and typing rules.
- **Uses:** `A.6.3` (Epistemic Viewing) — umbrella governing the viewing/compaction operation.
- **Uses:** `A.6.3.RT` (Representation-Scheme Transition) — the forward render: prose → typed slots.
- **Uses:** `A.1` (Holonic Foundation) — for U.Entity, U.Holon, U.System, U.Episteme types.
- **Uses:** `A.2` (Role Taxonomy) — for U.Role, U.RoleAssignment, U.Capability.
- **Uses:** `A.3.4` (U.Transformation) — for bounded change as narrative unit.
- **Uses:** `A.6.5` (U.RelationSlotDiscipline) — for slot typing discipline.
- **Uses:** `A.15` (Role-Method-Work Alignment) — for U.Method, U.MethodDescription, U.Work distinctions.
- **Uses:** `C.2.1` (U.EpistemeSlotRelation) — for output ontology: EntityOfConcern, ClaimGraph, ReferenceScheme.
- **Uses:** `E.10.D2` (EntityOfConcern/DescriptionEpisteme) — for the Describe_EoC_DescEp boundary.
- **Follows:** `ECPF.1` — formality must be selected before typing is applied.
- **Precedes:** `ECPF.3`, `ECPF.4`, `ECPF.5` — typing must be in place before aggregation, evidence, or distinction rules apply.
- **Inverse of:** `ECPF.7` — the reverse render (notation → prose); ECPF.7 reconstructs what ECPF.2 compacts.

### ECPF.2:End
