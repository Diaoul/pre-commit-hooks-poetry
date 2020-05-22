# pre-commit-hooks-poetry
My personnal poetry-related pre-commit hooks

## poetry-export
Prevent desync between poetry and `requirements.txt`.

Usage:
```yaml
  - repo: https://github.com/Diaoul/pre-commit-hooks-poetry
    rev: 0.3.0
    hooks:
      - id: poetry-export
```

All arguments to the [`poetry export` command](https://python-poetry.org/docs/cli/#export) are valid:
```yaml
  - repo: https://github.com/Diaoul/pre-commit-hooks-poetry
    rev: 0.3.0
    hooks:
      - id: poetry-export
        args: ["--without-hashes"]
```

For a another file:
```yaml
  - repo: https://github.com/Diaoul/pre-commit-hooks-poetry
    rev: 0.3.0
    hooks:
      - id: poetry-export
        args: ["--dev"]
        files: ^dev-requirements\.txt$
```
