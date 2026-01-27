"""Tests for cli.error.v0.1 emission."""

import json

import pytest

from demo_cli.errors import CliErrorV01, emit_cli_error


def test_cli_error_v01_valid():
    """Valid CliErrorV01 should serialize correctly."""
    err = CliErrorV01(
        level="ERROR",
        code="TST001",
        id="TEST.ERROR.001",
        title="Test error",
        what=["Something happened."],
        why=["Because of reasons."],
        fix=["Do this.", "Re-run: test --dry-run"],
    )
    payload = emit_cli_error(err)
    parsed = json.loads(payload)

    assert parsed["level"] == "ERROR"
    assert parsed["code"] == "TST001"
    assert parsed["id"] == "TEST.ERROR.001"
    assert parsed["title"] == "Test error"
    assert len(parsed["what"]) == 1
    assert len(parsed["why"]) == 1
    assert len(parsed["fix"]) == 2


def test_cli_error_v01_invalid_level():
    """Invalid level should raise ValueError."""
    with pytest.raises(ValueError, match="Invalid level"):
        CliErrorV01(
            level="FAILURE",
            code="TST001",
            id="TEST.001",
            title="Test",
            what=["X"],
            why=["Y"],
            fix=["Z"],
        )


def test_cli_error_v01_invalid_code_format():
    """Invalid code format should raise ValueError."""
    with pytest.raises(ValueError, match="Invalid code format"):
        CliErrorV01(
            level="ERROR",
            code="invalid",
            id="TEST.001",
            title="Test",
            what=["X"],
            why=["Y"],
            fix=["Z"],
        )


def test_cli_error_v01_valid_code_patterns():
    """Various valid code patterns should work."""
    # Short code: AB001 (2 chars + 3 digits)
    err1 = CliErrorV01(
        level="ERROR",
        code="AB001",
        id="TEST.001",
        title="Test",
        what=["X"],
        why=["Y"],
        fix=["Z"],
    )
    assert err1.code == "AB001"

    # Long code: DEMO001 (4 chars + 3 digits)
    err2 = CliErrorV01(
        level="ERROR",
        code="DEMO001",
        id="TEST.001",
        title="Test",
        what=["X"],
        why=["Y"],
        fix=["Z"],
    )
    assert err2.code == "DEMO001"

    # Medium code: DEM001 (3 chars + 3 digits)
    err3 = CliErrorV01(
        level="ERROR",
        code="DEM001",
        id="TEST.001",
        title="Test",
        what=["X"],
        why=["Y"],
        fix=["Z"],
    )
    assert err3.code == "DEM001"


def test_emit_cli_error_json_format():
    """Emitted JSON should be properly formatted."""
    err = CliErrorV01(
        level="WARN",
        code="TST002",
        id="TEST.WARN.001",
        title="Warning",
        what=["Minor issue."],
        why=["Expected behavior."],
        fix=["No action needed."],
    )
    payload = emit_cli_error(err)

    # Should be valid JSON
    parsed = json.loads(payload)
    assert parsed["level"] == "WARN"

    # Should have indentation (pretty-printed)
    assert "\n" in payload
    assert "  " in payload


def test_emit_cli_error_unicode():
    """Emitted JSON should handle unicode correctly."""
    err = CliErrorV01(
        level="ERROR",
        code="TST003",
        id="TEST.UNICODE.001",
        title="Unicode test: \u2713 \u2717",
        what=["Contains unicode: \u00e9\u00e8\u00ea"],
        why=["Multi-language support."],
        fix=["No changes needed."],
    )
    payload = emit_cli_error(err)
    parsed = json.loads(payload)

    assert "\u2713" in parsed["title"]
    assert "\u00e9" in parsed["what"][0]
