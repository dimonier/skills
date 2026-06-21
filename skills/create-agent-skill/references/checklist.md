# Agent Skill — Quick Checklist

## Should I create a skill?

- [ ] Is this task repetitive (done 3+ times)?
- [ ] Is it a multi-step procedure the agent might skip or misorder?
- [ ] Is my `AGENTS.md` bloated with exceptions and footnotes?
- [ ] Do I have an MCP tool without governance (agent has "hands" but no "profession")?
- [ ] Is there architectural documentation the agent needs only when touching that code?
- [ ] Do I need semantic filtering (dedup, grouping by meaning, not just URL collection)?
- [ ] Do multiple users/projects share the same workflow with different configs?

→ If you checked **any** of the above, a skill is likely appropriate.

## Should I NOT create a skill?

- [ ] Is this a one-off request? → Don't skill it.
- [ ] Is it a fact or preference? → Store in Memory or project rules.
- [ ] Is it purely external access without a procedure? → Just add MCP.
- [ ] Have I done this < 3 times? → Don't yet know the pattern.

## Anatomy check

- [ ] `SKILL.md` present with YAML frontmatter (`name` + `description`)
- [ ] `description` is a good trigger: WHAT it does + WHEN to use it
- [ ] Instructions step-by-step, with success and failure paths
- [ ] Heavy content externalized to `references/`, `scripts/`, `templates/`
- [ ] Evolution rule included:
      "If user is dissatisfied or clarifies the process, offer to update this skill."

## Atomicity check

- [ ] Skill does ONE thing well (not "mega-skill")
- [ ] Related skills can chain naturally (model → migration, code → test → deploy)

## Placement

- [ ] Global: `~/.agents/skills/` (base utilities, cross-cutting)
- [ ] Project-local: `<project>/.claude/skills/` (framework patterns, deployment)
- [ ] Symlinks set up (one source → multiple agent directories)

## Quality gate

- [ ] Tested on a weak model (Sonnet / GPT-4o-mini) — passes without extra questions?
- [ ] Explicit bash commands for fragile operations (not just "run the test command")
- [ ] Output templates provided (not "write a summary" but specific format)

## Anti-patterns — not present?

- [ ] NOT a mega-skill
- [ ] NOT blindly downloaded from awesome-list
- [ ] NOT Opus-only (works on weak models)
- [ ] NOT skill for everything (Memory/MCP/AGENTS.md were considered)

## Evolution loop

- [ ] Rule in SKILL.md: "If dissatisfied, offer to update"
- [ ] Structure clear enough that the agent knows WHERE to update (description / algorithm / references / script / template)
