# eu-ai-act-scanner

Scan your project for AI framework usage and check EU AI Act compliance. Detects **26 AI frameworks** in source code and dependency files.

This is the npm wrapper for the Python-based scanner. It auto-installs the Python package on first run.

## Quick start

```bash
npx eu-ai-act-scanner scan ./my-project
```

## Requirements

- Node.js 16+
- Python 3.9+ (auto-detected)

## Commands

```bash
npx eu-ai-act-scanner scan ./my-project          # Detect AI frameworks
npx eu-ai-act-scanner check ./my-project --risk limited  # Check compliance
npx eu-ai-act-scanner report ./my-project --json  # Full report
npx eu-ai-act-scanner suggest --use-case "chatbot"  # Suggest risk category
```

## Prefer Python?

```bash
pip install eu-ai-act-scanner
eu-ai-act-scanner scan ./my-project
```

## License

MIT
