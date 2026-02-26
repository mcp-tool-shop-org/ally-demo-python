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

一个精简的 Python 命令行工具，它会输出 `cli.error.v0.1`（作为参考标准），并演示 Ally 的完整流水线。

- `a11y-assist`（支持以下特性：低视力、认知负荷、屏幕阅读器、阅读障碍、简洁语言）
- `a11y-lint`（验证 + 扫描）
- `a11y-ci`（质量门控）

这个仓库故意设计得非常小且简单。它是一个参考集成示例。

## 快速入门

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -e .
pip install a11y-assist a11y-lint
```

运行一个会产生结构化 JSON 输出的命令：

```bash
demo-cli network-timeout --json-out /tmp/cli_error.json || true
```

使用不同的配置来解释相同的错误：

```bash
a11y-assist explain --json /tmp/cli_error.json --profile lowvision
a11y-assist explain --json /tmp/cli_error.json --profile cognitive-load
a11y-assist explain --json /tmp/cli_error.json --profile screen-reader
a11y-assist explain --json /tmp/cli_error.json --profile dyslexia
a11y-assist explain --json /tmp/cli_error.json --profile plain-language
```

验证消息的结构：

```bash
a11y-lint validate /tmp/cli_error.json
```

## 可用的错误场景

这个演示命令行工具包含多个错误场景，用于演示不同的模式：

| 命令 | 错误 ID | 描述 |
| --------- | ---------- | ------------- |
| `demo-cli network-timeout` | DEMO.NETWORK.TIMEOUT | HTTP 请求超时 |
| `demo-cli config-missing` | DEMO.CONFIG.MISSING | 缺少配置文件 |
| `demo-cli auth-failed` | DEMO.AUTH.INVALID_TOKEN | 身份验证失败 |
| `demo-cli permission-denied` | DEMO.FS.PERMISSION_DENIED | 文件权限错误 |
| `demo-cli validation-error` | DEMO.VALIDATION.SCHEMA | 模式验证失败 |

每个命令：
- 将可读的输出打印到标准输出
- 将 JSON 写入指定的 `--json-out` 路径
- 将 JSON 输出到标准错误流，供机器解析

## “良好”的输出是什么样的

命令行工具会以可预测的结构打印一条可读的消息：

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

命令行工具还会输出有效的 `cli.error.v0.1` JSON，供机器解析。

- `a11y-assist` 不会重写原始输出，而是添加一个 ASSIST 块。
- 建议仅使用 SAFE 模式的命令（并且仅当输入中存在这些命令时）。

## 设计说明

这个演示故意输出：

- 一个稳定的 `id` 命名空间 (DEMO.*)
- 包含 `--dry-run` 的“重新运行”命令（SAFE 模式）

这使得可以轻松地对整个流水线进行端到端的测试。

## 10 分钟内集成 Ally（面向工具作者）

1. 在发生错误时输出 `cli.error.v0.1` JSON（机器输出）
2. 以可预测的文本结构打印相同的内容（人类输出）
3. 添加 CI：
- `a11y-lint validate <message.json>`
- `a11y-ci gate` 用于 scorecard，如果 lint 文本输出
4. 告知用户：
- `a11y-assist explain --json <file>`
- 或者先使用包装器：`assist-run <command>` 然后 `a11y-assist last`

## 许可证

MIT
