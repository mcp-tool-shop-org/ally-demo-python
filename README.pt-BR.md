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

Uma interface de linha de comando (CLI) em Python, minimalista, que emite `cli.error.v0.1` (dados de referência) e demonstra todo o pipeline do Ally:

- `a11y-assist` (perfis: baixa visão, carga cognitiva, leitor de tela, dislexia, linguagem simples)
- `a11y-lint` (validação + análise)
- `a11y-ci` (controle de qualidade)

Este repositório é intencionalmente pequeno e simples. É uma integração de referência.

## Início rápido

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -e .
pip install a11y-assist a11y-lint
```

Execute um comando que falhe e que emita JSON estruturado:

```bash
demo-cli network-timeout --json-out /tmp/cli_error.json || true
```

Explique o mesmo erro usando diferentes perfis:

```bash
a11y-assist explain --json /tmp/cli_error.json --profile lowvision
a11y-assist explain --json /tmp/cli_error.json --profile cognitive-load
a11y-assist explain --json /tmp/cli_error.json --profile screen-reader
a11y-assist explain --json /tmp/cli_error.json --profile dyslexia
a11y-assist explain --json /tmp/cli_error.json --profile plain-language
```

Valide o contrato da mensagem:

```bash
a11y-lint validate /tmp/cli_error.json
```

## Cenários de erro disponíveis

A CLI de demonstração inclui vários cenários de erro para demonstrar diferentes padrões:

| Comando | ID do erro | Descrição |
| --------- | ---------- | ------------- |
| `demo-cli network-timeout` | DEMO.NETWORK.TIMEOUT | Tempo limite da requisição HTTP |
| `demo-cli config-missing` | DEMO.CONFIG.MISSING | Arquivo de configuração ausente |
| `demo-cli auth-failed` | DEMO.AUTH.INVALID_TOKEN | Falha na autenticação |
| `demo-cli permission-denied` | DEMO.FS.PERMISSION_DENIED | Erro de permissão de arquivo |
| `demo-cli validation-error` | DEMO.VALIDATION.SCHEMA | Falha na validação do esquema |

Cada comando:
- Imprime uma saída legível para o terminal (stdout)
- Escreve JSON no caminho especificado com `--json-out`
- Emite JSON para o fluxo de erro padrão (stderr) para captura por máquinas

## Como deve ser

A CLI imprime uma mensagem legível em uma estrutura previsível:

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

A CLI também emite JSON `cli.error.v0.1` válido para captura por máquinas.

- `a11y-assist` nunca reescreve a saída original; ele adiciona um bloco ASSIST.
- Apenas comandos "SAFE" são sugeridos (e apenas quando presentes na entrada).

## Notas de design

Esta demonstração emite intencionalmente:

- Um namespace `id` estável (DEMO.*)
- Linhas de correção que incluem um comando "Re-run:" contendo `--dry-run` (SAFE)

Isso facilita o teste de todo o pipeline de ponta a ponta.

## Adote o Ally em 10 minutos (para autores de ferramentas)

1. Emita JSON `cli.error.v0.1` em caso de falha (saída para máquinas)
2. Imprima o mesmo conteúdo em uma estrutura de texto previsível (saída para humanos)
3. Adicione o controle de qualidade (CI):
- `a11y-lint validate <message.json>`
- `a11y-ci gate` para "scorecards" se você validar a saída de texto
4. Informe aos usuários:
- `a11y-assist explain --json <file>`
- ou use um wrapper: `assist-run <comando>` e depois `a11y-assist last`

## Licença

MIT
