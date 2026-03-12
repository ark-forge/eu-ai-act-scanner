# Contributing to eu-ai-act-scanner

## Before you start

Open an issue first for non-trivial changes. For typos and small fixes, a PR directly is fine.

## Branching

- `main` is protected — no direct push
- Branch from `main`: `feat/your-feature` or `fix/your-fix`
- Open a PR against `main`

## Development setup

```bash
git clone https://github.com/ark-forge/eu-ai-act-scanner.git
cd eu-ai-act-scanner
pip install -e ".[dev]"
```

## Running the scanner

```bash
python -m eu_ai_act_scanner scan ./your-project
# or
npx eu-ai-act-scanner scan ./your-project
```

## Running tests

```bash
pytest tests/ -q
```

## Pull request checklist

- [ ] Tests pass locally
- [ ] README updated if behavior changed
- [ ] CHANGELOG entry added under `[Unreleased]`

## What we accept

- Bug fixes
- New AI framework detections (currently 26 supported)
- New EU AI Act / GDPR compliance rules
- CLI improvements

## What requires an issue first

- Changes to the output format
- Breaking CLI interface changes
- New required dependencies

## Questions

Open an issue or reach out at [arkforge.tech](https://arkforge.tech).
