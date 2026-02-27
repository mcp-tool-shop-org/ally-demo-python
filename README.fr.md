<p align="center">
  <a href="README.ja.md">日本語</a> | <a href="README.zh.md">中文</a> | <a href="README.es.md">Español</a> | <a href="README.md">English</a> | <a href="README.hi.md">हिन्दी</a> | <a href="README.it.md">Italiano</a> | <a href="README.pt-BR.md">Português (BR)</a>
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
|---------|----------|-------------|
| `demo-cli network-timeout` | DEMO.NETWORK.TIMEOUT | Dépassement du délai de la requête HTTP |
| `demo-cli config-missing` | DEMO.CONFIG.MISSING | Fichier de configuration manquant |
| `demo-cli auth-failed` | DEMO.AUTH.INVALID_TOKEN | Échec de l'authentification |
| `demo-cli permission-denied` | DEMO.FS.PERMISSION_DENIED | Erreur de permission d'accès au fichier |
| `demo-cli validation-error` | DEMO.VALIDATION.SCHEMA | Échec de la validation du schéma |

Chaque commande :
- Affiche un résultat lisible par l'utilisateur sur la sortie standard (stdout)
- Écrit un fichier JSON au chemin spécifié avec l'option `--json-out`
- Génère un JSON sur la sortie d'erreur standard (stderr) pour la capture par les machines

## À quoi ressemble une bonne solution

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
- Des lignes qui incluent une commande "Re-run :" contenant `--dry-run` (SAFE)

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

## Sécurité et confidentialité

**Données traitées :** uniquement des scénarios d'erreur de démonstration. Aucune donnée réelle n'est lue ou écrite, à l'exception de la sortie facultative du fichier JSON via l'option `--json-out`.

**Données NON traitées :** aucune information d'identification utilisateur, aucun fichier système, aucun appel réseau (toutes les erreurs sont simulées). Aucune télémétrie n'est collectée ou envoyée.

**Permissions :** uniquement l'écriture sur le système de fichiers pour le chemin spécifié par l'utilisateur via l'option `--json-out`. Consultez le fichier [SECURITY.md](SECURITY.md) pour connaître la politique complète.

## Licence

MIT

---

Créé par <a href="https://mcp-tool-shop.github.io/">MCP Tool Shop</a>
