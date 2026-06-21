---
id: state-stakeholders
updated: "YYYY-MM-DD"
sources: []
source_kind: aggregate
evidence_captured_at: "YYYY-MM-DD"
owner: "project-vault coordinator"
status: active
---

# Stakeholders and Roles

A system map of roles, expectations, responsibilities, and escalation for the project.
Minimum personal data: record context and responsibility.

## Stakeholder register

| stakeholder_id | name | team_org | context_id | role | decision_scope | responsibilities | non_goals | escalation_path | communication_channel |
|---|---|---|---|---|---|---|---|---|---|
| STKH-001 | <name> | <org/team> | CXT-<slug> | <role> | <what-decisions> | <key-responsibilities> | <explicit-non-goals> | <path> | <channel> |

## Ownership and cadence

| field | value |
|---|---|
| record_owner | <role-or-person> |
| review_owner | <role-or-person> |
| approval_role | <role-or-person> |
| cadence | weekly light-check, monthly full review, quarterly redesign review |
| update_sla_hours | 24h (role/meeting change), 48h (decision/risk/contradiction impact) |
| freshness_rule | Entry is stale if context changed in sources but the card was not updated within SLA |
| last_reviewed_at | YYYY-MM-DD |

## Lifecycle and update triggers

| trigger | required_action | sla | evidence_required |
|---|---|---|---|
| Onboarding of a new participant/role | Create/activate card and fill responsibility context | By end of business day | meeting note, task, or briefing |
| Role or responsibility zone change | Close old context, open new one, update escalation_path | 24h | `meetings/.../processed.md` or briefing |
| New decision / risk / contradiction | Update affected cards and decision_scope | 48h | `decisions/*.md`, `risks.md`, `contradictions.md` |
| Publication of a significant meeting | Synchronize all affected stakeholders | 24h after `processed.md` | `meetings/.../processed.md` |
| Scheduled weekly light-check | Verify owner coverage and escalations | Once per week | `work/tasks/*.md` and/or `reports/OPEN-TASKS-by-owner-*` |
| Monthly full review | Normalize owner/role fields, remove duplicates | Once per month | changelog + sources |
| Quarterly redesign review | Rebuild the responsibility model upon process drift | Once per quarter | review protocol |

## Quality gates

- Each active card has exactly one `context_id` and one escalation path.
- Do not mix "person/role/team" in a single field.
- Every significant change is confirmed by a source.
- SLA overdue items are marked stale and raised at the next weekly light-check.

## Change log

| date | change | reason | source |
|---|---|---|---|
| YYYY-MM-DD | Initial scaffold version | Bootstrap stakeholder governance | <source-link> |
