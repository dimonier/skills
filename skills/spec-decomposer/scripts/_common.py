from __future__ import annotations

import hashlib
import json
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

PATTERN_ID_RE = re.compile(r"\b((?:CC-)?[A-Z][A-Za-z]*(?:\.[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)+)\b")

_DASH_RUN = re.compile(r"-{4,}")
_SPACE_RUN = re.compile(r" {3,}")


@dataclass
class SizeStats:
    raw_bytes: int = 0
    optimized_bytes: int = 0


@dataclass
class ExtractedUnit:
    pid: str
    title: str
    body: str
    start_line: int
    end_line: int
    metadata: dict[str, Any] = field(default_factory=dict)


@dataclass
class DecomposeReport:
    spec_path: str
    spec_type: str
    total_patterns: int
    patterns_extracted: int
    toc_parsed: bool
    toc_entries: int
    warnings: list[str] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)
    non_extractable: list[str] = field(default_factory=list)
    size_stats: SizeStats = field(default_factory=SizeStats)

    def to_dict(self) -> dict[str, Any]:
        return {
            "spec_path": self.spec_path,
            "type": self.spec_type,
            "total_patterns": self.total_patterns,
            "patterns_extracted": self.patterns_extracted,
            "toc_parsed": self.toc_parsed,
            "toc_entries": self.toc_entries,
            "warnings": self.warnings,
            "errors": self.errors,
            "non_extractable_sections": self.non_extractable,
            "size_stats": {
                "raw_bytes": self.size_stats.raw_bytes,
                "optimized_bytes": self.size_stats.optimized_bytes,
                "saved_bytes": self.size_stats.raw_bytes - self.size_stats.optimized_bytes,
            },
        }

    def print(self):
        json.dump(self.to_dict(), sys.stdout, indent=2, ensure_ascii=False)
        sys.stdout.write("\n")


def slugify(pid: str) -> str:
    return f"{pid}.md"


def sha256(content: str) -> str:
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def yaml_frontmatter(meta: dict[str, Any]) -> str:
    lines = ["---"]
    for key, value in meta.items():
        lines.extend(_yaml_kv(key, value))
    lines.append("---")
    return "\n".join(lines) + "\n"


def _yaml_kv(key: str, value: Any, indent: int = 0) -> list[str]:
    prefix = "  " * indent
    if isinstance(value, dict):
        result = [f"{prefix}{key}:"]
        for k, v in value.items():
            result.extend(_yaml_kv(k, v, indent + 1))
        return result
    elif isinstance(value, list):
        if not value:
            return [f"{prefix}{key}: []"]
        result = [f"{prefix}{key}:"]
        for item in value:
            result.append(f"{prefix}  - {_yaml_scalar(item)}")
        return result
    elif value is None:
        return [f"{prefix}{key}: "]
    else:
        return [f"{prefix}{key}: {_yaml_scalar(value)}"]


def _yaml_scalar(value: Any) -> str:
    s = str(value)
    if any(ch in s for ch in (":", "#", "{", "}", "[", "]", ",", "&", "*", "?", "|", "-", "<", ">", "=", "!", "%", "@", "`")):
        return f'"{s}"'
    if s and s[0] in ("'", '"'):
        return s
    return s


def optimize_body(text: str) -> str:
    """Compress table separator lines and excessive whitespace."""
    lines = text.splitlines(keepends=True)
    result: list[str] = []
    for line in lines:
        stripped = line.rstrip("\n\r")
        if _is_table_sep(stripped):
            stripped = _DASH_RUN.sub("---", stripped)
        stripped = _SPACE_RUN.sub("  ", stripped)
        result.append(stripped + "\n")
    return "".join(result)


_TABLE_SEP_RE = re.compile(r"^\|[-: |]+\|$")


def _is_table_sep(line: str) -> bool:
    return bool(_TABLE_SEP_RE.match(line))


def format_reference(
    unit: ExtractedUnit,
    spec_filename: str,
) -> str:
    pid = unit.pid
    title = unit.title or pid
    meta = dict(unit.metadata)
    meta.setdefault("id", pid)
    meta.setdefault("title", title)

    lines: list[str] = []
    lines.append(yaml_frontmatter(meta).rstrip())
    lines.append("")
    lines.append(f"# {pid}: {title}")
    lines.append("")
    lines.append("> **Trigger:** [TODO: trigger condition — human review required]")
    lines.append("> **Governing patterns:**")
    lines.append(">   → [TODO: extract governing-pattern cues from body and convert to reference paths]")
    lines.append("")
    lines.append("---")
    lines.append("")

    body = unit.body.rstrip("\n")
    if body.endswith("---"):
        body = body[:-3].rstrip("\n")
    raw_len = len(body.encode("utf-8"))
    body = optimize_body(body)
    opt_len = len(body.encode("utf-8"))
    lines.append(body)

    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append(f"> **Source:** `{spec_filename}` lines L{unit.start_line}–L{unit.end_line}")
    lines.append("")

    return "\n".join(lines), raw_len, opt_len


def generate_index(
    entries: list[ExtractedUnit],
    skill_name: str,
    spec_filename: str,
    *,
    has_relations: bool = False,
) -> str:
    lines: list[str] = []
    lines.append(f"# {skill_name} — Pattern Index")
    lines.append("")
    lines.append("| Pattern ID | Title | Keywords |")
    lines.append("|---|---|---|")

    for unit in entries:
        pid = unit.pid
        title = unit.title or pid
        keywords_list = unit.metadata.get("keywords", [])
        keywords = ", ".join(keywords_list[:5]) if keywords_list else "—"
        lines.append(f"| {pid} | {title} | {keywords} |")

    lines.append("")
    lines.append("## Cross-references")
    if has_relations:
        lines.append("- See `relations.md` for pattern relation records (E.4.PFR)")
    lines.append(f"- Full monolith: `{spec_filename}`")
    lines.append("")

    return "\n".join(lines)


def idempotent_write(filepath: Path, content: str, dry_run: bool = False) -> bool:
    if filepath.exists():
        existing_hash = sha256(filepath.read_text(encoding="utf-8"))
        if existing_hash == sha256(content):
            return False

    if dry_run:
        print(f"[DRY-RUN] Would write: {filepath}", file=sys.stderr)
        return False

    filepath.parent.mkdir(parents=True, exist_ok=True)
    filepath.write_text(content, encoding="utf-8")
    return True


def remove_trivial(filepath: Path, min_non_empty: int = 3, dry_run: bool = False) -> bool:
    """Remove file if it has fewer than min_non_empty non-empty lines. Returns True if removed."""
    if not filepath.exists():
        return False
    text = filepath.read_text(encoding="utf-8")
    non_empty = [ln for ln in text.splitlines() if ln.strip()]
    if len(non_empty) < min_non_empty:
        if dry_run:
            print(f"[DRY-RUN] Would remove trivial: {filepath}", file=sys.stderr)
        else:
            filepath.unlink()
        return True
    return False
