"""Compliance guidance, risk categories, and templates for EU AI Act and GDPR."""

_EUR_LEX_BASE = "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024R1689"
_ART_URL_BASE = "https://artificialintelligenceact.eu/article"

# Per-framework compliance metadata
FRAMEWORK_COMPLIANCE_INFO = {
    "openai": {
        "risk_level": "high",
        "article_reference": "Art. 51-53 (GPAI obligations)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/51/", f"{_ART_URL_BASE}/52/", f"{_ART_URL_BASE}/53/"],
        "remediation": "Document OpenAI model usage, register as GPAI deployer, and ensure transparency per Art. 53.",
    },
    "anthropic": {
        "risk_level": "high",
        "article_reference": "Art. 51-53 (GPAI obligations)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/51/", f"{_ART_URL_BASE}/52/", f"{_ART_URL_BASE}/53/"],
        "remediation": "Document Anthropic model usage, ensure GPAI transparency obligations and downstream risk assessment.",
    },
    "gemini": {
        "risk_level": "high",
        "article_reference": "Art. 51-53 (GPAI obligations)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/51/", f"{_ART_URL_BASE}/52/", f"{_ART_URL_BASE}/53/"],
        "remediation": "Document Gemini model usage and GPAI obligations; assess if system falls under Annex III high-risk.",
    },
    "vertex_ai": {
        "risk_level": "high",
        "article_reference": "Art. 51-53 (GPAI obligations)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/51/", f"{_ART_URL_BASE}/52/", f"{_ART_URL_BASE}/53/"],
        "remediation": "Document Vertex AI usage, ensure GPAI provider obligations are met and risk category assessed.",
    },
    "mistral": {
        "risk_level": "high",
        "article_reference": "Art. 51-53 (GPAI obligations)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/51/", f"{_ART_URL_BASE}/52/", f"{_ART_URL_BASE}/53/"],
        "remediation": "Document Mistral model usage and ensure GPAI transparency requirements per Art. 53.",
    },
    "cohere": {
        "risk_level": "high",
        "article_reference": "Art. 51-53 (GPAI obligations)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/51/", f"{_ART_URL_BASE}/52/", f"{_ART_URL_BASE}/53/"],
        "remediation": "Document Cohere model usage and comply with GPAI transparency and documentation obligations.",
    },
    "aws_bedrock": {
        "risk_level": "high",
        "article_reference": "Art. 51-53 (GPAI obligations), Art. 25 (distributor obligations)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/51/", f"{_ART_URL_BASE}/52/", f"{_ART_URL_BASE}/53/", f"{_ART_URL_BASE}/25/"],
        "remediation": "Document Bedrock model usage; as a platform deployer, verify GPAI provider compliance upstream.",
    },
    "azure_openai": {
        "risk_level": "high",
        "article_reference": "Art. 51-53 (GPAI obligations), Art. 25 (distributor obligations)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/51/", f"{_ART_URL_BASE}/52/", f"{_ART_URL_BASE}/53/", f"{_ART_URL_BASE}/25/"],
        "remediation": "Document Azure OpenAI usage; verify Microsoft's GPAI compliance and assess your deployment risk.",
    },
    "deepseek": {
        "risk_level": "high",
        "article_reference": "Art. 51-53 (GPAI obligations)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/51/", f"{_ART_URL_BASE}/52/", f"{_ART_URL_BASE}/53/"],
        "remediation": "Document DeepSeek model usage and ensure GPAI obligations are met for EU deployment.",
    },
    "zhipu": {
        "risk_level": "high",
        "article_reference": "Art. 51-53 (GPAI obligations)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/51/", f"{_ART_URL_BASE}/52/", f"{_ART_URL_BASE}/53/"],
        "remediation": "Document ZhipuAI/GLM usage; verify GPAI compliance for non-EU provider models deployed in EU.",
    },
    "qwen": {
        "risk_level": "high",
        "article_reference": "Art. 51-53 (GPAI obligations)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/51/", f"{_ART_URL_BASE}/52/", f"{_ART_URL_BASE}/53/"],
        "remediation": "Document Qwen/DashScope usage; ensure GPAI transparency for non-EU provider models in EU.",
    },
    "moonshot": {
        "risk_level": "high",
        "article_reference": "Art. 51-53 (GPAI obligations)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/51/", f"{_ART_URL_BASE}/52/", f"{_ART_URL_BASE}/53/"],
        "remediation": "Document Moonshot/Kimi model usage and meet GPAI obligations for EU deployment.",
    },
    "langchain": {
        "risk_level": "medium",
        "article_reference": "Art. 50 (transparency), Art. 6 + Annex III (if high-risk use)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/50/", f"{_ART_URL_BASE}/6/"],
        "remediation": "Audit your LangChain pipeline for chained AI models; document each model and assess combined risk.",
    },
    "llamaindex": {
        "risk_level": "medium",
        "article_reference": "Art. 50 (transparency), Art. 6 + Annex III (if high-risk use)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/50/", f"{_ART_URL_BASE}/6/"],
        "remediation": "Document LlamaIndex data pipeline and underlying models; assess if RAG system is high-risk.",
    },
    "litellm": {
        "risk_level": "medium",
        "article_reference": "Art. 50 (transparency), Art. 51-53 (GPAI via proxied models)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/50/", f"{_ART_URL_BASE}/51/", f"{_ART_URL_BASE}/52/", f"{_ART_URL_BASE}/53/"],
        "remediation": "Document all models routed through LiteLLM; each proxied GPAI model carries its own obligations.",
    },
    "crewai": {
        "risk_level": "medium",
        "article_reference": "Art. 50 (transparency), Art. 14 (human oversight for agent systems)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/50/", f"{_ART_URL_BASE}/14/"],
        "remediation": "Document CrewAI agent roles and ensure human oversight over autonomous agent decisions.",
    },
    "autogen": {
        "risk_level": "medium",
        "article_reference": "Art. 50 (transparency), Art. 14 (human oversight for agent systems)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/50/", f"{_ART_URL_BASE}/14/"],
        "remediation": "Document AutoGen agent pipeline; implement human-in-the-loop for consequential decisions.",
    },
    "semantic_kernel": {
        "risk_level": "medium",
        "article_reference": "Art. 50 (transparency), Art. 6 + Annex III (if high-risk use)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/50/", f"{_ART_URL_BASE}/6/"],
        "remediation": "Document Semantic Kernel plugins and AI services; assess combined system risk category.",
    },
    "haystack": {
        "risk_level": "medium",
        "article_reference": "Art. 50 (transparency), Art. 6 + Annex III (if high-risk use)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/50/", f"{_ART_URL_BASE}/6/"],
        "remediation": "Document Haystack pipeline components and underlying models; assess RAG system risk.",
    },
    "dspy": {
        "risk_level": "medium",
        "article_reference": "Art. 50 (transparency), Art. 9(2) (risk management for optimized prompts)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/50/", f"{_ART_URL_BASE}/9/"],
        "remediation": "Document DSPy optimization pipeline; auto-optimized prompts need auditability per Art. 9(2).",
    },
    "groq": {
        "risk_level": "medium",
        "article_reference": "Art. 51-53 (GPAI obligations via inference provider)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/51/", f"{_ART_URL_BASE}/52/", f"{_ART_URL_BASE}/53/"],
        "remediation": "Document Groq-hosted model usage; verify GPAI compliance for models accessed via Groq.",
    },
    "replicate": {
        "risk_level": "medium",
        "article_reference": "Art. 51-53 (GPAI obligations via model hosting)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/51/", f"{_ART_URL_BASE}/52/", f"{_ART_URL_BASE}/53/"],
        "remediation": "Document Replicate-hosted models; each model has its own GPAI obligations to verify.",
    },
    "ollama": {
        "risk_level": "medium",
        "article_reference": "Art. 50 (transparency), Art. 53 (GPAI model documentation)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/50/", f"{_ART_URL_BASE}/53/"],
        "remediation": "Document locally-hosted Ollama models; ensure model cards and GPAI documentation exist.",
    },
    "huggingface": {
        "risk_level": "low",
        "article_reference": "Art. 6 + Annex III (risk depends on application)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/6/"],
        "remediation": "Assess your HuggingFace model's use case against Annex III to determine risk category.",
    },
    "tensorflow": {
        "risk_level": "low",
        "article_reference": "Art. 6 + Annex III (risk depends on application)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/6/"],
        "remediation": "TensorFlow is infrastructure; assess your trained model's use case against Annex III.",
    },
    "pytorch": {
        "risk_level": "low",
        "article_reference": "Art. 6 + Annex III (risk depends on application)",
        "eur_lex_url": _EUR_LEX_BASE,
        "article_urls": [f"{_ART_URL_BASE}/6/"],
        "remediation": "PyTorch is infrastructure; assess your trained model's use case against Annex III.",
    },
}

RISK_CATEGORIES = {
    "unacceptable": {
        "description": "Prohibited systems (behavioral manipulation, social scoring, mass biometric surveillance)",
        "requirements": ["Prohibited system - Do not deploy"],
    },
    "high": {
        "description": "High-risk systems (recruitment, credit scoring, law enforcement)",
        "requirements": [
            "Complete technical documentation",
            "Risk management system",
            "Data quality and governance",
            "Transparency and user information",
            "Human oversight",
            "Robustness, accuracy and cybersecurity",
            "Quality management system",
            "Registration in EU database",
        ],
    },
    "limited": {
        "description": "Limited-risk systems (chatbots, deepfakes)",
        "requirements": [
            "Transparency obligations",
            "Clear user information about AI interaction",
            "AI-generated content marking",
        ],
    },
    "minimal": {
        "description": "Minimal-risk systems (spam filters, video games)",
        "requirements": [
            "No specific obligations",
            "Voluntary code of conduct encouraged",
        ],
    },
}

ACTIONABLE_GUIDANCE = {
    "technical_documentation": {
        "what": "Create technical documentation describing your AI system's architecture, training data, and intended use",
        "why": "Art. 11 - High-risk systems require complete technical documentation for conformity assessment",
        "how": [
            "Create docs/TECHNICAL_DOCUMENTATION.md",
            "Document: system architecture, training data sources, model performance metrics",
            "Document: intended purpose, foreseeable misuse, limitations",
            "Include version history and change log",
        ],
        "eu_article": "Art. 11",
        "effort": "high",
    },
    "risk_management": {
        "what": "Implement a risk management system covering the full AI lifecycle",
        "why": "Art. 9 - High-risk systems must have continuous risk identification and mitigation",
        "how": [
            "Create docs/RISK_MANAGEMENT.md",
            "Identify known and foreseeable risks to health, safety, fundamental rights",
            "Define risk mitigation measures for each identified risk",
            "Plan testing procedures to validate mitigation effectiveness",
        ],
        "eu_article": "Art. 9",
        "effort": "high",
    },
    "transparency": {
        "what": "Ensure users know they are interacting with an AI system",
        "why": "Art. 52 - Users must be informed when they interact with AI",
        "how": [
            "Add clear AI disclosure in README.md and user-facing interfaces",
            "For chatbots: display notice BEFORE first interaction",
            "For generated content: label outputs as AI-generated",
        ],
        "eu_article": "Art. 52",
        "effort": "low",
    },
    "user_disclosure": {
        "what": "Clearly inform users that AI is involved in the system",
        "why": "Art. 52(1) - Natural persons must be notified of AI interaction",
        "how": [
            "Add an 'AI Disclosure' section to your README.md",
            "Include: which AI models are used, what they do, what data they process",
            "For web apps: add AI disclosure in footer or about page",
        ],
        "eu_article": "Art. 52(1)",
        "effort": "low",
    },
    "content_marking": {
        "what": "Mark AI-generated content so users can distinguish it from human content",
        "why": "Art. 52(3) - AI-generated text/image/audio/video must be labeled",
        "how": [
            "Add metadata or visible label to AI-generated outputs",
            "For text: prepend '[AI-generated]' or add metadata field",
            "For images: embed C2PA metadata or visible watermark",
        ],
        "eu_article": "Art. 52(3)",
        "effort": "low",
    },
    "data_governance": {
        "what": "Document data quality, collection, and governance practices",
        "why": "Art. 10 - Training data must meet quality criteria and be documented",
        "how": [
            "Create docs/DATA_GOVERNANCE.md",
            "Document: data sources, collection methods, preprocessing steps",
            "Document: data quality metrics, bias assessment, representativeness",
        ],
        "eu_article": "Art. 10",
        "effort": "high",
    },
    "human_oversight": {
        "what": "Ensure humans can monitor, intervene, and override AI decisions",
        "why": "Art. 14 - High-risk systems must allow effective human oversight",
        "how": [
            "Create docs/HUMAN_OVERSIGHT.md",
            "Design: human-in-the-loop or human-on-the-loop mechanism",
            "Implement: override/stop button for AI decisions",
        ],
        "eu_article": "Art. 14",
        "effort": "medium",
    },
    "robustness": {
        "what": "Ensure AI system accuracy, robustness, and cybersecurity",
        "why": "Art. 15 - High-risk systems must be resilient and secure",
        "how": [
            "Create docs/ROBUSTNESS.md",
            "Test: accuracy metrics on representative datasets",
            "Test: adversarial robustness (prompt injection, data poisoning)",
        ],
        "eu_article": "Art. 15",
        "effort": "high",
    },
    "basic_documentation": {
        "what": "Create a README.md describing the project",
        "why": "Best practice for all AI systems, even minimal risk",
        "how": [
            "Create README.md with: project description, setup instructions, usage examples",
            "Mention any AI/ML components and their purpose",
        ],
        "eu_article": "Voluntary (Art. 69)",
        "effort": "low",
    },
}

RISK_CATEGORY_INDICATORS = {
    "unacceptable": {
        "keywords": ["social scoring", "social credit", "mass surveillance", "biometric identification real-time",
                     "subliminal manipulation", "exploit vulnerabilities", "emotion recognition workplace",
                     "emotion recognition education", "predictive policing individual"],
        "description": "Prohibited AI practices under Art. 5",
    },
    "high": {
        "keywords": ["recruitment", "hiring", "credit scoring", "credit assessment", "insurance pricing",
                     "law enforcement", "border control", "immigration", "asylum",
                     "education admission", "student assessment", "critical infrastructure",
                     "medical device", "medical diagnosis", "biometric", "facial recognition",
                     "justice", "court", "democratic process", "election",
                     "essential services", "emergency services", "safety component"],
        "description": "High-risk AI systems under Annex III",
    },
    "limited": {
        "keywords": ["chatbot", "chat bot", "conversational", "content generation", "text generation",
                     "image generation", "deepfake", "synthetic media", "recommendation",
                     "customer support bot", "virtual assistant", "ai assistant"],
        "description": "AI systems with transparency obligations under Art. 52",
    },
    "minimal": {
        "keywords": ["spam filter", "spam detection", "video game", "search optimization",
                     "inventory management", "autocomplete", "spell check", "translation"],
        "description": "Minimal-risk AI systems (voluntary code of conduct)",
    },
}

# GDPR requirements and guidance
GDPR_REQUIREMENTS = {
    "controller": {
        "description": "Data controller obligations (you decide why and how personal data is processed)",
        "requirements": [
            "Lawful basis for processing (Art. 6)",
            "Privacy notice (Art. 13-14)",
            "Data Protection Impact Assessment if high risk (Art. 35)",
            "Records of processing activities (Art. 30)",
            "Data subject rights mechanisms (Art. 15-22)",
            "Data processing agreements with processors (Art. 28)",
        ],
    },
    "processor": {
        "description": "Data processor obligations (you process data on behalf of a controller)",
        "requirements": [
            "Data processing agreement with controller (Art. 28)",
            "Records of processing activities (Art. 30)",
            "Security measures (Art. 32)",
            "Data breach notification to controller (Art. 33)",
        ],
    },
    "minimal_processing": {
        "description": "Minimal personal data processing (e.g., basic auth, no analytics)",
        "requirements": [
            "Privacy notice (Art. 13)",
            "Lawful basis documented (Art. 6)",
            "Basic security measures (Art. 32)",
        ],
    },
}

GDPR_GUIDANCE = {
    "privacy_policy": {
        "what": "Create a privacy policy informing users about data processing",
        "why": "Art. 13-14 - Data subjects must be informed about processing",
        "gdpr_article": "Art. 13-14",
        "effort": "medium",
    },
    "consent_mechanism": {
        "what": "Implement consent collection where consent is the legal basis",
        "why": "Art. 7 - Consent must be freely given, specific, informed, unambiguous",
        "gdpr_article": "Art. 7",
        "effort": "medium",
    },
    "data_subject_rights": {
        "what": "Implement mechanisms for data subject rights (access, deletion, portability)",
        "why": "Art. 15-22 - Data subjects can request access, rectification, erasure, portability",
        "gdpr_article": "Art. 15-22",
        "effort": "high",
    },
    "security_measures": {
        "what": "Implement appropriate technical and organizational security measures",
        "why": "Art. 32 - Security appropriate to the risk",
        "gdpr_article": "Art. 32",
        "effort": "medium",
    },
    "records_of_processing": {
        "what": "Maintain records of processing activities",
        "why": "Art. 30 - Controllers and processors must document their processing activities",
        "gdpr_article": "Art. 30",
        "effort": "medium",
    },
    "dpia": {
        "what": "Conduct a Data Protection Impact Assessment for high-risk processing",
        "why": "Art. 35 - Required when processing is likely to result in high risk",
        "gdpr_article": "Art. 35",
        "effort": "high",
    },
    "data_breach_procedure": {
        "what": "Document data breach detection and notification procedure",
        "why": "Art. 33-34 - Notify supervisory authority within 72h",
        "gdpr_article": "Art. 33-34",
        "effort": "medium",
    },
    "dpa": {
        "what": "Establish Data Processing Agreements with all processors",
        "why": "Art. 28 - Processing by a processor must be governed by a contract",
        "gdpr_article": "Art. 28",
        "effort": "medium",
    },
}
