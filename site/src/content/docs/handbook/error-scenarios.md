---
title: Error Scenarios
description: All five demo error commands, their structured output, and what "good" looks like for both humans and machines.
sidebar:
  order: 2
---

The demo CLI ships with five built-in error scenarios. Each one emits both a human-readable message and a `cli.error.v0.1` JSON payload.

## Scenario reference

| Command | Error ID | Code | Description |
|---|---|---|---|
| `demo-cli network-timeout` | DEMO.NETWORK.TIMEOUT | DEM001 | HTTP request timed out |
| `demo-cli config-missing` | DEMO.CONFIG.MISSING | DEM002 | Missing configuration file |
| `demo-cli auth-failed` | DEMO.AUTH.INVALID_TOKEN | DEM003 | Authentication failure |
| `demo-cli permission-denied` | DEMO.FS.PERMISSION_DENIED | DEM004 | File permission error |
| `demo-cli validation-error` | DEMO.VALIDATION.SCHEMA | DEM005 | Schema validation failure |

Every command accepts `--json-out <path>` to write the JSON payload to a file.

## What "good" looks like

### Human output

The human-readable format prints to stdout in a predictable structure that a11y-lint scores highly:

```
[ERROR] Request timed out (ID: DEMO.NETWORK.TIMEOUT)

What:
  The HTTP request did not complete within 30 seconds.

Why:
  The server did not respond before the timeout limit.
  This may indicate network congestion or server overload.

Fix:
  Check your network connection.
  Verify the server is reachable: ping api.example.com
  Re-run with increased timeout: demo-cli network-timeout --timeout 60 --dry-run
```

The pattern is always: `[LEVEL] Title (ID: <dot-namespaced-id>)` followed by **What**, **Why**, and **Fix** sections. Each section contains one or more indented lines.

### JSON output for machine capture

The same error emits `cli.error.v0.1` JSON to stderr (and optionally to a file via `--json-out`):

```json
{
  "level": "ERROR",
  "code": "DEM001",
  "id": "DEMO.NETWORK.TIMEOUT",
  "title": "Request timed out",
  "what": ["The HTTP request did not complete within 30 seconds."],
  "why": [
    "The server did not respond before the timeout limit.",
    "This may indicate network congestion or server overload."
  ],
  "fix": [
    "Check your network connection.",
    "Verify the server is reachable: ping api.example.com",
    "Re-run with increased timeout: demo-cli network-timeout --timeout 60 --dry-run"
  ]
}
```

This JSON is the ground truth that a11y-assist reads and transforms for each accessibility profile.

## Running all scenarios

```bash
for cmd in network-timeout config-missing auth-failed permission-denied validation-error; do
  echo "=== $cmd ==="
  demo-cli "$cmd" --json-out "/tmp/${cmd}.json"
  echo ""
done
```

## Validating with a11y-lint

After capturing JSON output, validate that it conforms to the contract:

```bash
a11y-lint validate /tmp/network-timeout.json
```
