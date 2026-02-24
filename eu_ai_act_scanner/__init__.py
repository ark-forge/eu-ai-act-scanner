"""EU AI Act Scanner — Scan your project for AI framework usage and EU AI Act compliance."""

__version__ = "0.1.1"

from eu_ai_act_scanner.scanner import EUAIActScanner
from eu_ai_act_scanner.gdpr import GDPRScanner

__all__ = ["EUAIActScanner", "GDPRScanner", "__version__"]
