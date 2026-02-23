# Ally Demo (Python)

A minimal Python CLI that emits cli.error.v0.1 ground truth and demonstrates the full Ally accessibility pipeline.

## Key Features

- **Structured error JSON** — cli.error.v0.1 contract for machine-readable errors
- **5 a11y-assist profiles** — lowvision, cognitive-load, screen-reader, dyslexia, plain-language
- **End-to-end pipeline** — a11y-assist, a11y-lint, a11y-ci integration demo
- **5 error scenarios** — network-timeout, config-missing, auth-failed, permission-denied, validation-error

## Install / Quick Start

```bash
pip install -e .
pip install a11y-assist a11y-lint
demo-cli network-timeout --json-out /tmp/cli_error.json || true
a11y-assist explain --json /tmp/cli_error.json --profile lowvision
```

## Links

- [GitHub Repository](https://github.com/mcp-tool-shop-org/ally-demo-python)
- [MCP Tool Shop](https://github.com/mcp-tool-shop-org)
