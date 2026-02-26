<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
</p>

<p align="center">
  
            <img src="https://raw.githubusercontent.com/mcp-tool-shop-org/brand/main/logos/ally-demo-python/readme.png"
           alt="Ally Demo Python" width="400">
</p>

<p align="center">
  <a href="https://github.com/mcp-tool-shop-org/ally-demo-python/actions/workflows/ci.yml"><img src="https://github.com/mcp-tool-shop-org/ally-demo-python/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow" alt="MIT License"></a>
  <a href="https://mcp-tool-shop-org.github.io/ally-demo-python/"><img src="https://img.shields.io/badge/Landing_Page-live-blue" alt="Landing Page"></a>
</p>

これは、**cli.error.v0.1** (真の値) を出力し、Allyのパイプライン全体を示す、最小限のPythonコマンドラインインターフェース（CLI）です。

- `a11y-assist` (プロファイル: 低視力、認知負荷、スクリーンリーダー、ディスレクシア、平易な表現)
- `a11y-lint` (検証 + スキャン)
- `a11y-ci` (ゲート)

このリポジトリは、意図的に小さく、シンプルな構成になっています。これは、参照となる統合事例です。

## クイックスタート

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -e .
pip install a11y-assist a11y-lint
```

構造化されたJSONを出力するエラーを発生させるコマンドを実行します。

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

メッセージの構造を検証します。

```bash
a11y-lint validate /tmp/cli_error.json
```

## 利用可能なエラーシナリオ

このデモCLIには、さまざまなパターンを示すためのいくつかのエラーシナリオが含まれています。

| コマンド | エラーID | 説明 |
| --------- | ---------- | ------------- |
| `demo-cli network-timeout` | DEMO.NETWORK.TIMEOUT | HTTPリクエストのタイムアウト |
| `demo-cli config-missing` | DEMO.CONFIG.MISSING | 設定ファイルが見つかりません |
| `demo-cli auth-failed` | DEMO.AUTH.INVALID_TOKEN | 認証エラー |
| `demo-cli permission-denied` | DEMO.FS.PERMISSION_DENIED | ファイルアクセス権限エラー |
| `demo-cli validation-error` | DEMO.VALIDATION.SCHEMA | スキーマ検証エラー |

各コマンドは、以下の動作を行います。
- 標準出力に人間が読める形式で結果を出力します。
- 指定された`--json-out`パスにJSONファイルを書き込みます。
- マシンが解析できるように、JSONを標準エラー出力に送信します。

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

CLIは、マシンが解析できるように、有効な`cli.error.v0.1`形式のJSONも出力します。

- `a11y-assist`は、元の出力を書き換えることはありません。代わりに、ASSISTブロックを追加します。
- SAFEのみのコマンドが推奨されます（入力に存在する場合のみ）。

## 設計に関する注意点

このデモでは、意図的に以下のものが出力されます。

- 安定した`id`ネームスペース（DEMO.*）
- `--dry-run`を含む「再実行」コマンドを含む行を修正します（SAFE）。

これにより、パイプライン全体をエンドツーエンドで簡単にテストできます。

## ツール開発者向け：Allyの導入（10分で）

1. エラー発生時に`cli.error.v0.1`形式のJSONを出力します（マシン向け出力）。
2. 同じ内容を、予測可能なテキスト形式で出力します（人間向け出力）。
3. CIを設定します。
- `a11y-lint validate <message.json>`
- テキスト出力を検証する場合は、`a11y-ci gate`でスコアカードを取得します。
4. ユーザーに以下のコマンドを伝えます。
- `a11y-assist explain --json <file>`
- または、ラッパーを使用: `assist-run <command>`の後に`a11y-assist last`

## ライセンス

MIT
