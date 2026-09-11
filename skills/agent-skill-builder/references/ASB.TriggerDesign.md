---
id: ASB.TriggerDesign
title: "Trigger design: the `description` as the primary load trigger"
status: seed
keywords: [trigger-design, description, frontmatter, under-trigger, over-trigger, pushy, yaml-safety]
dependencies:
  builds_on:
    - E.11
---

## ASB.TriggerDesign - Trigger design: the `description` as the primary load trigger

> **Trigger:** When drafting or revising the `description` frontmatter field — the only text an agent sees before deciding whether to load the skill body.
> **Governing patterns:**
>   → `AS.2` (Trigger Design — the AS-DPF pattern this card specializes)
>   → `E.11` (first-practical entry — the `description` *is* the first-practical entry to the skill)
> **Skill dependencies:**
>   → `create-agent-skill` / `skill-creator` (description-trigger guidance, validation)

---

### ASB.TriggerDesign:1 - Problem frame

Use this pattern when writing the `description` so the agent loads the right skill in
one hop. The body is irrelevant until the `description` fires; trigger design is
first-class, not a labeling afterthought.

### ASB.TriggerDesign:2 - Problem

Two failure modes dominate: **under-triggering** (too short/generic — the agent
misses it in context) and **over-triggering** (too broad — the skill loads on
unrelated prompts, wasting context and creating false positives). A third failure is
mechanical: a `description` containing a bare `:` + space breaks the YAML
frontmatter and the whole skill fails to load.

### ASB.TriggerDesign:3 - Forces

| Force | Settlement |
|---|---|
| Brevity vs specificity | Too short misses in context; too long wastes context and over-fires. Aim ~100–300 chars in practice. |
| Pushiness vs precision | Pushy descriptions fight under-triggering but over-fire if vague. Be pushy **and** specific. |
| WHAT vs WHEN | A description that says only WHAT ("runs tests") under-triggers; say WHAT + WHEN + key context. |
| Keyword vs situation | Keyword match is brittle; describe the *situations* that should fire the skill. |
| Machine vs prose | The `description` must stay YAML-safe (block scalar or quotes when it contains `:` + space). |

### ASB.TriggerDesign:4 - Solution

1. **Answer three questions** in the `description`:
   1. **WHAT** the skill does (one clause).
   2. **WHEN** to use it (the situations, phrasings, contexts that should fire it).
   3. **Key context** that disambiguates it from neighbouring skills (file types,
      project states, tool names).
2. **Keep it valid.** `name` is kebab-case ≤64 chars; `description` ≤1024 chars
   (per the Anthropic `quick_validate.py` schema). In practice aim for ~300 chars.
   Use a YAML block scalar (`|`) or quotes whenever the text contains `:` + space.
3. **Be pushy to compensate under-triggering.** Use explicit instruction phrasing:
   "Use this skill whenever the user mentions X, Y, or Z, even if they do not
   explicitly ask for X." Name the near-miss triggers — the user describes the
   problem in their own words without naming the domain.
4. **Add should-not-apply disambiguators** only when a neighbouring skill creates a
   real collision.
5. **Multilingual triggers.** Write the WHEN and near-miss phrases in the language(s)
   the user actually speaks, or the skill will under-fire on non-English prompts even
   when semantically correct.
6. **Anti-recursion.** The `description` is a trigger, not a body — no procedure
   steps in it.

**Examples.**

- ❌ `"Testing"` — too short, will not fire.
- ❌ a 300+-char narrative covering "every possible test scenario" — over-fires,
  wastes context.
- ✅ `"Run tests before deployment and validate changes. Use when preparing a
  release, pushing to staging/production, or after modifying production-critical
  code."`

### ASB.TriggerDesign:5 - Archetypal Grounding

**Show.** Before: `"Formats changelogs."` (under-triggers on "add a release note for
the auth fix"). After: `"Format changes into a changelog entry following the
Keep-a-Changelog convention. Use whenever the user commits a feature, fix, or
breaking change, asks for a release note, or mentions a changelog — even if they
only say 'what changed in this PR'."` The after-version names WHAT, WHEN, and a
near-miss trigger.

### ASB.TriggerDesign:6 - Bias-Annotation

The temptation is **body-in-description**: stuffing procedure into the `description`
"to make sure the agent does the right thing", which wastes always-loaded context
and over-fires. The symmetric temptation is an over-short name/description tuned to
save tokens at the cost of ever firing. Pushy-and-specific is the counterweight.

### ASB.TriggerDesign:7 - Conformance Checklist

| ID | Requirement |
|---|---|
| CC-TD.1 | The description names both WHAT the skill does and WHEN to use it. |
| CC-TD.2 | `name` is kebab-case ≤64 chars; `description` ≤1024 chars (passes `quick_validate.py`). |
| CC-TD.3 | The description is pushy-and-specific: it names near-miss phrasings without becoming vague. |
| CC-TD.4 | The description contains no execution/procedure steps. |
| CC-TD.5 | The `description` is YAML-safe (block scalar or quotes on `:` + space). |
| CC-TD.6 | WHEN/near-miss phrases are written in the user's actual working language(s). |

### ASB.TriggerDesign:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| "Runs tests"-style description | Name WHAT + WHEN + key context. |
| Domain/procedure content in the description | Move to the body; keep the trigger lean. |
| Broad description that over-fires | Narrow to the situations; add disambiguators. |
| Bare `:` + space in the description | Use a block scalar (`|`/`>`) or quotes. |
| English-only trigger phrases for a non-English user | Add near-miss phrases in the working language. |

### ASB.TriggerDesign:9 - Consequences

A pushy, specific, valid trigger makes loading cheap and accurate, but it must be
maintained as neighbouring skills shift (see `ASB.Evolution` and `AS.7`). A
YAML-unsafe description breaks loading entirely; an over-long one taxes every session
that includes the skill metadata.

### ASB.TriggerDesign:10 - Rationale

`AS.2` makes the `description` the first-practical entry (`E.11`): the agent reads
only metadata until the trigger fires, so the trigger carries the whole routing cost.
The pushiness rule compensates a known under-triggering bias; the YAML-safety rule
protects the load itself.

### ASB.TriggerDesign:11 - SoTA-Echoing

| Source line | Adopt/adapt/reject | Locus in this card | Boundary |
|---|---|---|---|
| `agent-skill-builder` "Description — the trigger" (too short / too long / just right) | Adopt | WHAT + WHEN + near-miss, with the good/bad examples | Reopen on a skill-payload edition change |
| AS-DPF `AS.2` Trigger Design | Adopt | Pushy-and-specific, multilingual triggers, length limits | Reopen on `AS.2` revision |
| Anthropic `quick_validate.py` schema (`name` ≤64, `description` ≤1024) | Adopt | Length/schema constraints | Reopen on a schema-rule release |

Best-known line: the `description` is a trigger, not a summary. Rejected rival:
"body-in-description" — rejected as over-firing and context-wasting.

### ASB.TriggerDesign:12 - Relations

- **Builds on (DPF):** `AS.2` (trigger design).
- **Builds on (FPF):** `E.11` (practical entry).
- **Coordinates with (DPF):** `AS.7` (description optimization — eval-driven tuning of this card), `AS.4` (level-1 of progressive disclosure).
- **Specialized by (LPF):** `ASB.ProgressiveDisclosure` (the `description` is level 1).

### ASB.TriggerDesign:End
