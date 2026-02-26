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

Una CLI Python minimale che emette `cli.error.v0.1` (dati di riferimento) e dimostra l'intero flusso di lavoro di Ally:

- `a11y-assist` (profili: bassa visione, carico cognitivo, screen reader, dislessia, linguaggio semplice)
- `a11y-lint` (valida e analizza)
- `a11y-ci` (verifica)

Questo repository è volutamente piccolo e semplice. È un esempio di integrazione.

## Guida rapida

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -e .
pip install a11y-assist a11y-lint
```

Esegui un comando che genera un errore e produce un output JSON strutturato:

```bash
demo-cli network-timeout --json-out /tmp/cli_error.json || true
```

Spiega lo stesso errore utilizzando profili diversi:

```bash
a11y-assist explain --json /tmp/cli_error.json --profile lowvision
a11y-assist explain --json /tmp/cli_error.json --profile cognitive-load
a11y-assist explain --json /tmp/cli_error.json --profile screen-reader
a11y-assist explain --json /tmp/cli_error.json --profile dyslexia
a11y-assist explain --json /tmp/cli_error.json --profile plain-language
```

Verifica la struttura del messaggio:

```bash
a11y-lint validate /tmp/cli_error.json
```

## Scenari di errore disponibili

La CLI di esempio include diversi scenari di errore per dimostrare diversi modelli:

| Comando | ID dell'errore | Descrizione |
| --------- | ---------- | ------------- |
| `demo-cli network-timeout` | DEMO.NETWORK.TIMEOUT | Timeout della richiesta HTTP |
| `demo-cli config-missing` | DEMO.CONFIG.MISSING | File di configurazione mancante |
| `demo-cli auth-failed` | DEMO.AUTH.INVALID_TOKEN | Errore di autenticazione |
| `demo-cli permission-denied` | DEMO.FS.PERMISSION_DENIED | Errore di permesso del file |
| `demo-cli validation-error` | DEMO.VALIDATION.SCHEMA | Errore di validazione dello schema |

Ogni comando:
- Stampa un output leggibile da umano sull'output standard (stdout)
- Scrive il JSON nel percorso specificato con `--json-out`
- Emette il JSON sull'output di errore standard (stderr) per la cattura automatica

## Come dovrebbe apparire un output "corretto"

La CLI stampa un messaggio leggibile da umano con una struttura prevedibile:

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

La CLI emette anche un JSON `cli.error.v0.1` valido per la cattura automatica.

- `a11y-assist` non sovrascrive mai l'output originale; aggiunge un blocco ASSIST.
- Vengono suggeriti solo comandi SAFE (e solo quando presenti nell'input).

## Note sulla progettazione

Questa demo emette intenzionalmente:

- Un namespace `id` stabile (DEMO.*)
- Righe che includono un comando "Riprova:" contenente `--dry-run` (SAFE)

Questo semplifica il test dell'intero flusso di lavoro end-to-end.

## Integra Ally in 10 minuti (per gli autori di strumenti)

1. Emetti JSON `cli.error.v0.1` in caso di errore (output per macchine)
2. Stampa lo stesso contenuto con una struttura di testo prevedibile (output per umani)
3. Aggiungi CI:
- `a11y-lint validate <message.json>`
- `a11y-ci gate` per i report se analizzi l'output di testo
4. Informa gli utenti:
- `a11y-assist explain --json <file>`
- oppure usa un wrapper: `assist-run <comando>` quindi `a11y-assist last`

## Licenza

MIT
