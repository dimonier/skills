# PV.Artifact - Creating a track-bound, self-contained and alienable artifact

> **Trigger:** When a track needs an artifact (`artifacts/YYYY-MM-DD-slug.md`) — an analysis, a project, a specification — bound to the track and recorded by a WRK.

```episteme id="PV.Artifact" context="ProjectVault"
Grounding (FPF):
  builds_on: A.15.1, A.15.2, E.24.PUB

UseThisWhen:
  creating an artifact bound to a track: match it to a track's plan item, gather context, write it self-contained and alienable, record the work as a WRK

Result:
  a self-contained, alienable artifact in artifacts/, bound to a track and its PlanItem, recorded by a WRK

Solution:
  AR1.TrackBindingAndPlanCheck:
    determine the track the artifact belongs to (SocratiCode codebase_search by topic or grep -l "<keyword>" project-vault/tracks/TRK-*.md)
    check for an artifact-creation item in "Next moves": explicit item → use it as the future WRK's plan_item_ref; no item but topic matches → add an item before creating, announce in chat; no fitting track → create a track (PV.Track) status: cue, then add an item
    report: "The artifact [gist] belongs to track TRK-NNNN, plan item — [N or 'new item added']. Proceeding", await confirmation
  AR2.GatheringMaterials:
    read the track's ProblemCard@Context (the core of the problem)
    gather the track's materials (references to DEC, artifacts, WRKs on the topic); if needed read the atomic files of related entities
    if the artifact relies on FPF patterns → load them from fpf-core
  AR3.PreparationAndWriting:
    create artifacts/YYYY-MM-DD-slug.md
    maintain self-containedness/alienability: the artifact is read without reaching for other project entities; references to internal codes (DEC-NNNN, TRK-NNNN, WRK-…) are forbidden — give a brief substantive description instead
    language: Russian; English insertions only for proper names, technologies, terms without an equivalent
  AR4.RecordingTheWork:
    immediately after writing — create a WRK (PV.WorkRecord)
    plan_item_ref → the item from "Next moves" (AR.1); output_refs → the created artifact
    update the track's "Completed moves"; then python scripts/vault.py work
    if the artifact closes a PlanItem → remove it from "Next moves" (the WRK in "Completed moves" records it); never strike through ~~...~~, never [x]; partial → leave with a clarification

Stop:
  the artifact is written (self-contained, no internal codes), bound to a track/PlanItem, and recorded by a WRK

Checks:
  bound to a track and a PlanItem ("Next moves")
  self-contained; no internal entity codes in the text
  narrative in Russian; English only for proper names/technologies/terms
  work recorded by a WRK with plan_item_ref and output_refs
  a closed PlanItem removed from "Next moves" (not struck through, not [x])

Antipatterns:
  internal codes in the artifact → replace with a brief substantive description
  an artifact without a track binding → bind to a track/PlanItem before creating
  a PlanItem struck through / [x] → remove it; the WRK records it

Continues:
  PV.WorkRecord (record the work), PV.Track (the binding container)

Reopen:
  A.15.1 / A.15.2 / E.24.PUB revision