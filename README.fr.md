<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.fr.md">Français</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/mcp-tool-shop-org/ally-demo-python/main/assets/logo-ally-demo-python.png" alt="Ally Demo Python" width="400">
</p>

<p align="center">
  <a href="https://github.com/mcp-tool-shop-org/ally-demo-python/actions/workflows/ci.yml"><img src="https://github.com/mcp-tool-shop-org/ally-demo-python/actions/workflows/ci.yml/badge.svg" alt="CI"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow" alt="MIT License"></a>
  <a href="https://mcp-tool-shop-org.github.io/ally-demo-python/"><img src="https://img.shields.io/badge/Landing_Page-live-blue" alt="Landing Page"></a>
</p>

Une interface en ligne de commande (CLI) Python minimaliste qui génère `cli.error.v0.1` (données de référence) et qui illustre l'ensemble du pipeline Ally :

- `a11y-assist` (profils : basse vision, charge cognitive, lecteurs d'écran, dyslexie, langage clair)
- `a11y-lint` (validation + analyse)
- `a11y-ci` (contrôle)

Ce dépôt est intentionnellement petit et simple. Il s'agit d'une intégration de référence.

## Démarrage rapide

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate

pip install -e .
pip install a11y-assist a11y-lint
```

Exécutez une commande qui échoue et qui génère un JSON structuré :

```bash
demo-cli network-timeout --json-out /tmp/cli_error.json || true
```

Expliquez la même erreur en utilisant différents profils :

```bash
a11y-assist explain --json /tmp/cli_error.json --profile lowvision
a11y-assist explain --json /tmp/cli_error.json --profile cognitive-load
a11y-assist explain --json /tmp/cli_error.json --profile screen-reader
a11y-assist explain --json /tmp/cli_error.json --profile dyslexia
a11y-assist explain --json /tmp/cli_error.json --profile plain-language
```

Validez le contrat de message :

```bash
a11y-lint validate /tmp/cli_error.json
```

## Scénarios d'erreur disponibles

La CLI de démonstration comprend plusieurs scénarios d'erreur pour illustrer différents modèles :

| Commande | ID de l'erreur | Description |
| --------- | ---------- | ------------- |
| `demo-cli network-timeout` | DEMO.NETWORK.TIMEOUT | Dépassement du délai de la requête HTTP |
| `demo-cli config-missing` | DEMO.CONFIG.MISSING | Fichier de configuration manquant |
| `demo-cli auth-failed` | DEMO.AUTH.INVALID_TOKEN | Échec d'authentification |
| `demo-cli permission-denied` | DEMO.FS.PERMISSION_DENIED | Erreur de permission d'accès au fichier |
| `demo-cli validation-error` | DEMO.VALIDATION.SCHEMA | Échec de la validation du schéma |

Chaque commande :
- Affiche une sortie lisible par l'utilisateur sur la sortie standard (stdout)
- Écrit le JSON dans le chemin spécifié par `--json-out`
- Génère du JSON sur la sortie d'erreur standard (stderr) pour la capture par les machines

## À quoi ressemble une bonne sortie

La CLI affiche un message lisible par l'utilisateur dans une structure prévisible :

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

La CLI génère également un JSON `cli.error.v0.1` valide pour la capture par les machines.

- `a11y-assist` ne modifie jamais la sortie originale ; il ajoute un bloc ASSIST.
- Seules les commandes SAFE sont suggérées (et uniquement lorsqu'elles sont présentes dans l'entrée).

## Notes de conception

Cette démonstration génère intentionnellement :

- Un espace de noms `id` stable (DEMO.*)
- Des lignes de correction qui incluent une commande "Réexécuter :" contenant `--dry-run` (SAFE)

Cela facilite le test de l'ensemble du pipeline de bout en bout.

## Adoptez Ally en 10 minutes (pour les auteurs d'outils)

1. Générez un JSON `cli.error.v0.1` en cas d'échec (sortie pour les machines)
2. Affichez le même contenu dans une structure de texte prévisible (sortie pour les humains)
3. Ajoutez l'intégration continue (CI) :
- `a11y-lint validate <message.json>`
- `a11y-ci gate` pour les tableaux de bord si vous analysez la sortie textuelle
4. Informez les utilisateurs :
- `a11y-assist explain --json <file>`
- ou utilisez un wrapper : `assist-run <command>` puis `a11y-assist last`

## Licence

MIT
