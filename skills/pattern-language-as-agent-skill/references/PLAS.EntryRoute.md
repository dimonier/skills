---
id: PLAS.EntryRoute
title: "Deciding whether and what to author as a DPF-skill"
status: seed
keywords: [entry, cold-reader, outcomes, framework-scale, seed]
dependencies:
  builds_on:
    - E.4.DPF
    - E.4.PFAD
    - E.9
  coordinates_with:
    - E.4.DPF.DA
    - C.33
  specialized_by:
    - PLAS.SelfSufficient
    - PLAS.SkillLayout
---

## PLAS.EntryRoute - Deciding whether and what to author as a DPF-skill

> **Trigger:** Before writing the first pattern body — when the question is whether a new or revised DPF/LPF-as-skill is the right outcome at all.
> **Governing FPF patterns:**
>   → E.4.DPF
>   → E.4.PFAD
>   → E.9
>   → E.4.DPF.DA

---

### PLAS.EntryRoute:1 - Problem frame

Use this pattern at the start of DPF-skill authoring: run the `E.4.DPF` cold-reader
route, then fix one of its five outcomes, and only proceed to skill authoring when
the outcome is "new or revised framework". After outcome (a) is fixed, settle two
authoring-scenario axes before drafting any body: the FPF-dependency scope
(`FPF-grounded` vs `self-sufficient`) and the source-of-truth
(`language-from-scratch` vs `representation-of-external-standard`).

### PLAS.EntryRoute:2 - Problem

Teams rush a checklist or a source summary into a "skill" without deciding whether
a framework is the right result at all. They skip the cold-reader subtraction,
publish a singleton pattern under a broad name, author a skill before settling the
framework-scale question, or fix no authoring scenario (FPF-dependency scope and
source-of-truth), so governing cues, status semantics, and source pinning drift.
The result is a seed pretending to be a framework, or a projection that cannot
state where its truth lives.

### PLAS.EntryRoute:3 - Forces

| Force | Settlement |
|---|---|
| Urgency vs right outcome | Cheap routes (direct source use, an existing DPF, a guide) close first; a framework is only one of five outcomes. |
| Singleton vs language | `pattern_count = 1` is a strong diagnostic; the same semantic scale test runs at every count (`E.4.DPF:4.0`). |
| Authoring vs decision record | The `E.4.PFAD` answer is process state; it does not live in `SKILL.md`. |

### PLAS.EntryRoute:4 - Solution

1. **Cold-reader route** (`E.4.DPF:4` steps 1–9): name reader, useful move, what
   FPF + existing DPFs + sources already provide, then test a cheaper route or
   stop.
2. **Select one of five outcomes** via `E.4.PFAD` and record it in an `E.9` DRR
   when a later-used boundary is open: (a) new/revised framework, (b) contribution
   to an existing framework, (c) non-framework product, (d) thinner publication or
   access route, (e) no new product.
3. **Only (a) proceeds to skill authoring.** For (b)–(e), do not create a
   DPF-skill; the cheapest route or stop needs no seed package.
4. **Select the authoring scenario** — two orthogonal axes, fixed before drafting:
   - **FPF-dependency scope:** `FPF-grounded` (the normal case: governing-pattern
     cues to FPF + a dependency on FPF Core) vs `self-sufficient` (no FPF
     dependency; route to `PLAS.SelfSufficient`, which owns the boundary statement,
     the inlined section semantics, and the local readiness modes).
   - **Source of truth:** `language-from-scratch` (the DPF opens a language;
     single-surface as in `PLAS.SkillLayout`) vs `representation-of-external-standard`
     (an already-published external document is canonical and the skill is a derived
     projection; pin the source and refresh on its edition — see `PLAS.SkillLayout`).
5. **Run the framework-scale test** (`E.4.DPF:4.0`): coverage map, selected
   problem-family sets + material relations, a representative application, an
   internally usable first-edition set, honest omissions, a maintenance boundary.
   A singleton is a seed or contribution, not an edition.
6. **Keep the decision record out of the skill.** The DRR, the `E.4.PFAD` answer,
   and the coverage rationale are maintainer evidence (`E.4.DPF:4` step 11); `SKILL.md`
   exposes only the declared field, first use, and pattern index.

### PLAS.EntryRoute:5 - Archetypal Grounding

**Tell.** A "Health" domain produces one useful pattern. The cold-reader shows FPF
plus an existing Health DPF already answer most of it; the single pattern becomes a
contribution, not a new DPF-skill. No `SKILL.md` is created.

### PLAS.EntryRoute:6 - Bias-Annotation

The author of a framework is also its proposer, so outcome (a) "new framework" is
easily over-favoured when a cheaper route would serve. The five-outcome test is
easy to run as a formality; the honest signal is a documented subtraction that
actually closes contributions, not a box ticked on the way to authoring.

### PLAS.EntryRoute:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-ER.1 | Cold-reader route was run before any pattern body was drafted. |
| CC-ER.2 | One of the five `E.4.PFAD` outcomes is explicit; only "new/revised framework" proceeds. |
| CC-ER.3 | Framework-scale test was applied; `pattern_count = 1` is reported as a diagnostic. |
| CC-ER.4 | The DRR / PFAD answer is process state outside the skill. |
| CC-ER.5 | The FPF-dependency scope is explicit (`FPF-grounded` vs `self-sufficient`); self-sufficient routes to `PLAS.SelfSufficient`. |
| CC-ER.6 | The source-of-truth scenario is explicit (`language-from-scratch` vs `representation-of-external-standard`); the latter pins the source and refreshes on its edition. |

### PLAS.EntryRoute:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| Checklist promoted to a skill | Keep it a checklist until the scale test and `E.8` bodies pass. |
| Singleton published as a framework | Report it as a seed/contribution. |
| Decision record inside SKILL.md | Keep DRR/PFAD as maintainer evidence outside the skill. |

### PLAS.EntryRoute:9 - Consequences

Running the route before authoring spends effort up front but prevents a seed from
being published as a framework and a singleton under a broad name. Selecting a
non-framework outcome (b–e) avoids authoring entirely; selecting (a) commits the
author to the framework-scale test and a DRR before any body is drafted.

### PLAS.EntryRoute:10 - Rationale

The route is ordered so the cheapest exits close first: a framework is only one of
five outcomes, so the default is subtraction, not authoring. The DRR is kept out of
the skill because decision state is maintainer evidence, not pattern content
(`E.4.DPF:4` step 11).

### PLAS.EntryRoute:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| FPF `E.4.DPF:4` cold-reader route | Adopt | Five outcomes and the "singleton = seed, not edition" test gate the skill-carrier entry | Reopen on FPF `E.4.DPF` revision |
| FPF `E.4.PFAD` outcome selection | Adopt | The decision record stays outside `SKILL.md` (maintainer evidence) | Reopen on `E.4.PFAD` revision |
| `create-agent-skill` "When to (not) create a skill" | Adapt | Its triggers narrow to "is a DPF/LPF-as-skill the right outcome"; "no skill for a one-off" maps to "no DPF for a one-off" | Reopen when the skill-trigger guidance changes |

Best-known line: FPF's cold-reader route. Rejected rival: "author a monolith first, derive the
skill later" (fork/drift) — dropped in favor of the single-surface decision.

### PLAS.EntryRoute:12 - Relations

- **Builds on (FPF):** `E.4.DPF` (cold-reader + first-hour route), `E.4.PFAD` (outcome selection), `E.9` (decision record).
- **Coordinates with (FPF):** `E.4.DPF.DA` (package adequacy once authoring begins), `C.33` (carrier classification).
- **Specialized by (LPF):** `PLAS.SelfSufficient` (self-sufficient variant), `PLAS.SkillLayout` (carrier/edition layout).

### PLAS.EntryRoute:End
