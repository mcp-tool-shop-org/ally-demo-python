<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/ally-demo-python/readme.png" alt="Ally Demo Python" width="400">
</p>

<p align="center">
  <a href="https://github.com/mcp-tool-shop-org/ally-demo-python/actions/workflows/ci.yml"><img src="https://github.com/mcp-tool-shop-org/ally-demo-python/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow" alt="MIT License"></a>
  <a href="https://mcp-tool-shop-org.github.io/ally-demo-python/"><img src="https://img.shields.io/badge/Landing_Page-live-blue" alt="Landing Page"></a>
</p>

A minimal Python CLI that emits **cli.error.v0.1** (ground truth) and demonstrates the full Ally pipeline:

- `a11y-assist` (profiles: lowvision, cognitive-load, screen-reader, dyslexia, plain-language)
- `a11y-lint` (validate + scan)
- `a11y-ci` (gate)

This repo is intentionally small and boring. It's a reference integration.

## Quickstart

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -e .
pip install a11y-assist a11y-lint
```

Run a failing command that emits structured JSON:

```bash
demo-cli network-timeout --json-out /tmp/cli_error.json || true
```

Explain the same error using different profiles:

```bash
a11y-assist explain --json /tmp/cli_error.json --profile lowvision
a11y-assist explain --json /tmp/cli_error.json --profile cognitive-load
a11y-assist explain --json /tmp/cli_error.json --profile screen-reader
a11y-assist explain --json /tmp/cli_error.json --profile dyslexia
a11y-assist explain --json /tmp/cli_error.json --profile plain-language
```

Validate the message contract:

```bash
a11y-lint validate /tmp/cli_error.json
```

## Available Error Scenarios

The demo CLI includes several error scenarios to demonstrate different patterns:

| Command | Error ID | Description |
|---------|----------|-------------|
| `demo-cli network-timeout` | DEMO.NETWORK.TIMEOUT | HTTP request timeout |
| `demo-cli config-missing` | DEMO.CONFIG.MISSING | Missing config file |
| `demo-cli auth-failed` | DEMO.AUTH.INVALID_TOKEN | Authentication failure |
| `demo-cli permission-denied` | DEMO.FS.PERMISSION_DENIED | File permission error |
| `demo-cli validation-error` | DEMO.VALIDATION.SCHEMA | Schema validation failure |

Each command:
- Prints human-readable output to stdout
- Writes JSON to the specified `--json-out` path
- Emits JSON to stderr for machine capture

## What "good" looks like

The CLI prints a human-readable message in a predictable structure:

```
[ERROR] Title (ID: ...)

What:
  Description of what happened.

Why:
  Explanation of why it happened.

Fix:
  Steps to resolve the issue.
  Re-run: command --dry-run
```

The CLI also emits valid `cli.error.v0.1` JSON for machine capture.

- `a11y-assist` never rewrites the original output; it adds an ASSIST block.
- SAFE-only commands are suggested (and only when present in the input).

## Design notes

This demo intentionally emits:

- A stable `id` namespace (DEMO.*)
- Fix lines that include a `Re-run:` command containing `--dry-run` (SAFE)

That makes it easy to test the whole pipeline end-to-end.

## Adopt Ally in 10 minutes (for tool authors)

1. Emit `cli.error.v0.1` JSON on failure (machine output)
2. Print the same content in a predictable text structure (human output)
3. Add CI:
   - `a11y-lint validate <message.json>`
   - `a11y-ci gate` for scorecards if you lint text output
4. Tell users:
   - `a11y-assist explain --json <file>`
   - or wrapper-first: `assist-run <command>` then `a11y-assist last`

## License

MIT
