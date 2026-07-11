---
name: fpf-narrative
description: |
  Generate compact, unambiguous FPF-structured output at F4-F5 formality level.
  Use when writing for AI agent consumers or FPF-literate humans where token
  economy and auditability matter: diagnostics, architecture decisions, code
  reviews, status reports, trust assessments, system compositions. Replaces
  verbose prose (F0) with typed-slot notation (~65% token savings, lossless).
  Do NOT use for: casual chat, teaching, non-technical audiences, creative tasks.
generatedFrom: FPFNarrativeProsePrinciplesFramework@2026-07-11
---

# FPF Narrative Prose — Runtime

## CONCEPTS

Ontology: output IS `U.Episteme` with filled `U.EpistemeSlotRelation`. Rendering IS `Describe_EoC_DescEp`: EntityOfConcern → DescriptionEpisteme.

U.System acts. U.Episteme does NOT. U.Work = run-time (Tᴿ), immutable. U.Method / U.MethodDescription = design-time (Tᴰ). Tᴰ and Tᴿ never mix in one slot.

U.Role = mask. U.RoleAssignment = `System#Role:Context`. Roles NEVER in parts lists. Holarchies = substantive holons only.

U.Transformation = bounded change of a holon under conditions. Base narrative unit (actions, events). U.Capability = system ability/envelope to enact a Method under conditions.

U.ClaimGraph = claim body of an Episteme (nodes=claims, edges=relations). U.ReferenceScheme = how claims bind to entities as statements about EntityOfConcern.

Γ aggregation: weakest-link. `F_eff = min(F_i)`. `R_eff = max(0, min(R_i) − Φ(CL_min))`. All 5 Quintet invariants checked when `[aggregation]` present.

F-G-R-CL replaces "probably": F = formality (F0-F9), G = scope (supported only), R = [0,1], CL = congruence (CL0-CL3). Φ(CL): lower CL → larger penalty.

Evidence: `verifiedBy` (formal), `validatedBy` (empirical). SCR: `scr://<domain>/<id>`. ED: `k × max(0, today − valid_until)`. valid_until null = perpetual (axioms/laws only). ED actions: Refresh / Deprecate / Waive.

ADI: ≥3 hypotheses in Abduction. ≥1 prediction per hypothesis. ≥2 tested in Induction (✓/✗). Never 1 hypothesis. Never delete falsified.

Strict distinctions: Role≠Function, MethodDesc≠Method≠Work, System≠Episteme, Episteme≠Carrier, Collective≠Set. Scan every output before emitting.

External transformer: holder(Agent) ≠ Target. No self-magic. Self-action → Reflexive Split: System = {Regulator, Regulated} with HolonDelimitation and HolonBoundaryCrossing.

## FORMAT SELECTION

| Consumer | Task | Audit? | Formality |
|---|---|---|---|
| AI agent | Diagnostics, ADR, review, trust | Yes | F4-F5 |
| AI agent | Status, work log | Sometimes | F3-F4 |
| FPF-literate human | ADR, safety case | Yes | F4-F5 |
| FPF-literate human | Status, casual review | No | F3 hybrid |
| Non-technical human | Any | No | F0 plain |
| Mixed (agent + human) | Any | Yes | F4-F5 + 1-sentence plain |

Rules: Default F0. Upgrade per table. Downstream consumer needs F4-F5 → whole chain uses F4-F5. Consumer unknown → F3 hybrid. Teaching → F0-F2 regardless.

Fallback:

| Situation | Action |
|---|---|
| Non-technical human | F0. No FPF notation. |
| Educational/training | F0-F2. |
| Casual dialogue/chat | F0. |
| Creative/brainstorming | F0. |
| Consumer rejects FPF | F0 or F3 hybrid. |

Rendering mode: `retelling-fidelity` (recoverable to source-like text) vs `structural-analysis` (expose structure). Reconstruction-oriented task → `retelling-fidelity`: no generalization/conclusions in sourceClaims, do not erase source instances via pattern-compression.

## OUTPUT TEMPLATE

````
```episteme id="<id>" context="<BoundedContext>"
section:
 claim-value [confidence: high/medium/low] [src: scr-ref]
 claim-value:
  sub-value

[aggregation]:           # only when claims compose
 F_eff = min(F_i)
 R_raw = min(R_i) along cutset
 R_eff = max(0, R_raw − Φ(CL_min))
 G_eff = SpanUnion({G_i})
 invariants:
  IDEM: ✓/✗  COMM: ✓/✗  LOC: ✓/✗  WLNK: enforced/cutset  MONO: holds/conditional

[assurance]:             # only when trust assessment
 F_eff = value
 G_eff = coverage
 R_eff = max(0, min(R_i) − Φ(CL_min))
 CL_min = CLk (edge description)
 Cutset: bottleneck path

[reasoning]:             # only when diagnostic/ADR
 Abduction:
  H₁: hypothesis
  ...  (≥3, recommend 5)
 Deduction:
  H₁ → prediction
  ...
 Induction:
  test(H₁): method → result ✓/✗
  test(H₂): method → result ✓/✗  (≥2 tested)
  src: scr-ref
 Conclusion: selected hypothesis; R = high/medium/low; falsified: [H…]

[evidence]:              # only when source has evidence
  verifiedBy: [proof-ids | pending]
  validatedBy: [test-ids | pending]
  valid_until: ISO-date | null
  ED: number

[style]:                  # optional; form descriptor; guides reconstruction, never becomes prose
  genre: <required — e.g. Russian folk tale / diagnostic report / ADR>
  register: <required — e.g. oral-colloquial, archaic / technical-neutral>
  voice: <optional; e.g. 3rd-person narrator, formulaic>
  devices: <optional; e.g. repetition-with-increment, rhyming refrain, epithets>
  signature: <optional; verbatim recurring surface, if load-bearing — e.g. song, catchphrase>
```
````

- `id` and `context` on opening fence line are required.
- Section names: free-form, source-derived. Dotted-notation for hierarchy.
- Claims: indented values. No `claim:` prefix. Deeper indent = sub-claim.
- `[confidence]` only when source expresses uncertainty.
- `[src]` only when source has explicit reference.
- `[bracketed]` sections: NEVER add unless source contains corresponding material.
- sourceClaims = ONLY propositions present in or directly recoverable from the source. Interpretation, strategy analysis, method-step labels, cross-episode generalization, and conclusions the source does not state → `[bracketed]`. Litmus: "asserted by source, or inferred by renderer?" Inferred → bracket it.
- `[aggregation]`: all-or-nothing. If present → all 5 invariants + fields present.
- `[reasoning]`: ≥3 hypotheses, ≥2 tested. Never 1 hypothesis. Never delete falsified.
- `[evidence]`: SCR: `scr://domain/id`. ED formula. valid_until null = perpetual.

| Source type | Typical sections | Typical bracketed |
|---|---|---|
| Diagnostic | RootCause, Trigger, Path, Fix | [reasoning] + [evidence] |
| ADR | Decision, Context, Rationale, Tradeoffs | [assurance] + [evidence] |
| Review | Issue, Current, Problem, Fix | none |
| Status | Progress, Done, InProgress, Blocked | none |
| Composition | parts | [aggregation] |
| Trust claim | claim | [assurance] |
| Explanation/body | source-derived | none |
| Narrative source | source-derived sections | [style] |

`[style]` rules:
- Optional. Fill when reconstruction must reproduce a recognizable source form (narrative, tale, legal, marketing).
- `genre` + `register` required if `[style]` present; `voice`, `devices`, `signature` optional.
- `[style]` is fpfMetadata: its content does NOT emit as prose claims.
- **Exception:** reconstruction reads `[style]` as form instruction (genre/register/voice/devices, signature verbatim). All other `[bracketed]` omitted.
- `signature`: optional within optional `[style]`. Fill only when a load-bearing recurring signature exists (refrain, catchphrase); otherwise omit.

## FORMATTING RULES

**Markers**

| Marker | Meaning | Required when |
|---|---|---|
| `[confidence: high/medium/low]` | Claim certainty | Uncertain claim |
| `[pending]` | Unverified | Unverified claim |
| `[src: scr-ref]` | Source reference | Source-backed claim |
| `→` | Causality/sequence | Trigger chain |
| `@` | Time window | Work record |
| `#` | RoleAssignment | Action performer |
| `Tᴰ` / `Tᴿ` | Design-time / Run-time | Method vs Work separation |

**Prohibitions**

| # | NEVER | Wrong | Correct |
|---|---|---|---|
| 1 | Preambles | "I've reviewed your code…" | Start with ````episteme id="..." context="..."```` fence |
| 2 | Pleasantries | "Hope this helps!" | End at last slot value |
| 3 | Unmarked uncertainty | "probably a race condition" | `[confidence: medium]` |
| 4 | Mixed Tᴰ/Tᴿ | "MethodDescription executed at 3pm" | Tᴰ and Tᴿ in separate slots |
| 5 | Episteme actions | "The spec decided to require X" | `System#Role:Ctx` updated carrier |
| 6 | Role in partOf | `parts: [Cell, MonitorRole]` | RoleAssignment only |
| 7 | Prose-in-slots | `Problem: "service is down…"` | Typed sub-slots |
| 8 | Non-English output | Slot values in Russian, etc. | English; exceptions: proper names, wordplay, domain terms, quoted material |

**Mandatory per claim type**

| Claim type | Must include |
|---|---|
| Uncertainty | `[confidence: high/medium/low]` |
| Source-backed | `[src: scr-ref]` |
| Trust/reliability | F, G, R, CL tuple |
| Aggregation | Γ flavor + Quintet invariants |
| Evidence | SCR reference |
| Action/execution | `System#Role:Context` + Method or Work |

## HYBRID MODE

- FPF block self-contained (parsable without plain text).
- Plain text must not contradict or broaden FPF block.
- Separate blocks with clear division.

## RECONSTRUCTION CONSTRAINTS

Take ONLY source claims. Omit all `[bracketed]` content.

**NEVER include in reconstructed prose:**

| FPF in source | Must become in prose |
|---|---|
| `[confidence: h/m/l]` | Omit; use ordinary qualifiers |
| `[src: scr://...]` | Omit |
| `[pending]` | Omit |
| `U.*` prefixes | Plain words, no `U.` |
| `Tᴰ` / `Tᴿ` | Omit or use ordinary equivalents |
| `Γ_*` | Never appear |
| `ComponentOf`, `ConstituentOf`, `PortionOf`, `PhaseOf` | "part of", "belongs to", or restructure |
| `PhaseOf` | "during", "at time", or restructure sentence |
| `PortionOf` | "part of", "amount of" |
| `[aggregation]`, `[assurance]`, `[reasoning]`, `[evidence]` content | Omit entirely |

Section names of the Episteme are **scaffolding, not prose headings.** Do NOT emit them as titles/labels in the reconstruction.

Reconstruction MUST be connected narrative in the **genre and voice of the source** (a tale reads as a tale, a diagnostic as a diagnostic), not a labelled dump of sections.

Pattern-compressed repetition (`pattern: X → Y → Z`, `each encounter extends … by one`) MUST be **re-expanded into concrete instances** in the reconstruction, matching the source's own unfolding.

| FPF in source | Reconstruction must |
|---|---|
| `Setup:` / `Encounters:` section labels | Dissolve into narrative flow; no heading |
| `pattern: Predator threatens → sings → rolls away` | Re-expand each encounter as its own passage |
| `each encounter extends escaped-from list by one` | Actually list the growing sequence per encounter |

Result: connected prose in the source's genre — section labels dissolved, repetition re-expanded, no brackets, no reference tokens, no FPF vocabulary.

If `[style]` is present, the reconstruction MUST adopt its genre, register, voice, and devices, and reproduce any `signature` verbatim. `[style]` is read as a form instruction; its lines never appear as labelled claims. All other `[bracketed]` sections remain omitted.

## REFLEXIVE SPLIT

Rule: holder(Agent) ≠ Target. No self-magic. Self-action → split System into Regulator and Regulated:

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

## EXAMPLES

### Diagnostic (~80 tokens, 68% savings vs F0)

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
  H₁ → unauth reqs counted against RL
  H₁ → RL exhaustion blocks legit users
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

### ADR (~100 tokens, 67% savings vs F0)

````
```episteme id="PrimaryDB" context="DataLayer"
Decision:
 PostgreSQL v16 as primary OLTP store
Context:
 NewPlatform#DataLayer:StorageCtx
Rationale:
 team: existing PostgreSQL operational knowledge; no MongoDB/CockroachDB ops experience
 system: PostgreSQL handles projected load with ≥3x headroom
 failure: PostgreSQL proven reliability vs MongoDB unknown failure modes for team
Tradeoffs:
 +cost: higher than managed NoSQL; acceptable within budget
 +overhead: ORM layer required; acceptable for team productivity

[assurance]:
 F_eff = F2 (structured plan, not yet deployed)
 G_eff = OLTP workload; analytical queries out of scope
 R_eff = max(0, 0.85 − Φ(CL1))
 CL_min = CL1 (plausible; pending load test validation)
 Cutset: load projection validation gap

[evidence]:
 validatedBy: [load-projection-model, src: scr://plan/capacity-2025-07]
 validatedBy: [team-survey, src: scr://hr/skills-matrix-2025]
 valid_until: 2026-01-01
 ED: 0
```
````

### Status (~55 tokens, 61% savings vs F0)

````
```episteme id="AuthModule" context="ProjectTracking"
Progress: 72%
Done:
 Registration
 Login
InProgress:
 PasswordReset (ETA: 2026-07-08)
Blocked:
 TwoFactorAuth
 Issue: SMS provider contract pending
 RootCause: legal review not complete
 Fix: awaiting signature [pending]
Overall:
 on-track, ETA: 2026-07-15
 Risk: if SMS contract unsigned by Jul 9 → descope 2FA from release
```
````

## SELF-CHECK

Answer all. If any answer is NO, repair.

| # | Check | Must be YES |
|---|---|---|
| 1 | Formality selected from decision table? | YES |
| 2 | At least one section with ≥1 indented claim? | YES |
| 3 | `[confidence]` only when source has uncertainty? | YES |
| 4 | `[src]` only when source has explicit reference? | YES |
| 5 | Zero preambles, zero pleasantries, zero `claim:` prefix? | YES |
| 6 | No Episteme acting — all action verbs on System#Role:Context? | YES |
| 7 | No Role in parts/composition lists? | YES |
| 8 | No MethodDescription in Tᴿ slots; no Work in Tᴰ slots? | YES |
| 9 | No fabricated `[bracketed]` sections (check each against source)? | YES |
| 10 | `[aggregation]` present → all 5 Quintet invariants + fields filled? | YES |
| 11 | `[aggregation]` present → Γ flavor named, cutset named, CL_min justified, Φ(CL) applied? | YES |
| 12 | `[reasoning]` present → ≥3 hypotheses, ≥2 tested ✓/✗, falsified visible, conclusion explicit? | YES |
| 13 | `[evidence]` present → ≥1 verifiedBy/validatedBy/pending, valid_until explicit, ED calculated? | YES |
| 14 | All claim values in English? (exceptions: proper names, wordplay, domain terms, quoted material) | YES |
| 15 | Reconstruction: no `[bracketed]` content, no FPF markers/notation in prose? | YES |
| 16 | EntityOfConcernSlot filled — what is being described? (topic, system, event) | YES |
| 17 | ClaimGraphSlot filled — at least one section with ≥1 indented claim? | YES (same as #2) |
| 18 | ViewpointSlot implied — consumer type from decision table? | YES |
| 19 | `[bracketed]` sections present only when source justifies them? | YES |
| 20 | Every non-bracketed claim is source-asserted, not renderer-inferred? (interpretation → `[bracketed]`) | YES |
| 21 | If source has a recognizable form to preserve → `[style]` present (with genre + register)? | YES |
| 22 | Reconstruction conforms to `[style]` (genre/register/voice/devices, signature verbatim if present)? | YES |

## REFERENCE

### U.-Prefix

| Type | Meaning | Acts? |
|---|---|---|
| `U.Entity` | Anything individuable and referable | NO |
| `U.Holon` | Whole-with-parts; part of larger wholes | NO |
| `U.System` | Acting physical/operational holon; bears roles, executes Work | YES |
| `U.Episteme` | Knowledge holon (spec, proof, model, narrative output) | NO |
| `U.Role` | Context-bound work-facing role value (mask) | NO |
| `U.RoleAssignment` | Holder#Role:Context binding | NO |
| `U.Capability` | System ability/envelope to enact a Method under conditions | NO |
| `U.Method` | Abstract order-sensitive way-of-doing (Tᴰ) | NO |
| `U.MethodDescription` | Description episteme of a Method (Tᴰ, recipe/SOP) | NO |
| `U.Work` | Dated execution (Tᴿ, IMMUTABLE) | NO |
| `U.Transformation` | Bounded change of a holon under conditions (Tᴿ) | NO |
| `U.BoundedContext` | Context where terms have meaning | NO |
| `U.ClaimGraph` | Claim body of an Episteme (nodes=claims, edges=relations) | NO |
| `U.ReferenceScheme` | How claims are read as statements about EntityOfConcern | NO |

### Boundary Relations (relations, NOT U.-types)

| Relation | Use for |
|---|---|
| `HolonDelimitationRelation` | Delimitation between holon and its environment |
| `HolonBoundaryCrossingRelation` | Relation crossing the delimitation (signal, control, flow) |

### Γ Flavors

| Γ | Domain | Relaxed |
|---|---|---|
| `Γ_sys` | Physical/cyber-physical | — |
| `Γ_epist` | Knowledge, meta-analysis | — |
| `Γ_ctx` | Order-sensitive processes | COMM, LOC |
| `Γ_time` | Time series, digital twins | COMM partial, LOC |
| `Γ_work` | Resources | — |
| `Γ_method` | Methods | — |

### Quintet Invariants

| Code | Meaning | Test |
|---|---|---|
| `IDEM` | Γ({h}) = h | One part = itself? |
| `COMM` | Γ({a,b}) = Γ({b,a}) | Order of independent parts irrelevant? |
| `LOC` | Worker-agnostic | Where fold executes irrelevant? |
| `WLNK` | R_eff = min(R_i) | Whole ≤ weakest part? |
| `MONO` | ↑R_i → ↑R_eff | Improving part never hurts? |

### F-G-R-CL

| Char | Scale | Meaning |
|---|---|---|
| `F` (Formality) | F0-F9 | F0=unstructured, F4=predicates/invariants, F5=executable math |
| `G` (ClaimScope) | Coverage | Supported only; unsupported dropped |
| `R` (Reliability) | [0,1] | Probability of truth |
| `CL` (Congruence) | CL0-CL3 | CL0=weak guess, CL1=plausible, CL2=validated, CL3=verified |

Formulas (mandatory):
```
F_eff = min(F_i)           G_eff = SpanUnion({G_i}) | support
R_raw = min(R_i)           R_eff = max(0, R_raw − Φ(CL_min))
```
Φ(CL): lower CL → larger penalty. Never skip.

### ADI Reasoning

| Phase | Action | Minimum |
|---|---|---|
| **A**bduction | Generate hypotheses | ≥3, recommend 5 |
| **D**eduction | Testable predictions | ≥1 per hypothesis |
| **I**nduction | Test against evidence | ≥2 hypotheses, ✓/✗ |
| Conclusion | Selected, rejected, R | "H₁ confirmed; H₃ falsified" |

Never 1 hypothesis. Never delete falsified (keep ✗). Never "probably" — use ✓/✗ and R.

### Evidence

| Anchor | Type | Use |
|---|---|---|
| `verifiedBy` | Formal | Static guarantees, model-checking |
| `validatedBy` | Empirical | Measurements, load tests, observations |

SCR: `scr://<domain>/<id>`. ED: `k × max(0, today − valid_until)`. valid_until null = perpetual (axioms/laws only). ED actions: Refresh / Deprecate / Waive.

### Strict Distinctions

| # | Violation | Scan for | Fix |
|---|---|---|---|
| 1 | Role = Function | Role + action verb | `System#Role:Ctx` executes Method |
| 2 | MethodDesc = Method = Work | Tᴿ slot has MethodDesc; Tᴰ slot has Work | Split with Tᴰ/Tᴿ |
| 3 | System = Episteme | Episteme noun + action verb | `System#Role:Ctx` → Work on Episteme carrier |
| 4 | Episteme = Carrier | "The document updated itself" | System → Work on carrier; Episteme = content |
| 5 | Collective = Set | MemberOf for acting group | ComponentOf for collective; MemberOf for sets |

**Rewrites**

| Wrong | Correct |
|---|---|
| "The spec decided to require X" | `DesignService#TransformerRole:SpecCtx` updated carrier → req X |
| "The process executed the rule" | `System#TransformerRole:Ctx` executed `Method`; `Work` → SCR |
| "Holon bearing TransformerRole" | `System bearing TransformerRole` |
| "parts: [Cell, MonitorRole]" | `parts: [Cell, …]`; `RoleAssignment: BMSSystem#MonitorRole:PackCtx` |
| "The report concluded that…" | `AnalystSystem#TransformerRole:Ctx` executed Method; conclusion ∈ U.Episteme(X) |

### Mereology

| Relation | For | Domain |
|---|---|---|
| `ComponentOf` | Structural part | U.System |
| `ConstituentOf` | Logical/content part | U.Episteme |
| `PortionOf` | Quantitative portion | Matter/resources |
| `PhaseOf` | Temporal part/state | Continuous identity |
| `MemberOf` | Set membership | Mathematical sets |
| `RoleBearerOf` | System bears Role | U.System ↔ U.Role |

Roles NEVER in parts lists. Holarchies = holons. Roles → RoleAssignment.
