---
id: PLAS.QualityAndRefresh
title: "Evaluating, improving, and refreshing a DPF-skill"
status: stable
keywords: [quality, evaluation, improvement, refresh, currentness, weak-model, wording-pass]
dependencies:
  builds_on:
    - E.4.DPF.DA
    - E.21
    - E.23
    - G.11
  coordinates_with:
    - E.22
    - E.19
    - E.4.PFR
    - F.18
    - F.19
---

## PLAS.QualityAndRefresh - Evaluating, improving, and refreshing a DPF-skill

> **Trigger:** After a DPF-skill seed exists — before relying on it, and again whenever sources, FPF, or local use change.
> **Skill dependencies:**
>   → create-agent-skill (weak-model gate)

---

### PLAS.QualityAndRefresh:1 - Problem frame

Use this pattern to decide when a DPF-skill is good enough to rely on, how to
improve it, and what reopens it — applied to the skill form directly, without a
publication form to check.

### PLAS.QualityAndRefresh:2 - Problem

A seed is useful but not yet trustworthy. Teams either ship it ("works in the
demo") or improve it without evaluation characteristics ("change the wording until
it looks better"). Without package adequacy (`E.4.DPF.DA`), pattern quality
(`E.21`), an improvement loop (`E.23`), and refresh triggers (`G.11`), the skill
silently goes stale. A YAML-unsafe `description` can break loading entirely, and
the loop has no syntactic check to catch it. The generated relation map
(`relations.md`) can also drift from the authored frontmatter graph, because nothing
compares them mechanically.

### PLAS.QualityAndRefresh:3 - Forces

| Force | Settlement |
|---|---|
| Package vs pattern | `E.4.DPF.DA` evaluates the package; `E.21` evaluates each body. |
| Reviewer vs author | A separate reviewer improves; "you can't check yourself" (`E.23`). |
| Publication checks vs skill | The `PFM1`–`PFM12` sub-pass (`E.11.PFP`, `CC-DPF.8/18`) is N/A — there is no reader-facing publication form; the D1–D12 coordinates stay mandatory. |

### PLAS.QualityAndRefresh:4 - Solution

1. **Frame the purpose** with `E.22` when it is not already scoped.
2. **Package adequacy** with `E.4.DPF.DA`: judge every D1–D12 coordinate (they are
   semantic and carrier-neutral — D2 names "skill entries", D9 covers
   edition/currentness, D10 is the improvement/refresh loop this card owns). Run the
   `PFM1`–`PFM12` sub-pass separately and mark its reader-facing publication-form
   checks N/A; do not drop a D-coordinate.
3. **Pattern quality** with `E.21`; mark bodies `seed` until they pass (what promotes a
   body is `CC-QR.2`). Read the findings of FPF `F.19` (ontology-first plain technical
   rewriting) into the `E.21` `PrecisionRestorationProfile` (`F.19:12`): before relying on
   the skill, every hand-authored body **and** `SKILL.md` is read once, in one continuous
   pass, as ordinary technical prose (wording-pass). The normal outcome is corrected text
   or a named blocker with an unresolved meaning — "read it, nothing found" is not an
   outcome. Structural checks cannot see a flipped source meaning, so prose is checked by
   reading, not by layout. Keep the before/after comparison of disputed or high-risk
   passages **outside** the carrier (project vault, git history), never as card content
   (`PLAS.SkillLayout:4` item 7).
4. **Machine frontmatter check (cheap, before any "rely on").** Parse every card's
   YAML frontmatter — and the `SKILL.md` `description` — and fail on any parse error
   before relying on the skill. A `description` with a bare `:` + space breaks the
   whole frontmatter (`ScannerError`); the check catches it mechanically, not by eye.
   The check is **parametrized by carrier** (a documented contract, not a shipped PLAS
   script): the `id`-prefix/template and the **valid status set** are arguments — an
   FPF-grounded carrier checks `seed`/`stable`; a self-sufficient carrier checks
   `source-faithful`/`case-validated`; a compacted projection expects **no card
   frontmatter** (identity = filename stem + body H1). The check also validates
   `SKILL.md` `description` YAML-safety, `INDEX.md ↔ references/` consistency, and
   rejects a `readiness:` key or a body cue block. `CC-QR.6` names this contract so the
   check is executable uniformly for every carrier form; a carrier may host its own
   implementation (e.g. `project-vault/scripts/check_frontmatter.py`), but the contract —
   not the file location — is normative.
5. **Graph check (cheap, alongside item 4).** The dependency graph has one authored
   home — frontmatter `dependencies` (`PLAS.GoverningCues:4`). Run
   `python scripts/build_relations.py --check`: it fails if the generated
   `relations.md` drifts from the frontmatter, and it warns when a local card is
   referenced child-side only. Verify that every card's `:12 Relations` is a one-line
   pointer (no repeated edges), that no card body carries a `Governing FPF patterns`
   cue block, and that no `governs`/`applies-to`/`*all cards*` pseudo-edge appears
   (relation functions come only from `E.4.PFR:3.3`). For a **self-sufficient**
   carrier, also grep `references/` + `SKILL.md` for authoring-infrastructure leaks —
   `DEC-|TRK-|WRK-|Q-|CON-|RISK-`, `инбокс|inbox|outbox`, `project-vault/` — and fail
   on a hit (bare source filenames allowed; `PLAS.SelfSufficient` `CC-SS.6`). Regenerate
   with `python scripts/build_relations.py` after any frontmatter change
   (`E.4.PFR:3.2`: derived views cite one assertion and are never maintained
   independently). The carrier must ship the **canonical** script contract
   (`PLAS.SkillLayout:4` item 10): regenerate + `--check`, non-zero on drift,
   `BEGIN`/`END` markers, no card edits. A copied/truncated variant that ignores
   arguments and always rewrites defeats the check; when the Specialization graph is
   empty, `--check` accepts the explicit stub line, not an empty graph.
6. **Improve** with `E.23` in a loop, with a separate reviewer and a target level.
7. **Weak-model gate** (`create-agent-skill`): a weaker model must follow every
   step without inventing steps or asking for clarification.
8. **Refresh** with `G.11`: reopen on source change, FPF edition change, local
   misuse telemetry, or supersession. When the refresh is driven by a **new normative
   source** (an added directive, an amended standard), transfer its requirements before
   editing any body: (a) place each requirement in the one existing pattern whose problem
   and scope cover it — if no pattern covers it, author a new pattern instead of a rule
   inside somebody else's card, and express any intended delegation in the carrier's graph
   vocabulary (FPF codes in `builds_on`/`coordinates_with`, local specialization child-side
   `specializes`), never as an invented edge or a dangling "see …" pointer; (b) reproduce
   the source's wording literally ("debug logs" stays "debug logs", not `TRACE`/`DEBUG`) —
   extending it takes an explicit owner decision; (c) name new terms by the card's local
   convention (`actor_id`, not the source's verbatim `act_sub`) and record the divergence
   in `:11 SoTA-Echoing`.
9. **Owner-performed sync.** A repo-carrier change is materialized into the
   installed copy only by an **owner-performed sync** — the authoring agent
   refreshes the bodies in the repo, never the deployed projection.

### PLAS.QualityAndRefresh:5 - Archetypal Grounding

**Show.** `pattern-language-as-agent-skill` ran this loop on itself: `E.4.DPF.DA` D1–D12,
a per-coordinate `E.21` pass over every body, four heterogeneous applications, and
repeated feedback-driven repairs; five bodies now carry `stable`, the rest stay `seed`
with the reason named in `SKILL.md`. Before reliance, run the same loop, the weak-model
gate, and the wording-pass.

### PLAS.QualityAndRefresh:6 - Bias-Annotation

"Works in the demo" is the classic adequacy illusion: a seed that succeeds on one
prompt is mistaken for a reliable framework. The author also cannot reliably
self-review ("you can't check yourself", `E.23`). Publication-form checks are easy
to silently drop rather than mark N/A, which hides the carrier-specific gap.

### PLAS.QualityAndRefresh:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-QR.1 | Package adequacy is evaluated with all `E.4.DPF.DA` D1–D12 coordinates, not assumed from a build. |
| CC-QR.2 | Each body has an `E.21` result or an explicit `seed` mark. A body moves `seed` → `stable` only when it has **both** a per-coordinate `E.21` result **and** at least two distinct feedback-driven repairs in the trailing month (each repair traceable to a real downstream application, not to authoring churn); repairs made inside the current quality cycle do not count until a downstream application exercises them. A `seed` left in place names its reason. |
| CC-QR.3 | Improvement uses a separate reviewer and a target level (`E.23`). |
| CC-QR.4 | Refresh triggers are named (`G.11`). |
| CC-QR.5 | Publication-form checks are explicitly N/A, not silently dropped. |
| CC-QR.6 | A machine frontmatter-parse check (incl. `description` YAML-safety) passes before reliance — parametrized by carrier: id-prefix/template + valid status set (`seed`/`stable`, or `source-faithful`/`case-validated`, or no-frontmatter for a compacted projection), plus `INDEX.md ↔ references/` consistency and no `readiness:` key / body cue block. |
| CC-QR.7 | The dependency graph has one authored home (frontmatter); `:12` is a pointer; no card body repeats a `Governing FPF patterns` cue block; `scripts/build_relations.py --check` passes (generated `relations.md` matches the frontmatter; an empty Specialization graph yields the explicit stub line matching FPF-edge presence (with FPF edges vs self-sufficient/none), not an empty graph); the carrier ships the canonical script contract (regenerate + `--check`, non-zero on drift, markers, no card edits); no `governs`/`applies-to` pseudo-edges. |
| CC-QR.8 | Before reliance, every hand-authored body and `SKILL.md` passed one continuous prose read (wording-pass, item 3), with FPF `F.19` findings taken into the `E.21` `PrecisionRestorationProfile`; the recorded outcome is corrected text or a named blocker, and the before/after comparison for disputed passages lives outside the carrier. |
| CC-QR.9 | A source-change refresh transferred requirements by all three rules of item 8: one covering pattern (or a newly authored pattern, with any delegation expressed in the carrier's graph vocabulary), literal source wording unless extended by an explicit owner decision, local naming convention with the divergence recorded in `:11 SoTA-Echoing`. |

### PLAS.QualityAndRefresh:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| "Works in the demo" = adequate | Run `E.4.DPF.DA` + `E.21` before reliance. |
| Improvement without characteristics | Frame with `E.22`; pick a measured aspect. |
| Publication-form checks forced on a skill | Mark them N/A; there is no reader form. |
| Frontmatter never machine-parsed | Run a cheap YAML/parse check before reliance. |
| A frontmatter checker hardened to one carrier (e.g. `PV.`-prefix, `seed`/`stable`) applied to another (self-sufficient) | Parametrize by carrier (id-prefix/template + status set); see `CC-QR.6`. |
| Graph views drift (direction flip between frontmatter / `:12` / `relations.md`) | Frontmatter is the single home; regenerate `relations.md` with `build_relations.py`; keep `:12` a pointer. |
| `--check` never fails (a truncated script copy is shipped) | Ship the canonical contract (regenerate + `--check`, non-zero on drift); verify it fails on a deliberate drift. |
| A new source requirement dropped into a neighbouring card | Find the one pattern whose problem covers it; otherwise author a new pattern. Express delegation in the carrier's graph vocabulary, not a dangling "see …" reference. |
| Source wording extended while transferring ("debug logs" → `TRACE`/`DEBUG`) | Reproduce the source literally; extend only on an explicit owner decision (item 8, `CC-QR.9`). |
| The source's verbatim term adopted as the local name (`act_sub` beside `user_id`) | Name by the card's local convention; record the divergence in `:11 SoTA-Echoing`. |
| Structural conformance read as prose correctness | Run the wording-pass (item 3, `CC-QR.8`): a structurally clean body can still flip the source's meaning. |

### PLAS.QualityAndRefresh:9 - Consequences

Running package adequacy (D1–D12) and per-pattern `E.21` before reliance is
expensive but prevents a stale or overclaimed seed from being shipped; refresh
triggers keep the skill from silently decaying. The cost is a recurring evaluation
loop rather than a one-time build.

### PLAS.QualityAndRefresh:10 - Rationale

`E.4.DPF.DA` evaluates the package, `E.21` each body, `E.23` the improvement loop,
and `G.11` currentness — four distinct quality functions, none substitutable for
the others. A skill has no publication form, so reader-facing checks are marked
N/A rather than silently omitted.

### PLAS.QualityAndRefresh:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| FPF `E.4.DPF.DA` (D1–D12) + `E.21` + `E.23` + `G.11` quality stack | Adopt | Package adequacy judges all D1–D12; `PFM1`–`PFM12` sub-pass N/A for a skill carrier | Reopen on FPF quality-pattern revision |
| `create-agent-skill` "Quality Gate: weak-model test" | Adopt | A weaker model must follow every step without inventing steps or asking for clarification | Reopen when the weak-model gate changes |
| `skill-creator` eval loop (test cases, baseline, benchmark) | Adapt | Recorded as the refresh/improve route; full evals deferred while the framework stays `seed` | Reopen when the seed is promoted |
| Feedback from a crafted skill: prose review of a nine-card LPF (`F.19` applied to bodies that passed every structural check) | Adapt | Item 3 wording-pass and `CC-QR.8`: prose is read as prose, `F.19` findings feed `PrecisionRestorationProfile`; evidence stays outside the carrier | Reopen when `F.19` or its `E.21` bridge changes |
| Feedback from a crafted skill: directive-transfer run (three defects caught by hand: wrong host pattern, widened source wording, non-conform term) | Adopt | Item 8 transfer procedure, `CC-QR.9`, three anti-pattern rows | Reopen on further transfer misuse signals |

Best-known line: FPF quality stack + weak-model gate. Rejected rival: "works in the demo" /
self-review ("you can't check yourself") — dropped.

### PLAS.QualityAndRefresh:12 - Relations

The dependency graph (FPF content edges + Specialization) has its single authored home
in this card's frontmatter `dependencies`; it is not repeated here. The readable
intra-LPF map is generated in `references/relations.md`.

### PLAS.QualityAndRefresh:End
