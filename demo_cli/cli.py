"""Demo CLI with multiple failure scenarios.

Each command demonstrates a different error pattern while emitting valid
cli.error.v0.1 JSON for machine capture.
"""

import sys
from pathlib import Path

import click

from .errors import CliErrorV01, emit_cli_error


def print_human_error(err: CliErrorV01) -> None:
    """Print error in predictable human-readable structure.

    This is the pattern a11y-lint expects for high accessibility scores.
    """
    click.echo(f"[{err.level}] {err.title} (ID: {err.id})")
    click.echo("")
    click.echo("What:")
    for line in err.what:
        click.echo(f"  {line}")
    click.echo("")
    click.echo("Why:")
    for line in err.why:
        click.echo(f"  {line}")
    click.echo("")
    click.echo("Fix:")
    for line in err.fix:
        click.echo(f"  {line}")


def emit_and_exit(err: CliErrorV01, json_out: str | None) -> None:
    """Emit error to human output, optional file, and stderr JSON."""
    # Human-readable output (stdout)
    print_human_error(err)

    # Machine-readable JSON
    payload = emit_cli_error(err)

    # Optional file output
    if json_out:
        Path(json_out).write_text(payload, encoding="utf-8")
        click.echo(f"\nJSON written to: {json_out}", err=True)

    # Always emit JSON to stderr for machine capture
    print(payload, file=sys.stderr)

    raise SystemExit(1)


@click.group()
def main() -> None:
    """Demo CLI for Ally integration.

    Run any subcommand to see a structured error message.
    Use --json-out to capture cli.error.v0.1 JSON.
    """
    pass


@main.command()
@click.option("--json-out", type=click.Path(dir_okay=False), help="Write JSON to file")
def network_timeout(json_out: str | None) -> None:
    """Simulate a network timeout error."""
    err = CliErrorV01(
        level="ERROR",
        code="DEM001",
        id="DEMO.NETWORK.TIMEOUT",
        title="Request timed out",
        what=["The HTTP request did not complete within 30 seconds."],
        why=[
            "The server did not respond before the timeout limit.",
            "This may indicate network congestion or server overload.",
        ],
        fix=[
            "Check your network connection.",
            "Verify the server is reachable: ping api.example.com",
            "Re-run with increased timeout: demo-cli network-timeout --timeout 60 --dry-run",
        ],
    )
    emit_and_exit(err, json_out)


@main.command()
@click.option("--json-out", type=click.Path(dir_okay=False), help="Write JSON to file")
def config_missing(json_out: str | None) -> None:
    """Simulate a missing config file error."""
    err = CliErrorV01(
        level="ERROR",
        code="DEM002",
        id="DEMO.CONFIG.MISSING",
        title="Config file not found",
        what=["The configuration file 'config.json' was not found."],
        why=[
            "The tool requires a config file to know which project to use.",
            "The file may have been deleted or never created.",
        ],
        fix=[
            "Create config.json in the current directory.",
            "Copy the template: cp config.example.json config.json",
            "Re-run: demo-cli config-missing --dry-run",
        ],
    )
    emit_and_exit(err, json_out)


@main.command()
@click.option("--json-out", type=click.Path(dir_okay=False), help="Write JSON to file")
def auth_failed(json_out: str | None) -> None:
    """Simulate an authentication failure."""
    err = CliErrorV01(
        level="ERROR",
        code="DEM003",
        id="DEMO.AUTH.INVALID_TOKEN",
        title="Authentication failed",
        what=["The API token was rejected by the server."],
        why=[
            "The token may have expired.",
            "The token may lack required permissions.",
        ],
        fix=[
            "Generate a new token at https://example.com/settings/tokens",
            "Set the token: export DEMO_API_TOKEN=<new-token>",
            "Re-run: demo-cli auth-failed --dry-run",
        ],
    )
    emit_and_exit(err, json_out)


@main.command()
@click.option("--json-out", type=click.Path(dir_okay=False), help="Write JSON to file")
def permission_denied(json_out: str | None) -> None:
    """Simulate a file permission error."""
    err = CliErrorV01(
        level="ERROR",
        code="DEM004",
        id="DEMO.FS.PERMISSION_DENIED",
        title="Permission denied",
        what=["Cannot write to '/var/log/demo.log'."],
        why=[
            "The current user does not have write permission.",
            "The directory may be owned by root.",
        ],
        fix=[
            "Check permissions: ls -la /var/log/demo.log",
            "Run with appropriate permissions or change the log path.",
            "Re-run: demo-cli permission-denied --log-path ./demo.log --dry-run",
        ],
    )
    emit_and_exit(err, json_out)


@main.command()
@click.option("--json-out", type=click.Path(dir_okay=False), help="Write JSON to file")
def validation_error(json_out: str | None) -> None:
    """Simulate a data validation error."""
    err = CliErrorV01(
        level="ERROR",
        code="DEM005",
        id="DEMO.VALIDATION.SCHEMA",
        title="Schema validation failed",
        what=[
            "The input file 'data.json' does not match the expected schema.",
            "Field 'email' is required but missing.",
        ],
        why=[
            "The schema requires all user records to have an email field.",
            "Record at index 3 is missing this field.",
        ],
        fix=[
            "Add the missing 'email' field to record 3.",
            "Validate locally: demo-cli validate data.json --dry-run",
        ],
    )
    emit_and_exit(err, json_out)


if __name__ == "__main__":
    main()
