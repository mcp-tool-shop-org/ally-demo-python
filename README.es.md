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

Una herramienta de línea de comandos (CLI) de Python minimalista que emite `cli.error.v0.1` (datos de referencia) y demuestra todo el flujo de trabajo de Ally:

- `a11y-assist` (perfiles: baja visión, carga cognitiva, lector de pantalla, dislexia, lenguaje sencillo)
- `a11y-lint` (validación + análisis)
- `a11y-ci` (control de calidad)

Este repositorio es intencionalmente pequeño y sencillo. Es una integración de referencia.

## Guía de inicio rápido

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -e .
pip install a11y-assist a11y-lint
```

Ejecute un comando que falle y que emita JSON estructurado:

```bash
demo-cli network-timeout --json-out /tmp/cli_error.json || true
```

Explique el mismo error utilizando diferentes perfiles:

```bash
a11y-assist explain --json /tmp/cli_error.json --profile lowvision
a11y-assist explain --json /tmp/cli_error.json --profile cognitive-load
a11y-assist explain --json /tmp/cli_error.json --profile screen-reader
a11y-assist explain --json /tmp/cli_error.json --profile dyslexia
a11y-assist explain --json /tmp/cli_error.json --profile plain-language
```

Valide el contrato del mensaje:

```bash
a11y-lint validate /tmp/cli_error.json
```

## Escenarios de error disponibles

La CLI de demostración incluye varios escenarios de error para demostrar diferentes patrones:

| Comando | ID de error | Descripción |
| --------- | ---------- | ------------- |
| `demo-cli network-timeout` | DEMO.NETWORK.TIMEOUT | Tiempo de espera de la solicitud HTTP |
| `demo-cli config-missing` | DEMO.CONFIG.MISSING | Archivo de configuración faltante |
| `demo-cli auth-failed` | DEMO.AUTH.INVALID_TOKEN | Error de autenticación |
| `demo-cli permission-denied` | DEMO.FS.PERMISSION_DENIED | Error de permisos de archivo |
| `demo-cli validation-error` | DEMO.VALIDATION.SCHEMA | Error de validación del esquema |

Cada comando:
- Imprime una salida legible por humanos en la salida estándar (stdout).
- Escribe JSON en la ruta especificada con `--json-out`.
- Emite JSON a la salida de error estándar (stderr) para su procesamiento automático.

## ¿Cómo se ve "lo bueno"?

La CLI imprime un mensaje legible por humanos con una estructura predecible:

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

La CLI también emite JSON `cli.error.v0.1` válido para su procesamiento automático.

- `a11y-assist` nunca reescribe la salida original; agrega un bloque ASSIST.
- Se sugieren comandos SOLO-SAFE (y solo cuando están presentes en la entrada).

## Notas de diseño

Esta demostración emite intencionalmente:

- Un espacio de nombres `id` estable (DEMO.*)
- Líneas que incluyen un comando "Re-run:" que contiene `--dry-run` (SAFE)

Esto facilita la prueba de todo el flujo de trabajo de extremo a extremo.

## Adopte Ally en 10 minutos (para autores de herramientas)

1. Emita JSON `cli.error.v0.1` en caso de error (salida para máquinas).
2. Imprima el mismo contenido en una estructura de texto predecible (salida para humanos).
3. Agregue CI:
- `a11y-lint validate <message.json>`
- `a11y-ci gate` para obtener puntuaciones si analiza la salida de texto.
4. Informe a los usuarios:
- `a11y-assist explain --json <file>`
- o primero con un envoltorio: `assist-run <command>` y luego `a11y-assist last`

## Licencia

MIT
