# Scorecard

> Score a repo before remediation. Fill this out first, then use SHIP_GATE.md to fix.

**Repo:** ally-demo-python
**Date:** 2026-02-27
**Type tags:** `[all]` `[pypi]` `[cli]`

## Pre-Remediation Assessment

| Category | Score | Notes |
|----------|-------|-------|
| A. Security | 3/10 | No SECURITY.md, no threat model, no telemetry statement |
| B. Error Handling | 9/10 | Excellent CliErrorV01 structured shape already exists |
| C. Operator Docs | 6/10 | README good, CHANGELOG template only (empty), LICENSE present |
| D. Shipping Hygiene | 4/10 | CI workflow_dispatch only, no coverage, no verify script, no dep audit |
| E. Identity (soft) | 9/10 | Logo, translations, landing page all present |
| **Overall** | **31/50** | |

## Key Gaps

1. No SECURITY.md or threat model (Section A)
2. CI only manual-trigger, no push paths (Section D)
3. No coverage, no dep audit, no verify script (Section D)
4. CHANGELOG was empty template (Section C)

## Post-Remediation

| Category | Before | After |
|----------|--------|-------|
| A. Security | 3/10 | 10/10 |
| B. Error Handling | 9/10 | 10/10 |
| C. Operator Docs | 6/10 | 10/10 |
| D. Shipping Hygiene | 4/10 | 10/10 |
| E. Identity (soft) | 9/10 | 10/10 |
| **Overall** | 31/50 | **50/50** |
