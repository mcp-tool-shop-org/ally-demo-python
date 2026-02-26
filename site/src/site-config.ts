import type { SiteConfig } from '@mcptoolshop/site-theme';

export const config: SiteConfig = {
  title: 'Ally Demo Python',
  description: 'Reference integration demonstrating the Ally accessibility toolchain',
  logoBadge: 'A',
  brandName: 'ally-demo-python',
  repoUrl: 'https://github.com/mcp-tool-shop-org/ally-demo-python',
  footerText: 'MIT Licensed — built by <a href="https://github.com/mcp-tool-shop-org" style="color:var(--color-muted);text-decoration:underline">mcp-tool-shop-org</a>',

  hero: {
    badge: 'Reference integration',
    headline: 'Ally Demo',
    headlineAccent: 'Python.',
    description: 'A minimal CLI that emits structured error messages and demonstrates the full Ally pipeline — a11y-assist, a11y-lint, and a11y-ci working together.',
    primaryCta: { href: '#quick-start', label: 'Get started' },
    secondaryCta: { href: '#features', label: 'Learn more' },
    previews: [
      { label: 'Install', code: 'pip install -e .' },
      { label: 'Emit', code: 'demo-cli network-timeout --json-out error.json' },
      { label: 'Explain', code: 'a11y-assist explain --json error.json --profile lowvision' },
    ],
  },

  sections: [
    {
      kind: 'features',
      id: 'features',
      title: 'What This Demonstrates',
      subtitle: 'End-to-end Ally pipeline in a single repo.',
      features: [
        { title: 'Structured Errors', desc: 'Emits cli.error.v0.1 JSON on every failure — machine-readable ground truth alongside human-friendly output.' },
        { title: 'Five A11y Profiles', desc: 'Low vision, cognitive load, screen reader, dyslexia, and plain language — each transforms the same error differently.' },
        { title: 'Lint & Validate', desc: 'a11y-lint validates your error messages against the contract. a11y-ci gates your CI pipeline with scorecards.' },
        { title: 'Safe Commands Only', desc: 'a11y-assist only suggests commands marked SAFE (like --dry-run). Never escalates privilege or mutates state.' },
        { title: 'Copy-Paste Adoption', desc: 'Designed as a template — adopt the Ally pipeline in your own CLI in under 10 minutes.' },
        { title: 'Intentionally Boring', desc: 'No magic, no frameworks. Just a reference integration that shows exactly what "good" looks like.' },
      ],
    },
    {
      kind: 'code-cards',
      id: 'quick-start',
      title: 'Quick Start',
      cards: [
        {
          title: 'Install & run',
          code: 'python -m venv .venv\nsource .venv/bin/activate\n\npip install -e .\npip install a11y-assist a11y-lint\n\ndemo-cli network-timeout --json-out /tmp/error.json',
        },
        {
          title: 'Explain with profiles',
          code: 'a11y-assist explain --json /tmp/error.json --profile lowvision\na11y-assist explain --json /tmp/error.json --profile cognitive-load\na11y-assist explain --json /tmp/error.json --profile screen-reader\na11y-assist explain --json /tmp/error.json --profile dyslexia\na11y-assist explain --json /tmp/error.json --profile plain-language',
        },
      ],
    },
    {
      kind: 'data-table',
      id: 'scenarios',
      title: 'Error Scenarios',
      subtitle: 'Built-in demo commands that emit structured errors.',
      columns: ['Command', 'Error ID', 'Description'],
      rows: [
        ['demo-cli network-timeout', 'DEMO.NETWORK.TIMEOUT', 'HTTP request timeout'],
        ['demo-cli config-missing', 'DEMO.CONFIG.MISSING', 'Missing config file'],
        ['demo-cli auth-failed', 'DEMO.AUTH.INVALID_TOKEN', 'Authentication failure'],
        ['demo-cli permission-denied', 'DEMO.FS.PERMISSION_DENIED', 'File permission error'],
        ['demo-cli validation-error', 'DEMO.VALIDATION.SCHEMA', 'Schema validation failure'],
      ],
    },
    {
      kind: 'code-cards',
      id: 'output',
      title: 'What "Good" Looks Like',
      cards: [
        {
          title: 'Human output',
          code: '[ERROR] Title (ID: DEMO.NETWORK.TIMEOUT)\n\nWhat:\n  Description of what happened.\n\nWhy:\n  Explanation of why it happened.\n\nFix:\n  Steps to resolve the issue.\n  Re-run: command --dry-run',
        },
        {
          title: 'Validate with lint',
          code: '# Validate message contract\na11y-lint validate /tmp/error.json\n\n# Gate CI with scorecards\na11y-ci gate',
        },
      ],
    },
    {
      kind: 'data-table',
      id: 'adopt',
      title: 'Adopt Ally in 10 Minutes',
      subtitle: 'Four steps to accessible error messages in your CLI.',
      columns: ['Step', 'Action'],
      rows: [
        ['1', 'Emit cli.error.v0.1 JSON on failure (machine output)'],
        ['2', 'Print the same content in a predictable text structure (human output)'],
        ['3', 'Add CI: a11y-lint validate + a11y-ci gate for scorecards'],
        ['4', 'Tell users: a11y-assist explain --json <file>'],
      ],
    },
  ],
};
