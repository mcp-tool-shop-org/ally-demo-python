---
title: Adopt Ally in 10 Minutes
description: Four steps to add accessible, structured error messages to your own CLI using the Ally toolchain.
sidebar:
  order: 3
---

Adding the Ally pipeline to your own CLI takes four steps. The demo repo is your working reference for each one.

## Step 1: Emit cli.error.v0.1 JSON

When your CLI encounters an error, emit a JSON object following the `cli.error.v0.1` schema. At minimum, include these fields:

```json
{
  "level": "ERROR",
  "code": "APP001",
  "id": "MYAPP.CATEGORY.REASON",
  "title": "Short human summary",
  "what": ["What happened."],
  "why": ["Why it happened."],
  "fix": ["How to fix it."]
}
```

The `code` field follows the pattern `^[A-Z][A-Z0-9]{1,3}[0-9]{3}$`. The `id` field is a dot-namespaced identifier for grouping and filtering.

Write this JSON to stderr or to a file via a `--json-out` flag. This is the machine-readable ground truth.

## Step 2: Print predictable human text

Alongside the JSON, print the same content in a predictable structure on stdout:

```
[ERROR] Title (ID: MYAPP.CATEGORY.REASON)

What:
  Description of what happened.

Why:
  Explanation of why it happened.

Fix:
  Steps to resolve the issue.
```

This format is what a11y-lint expects for high accessibility scores. The structure is always `[LEVEL] Title (ID: <id>)` followed by **What**, **Why**, and **Fix** sections with indented lines.

## Step 3: Add CI validation

Add a11y-lint and a11y-ci to your CI pipeline to catch regressions:

```bash
# Validate that error messages conform to the contract
a11y-lint validate /path/to/captured-errors/

# Gate the pipeline with scorecards
a11y-ci gate
```

These tools read the JSON output your CLI emits and check it against the `cli.error.v0.1` contract. If a message is missing required fields or uses invalid codes, CI fails with a clear explanation.

## Step 4: Tell users about a11y-assist

The final step is user-facing. Let your users know they can get accessible explanations of any error:

```bash
a11y-assist explain --json error.json --profile lowvision
```

a11y-assist reads the same `cli.error.v0.1` JSON your CLI emits and transforms it for the chosen accessibility profile. The five built-in profiles are: **lowvision**, **cognitive-load**, **screen-reader**, **dyslexia**, and **plain-language**.

Add a note in your `--help` output or README pointing users to a11y-assist. The tool only suggests commands marked SAFE (like `--dry-run`), so it never escalates privilege or mutates state.

## That's it

Four steps, one JSON schema, and your CLI is part of the Ally ecosystem. See the [Error Scenarios](/ally-demo-python/handbook/error-scenarios/) page for working examples of every pattern.
