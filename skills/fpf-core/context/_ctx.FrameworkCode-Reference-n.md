---
id: "_ctx.FrameworkCode-Reference-n"
title: "<FrameworkCode>.Reference:<n> - <Title>"
---

# _ctx.FrameworkCode-Reference-n: <FrameworkCode>.Reference:<n> - <Title>

---

## <FrameworkCode>.Reference:<n> - <Title>
### <FrameworkCode>.Reference:<n>.<m> - <Title>
```

For example, `## STR.Reference:1 - Problem frame - Direction and commitment under changing conditions` identifies the first section of a Strategy architectural-reference unit whose key is `Reference`. `#### FPF.Reference:16.8.2 - Production and situated use are different contributions` identifies a nested section in the FPF Core architectural-reference unit. Use the framework's declared public code; name the framework as well when quoting outside a context that identifies it. The enclosing H1 gives the qualified Architectural Reference title and has a product-declared ToC entry. Changing a former section key requires updating its maintained current returns; changing the title alone does not preserve a former URL fragment.

Close the complete architectural-reference unit with one content-free H2 heading, `## <FrameworkCode>.Reference:End`, after its last paragraph, list or other content and before the next publication unit. For example, the Strategy architectural-reference unit ends with `## STR.Reference:End`. This visible boundary shows where the unit ends when it is copied or retrieved separately. It closes the whole unit, not each numbered subsection; it adds neither a content section nor a pattern-index entry. A heading shown inside a fenced example does not close the unit.

Number sibling sections in reading order, starting at 1, and carry the complete parent path into nested headings. Each nesting level adds one heading level and one ordinal. These ordinals locate sections in this publication unit; their titles state the content functions. An account can combine several E.8 functions in one section or explain one function across several sections. Keep that useful arrangement instead of adding twelve empty sections to match numbers. The rule introduces no limit on useful conceptual scales; physical Markdown heading depth remains a carrier constraint.

`STR.Reference` names a publication unit. Its section addresses are `SectionRef` uses under E.8, not declarations of additional patterns: the pattern index continues to contain the individually declared pattern bodies. Apply the same self-identifying construction to a profile account or other support unit when it needs its own section addresses, using its product-declared unit key. A profile explained inside the architectural reference retains that unit's section path; this text position does not decide the profile's semantic relations.

The prefix lets a reader distinguish a whole-language Problem frame from the Problem frame of one pattern before choosing what to read or cite. Visible names and numbers also survive copying and printing, where a hidden anchor cannot help.

The visible address and title use the ASCII ` - ` separator. Build each clickable fragment from the complete rendered heading according to the target Markdown carrier's rules, including punctuation removal and duplicate handling. When a heading changes, update its direct links in the publication, source templates and public consumers together. Check that the link resolves to the intended heading, then read that target for the answer the link promises. Keep the visible address usable for search and non-clickable copies. E.8:4.1.1 excludes raw HTML from this form, including compatibility anchors.
