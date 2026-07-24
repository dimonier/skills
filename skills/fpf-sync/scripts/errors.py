from __future__ import annotations

from dataclasses import dataclass


@dataclass
class PatternExtractionError(Exception):
    pattern_id: str
    spec_path: str
    message: str
    candidates: tuple[str, ...] = ()

    def __str__(self) -> str:
        base = f"Pattern '{self.pattern_id}' in {self.spec_path}: {self.message}"
        if self.candidates:
            base += f" (candidates: {', '.join(self.candidates[:10])})"
        return base
