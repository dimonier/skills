# PV.Migration - Vault migration: retiring legacy directories and entity kinds into the DEC card / artifacts

> **Trigger:** When an existing vault predates a schema revision and still carries retired directories or entity kinds — the open-question/risk/contradiction directories, or `reports/`/`state/` — with live files or empty placeholders.

```episteme id="PV.Migration" context="ProjectVault"
Grounding (FPF):
  builds_on: A.7, C.32.ADR, E.4.DPF
  coordinates_with: F.14, F.18

UseThisWhen:
  migrating a pre-revision vault: retire the superseded directories and entity kinds and fold every live entity into the surviving kinds (the DEC card and artifacts/) without losing content or breaking references; target schema — PV.VaultSchema, card-filling rules — PV.StateUpdate

Result:
  a single-kind schema with no retired residue; live entities migrated; references re-pointed; retired directories removed

Solution:
  inventory:
    list the retired open-position directories (open questions, risks, contradictions); for each list its entities (Get-ChildItem / ls)
  mapByOldKind:
    open question → DEC card status: open, question into "Context and question"
    risk → DEC card status: open (or proposed if a response is formed), risk into "Revisit conditions"/"Consequences"
    contradiction → DEC card status: open, the two incompatible positions into "Considered options", the tension into "Context and question"
    content already reflected in an existing card/track → fold in as a signal, no duplicate
  allocateAndCarryOver:
    new ID only via vault.py next-id DEC; preserve status (old accepted stays accepted; old open → open/proposed); record the retired ID in the new card's frontmatter references (historical trace)
  rePointReferences:
    grep the vault for the old ID prefix; update each reference to the new card ID
  removeRetiredDirs:
    only once empty; a non-empty directory → migrate that file first, do not delete non-empty
  verify:
    vault.py check passes (old prefixes no longer resolve); migrated cards pass the decision export check (no internal IDs in the body)
  RetireReportsAndState:
    map state/constraints.md → DEC card(s): a constraint is a bounded state position with a long-lived consequence; one card each (status open/proposed; decision_type: adr for architectural, scope/process for regulatory); record state/constraints.md in the new card's frontmatter sources; not a track (a constraint is state, not an operational line)
    map each reports/* by content type: self-contained analysis with lasting value → move to artifacts/YYYY-MM-DD-slug.md (retitle slug to substance; bind a matching track + "Next moves" item, otherwise flag "unbound"); derived projection (agenda, status snapshot) → no standalone entity, fold still-relevant signals into the matching DEC ("Related entities"/"External signals") or TRK ("Next moves"), then drop the report file
    re-point, remove, verify: re-point references to the new DEC/artifact; remove reports/ and state/ only when empty; run vault.py check

Stop:
  retired directories removed (only when empty), vault.py check passes, references no longer resolve to retired IDs

Checks:
  every live entity migrated into its surviving kind (DEC card or artifacts/) before its directory is removed
  the retired ID recorded in the new card's frontmatter references
  incoming references to a retired ID re-pointed to the new card ID
  a retired directory removed only when empty
  vault.py check passes after migration
  a state/ constraint becomes a DEC card; a reports/ analysis moves to artifacts/, a projection is folded as a signal

Antipatterns:
  delete directories first, then discover the content → inventory + migrate before delete
  a contradiction split into two cards → one card; the two positions under "Considered options"
  retired directories left "just in case" → remove when empty; migration is the retire step
  a report moved to artifacts/ but left as a projection → analyses move; projections fold into DEC/TRK as signals
  reusing the old ID prefix for new cards → new ID only via vault.py next-id DEC

Continues:
  PV.VaultSchema (target schema), PV.StateUpdate (card-filling rules)

Reopen:
  A.7 / E.4.DPF / F.14 revision, or a new retired directory/kind appears