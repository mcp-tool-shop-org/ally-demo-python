# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [1.0.0] - 2026-02-27

### Added
- SECURITY.md with vulnerability reporting policy and data scope
- Threat model section in README (data touched, data NOT touched, permissions)
- Codecov and PyPI badges in README
- MCP Tool Shop footer in README
- `scripts/verify.sh` — one-command test + CLI smoke + build
- Coverage reporting with pytest-cov and Codecov in CI
- Dependency audit job with pip-audit in CI
- SHIP_GATE.md and SCORECARD.md for product standards tracking

### Changed
- CI now triggers on push paths (was workflow_dispatch only)
- Promoted to v1.0.0 — all Shipcheck hard gates pass
- Development Status classifier updated to Production/Stable

## [0.2.2] - 2026-02-26

### Added
- Publish workflow for PyPI with trusted publishers

## [0.2.0] - 2026-02-26

### Added
- Initial release with 5 demo error commands
- `cli.error.v0.1` structured error schema (CliErrorV01 dataclass)
- Human-readable + machine-readable (JSON) dual output
- a11y-lint validation in CI
- Translations (7 languages via polyglot-mcp)
- Landing page via @mcptoolshop/site-theme

## [0.1.0] - 2026-02-25

### Added
- Initial scaffolding with Click CLI
