# Security Policy

## Supported Versions

| Version | Supported |
|---------|-----------|
| 1.x     | Yes       |
| < 1.0.0 | No        |

## Reporting a Vulnerability

Email: **64996768+mcp-tool-shop@users.noreply.github.com**

Include:
- Description of the vulnerability
- Steps to reproduce
- Version affected
- Potential impact

### Response timeline

| Action | Target |
|--------|--------|
| Acknowledge report | 48 hours |
| Assess severity | 7 days |
| Release fix | 30 days |

## Scope

This is a reference demo CLI that intentionally produces structured error messages for testing a11y-lint and a11y-assist integration.

- **Data touched:** demonstration error scenarios only — no real data is read or written beyond optional `--json-out` file
- **Data NOT touched:** no user credentials, no system files, no network calls (all errors are simulated)
- **Network:** no network egress. Simulated error messages mention fictional endpoints for demonstration only.
- **File writes:** only the optional `--json-out` path specified by the user
- **No telemetry** is collected or sent
- **No secrets handling** — does not read, store, or transmit credentials
