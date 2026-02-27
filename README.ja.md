<p align="center">
  <a href="README.md">English</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/ally-demo-python/readme.png" alt="Ally Demo Python" width="400">
</p>

<p align="center">
  <a href="https://github.com/mcp-tool-shop-org/ally-demo-python/actions/workflows/ci.yml"><img src="https://github.com/mcp-tool-shop-org/ally-demo-python/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="https://codecov.io/gh/mcp-tool-shop-org/ally-demo-python"><img src="https://codecov.io/gh/mcp-tool-shop-org/ally-demo-python/branch/main/graph/badge.svg" alt="codecov"></a>
  <a href="https://pypi.org/project/ally-demo-python/"><img src="https://img.shields.io/pypi/v/ally-demo-python" alt="PyPI"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow" alt="MIT License"></a>
  <a href="https://mcp-tool-shop-org.github.io/ally-demo-python/"><img src="https://img.shields.io/badge/Landing_Page-live-blue" alt="Landing Page"></a>
</p>

これは、**cli.error.v0.1** (真の値) を出力し、Allyのパイプライン全体を実証する、最小限のPython CLIです。

- `a11y-assist` (プロファイル: 低視力、認知負荷、スクリーンリーダー、ディスレクシア、平易な表現)
- `a11y-lint` (検証 + スキャン)
- `a11y-ci` (ゲート)

このリポジトリは、意図的に小さく、シンプルな構成になっています。これは、参照となる統合例です。

## クイックスタート

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -e .
pip install a11y-assist a11y-lint
```

構造化されたJSONを出力するコマンドを実行します。

```bash
demo-cli network-timeout --json-out /tmp/cli_error.json || true
```

異なるプロファイルを使用して、同じエラーを説明します。

```bash
a11y-assist explain --json /tmp/cli_error.json --profile lowvision
a11y-assist explain --json /tmp/cli_error.json --profile cognitive-load
a11y-assist explain --json /tmp/cli_error.json --profile screen-reader
a11y-assist explain --json /tmp/cli_error.json --profile dyslexia
a11y-assist explain --json /tmp/cli_error.json --profile plain-language
```

メッセージのスキーマを検証します。

```bash
a11y-lint validate /tmp/cli_error.json
```

## 利用可能なエラーシナリオ

このデモCLIには、さまざまなパターンを示すためのいくつかのエラーシナリオが含まれています。

| コマンド | エラーID | 説明 |
|---------|----------|-------------|
| `demo-cli network-timeout` | DEMO.NETWORK.TIMEOUT | HTTPリクエストのタイムアウト |
| `demo-cli config-missing` | DEMO.CONFIG.MISSING | 設定ファイルが見つかりません |
| `demo-cli auth-failed` | DEMO.AUTH.INVALID_TOKEN | 認証エラー |
| `demo-cli permission-denied` | DEMO.FS.PERMISSION_DENIED | ファイルアクセス権限エラー |
| `demo-cli validation-error` | DEMO.VALIDATION.SCHEMA | スキーマ検証エラー |

各コマンドは、以下の動作を行います。
- 人間が読める出力を標準出力に出力します。
- JSONを、指定された`--json-out`パスに書き込みます。
- JSONを標準エラー出力に出力し、機械による処理を可能にします。

## 「良い」状態とは

CLIは、予測可能な構造で人間が読めるメッセージを出力します。

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

CLIは、機械による処理のために、有効な`cli.error.v0.1` JSONも出力します。

- `a11y-assist`は、元の出力を書き換えることはなく、ASSISTブロックを追加します。
- SAFEのみのコマンドは、入力に存在する場合にのみ提案されます。

## 設計に関する注意点

このデモでは、意図的に以下の内容を出力します。

- 安定したIDネームスペース (DEMO.*)
- `--dry-run`を含む「再実行」コマンドを含む行を修正します (SAFE)。

これにより、パイプライン全体をエンドツーエンドで簡単にテストできます。

## Allyを10分で導入する (ツール開発者向け)

1. エラー発生時に`cli.error.v0.1` JSONを出力します (機械出力)。
2. 同じ内容を、予測可能なテキスト構造で出力します (人間出力)。
3. CIを設定します。
- `a11y-lint validate <message.json>`
- テキスト出力を検証する場合は、`a11y-ci gate`でスコアカードを作成します。
4. ユーザーに伝える内容:
- `a11y-assist explain --json <file>`
- または、ラッパーを使用: `assist-run <command>`の後に`a11y-assist last`

## セキュリティとプライバシー

**アクセスするデータ:** デモンストレーション用のエラーシナリオのみ。オプションの`--json-out`ファイル出力以外の実際のデータは読み込まれたり書き込まれたりしません。

**アクセスしないデータ:** ユーザーの認証情報、システムファイル、ネットワーク接続 (すべてのエラーはシミュレーション)。テレメトリは収集も送信もされません。

**権限:** ユーザーが指定した`--json-out`パスへのファイルシステムへの書き込みのみ。詳細については、[SECURITY.md](SECURITY.md)を参照してください。

## ライセンス

MIT

---

作成者: <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a>
