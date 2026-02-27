#!/usr/bin/env bash
set -euo pipefail

echo "=== pytest ==="
pytest tests/ -v

echo "=== CLI smoke test ==="
for cmd in network-timeout config-missing auth-failed permission-denied validation-error; do
  demo-cli "$cmd" --json-out "/tmp/cli_error_${cmd}.json" 2>/dev/null || true
done

echo "=== build ==="
python -m build

echo "=== verify done ==="
