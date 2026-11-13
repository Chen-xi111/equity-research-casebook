from pathlib import Path

import pytest

from src.publication_guard import scan_publication


def test_current_repository_passes_publication_boundary():
    root = Path(__file__).parents[1]

    assert scan_publication(root) == []


@pytest.mark.parametrize("suffix", [".html", ".json", ".csv", ".xlsx"])
def test_private_artifact_types_are_rejected(tmp_path, suffix):
    (tmp_path / f"private{suffix}").write_text("example", encoding="utf-8")

    findings = scan_publication(tmp_path)

    assert len(findings) == 1
    assert "forbidden file type" in findings[0].reason


@pytest.mark.parametrize(
    "content",
    [
        "Your cost basis should determine this action.",
        "User's shares are included in the calculation.",
        "Your account value is used for position sizing.",
        "用户持仓用于计算。",
        "持有 4,700 股。",
    ],
)
def test_personal_position_language_is_rejected(tmp_path, content):
    (tmp_path / "report.md").write_text(content, encoding="utf-8")

    assert scan_publication(tmp_path)


def test_market_level_language_is_allowed(tmp_path):
    (tmp_path / "report.md").write_text(
        "Price held above support, but the scenario can still fail.",
        encoding="utf-8",
    )

    assert scan_publication(tmp_path) == []
