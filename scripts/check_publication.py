from pathlib import Path

from src.publication_guard import scan_publication

ROOT = Path(__file__).parents[1]


def main() -> int:
    findings = scan_publication(ROOT)
    if not findings:
        print("Publication boundary passed.")
        return 0

    for finding in findings:
        print(f"{finding.path.relative_to(ROOT)}: {finding.reason}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
