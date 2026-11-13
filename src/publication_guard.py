"""Conservative checks for the public-report publication boundary."""

import re
from dataclasses import dataclass
from pathlib import Path

FORBIDDEN_SUFFIXES = {".html", ".json", ".csv", ".xlsx", ".xls"}

# These expressions target individualized portfolio language, not ordinary
# discussion of market risk or company fundamentals.
FORBIDDEN_PATTERNS = {
    "personal position quantity": re.compile(
        r"(?:my|your|user(?:'s)?)\s+(?:shares?|position|holdings?)",
        re.IGNORECASE,
    ),
    "personal cost basis": re.compile(
        r"(?:my|your|user(?:'s)?)\s+(?:cost basis|average cost|entry price)",
        re.IGNORECASE,
    ),
    "personal account value": re.compile(
        r"(?:my|your|user(?:'s)?)\s+(?:account|portfolio)\s+"
        r"(?:value|size|balance)",
        re.IGNORECASE,
    ),
    "Chinese personal position": re.compile(
        r"(?:你的|你的账户|用户|本人)(?:持仓|成本|股数|账户|仓位)",
    ),
    "Chinese exact holding": re.compile(r"持有\s*\d[\d,]*\s*股"),
}


@dataclass(frozen=True)
class Finding:
    path: Path
    reason: str


def scan_publication(root: Path) -> list[Finding]:
    """Return publication-boundary findings below ``root``."""

    findings: list[Finding] = []
    for path in sorted(root.rglob("*")):
        if not path.is_file() or any(
            part.startswith(".") for part in path.relative_to(root).parts
        ):
            continue
        if "tests" in path.relative_to(root).parts:
            continue
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            findings.append(Finding(path, f"forbidden file type {path.suffix}"))
            continue
        if path.suffix.lower() != ".md":
            continue
        text = path.read_text(encoding="utf-8")
        for reason, pattern in FORBIDDEN_PATTERNS.items():
            if pattern.search(text):
                findings.append(Finding(path, reason))
    return findings
