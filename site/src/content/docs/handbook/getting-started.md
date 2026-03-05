---
title: Getting Started
description: Install the demo CLI and run your first structured error message with a11y-assist accessibility profiles.
sidebar:
  order: 1
---

## Prerequisites

- Python 3.10 or later
- pip

## Install

Create a virtual environment and install the demo CLI along with the Ally tools:

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

pip install -e .
pip install a11y-assist a11y-lint
```

This installs:

- **demo-cli** -- the reference CLI that emits `cli.error.v0.1` JSON.
- **a11y-assist** -- explains errors using accessibility profiles.
- **a11y-lint** -- validates your error messages against the contract.

## Run a demo scenario

Trigger the network timeout error and capture JSON output:

```bash
demo-cli network-timeout --json-out /tmp/error.json
```

You will see human-readable output on stdout and machine-readable JSON written to the file.

## Explain with different profiles

Pass the captured JSON to a11y-assist with any of the five built-in profiles:

```bash
a11y-assist explain --json /tmp/error.json --profile lowvision
a11y-assist explain --json /tmp/error.json --profile cognitive-load
a11y-assist explain --json /tmp/error.json --profile screen-reader
a11y-assist explain --json /tmp/error.json --profile dyslexia
a11y-assist explain --json /tmp/error.json --profile plain-language
```

Each profile transforms the same error into a presentation tuned for that audience. The ground truth stays the same; only the delivery changes.
