# PV.Inbox - Intake: inbox procedure, PDF preprocessing, routing

> **Trigger:** When the owner asks to "process the inbox" (or similar), or when new sources (transcripts, PDFs, articles, research) have appeared in `inbox/`.
> **Skill dependency:** `pdf2md` (PDF → Markdown).

```episteme id="PV.Inbox" context="ProjectVault"
Grounding (FPF):
  builds_on: C.2.1, E.11
  coordinates_with: A.15.1

UseThisWhen:
  intaking raw sources from inbox/: capture, preprocess, route each to StateUpdate / ExternalResearch / Track
  never by analysing the original PDF directly — always via a faithful Markdown conversion

Result:
  inbox/ processed and cleared; every material routed by type; a source copy in project-vault/sources/; the pass recorded as a WRK

Solution:
  Request:
    process files in inbox/ with LPF procedures; after full processing clear inbox/ (delete the channel file) — for every material type (PDF, transcript, article, outbox-style proposal)
    nothing is lost: content lives in the target track/entity, source copy in project-vault/sources/
    *.bak files ignored — backup/edit artifacts, not copied to sources/, not routed, removed without substantive processing
  Preprocess:
    .txt (incl. Cyrillic) → read with a filesystem reader (the agent's Read tool); never shell console (Get-Content/redirect) — the console codepage mangles Cyrillic; never transcode a valid UTF-8 file "blindly"
    .pdf → convert each to Markdown via pdf2md (script scripts/extract_pdfs.py, parameters --source <inbox_dir> --first N) before substantive processing; use the result (.md in inbox/_markdown/) as the source; never analyse the original PDF directly
    pdf2md unavailable or conversion fails → record this in the intake result and notify the owner
  Route:
    meeting transcript/protocol → StateUpdate
    independent study (Knowy) / narrativization / article / talk / tutorial → ExternalResearch with two-way binding
    material with valuable artifacts → file into a fitting track or create one (Track)
    outbox-style proposal (addressee/source_project frontmatter addressing this project/skill) → same routing: source copy in sources/, gist into a new or fitting track, then clear
    *.bak never routed
  RecordIntakeAct:
    record the pass as a WRK — into the fitting target track
    service track (PV.Track T.5) only when no track fits (e.g. the material produced only atomic entities — DEC — with no operational line)
    never open a track solely to contain the intake WRK itself

Stop:
  inbox/ empty; each material routed + source copy in sources/; the intake pass recorded as a WRK

Checks:
  PDF converted to Markdown before processing; original never analysed directly
  every material routed by type (StateUpdate / ExternalResearch / Track)
  inbox/ cleared after full processing for every type; nothing lost
  conversion failure recorded and brought to the owner
  *.bak files ignored (not copied/routed, removed without substantive processing)
  intake pass recorded as a WRK in the fitting target track; service track only when no track fits (PV.Track T.5)
  .txt read with a filesystem reader, never a shell console; Cyrillic never transcoded "blindly"

Antipatterns:
  direct PDF analysis without conversion → first pdf2md, then process the .md
  material without explicit routing → determine the type, route the correct procedure
  inbox/ not cleared (incl. a retained outbox-proposal file) → source copy in sources/, then delete the inbox file
  *.bak processed as standalone material → ignore (backup/edit artifact, not a source)
  Cyrillic .txt via console redirection / transcoded "blindly" → filesystem reader, never transcode valid UTF-8
  intake without a WRK, or a track opened just for it → WRK in the fitting target track; service track only when none fits

Continues:
  PV.StateUpdate / PV.ExternalResearch / PV.Track (route targets); PV.Outbox (for outbox-style proposals)

Reopen:
  E.11 / C.2.1 revision, or a converter (pdf2md) change