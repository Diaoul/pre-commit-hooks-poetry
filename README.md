# pre-commit-hooks-poetry
My personnal poetry-related pre-commit hooks

## poetry-export - DEPRECATED
Prevent desync between poetry and `requirements.txt`.

**DEPRECATION NOTICE:** See https://github.com/python-poetry/poetry/issues/2457
for better implementations.

Usage:
```yaml
  - repo: https://github.com/Diaoul/pre-commit-hooks-poetry
    rev: 0.5.0
    hooks:
      - id: poetry-export
```

All arguments to the [`poetry export` command](https://python-poetry.org/docs/cli/#export) are valid:
```yaml
  - repo: https://github.com/Diaoul/pre-commit-hooks-poetry
    rev: 0.5.0
    hooks:
      - id: poetry-export
        args: ["--without-hashes"]
```

For a another file:
```yaml
  - repo: https://github.com/Diaoul/pre-commit-hooks-poetry
    rev: 0.5.0
    hooks:
      - id: poetry-export
        args: ["--dev"]
        files: ^dev-requirements\.txt$
```
