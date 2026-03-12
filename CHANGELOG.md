# Changelog

All notable changes to this project will be documented here.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.0.0/)
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

---

## [Unreleased]

---

## [0.1.2] — 2026-03-12

### Added
- Hosted MCP scanner CTA displayed after CLI scan output
- MCP server section in README with setup instructions for Claude, Cursor, Windsurf
- Star badge and PATH troubleshooting section in README

### Fixed
- Removed non-existent `suggest` and `check` subcommands from CI workflow

---

## [0.1.1] — 2025-12-01

### Added
- Detection of 26 AI frameworks across GPAI providers, orchestration layers, and ML infrastructure
- EU AI Act risk mapping per framework (high / medium / low)
- GDPR compliance scan (`--gdpr` flag) with personal data detection
- JSON output mode (`--json`) for CI/CD integration
- Python API (`EUAIActScanner`, `GDPRScanner`)
- npx support via npm package
- Actionable remediation guidance per compliance check (what / why / how)
- Risk category auto-suggestion based on detected frameworks
- `--scan-only` flag to skip compliance check and only detect frameworks
- `--risk` flag to override the suggested risk category

### Frameworks detected
- **GPAI providers (High risk)**: OpenAI, Anthropic, Gemini, Mistral, Cohere, DeepSeek, Vertex AI, AWS Bedrock, Azure OpenAI, ZhipuAI, Qwen, Moonshot
- **Orchestration (Medium risk)**: LangChain, LlamaIndex, LiteLLM, CrewAI, AutoGen, Semantic Kernel, Haystack, DSPy, Groq, Replicate, Ollama
- **ML infrastructure (Low risk)**: HuggingFace, TensorFlow, PyTorch

### EU AI Act articles covered
- Art. 5 (Prohibited practices)
- Art. 6 + Annex III (High-risk classification)
- Art. 9 (Risk management)
- Art. 10 (Data governance)
- Art. 11 (Technical documentation)
- Art. 14 (Human oversight)
- Art. 15 (Robustness and cybersecurity)
- Art. 50 / 51-53 (GPAI and transparency obligations)

---

## [0.1.0] — 2025-11-01

### Added
- Initial release
- Zero-dependency project scanner (Python 3.9+)
- Detection of AI framework imports and dependencies across `.py`, `.js`, `.ts`, and other source files
- EU AI Act risk level mapping for common GPAI frameworks
- Basic compliance checklist output

---

[Unreleased]: https://github.com/ark-forge/eu-ai-act-scanner/compare/v0.1.2...HEAD
[0.1.2]: https://github.com/ark-forge/eu-ai-act-scanner/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/ark-forge/eu-ai-act-scanner/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/ark-forge/eu-ai-act-scanner/releases/tag/v0.1.0
