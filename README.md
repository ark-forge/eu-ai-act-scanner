# EU AI Act Scanner

[![PyPI version](https://img.shields.io/pypi/v/eu-ai-act-scanner.svg)](https://pypi.org/project/eu-ai-act-scanner/)
[![npm version](https://img.shields.io/npm/v/eu-ai-act-scanner.svg)](https://www.npmjs.com/package/eu-ai-act-scanner)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

**Scan your codebase for AI framework usage and check EU AI Act + GDPR compliance in seconds.**

Zero dependencies. Works offline. Detects 26 AI frameworks including OpenAI, Anthropic, LangChain, HuggingFace, and more.

## Quick Start

```bash
pip install eu-ai-act-scanner
eu-ai-act-scanner scan ./my-project
```

Or with npx (no install):

```bash
npx eu-ai-act-scanner scan ./my-project
```

## What It Does

1. **Scans** your project for AI framework usage (imports, dependencies, model references)
2. **Maps** each framework to its EU AI Act risk level and obligations
3. **Checks** your compliance documentation against requirements
4. **Reports** what's missing with actionable fix instructions

## Example Output

```
EU AI Act Scanner v0.1.0
Scan your project for AI framework usage and EU AI Act / GDPR compliance

Scanning: ./my-ai-app

Scan Results
  Files scanned: 47
  AI files found: 3

  Detected Frameworks:
    openai (2 files)
    langchain (1 file)

  Risk Assessment:
    [HIGH] openai: Art. 51-53 (GPAI obligations)
           Document OpenAI model usage, register as GPAI deployer...
    [MEDIUM] langchain: Art. 50 (transparency), Art. 6 + Annex III
           Audit your LangChain pipeline for chained AI models...

  Compliance: 1/3 (33.3%) for limited-risk

    PASS transparency
    FAIL user_disclosure
         Clearly inform users that AI is involved in the system
         Art. 52(1) - Natural persons must be notified of AI interaction
           - Add an 'AI Disclosure' section to your README.md
           - Include: which AI models are used, what they do, what data they process
    FAIL content_marking
         Mark AI-generated content so users can distinguish it from human content
         Art. 52(3) - AI-generated text/image/audio/video must be labeled
           - Add metadata or visible label to AI-generated outputs
```

## Supported Frameworks (26)

| Provider | Frameworks | Risk Level |
|----------|-----------|------------|
| **GPAI Providers** | OpenAI, Anthropic, Gemini, Mistral, Cohere, DeepSeek, Vertex AI, AWS Bedrock, Azure OpenAI, ZhipuAI, Qwen, Moonshot | High |
| **Orchestration** | LangChain, LlamaIndex, LiteLLM, CrewAI, AutoGen, Semantic Kernel, Haystack, DSPy, Groq, Replicate, Ollama | Medium |
| **ML Infrastructure** | HuggingFace, TensorFlow, PyTorch | Low (use-case dependent) |

## Usage

### Basic Scan

```bash
# Scan current directory
eu-ai-act-scanner scan

# Scan a specific project
eu-ai-act-scanner scan ./path/to/project

# Scan with explicit risk category
eu-ai-act-scanner scan ./project --risk high
```

### GDPR Scan

```bash
# Include GDPR compliance check
eu-ai-act-scanner scan ./project --gdpr
```

### JSON Output

```bash
# Full report as JSON (for CI/CD integration)
eu-ai-act-scanner scan ./project --json
```

### Python API

```python
from eu_ai_act_scanner import EUAIActScanner, GDPRScanner

# EU AI Act scan
scanner = EUAIActScanner("./my-project")
results = scanner.scan()
print(f"Found: {list(results['detected_models'].keys())}")

# Compliance check
compliance = scanner.check_compliance("limited")
print(f"Score: {compliance['compliance_score']}")

# GDPR scan
gdpr = GDPRScanner("./my-project")
gdpr_results = gdpr.scan()
print(f"Personal data: {gdpr_results['processing_summary']['processes_personal_data']}")
```

## CI/CD Integration

Add to your GitHub Actions workflow:

```yaml
- name: EU AI Act Compliance Check
  run: |
    pip install eu-ai-act-scanner
    eu-ai-act-scanner scan . --json > compliance-report.json
```

## How Risk Levels Work

The EU AI Act classifies AI systems into 4 risk categories:

- **Unacceptable**: Banned (social scoring, mass biometric surveillance)
- **High**: Strict requirements (recruitment, credit scoring, medical devices)
- **Limited**: Transparency obligations (chatbots, content generation)
- **Minimal**: No specific obligations (spam filters, games)

This scanner detects which frameworks you use and maps them to their default risk level. Your actual risk category depends on your specific use case — the scanner suggests a starting point.

## Contributing

Issues and PRs welcome at [github.com/ark-forge/eu-ai-act-scanner](https://github.com/ark-forge/eu-ai-act-scanner).

## License

MIT

