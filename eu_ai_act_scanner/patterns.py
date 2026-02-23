"""Detection patterns for AI frameworks and GDPR data processing."""

# ============================================================
# EU AI Act — Dependency file patterns
# ============================================================

CONFIG_FILE_NAMES = {
    "package.json", "package-lock.json",
    "requirements.txt", "requirements-dev.txt", "requirements_dev.txt",
    "setup.py", "setup.cfg", "pyproject.toml",
    "Pipfile", "Pipfile.lock",
    "environment.yml", "conda.yml",
    "pom.xml", "build.gradle", "build.gradle.kts",
    "Cargo.toml", "go.mod",
}

CODE_EXTENSIONS = {".py", ".js", ".ts", ".jsx", ".tsx", ".java", ".go", ".rs", ".cpp", ".c", ".rb", ".php"}

SKIP_DIRS = {
    ".venv", "venv", ".env", "env", "node_modules", ".git",
    "__pycache__", ".pytest_cache", ".tox", ".mypy_cache",
    "dist", "build", ".eggs", ".smithery", ".cache",
}

MAX_FILES = 5000
MAX_FILE_SIZE = 1_000_000  # 1MB
MAX_SCAN_DURATION = 120  # seconds

# Patterns for detecting AI dependencies in config/manifest files
CONFIG_DEPENDENCY_PATTERNS = {
    "openai": [r'"openai"', r"\bopenai\s*[>=<~!]", r"\bopenai\s*$"],
    "anthropic": [r'"anthropic"', r"\banthropic\s*[>=<~!]", r"\banthropic\s*$", r'"@anthropic-ai/'],
    "huggingface": [r'"transformers"', r"\btransformers\s*[>=<~!]", r'"diffusers"', r"\bdiffusers\s*[>=<~!]", r'"accelerate"', r"\baccelerate\s*[>=<~!]", r'"smolagents"', r"\bsmolagents\s*[>=<~!]"],
    "tensorflow": [r'"tensorflow"', r"\btensorflow\s*[>=<~!]"],
    "pytorch": [r'"torch"', r"\btorch\s*[>=<~!]", r"\btorch\s*$", r'"torchvision"', r"\btorchvision\s*[>=<~!]", r'"torchaudio"'],
    "langchain": [r'"langchain"', r"\blangchain\s*[>=<~!]", r"\blangchain\s*$", r"\blangchain-core\b", r"\blangchain-community\b", r"\blangchain-openai\b", r"\blangchain-anthropic\b", r'"@langchain/'],
    "gemini": [r'"google-generativeai"', r"\bgoogle-generativeai\s*[>=<~!]", r'"google-genai"', r"\bgoogle-genai\s*[>=<~!]", r'"@google/generative-ai"'],
    "vertex_ai": [r'"google-cloud-aiplatform"', r"\bgoogle-cloud-aiplatform\s*[>=<~!]"],
    "mistral": [r'"mistralai"', r"\bmistralai\s*[>=<~!]", r'"@mistralai/'],
    "cohere": [r'"cohere"', r"\bcohere\s*[>=<~!]", r"\bcohere\s*$"],
    "aws_bedrock": [r'"amazon-bedrock"', r'"@aws-sdk/client-bedrock"', r"\bamazon-bedrock\s*[>=<~!]", r"\bamazon-bedrock\s*$"],
    "azure_openai": [r'"azure-ai-openai"', r'"@azure/openai"', r"\bazure-ai-openai\s*[>=<~!]", r"\bazure-ai-openai\s*$"],
    "ollama": [r'"ollama"', r"\bollama\s*[>=<~!]"],
    "llamaindex": [r'"llama-index"', r"\bllama-index\s*[>=<~!]", r"\bllama.index\s*[>=<~!]"],
    "replicate": [r'"replicate"', r"\breplicate\s*[>=<~!]"],
    "groq": [r'"groq"', r"\bgroq\s*[>=<~!]"],
    "litellm": [r'"litellm"', r"\blitellm\s*[>=<~!]", r"\blitellm\s*$"],
    "crewai": [r'"crewai"', r"\bcrewai\s*[>=<~!]", r"\bcrewai\s*$", r"\bcrewai\["],
    "autogen": [r'"pyautogen"', r"\bpyautogen\s*[>=<~!]", r'"autogen"', r"\bautogen\s*[>=<~!]", r'"ag2"'],
    "semantic_kernel": [r'"semantic-kernel"', r"\bsemantic-kernel\s*[>=<~!]", r'"semantic_kernel"'],
    "haystack": [r'"haystack-ai"', r"\bhaystack-ai\s*[>=<~!]", r'"farm-haystack"', r"\bfarm-haystack\s*[>=<~!]"],
    "dspy": [r'"dspy"', r"\bdspy\s*[>=<~!]", r'"dspy-ai"', r"\bdspy-ai\s*[>=<~!]"],
    "zhipu": [r'"zhipuai"', r"\bzhipuai\s*[>=<~!]", r'"chatglm"'],
    "qwen": [r'"dashscope"', r"\bdashscope\s*[>=<~!]", r'"modelscope"', r"\bmodelscope\s*[>=<~!]"],
    "moonshot": [r'"moonshot"', r"\bmoonshot\s*[>=<~!]"],
    "deepseek": [r'"deepseek"', r"\bdeepseek\s*[>=<~!]"],
}

# Patterns for detecting AI model usage in source code
AI_MODEL_PATTERNS = {
    "openai": [
        r"openai\.ChatCompletion", r"openai\.Completion",
        r"from openai import", r"import openai",
        r"gpt-3\.5", r"gpt-4", r"gpt-4o", r"gpt-4-turbo",
        r"text-davinci", r"\bo1-preview\b", r"\bo1-mini\b", r"\bo3\b",
        r"text-embedding-3",
    ],
    "anthropic": [
        r"from anthropic import", r"import anthropic",
        r"claude-", r"Anthropic\(\)", r"messages\.create",
        r"claude-opus", r"claude-sonnet", r"claude-haiku",
    ],
    "huggingface": [
        r"from transformers import", r"AutoModel", r"AutoTokenizer",
        r"transformers\.pipeline", r"huggingface_hub",
        r"from diffusers import", r"from accelerate import",
        r"from smolagents import",
    ],
    "tensorflow": [
        r"import tensorflow", r"from tensorflow import",
        r"tf\.keras", r"\.h5$",
    ],
    "pytorch": [
        r"import torch", r"from torch import",
        r"nn\.Module", r"\.pt$", r"\.pth$",
    ],
    "langchain": [
        r"from langchain import", r"import langchain",
        r"LLMChain", r"ChatOpenAI",
        r"from langchain_core import", r"from langchain_community import",
        r"from langchain_openai import", r"from langchain_anthropic import",
    ],
    "gemini": [
        r"from google import genai", r"from google\.genai import",
        r"import google\.generativeai", r"from google\.generativeai import",
        r"GenerativeModel", r"gemini-pro", r"gemini-ultra",
        r"gemini-1\.5", r"gemini-2", r"gemini-3", r"gemini-flash",
    ],
    "vertex_ai": [
        r"from vertexai import", r"import vertexai",
        r"vertexai\.generative_models", r"google\.cloud\.aiplatform",
        r"from vertexai\.generative_models import",
    ],
    "mistral": [
        r"from mistralai import", r"import mistralai",
        r"from mistralai\.client import", r"Mistral\(",
        r"mistral-large", r"mistral-medium", r"mistral-small",
        r"mistral-nemo", r"magistral", r"codestral", r"mixtral",
    ],
    "cohere": [
        r"from cohere import", r"import cohere",
        r"cohere\.Client", r"cohere\.ClientV2",
        r"command-r", r"command-r-plus",
        r"embed-english", r"embed-multilingual", r"CohereClient",
    ],
    "aws_bedrock": [
        r"bedrock-runtime", r"bedrock-agent-runtime", r"BedrockRuntime",
        r"invoke_model", r"\.converse\(\s*modelId",
        r"from boto3.*bedrock", r"anthropic\.bedrock",
    ],
    "azure_openai": [
        r"AzureOpenAI", r"azure\.ai\.openai", r"azure_endpoint\s*=",
        r"AZURE_OPENAI", r"from openai import AzureOpenAI",
    ],
    "ollama": [
        r"import ollama", r"from ollama import",
        r"ollama\.chat", r"ollama\.generate", r"ollama\.Client",
    ],
    "llamaindex": [
        r"from llama_index import", r"import llama_index",
        r"from llama_index\.core import", r"from llama_index\.llms import",
        r"from llamaindex import", r"VectorStoreIndex",
        r"SimpleDirectoryReader", r"LlamaIndex",
    ],
    "replicate": [
        r"import replicate", r"from replicate import",
        r"replicate\.run", r"replicate\.models", r"replicate\.Client",
    ],
    "groq": [
        r"from groq import", r"import groq",
        r"groq\.Groq", r"Groq\(\)",
    ],
    "litellm": [
        r"from litellm import", r"import litellm",
        r"litellm\.completion", r"litellm\.acompletion", r"litellm\.embedding",
    ],
    "crewai": [
        r"from crewai import", r"import crewai",
        r"CrewAI", r"from crewai\.agent import",
    ],
    "autogen": [
        r"from autogen import", r"import autogen",
        r"from pyautogen import", r"import pyautogen",
        r"AssistantAgent", r"UserProxyAgent",
    ],
    "semantic_kernel": [
        r"from semantic_kernel import", r"import semantic_kernel",
        r"from semantic_kernel\.connectors import",
    ],
    "haystack": [
        r"from haystack import", r"import haystack",
        r"from haystack\.components import", r"from haystack\.nodes import",
    ],
    "dspy": [
        r"from dspy import", r"import dspy",
        r"dspy\.Predict", r"dspy\.ChainOfThought", r"dspy\.Module",
    ],
    "zhipu": [
        r"from zhipuai import", r"import zhipuai",
        r"ZhipuAI\(", r"zhipuai\.ZhipuAI",
        r"glm-4", r"glm-3", r"chatglm",
    ],
    "qwen": [
        r"from dashscope import", r"import dashscope",
        r"dashscope\.Generation",
        r"qwen-turbo", r"qwen-plus", r"qwen-max", r"qwen-vl",
        r"qwen2", r"qwen3", r"from modelscope import",
    ],
    "moonshot": [
        r"from moonshot import", r"import moonshot",
        r"moonshot-v1", r"kimi",
    ],
    "deepseek": [
        r"from deepseek import", r"import deepseek",
        r"deepseek-chat", r"deepseek-coder", r"deepseek-reasoner",
        r"deepseek-v3", r"deepseek-r1",
    ],
}

# ============================================================
# GDPR — Data processing patterns
# ============================================================

GDPR_CONFIG_PATTERNS = {
    "database_orm": [
        r'"sqlalchemy"', r"\bsqlalchemy\s*[>=<~!]",
        r'"django"', r"\bdjango\s*[>=<~!]",
        r'"sequelize"', r'"prisma"', r'"mongoose"',
        r'"typeorm"', r'"peewee"', r'"tortoise-orm"',
    ],
    "analytics": [
        r'"google-analytics"', r'"@google-analytics/',
        r'"segment"', r'"mixpanel"', r'"amplitude"',
        r'"posthog"', r'"plausible"', r'"matomo"',
    ],
    "email_service": [
        r'"sendgrid"', r'"mailgun"', r'"nodemailer"',
        r'"mailchimp"', r'"ses"', r'"postmark"',
    ],
    "auth_provider": [
        r'"passport"', r'"auth0"', r'"firebase-admin"',
        r'"keycloak"', r'"next-auth"', r'"supertokens"',
        r'"python-jose"', r'"pyjwt"',
    ],
    "payment": [
        r'"stripe"', r"\bstripe\s*[>=<~!]",
        r'"braintree"', r'"paypal"',
    ],
    "cookie_tracking": [
        r'"cookie-parser"', r'"js-cookie"',
        r'"react-cookie"', r'"cookies-next"',
    ],
    "cloud_storage": [
        r'"boto3"', r'"aws-sdk"', r'"@aws-sdk/',
        r'"google-cloud-storage"', r'"azure-storage"',
    ],
    "encryption": [
        r'"bcrypt"', r"\bbcrypt\s*[>=<~!]",
        r'"argon2"', r'"cryptography"',
        r'"passlib"', r'"python-dotenv"',
    ],
}

GDPR_CODE_PATTERNS = {
    "pii_fields": [
        r"\bemail\b.*=", r"\bphone\b.*=", r"\baddress\b.*=",
        r"\bfirst_name\b", r"\blast_name\b", r"\bfull_name\b",
        r"\bdate_of_birth\b", r"\bbirthday\b",
        r"\bssn\b", r"\bsocial_security\b",
        r"\bpassport_number\b", r"\bnational_id\b",
        r"\bip_address\b", r"\buser_agent\b",
    ],
    "database_queries": [
        r"SELECT\s+.*FROM\s+users", r"INSERT\s+INTO\s+users",
        r"UPDATE\s+users\s+SET", r"DELETE\s+FROM\s+users",
        r"\.find\(\{.*email", r"User\.objects\.", r"User\.query\.",
    ],
    "cookie_operations": [
        r"document\.cookie", r"res\.cookie\(", r"set_cookie\(",
        r"setCookie\(", r"response\.set_cookie",
    ],
    "ip_logging": [
        r"request\.ip\b", r"request\.remote_addr",
        r"X-Forwarded-For", r"req\.ip\b", r"REMOTE_ADDR",
    ],
    "user_tracking": [
        r"analytics\.track", r"analytics\.identify",
        r"gtag\(", r"fbq\(", r"_paq\.push",
        r"mixpanel\.track", r"posthog\.capture",
    ],
    "geolocation": [
        r"navigator\.geolocation", r"geoip", r"geo_ip",
        r"maxmind", r"ip2location",
    ],
    "file_uploads": [
        r"multer\(", r"formidable\(", r"file\.save\(",
        r"upload_file", r"FileField", r"ImageField",
    ],
    "consent_mechanism": [
        r"consent", r"opt.in", r"opt.out",
        r"cookie.banner", r"cookie.consent",
        r"gdpr.consent", r"privacy.accept",
    ],
    "data_deletion": [
        r"delete.account", r"delete.user", r"right.to.erasure",
        r"data.erasure", r"forget.me", r"anonymize", r"pseudonymize",
    ],
    "encryption_usage": [
        r"bcrypt\.hash", r"argon2\.hash", r"hashlib\.",
        r"crypto\.createHash", r"AES", r"encrypt\(", r"decrypt\(",
    ],
    "data_export": [
        r"export.data", r"download.data", r"data.portability",
        r"to_csv", r"to_json.*user",
    ],
}
