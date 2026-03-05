---
title: Ally Demo Python Handbook
description: Reference integration for the Ally accessibility toolchain — a minimal CLI demonstrating a11y-assist, a11y-lint, and a11y-ci together.
sidebar:
  order: 0
---

Ally Demo Python is the reference integration for the Ally accessibility toolchain. It is a minimal CLI that emits structured error messages following the `cli.error.v0.1` schema, and demonstrates how **a11y-assist**, **a11y-lint**, and **a11y-ci** work together.

## What this repo does

- Emits `cli.error.v0.1` JSON on every failure -- machine-readable ground truth alongside human-friendly output.
- Provides five demo error scenarios you can run, inspect, and explain with any a11y-assist profile.
- Serves as a copy-paste template for adopting the Ally pipeline in your own CLI.

## Handbook pages

- [Getting Started](/ally-demo-python/handbook/getting-started/) -- install, run, and explain your first error.
- [Error Scenarios](/ally-demo-python/handbook/error-scenarios/) -- all five demo commands and what "good" output looks like.
- [Adoption Guide](/ally-demo-python/handbook/adoption/) -- add Ally to your own CLI in 10 minutes.

[Back to landing page](/ally-demo-python/)
