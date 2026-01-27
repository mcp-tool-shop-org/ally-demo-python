"""cli.error.v0.1 schema helpers.

This module provides a dataclass and helper for emitting valid cli.error.v0.1 JSON.
Copy this pattern into your own CLIs.
"""

from dataclasses import asdict, dataclass
import json
import re


@dataclass(frozen=True)
class CliErrorV01:
    """Ground truth error message following cli.error.v0.1 schema.

    Attributes:
        level: OK, WARN, or ERROR (required)
        code: Error code matching pattern ^[A-Z][A-Z0-9]{1,3}[0-9]{3}$ (e.g., "DEM001")
        id: Alternate dot-namespaced identifier (e.g., "DEMO.NETWORK.TIMEOUT")
        title: Short human-readable summary
        what: List of sentences describing what happened (required)
        why: List of sentences explaining why it happened (required for ERROR)
        fix: List of actionable steps (required for ERROR, include SAFE commands)
    """

    level: str
    code: str
    id: str
    title: str
    what: list[str]
    why: list[str]
    fix: list[str]

    def __post_init__(self) -> None:
        """Validate fields."""
        if self.level not in ("OK", "WARN", "ERROR"):
            raise ValueError(f"Invalid level: {self.level}")
        # Code pattern: ^[A-Z][A-Z0-9]{1,3}[0-9]{3}$
        if not re.match(r"^[A-Z][A-Z0-9]{1,3}[0-9]{3}$", self.code):
            raise ValueError(f"Invalid code format: {self.code} (expected e.g., DEM001)")


def emit_cli_error(err: CliErrorV01) -> str:
    """Serialize a CliErrorV01 to JSON string.

    Args:
        err: The error to serialize.

    Returns:
        JSON string with 2-space indent.
    """
    return json.dumps(asdict(err), indent=2, ensure_ascii=False)
