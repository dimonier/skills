---
id: PLAS.QualityAndRefresh
title: "Evaluating, improving, and refreshing a DPF-skill"
status: seed
keywords: [quality, evaluation, improvement, refresh, currentness, weak-model]
dependencies:
  builds_on:
    - E.4.DPF.DA
    - E.21
    - E.23
    - G.11
  coordinates_with:
    - E.22
    - E.19
---

## PLAS.QualityAndRefresh - Evaluating, improving, and refreshing a DPF-skill

> **Trigger:** After a DPF-skill seed exists — before relying on it, and again whenever sources, FPF, or local use change.
> **Governing FPF patterns:**
>   → E.4.DPF.DA
>   → E.21
>   → E.23
>   → G.11
>   → E.22
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
the loop has no syntactic check to catch it.

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
3. **Pattern quality** with `E.21`; mark bodies `seed` until they pass.
4. **Machine frontmatter check (cheap, before any "rely on").** Parse every card's
   YAML frontmatter — and the `SKILL.md` `description` — with a validator (e.g.
   `skill-creator/scripts/quick_validate.py`) and fail on any parse error before
   relying on the skill. A `description` with a bare `:` + space breaks the whole
   frontmatter (`ScannerError`); the check catches it mechanically, not by eye.
5. **Improve** with `E.23` in a loop, with a separate reviewer and a target level.
6. **Weak-model gate** (`create-agent-skill`): a weaker model must follow every
   step without inventing steps or asking for clarification.
7. **Refresh** with `G.11`: reopen on source change, FPF edition change, local
   misuse telemetry, or supersession.

### PLAS.QualityAndRefresh:5 - Archetypal Grounding

**Show.** `pattern-language-as-agent-skill` is a first seed: bodies are `seed`, not yet
`E.21`-evaluated; `SKILL.md` says so. Before reliance, run `E.4.DPF.DA` D1–D12 and
the weak-model gate.

### PLAS.QualityAndRefresh:6 - Bias-Annotation

"Works in the demo" is the classic adequacy illusion: a seed that succeeds on one
prompt is mistaken for a reliable framework. The author also cannot reliably
self-review ("you can't check yourself", `E.23`). Publication-form checks are easy
to silently drop rather than mark N/A, which hides the carrier-specific gap.

### PLAS.QualityAndRefresh:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-QR.1 | Package adequacy is evaluated with all `E.4.DPF.DA` D1–D12 coordinates, not assumed from a build. |
| CC-QR.2 | Each body has an `E.21` result or an explicit `seed` mark. |
| CC-QR.3 | Improvement uses a separate reviewer and a target level (`E.23`). |
| CC-QR.4 | Refresh triggers are named (`G.11`). |
| CC-QR.5 | Publication-form checks are explicitly N/A, not silently dropped. |
| CC-QR.6 | A machine frontmatter-parse check (incl. `description` YAML-safety) passes before reliance. |

### PLAS.QualityAndRefresh:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| "Works in the demo" = adequate | Run `E.4.DPF.DA` + `E.21` before reliance. |
| Improvement without characteristics | Frame with `E.22`; pick a measured aspect. |
| Publication-form checks forced on a skill | Mark them N/A; there is no reader form. |
| Frontmatter never machine-parsed | Run a cheap YAML/parse check before reliance. |

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

Best-known line: FPF quality stack + weak-model gate. Rejected rival: "works in the demo" /
self-review ("you can't check yourself") — dropped.

### PLAS.QualityAndRefresh:12 - Relations

- **Builds on:** `E.4.DPF.DA` (package), `E.21` (pattern), `E.23` (improvement), `G.11` (currentness).
- **Coordinates with:** `E.22` (framing), `E.19` (admission gating), `create-agent-skill` (weak-model gate).

### PLAS.QualityAndRefresh:End
