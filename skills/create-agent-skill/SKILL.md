---
name: agent-skill-builder
description: |
  Guide for deciding when to create agent skills, how to design them well,
  and what anti-patterns to avoid. Use when: (1) creating a new skill,
  (2) deciding between skills vs AGENTS.md vs MCP vs Memory,
  (3) reviewing an existing skill for quality,
  (4) unsure if a skill is needed at all.
---

# Agent Skill Builder

Helps you answer three questions: **Should I create a skill?**, **Is it well designed?**, and **Where should it live?**.

For the technical process (initialization, packaging, iteration) see the `skill-creator` skill.

---

## The Four Layers

A skill is one layer in a stack of tools for guiding agents.

| Layer | Role | Analogy |
|---|---|---|
| `AGENTS.md` / Rules | Project context: build commands, naming conventions, "what repo is this" | "Where I am" |
| **Skills** | Reusable procedures: how to test, deploy, review, generate code | **"Profession"** |
| MCP | Access to external systems: GitHub API, databases, browser, file system | "Hands" |
| Memory | Facts and preferences: user writes in Laravel, prefers tabs over spaces | "Past" |

**Memory remembers facts ("we chose Redis over Ristretto"). A skill remembers procedures ("how to add a Redis cache layer").**

**MCP gives the agent hands. A skill tells it what to do with those hands.**

---

## When to Create a Skill

Create a skill when you recognize one of these patterns:

### 1. Repetitive routine
A multi-step process you repeat often: run tests before deploy, generate a migration from a model, write a changelog before opening a PR.

The skill guarantees the agent never skips a step. *Example: a `migration` skill that reads the model's `$fillable` and `$casts`, then generates a matching migration file with `id()`, `timestamps()`, and `softDeletes()` in the correct order.*

### 2. Bloated `AGENTS.md`
Your rules file has grown exceptions, footnotes, "VERY IMPORTANT" clauses. Each line of context is always loaded — even when irrelevant.

Each exception should live in a skill pulled only when needed, not in the always-loaded context.

### 3. MCP tool without governance
You added an MCP server (GitHub search, database, browser) but the agent doesn't know *when* or *how* to use the tool.

The skill provides the procedure. The MCP provides the mechanism. *Example: an MCP gives `github.search_issues`. A skill decides which issues count as bugs, how to group duplicates, and what format to return.*

### 4. Architecture docs the agent needs mid-task
You have documentation about the outbox pattern, CQRS, or a complex deployment pipeline. The agent only needs it when touching that specific code.

Package it as a skill — the agent pulls it exactly when relevant, not a second sooner.

### 5. Semantic filtering over URL collection
You want to deduplicate news, merge related information, or group by meaning — not just collect links.

A skill applies semantic understanding (it can skip five reposts of the same release). A script can only compare strings and timestamps.

### 6. Same workflow, different configs
You want to share a skill with a team, but each person has different sources, themes, or preferences.

Hardcode the procedure in the skill. Store configuration in each user's workspace. The skill stays reusable and portable.

---

## When NOT to Create a Skill

| Situation | Better approach |
|---|---|
| One-off request ("fix this typo") | Just answer, no skill needed |
| Fact or preference ("user prefers tabs") | Store in Memory or project rules |
| External system access without a procedure | Just add an MCP server |
| You haven't done the task manually at least 3 times | You don't yet understand the pattern to encode |

---

## Anatomy of a Skill

```
my-skill/
├── SKILL.md              # YAML frontmatter + instructions
├── scripts/              # executable code (Python, Bash)
├── references/           # docs loaded on demand (troubleshooting, deep dives)
├── templates/            # output templates, config skeletons
└── assets/               # files used in output (logos, fonts, boilerplate)
```

### SKILL.md frontmatter

```yaml
---
name: my-skill
description: |
  Clear, concise description of what the skill does and when to use it.
  This is the primary trigger — the agent reads only `name` + `description`
  until it decides to load the full skill.
---
```

### Description — the trigger

The `description` is the only thing the agent sees before deciding to load the skill body.

- **Too short** (`"Runs tests"`) → agent misses it in context
- **Too long** (300+ chars) → wastes context, false positives
- **Just right** → mentions WHAT it does, WHEN to use it, and key context

**✅ Good:**
> "Run tests before deployment and validate changes. Use when preparing a release, pushing to staging/production, or after modifying production-critical code."

**❌ Bad:**
> "Testing"

**❌ Also bad:**
> "A comprehensive skill for running all kinds of tests in any environment for any project across the organization with detailed instructions on how to handle every possible test scenario..."

### Progressive disclosure (3 levels)

1. **Metadata** (`name` + `description`) — always in context (~100 tokens)
2. **SKILL.md body** — loaded only when the skill triggers
3. **Bundled resources** — loaded on demand (`references/` into context, `scripts/` executed)

This is the key difference from a monolithic `AGENTS.md`: context is not consumed until the moment it's needed.

---

## The Atomicity Principle

**Split by action, not by domain.**

✅ `model` — creates and updates Eloquent models
✅ `migration` — creates and validates migrations
✅ `pest-tests` — writes and updates PHP tests
✅ `api-resource` — enforces API response format
✅ `changelog` — formats changes into a changelog entry

❌ `mega-laravel-skill` — models, migrations, tests, controllers, OpenAPI, deploy, coffee, massage

A mega-skill becomes `AGENTS.md` in a different directory — with the same bloat problems, just hidden.

Small skills are:
- Easier to debug (one responsibility)
- Easier to reuse (pull only what you need)
- Easier to improve (change one without touching others)
- Chained by the agent naturally (creates model → triggers migration skill)

---

## Skill Creation Checklist

- [ ] **Atomic responsibility** — skill does ONE thing well
- [ ] **Frontmatter** — both `name` and `description` present
- [ ] **Description is a trigger** — mentions WHAT + WHEN (not just WHAT)
- [ ] **Instructions are step-by-step** — includes success AND failure paths
- [ ] **Heavy content externalized** — long docs → `references/`, scripts → `scripts/`, templates → `templates/`
- [ ] **Evolution rule present** — "If user is dissatisfied, offer to update this skill"
- [ ] **Placement correct** — global vs project-local (see guide below)
- [ ] **Passes weak model test** — see Quality Gate below

---

## Anti-Patterns

### 1. The Mega-Skill
Trying to cover everything in one skill. It reproduces all the problems of a bloated `AGENTS.md`.

**Fix:** Split into atomic skills. Let the agent chain them.

### 2. Downloading Awesome Lists
Installing 100 skills from awesome-agent-skills repositories. Each carries:
- A foreign workflow that doesn't match yours
- Potential security holes (scripts run with your agent's permissions)
- Noise in the skill selection (more skills = harder to pick the right one)

**Fix:** Learn from them. Write your own. Only install base utilities (official Anthropic skills, `agent-browser`).

### 3. Blind `skill-creator` Trust
The generated skill needs your judgment. Always review and tune — especially the `description`.

### 4. Opus-Only Dependency
If a skill can't guide a weaker model (Sonnet, GPT-4o-mini) through the process, it's poorly structured.

**Fix:** Break down steps further. Add explicit commands. Provide ready-made scripts. Use templates for output formats.

### 5. Skills for Everything
Not every task needs a skill. See "When NOT to Create a Skill" above.

---

## Placement Guide

### Global skills (available to all agents / all projects)
- Base utilities: official Anthropic skills (PDF, XLSX, DOCX, skill-creator)
- `agent-browser` for web testing
- Cross-cutting concerns: `go-packages` (package selection), `news-digest` (daily digests)

Store in: `~/.agents/skills/`, `~/.claude/skills/`, etc.

### Project-local skills (specific to one repository)
- Framework patterns (`model`, `migration`, `controller` for Laravel)
- Architecture documentation (outbox pattern, CQRS, error handling)
- Deployment procedures

Store in: `<project>/.claude/skills/`, `<project>/.codex/skills/`

### Symlink strategy (recommended)
Keep one source directory, symlink into per-agent paths:

```
~/.agents/skills/           # source of truth
~/.claude/skills/           → symlink to ~/.agents/skills/
~/.codex/skills/            → symlink to ~/.agents/skills/
```

Some agents (OpenCode) natively read multiple directories — check their documentation before symlinking.

> **Security:** Be selective with global skills. Each skill with scripts is an attack surface. Install only what you trust and need daily.

---

## Quality Gate

> **If a weak model (Sonnet, GPT-4o-mini) performs the skill without extra questions or hallucinated steps, the skill is well written.**
>
> If a skill only works with Opus on max thinking, you haven't written a skill — you've hidden a prompt in a file and hope the expensive model carries your laziness.

### The test
1. Give the weak model a typical prompt that should trigger the skill
2. Observe: does it follow every step? Does it ask for clarification? Does it invent missing steps?
3. If it stumbles: add more explicit commands, script `bash` calls, provide output templates
4. Iterate

### Why it matters
- Tokens aren't free (11 billion tokens in 3 months is a real budget)
- Weaker models execute faster
- A skill that works on weak models works *better* on strong ones (less hallucination, fewer skipped steps)

---

## Making Skills Evolve

Hardcode this rule in every skill:

> If the user is dissatisfied with the result or clarifies the process, offer to update this skill.

The agent will then:
1. Identify what to change — `description`, algorithm, `references/`, template, or troubleshooting file
2. Update the relevant file
3. Optionally log the change in a `CHANGELOG.md` inside the skill directory

A well-structured skill makes it obvious where to apply the fix. If it doesn't, the skill is probably too large or poorly organized.

---

## Summary

| Tool | Role | When to use |
|---|---|---|
| `AGENTS.md` | Project context | Always needed, keep lean |
| **Skill** | Reusable procedure | Repetitive tasks, complex workflows, MCP governance |
| MCP | External system access | Need to talk to GitHub, DB, browser |
| Memory | Facts and preferences | User habits, past decisions, project history |

> `AGENTS.md` tells the agent where it is.
> MCP gives it hands.
> Memory gives it a past.
> **Skills give it a profession.**
