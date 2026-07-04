---
name: fpf-narrative
description: |
  Generate compact, unambiguous FPF-structured output at F4-F5 formality level.
  Use when writing for AI agent consumers or FPF-literate humans where token
  economy and auditability matter: diagnostics, architecture decisions, code
  reviews, status reports, trust assessments, system compositions. Replaces
  verbose prose (F0) with typed-slot notation (~65% token savings, lossless).
  Do NOT use for: casual chat, teaching, non-technical audiences, creative tasks.
---

# FPF Narrative Prose — Runtime Instructions

## CONCEPTS (runtime ontology — apply these facts)

`U.System` acts. `U.Episteme` does NOT. `U.Work` = run-time (Tᴿ), immutable. `U.Method` / `U.MethodDescription` = design-time (Tᴰ). Tᴰ and Tᴿ never mix in one slot.

`U.Role` = mask; `U.RoleAssignment` = `System#Role:Context`. Roles NEVER in parts lists. Holarchies = substantive holons only.

Γ aggregation: weakest-link. `F_eff = min(F_i)`, `R_eff = max(0, min(R_i) − Φ(CL_min))`. All 5 Quintet invariants checked per Γ block.

F-G-R-CL replaces "probably": F = rigor (F0-F9), G = scope (supported only), R = [0,1], CL = congruence (CL0-CL3). Φ(CL): lower CL → larger penalty.

Evidence: `verifiedBy` (formal), `validatedBy` (empirical). SCR: `scr://<domain>/<id>`. ED: `k × max(0, today − valid_until)`. valid_until null = perpetual (axioms/laws only). ED actions: Refresh / Deprecate / Waive.

ADI: ≥3 hypotheses in Abduction. ≥1 prediction per hypothesis. ≥2 tested in Induction (✓/✗). Never 1 hypothesis. Never delete falsified.

5 strict distinctions: Role≠Function, MethodDesc≠Method≠Work, System≠Episteme, Episteme≠Carrier, Collective≠Set. Scan every output before emitting.

---

## FORMAT SELECTION

| Consumer | Task | Audit? | Formality |
|---|---|---|---|
| AI agent | Diagnostics, ADR, review, trust | Yes | F4-F5 |
| AI agent | Status, work log | Sometimes | F3-F4 |
| FPF-literate human | ADR, safety case | Yes | F4-F5 |
| FPF-literate human | Status, casual review | No | F3 hybrid |
| Non-technical human | Any | No | F0 plain |
| Mixed (agent + human) | Any | Yes | F4-F5 + 1-sentence plain |

Rules: Default F0. Upgrade only per table. Any downstream consumer in chain needs F4-F5 → entire chain renders F4-F5. Consumer unknown → F3 hybrid. Teaching → F0-F2.

---

## OUTPUT TEMPLATES

Pick one. Fill all slots. Do not invent new templates.

**Diag(issue)**
```
Diag(<issue-id>):
  RootCause: <cause> [confidence: high/medium/low]
  Trigger: <chain with →>
  Path: <execution path>
  Fix:
    - <action> [confidence: high/medium/low]
  Evidence:
    verifiedBy: [<proof-id>, src: <scr-ref>]
    validatedBy: [<test-id>, src: <scr-ref>]
    valid_until: <ISO-date | null>
    ED: <number>
  Reasoning:
    Abduction: H₁…H₅
    Deduction: H₁ → …
    Induction: test(H₁) → result
```

**ADR(topic)**
```
ADR(<topic>):
  Decision: <decision>
  Context: <U.BoundedContext>
  Rationale:
    Γ_team: <argument>
    Γ_sys: <argument>
    Γ_failure: <argument>
  Tradeoffs:
    +<cost>: <description>
    +<overhead>: <description>
  Assurance:
    F: <Fk>
    G: <scope>
    R: <[0,1]>
    CL: <CLk>
  Evidence:
    verifiedBy: [<proof-ids>]
    validatedBy: [<test-ids>]
```

**Review(target)**
```
Review(<target-id>):
  Issue: <name>
  Current: <state with →>
  Problem: <description>
  Fix: <fix>
  Rationale: <justification>
  Severity: critical/high/medium/low
  Evidence: [src: <id>]
```

**Status(project)**
```
Status(<project>):
  Progress: <N>%
  Done: [<items>]
  InProgress: <item> (ETA: <date>)
  Blocked: <item>
    Issue: <description>
    RootCause: <cause>
    Fix: <status>
  Overall: on-track/at-risk/off-track, ETA: <date>
  Work:
    - W₁: <desc> @ <time>, performedBy: <System#Role:Ctx>
```

**Assurance(Holon, Claim | Context, Scope)**
```
Assurance(<Holon>, Claim: <C> | Context: <K>, Scope: <S>):
  F_eff = min(F₁, F₂, …) = <value>
  G_eff = SpanUnion({G_i}) = <coverage>
  R_raw = min(R_i) = <value>
  R_eff = max(0, R_raw − Φ(CL_min)) = <value>
  CL_min = <CLk> (<edge description>)
  Cutset: <bottleneck path>
  SCR: [<carrier-ids>]
  ED: <value> (valid_until: <date>)
```

**Γ_sys(Name) / Γ_epist(Name) / … — system composition**
```
Γ_<flavor>(<Name>):
  parts: [<holon₁>, <holon₂>, …]
  graph: <acyclic; dependencies>
  aggregation:
    F_eff = min(F_i)
    R_raw = min(R_i) along <cutset>
    R_eff = max(0, R_raw − Φ(CL_min))
    G_eff = SpanUnion({G_i}) constrained by support
  invariants:
    IDEM: ✓/✗
    COMM: ✓/✗ (<reason if ✗>)
    LOC: ✓/✗
    WLNK: <enforced/cutset>
    MONO: <holds/conditional>
  SCR: [<carrier-ids>]
  emergence: none | MHT: <description>
```

**ReflexiveSplit(System)**
```
ReflexiveSplit(<System>):
  Regulator: <Sub₁>#TransformerRole:<InternalCtx>
  Regulated: <Sub₂>
  Boundary: <U.Boundary description>
  Interaction: <U.Interaction description>
  Method: <U.Method>
  MethodDescription: <U.MethodDescription> [src: scr://…]
  Work: <U.Work> @ <time>, resources: <Γ_work>
  Evidence:
    externalObserver: <System#ObserverRole:Ctx>
    verifiedBy: [<proof-ids>]
```

---

## FORMATTING RULES

Block structure:
```
<Type>(<target>):
  <Slot>: <value>
  <NestedSlot>:
    <SubSlot>: <value>
```

**Markers**

| Marker | Meaning | Required when |
|---|---|---|
| `[confidence: high/medium/low]` | Claim certainty | Uncertain claim |
| `[pending]` | Unverified | Unverified claim |
| `[src: <SCR-id>]` | Source reference | Source-backed claim |
| `→` | Causality/sequence | Trigger chain |
| `@` | Time window | Work record |
| `#` | RoleAssignment | Action performer |
| `Tᴰ` / `Tᴿ` | Design-time / Run-time | Method vs Work separation |

**Prohibitions**

| # | NEVER | Wrong | Correct |
|---|---|---|---|
| 1 | Preambles | "I've reviewed your code…" | Start with template |
| 2 | Pleasantries | "Hope this helps!" | End at last slot value |
| 3 | Unmarked uncertainty | "probably a race condition" | `[confidence: medium]` |
| 4 | Mixed Tᴰ/Tᴿ | "MethodDescription executed at 3pm" | Tᴰ and Tᴿ in separate slots |
| 5 | Episteme actions | "The spec decided to require X" | `System#Role:Ctx` updated carrier |
| 6 | Role in partOf | `parts: [Cell, MonitorRole]` | RoleAssignment only |
| 7 | Prose-in-slots | `Problem: "service is down…"` | Typed sub-slots |
| 8 | Slot invention | Non-canonical top-level slots | Sub-slots under canonical |
| 9 | Non-English output | Slot values in Russian, German, etc. | Translate to English UNLESS translation distorts meaning (proper names, wordplay, domain terms, quoted material — keep original) |

**Mandatory per claim type**

| Claim type | Must include |
|---|---|
| Uncertainty | `[confidence: high/medium/low]` |
| Source-backed | `[src: <SCR-id>]` |
| Trust/reliability | F, G, R, CL tuple |
| Aggregation | Γ flavor + Quintet invariants |
| Evidence | SCR reference |
| Action/execution | `System#Role:Context` + Method or Work |

---

## FPF BLOCK STRUCTURE

When emitting a Γ block, separate:

| Source claims | Computed metadata |
|---|---|
| `parts` entries | `graph` |
| Factual slot values | `aggregation` (F_eff, R_raw, R_eff, G_eff) |
| | `invariants` (IDEM, COMM, LOC, WLNK, MONO) |
| | `emergence` |
| | `Assurance(...)` block |

---

## RECONSTRUCTION CONSTRAINTS

When reconstructing prose from an FPF block:

**Take ONLY source claims.** Omit all computed metadata.

**NEVER include in reconstructed prose:**

Metadata values:
- F_eff, R_eff, R_raw, G_eff values
- Quintet invariants (IDEM, COMM, LOC, WLNK, MONO)
- Emergence descriptions (MHT, etc.)
- Assurance blocks
- Aggregation formulas
- Graph dependency descriptions
- Cutset names
- SCR references (computed or source — SCR is FPF-internal tracking)
- Evidence block content (valid_until, ED, verifiedBy, validatedBy)

FPF terminology — translate to domain language:
- `U.*` prefixes (U.MethodDescription, U.Work, U.Method) → plain words ("description", "work", "method")
- `Tᴰ` / `Tᴿ` markers → omit or use ordinary equivalents ("design", "execution")
- `[confidence: high/medium/low]` → omit; use ordinary qualifiers if needed ("likely", "confirmed")
- `[src: scr://...]` → omit entirely
- `[pending]` → omit; do NOT render as "unverified", "pending evidence" etc.
- `ComponentOf`, `ConstituentOf`, etc. → "part of", "belongs to", or restructure
- `Γ_epist`, `Γ_sys`, operator names → never appear

**Emit clean prose.** No service markers, no brackets, no reference tokens, no FPF vocabulary. Prose must be indistinguishable in form from fresh original source text.

---

## HYBRID MODE

When F3 hybrid:
- FPF block self-contained (parsable without plain text).
- Plain text must not contradict or broaden FPF block.
- Separate blocks with clear division.

---

## EXAMPLES

### Diagnostic

F0 (250 tokens):
> I've analyzed the authentication service crashes and found the root cause. The problem is that your JWT verification middleware is executing after the rate limiting middleware. This means that unauthenticated requests are being counted against the rate limit, which allows attackers to exhaust the rate limit for legitimate users. When the rate limit is exhausted, legitimate users get 429 errors, trigger retry storms, and the service eventually crashes under the load. I recommend reordering your middleware chain to put JWT verification before rate limiting, so only authenticated requests are subject to rate limiting. You should also add a null check before accessing user properties. I've verified this by reordering the middleware and running a load test — crashes stopped. The race condition hypothesis was disproved by the load test.

F4-F5 (80 tokens, 68% savings):
```
Diag(AuthService crashes):
  RootCause: JWTVerify executes after RateLimit [confidence: high]
  Trigger: unauth reqs → RL exhaustion → legit lockout → cascade fail
  Path: RateLimit → JWTVerify → null user → NPE → crash
  Fix:
    - reorder: JWTVerify → RateLimit [confidence: high]
    - add null-check before user.* [confidence: medium]
  Evidence:
    verifiedBy: [proof: middleware-order.sc, src: scr://proof/mw-042]
    validatedBy: [test: auth-load-2025-07, src: scr://test/alt-789]
    valid_until: 2026-01-01
    ED: 0
  Reasoning:
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
```

### ADR

F0 (300 tokens):
> We've decided to use PostgreSQL as our primary database for the new platform. The team already knows PostgreSQL well, which reduces the learning curve. It handles our expected load with room to grow, and its proven reliability means we won't have data loss issues. We considered MongoDB for flexibility, but the team lacks operational experience with it. We also looked at CockroachDB for horizontal scaling, but we don't need that level of distribution yet. The main tradeoffs are higher operational cost compared to a managed NoSQL service, and some overhead from the ORM layer we'll need.

F4-F5 (100 tokens, 67% savings):
```
ADR(PrimaryDB: PostgreSQL):
  Decision: PostgreSQL v16 as primary OLTP store
  Context: NewPlatform#DataLayer:StorageCtx
  Rationale:
    Γ_team: existing PostgreSQL operational knowledge; no MongoDB/CockroachDB ops experience
    Γ_sys: PostgreSQL handles projected load with ≥3x headroom
    Γ_failure: PostgreSQL proven reliability vs MongoDB unknown failure modes for team
  Tradeoffs:
    +cost: higher than managed NoSQL; acceptable within budget
    +overhead: ORM layer required; acceptable for team productivity
  Assurance:
    F: F2 (structured plan, not yet deployed)
    G: OLTP workload; analytical queries out of scope
    R: 0.85 (team experience strong; load projection not yet validated)
    CL: CL1 (plausible; pending load test validation)
  Evidence:
    validatedBy: [load-projection-model, src: scr://plan/capacity-2025-07]
    validatedBy: [team-survey, src: scr://hr/skills-matrix-2025]
    valid_until: 2026-01-01
```

### Status

F0 (140 tokens):
> We're at about 72% completion on the AuthModule. Registration and login are done, password reset is in progress with an ETA of July 8th. Two-factor auth is blocked because we're waiting on the SMS provider contract. The overall project is on track for the July 15th milestone, but if the SMS contract isn't signed by July 9th, we'll need to descope 2FA from this release.

F4-F5 (55 tokens, 61% savings):
```
Status(AuthModule):
  Progress: 72%
  Done: [Registration, Login]
  InProgress: PasswordReset (ETA: 2026-07-08)
  Blocked: TwoFactorAuth
    Issue: SMS provider contract pending
    RootCause: legal review not complete
    Fix: awaiting signature [pending]
  Overall: on-track, ETA: 2026-07-15
    Risk: if SMS contract unsigned by Jul 9 → descope 2FA from release
```

---

## SELF-CHECK

Answer all. If any answer is NO, repair.

| # | Check | Must be YES |
|---|---|---|
| 1 | Formality from decision table (not default)? | YES |
| 2 | All required template slots filled? | YES |
| 3 | Every slot value typed (U.-type, [confidence], [src], or typed sub-slot)? | YES |
| 4 | All uncertain claims marked [confidence] or [pending]? | YES |
| 5 | Zero prose sentences as slot values? | YES |
| 6 | Zero preambles, zero pleasantries? | YES |
| 7 | All action verbs on System#Role:Context (no Episteme acting)? | YES |
| 8 | Evidence block has ≥1 verifiedBy / validatedBy / [pending]? | YES |
| 9 | (Diag/ADR) ADI block has ≥3 hypotheses in Abduction? | YES |
| 10 | (Diag/ADR) ≥2 hypotheses tested in Induction (✓/✗)? | YES |
| 11 | (Γ blocks) All 5 Quintet invariants checked (✓/✗)? | YES |
| 12 | (Γ blocks) Cutset explicitly named (not "min")? | YES |
| 13 | All slot values in English? (exceptions: proper names, quoted material) | YES |
| 14 | (Γ block) parts = source claims, rest = computed metadata? | YES |
| 15 | (Reconstruction) No FPF metadata (R_eff, F_eff, invariants, emergence, Assurance, Evidence) in prose? | YES |
| 16 | (Reconstruction) No U.* prefixes, Tᴰ/Tᴿ markers, [confidence], [src], [pending] in prose? | YES |
| 17 | (Reconstruction) No Γ operator names or mereological terms (ComponentOf, etc.) in prose? | YES |
| 18 | (Reconstruction) Prose clean — no FPF vocabulary, indistinguishable from fresh text? | YES |

---

## REFERENCE

### U.-Prefix

| Type | Meaning | Acts? |
|---|---|---|
| `U.Entity` | Anything distinguishable | — |
| `U.Holon` | Whole AND part; has U.Boundary | — |
| `U.System` | Physical/operational holon | **YES** |
| `U.Episteme` | Knowledge (spec, proof, model) | **NO** |
| `U.Boundary` | Holon boundary (open/closed/permeable) | — |
| `U.Interaction` | Flow across boundary | — |
| `U.Role` | Capability/obligation mask | — |
| `U.RoleAssignment` | Holder#Role:Context binding | — |
| `U.BoundedContext` | Context where terms have meaning | — |
| `U.MethodDescription` | Recipe (Tᴰ) | — |
| `U.Method` | Capability to execute (Tᴰ) | — |
| `U.Work` | Dated execution (Tᴿ, IMMUTABLE) | — |

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
| `F` (Formality) | F0-F5 | F0=unstructured, F1=stable terms, F2=structured outline, F3=controlled narrative, F4=predicates/invariants, F5=executable math |
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
| Conclusion | Selected, rejected, confidence | "H₁ confirmed; H₃ falsified" |

Rules: Never 1 hypothesis. Never delete falsified (keep ✗). Never "probably" — use ✓/✗ and R.

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

Rule: Roles NEVER in parts lists. Holarchies = holons. Roles → RoleAssignment.
