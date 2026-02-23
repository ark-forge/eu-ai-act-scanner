"""EU AI Act compliance scanner — detects AI frameworks and checks compliance."""

import os
import re
import time
import logging
from pathlib import Path
from typing import Dict, List, Any

from eu_ai_act_scanner.patterns import (
    AI_MODEL_PATTERNS, CONFIG_DEPENDENCY_PATTERNS,
    CONFIG_FILE_NAMES, CODE_EXTENSIONS, SKIP_DIRS,
    MAX_FILES, MAX_FILE_SIZE, MAX_SCAN_DURATION,
)
from eu_ai_act_scanner.guidance import (
    FRAMEWORK_COMPLIANCE_INFO, RISK_CATEGORIES,
    ACTIONABLE_GUIDANCE, RISK_CATEGORY_INDICATORS,
    _ART_URL_BASE, _EUR_LEX_BASE,
)

logger = logging.getLogger(__name__)


class EUAIActScanner:
    """Scan a project for AI framework usage and check EU AI Act compliance."""

    def __init__(self, project_path: str):
        self.project_path = Path(project_path).resolve()
        self.detected_models: Dict[str, List[str]] = {}
        self.files_scanned = 0
        self.ai_files: List[Dict[str, Any]] = []

    def scan(self) -> Dict[str, Any]:
        """Scan the project to detect AI model usage."""
        if not self.project_path.exists():
            return {"error": f"Path does not exist: {self.project_path}", "detected_models": {}}
        if not self.project_path.is_dir():
            return {"error": f"Not a directory: {self.project_path}", "detected_models": {}}

        start = time.time()
        for dirpath, dirnames, filenames in os.walk(self.project_path, topdown=True):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            if self.files_scanned >= MAX_FILES:
                break
            if time.time() - start > MAX_SCAN_DURATION:
                return {
                    "files_scanned": self.files_scanned,
                    "ai_files": self.ai_files,
                    "detected_models": self.detected_models,
                    "findings": self._enrich_findings(),
                    "warning": f"Scan timed out after {MAX_SCAN_DURATION}s. Results are partial.",
                    "timed_out": True,
                }
            for fname in filenames:
                file_path = Path(dirpath) / fname
                if self.files_scanned >= MAX_FILES:
                    break
                try:
                    if file_path.stat().st_size > MAX_FILE_SIZE:
                        continue
                except OSError:
                    continue
                if file_path.suffix in CODE_EXTENSIONS:
                    self._scan_file(file_path)
                elif file_path.name in CONFIG_FILE_NAMES:
                    self._scan_config_file(file_path)

        return {
            "files_scanned": self.files_scanned,
            "ai_files": self.ai_files,
            "detected_models": self.detected_models,
            "findings": self._enrich_findings(),
        }

    def _scan_file(self, file_path: Path):
        self.files_scanned += 1
        try:
            first_bytes = file_path.read_bytes()[:1024]
            if b'\x00' in first_bytes:
                return
            content = file_path.read_text(encoding="utf-8", errors="ignore")
            file_detections = []
            for framework, patterns in AI_MODEL_PATTERNS.items():
                for pattern in patterns:
                    if re.search(pattern, content, re.IGNORECASE):
                        file_detections.append(framework)
                        self.detected_models.setdefault(framework, []).append(
                            str(file_path.relative_to(self.project_path))
                        )
                        break
            if file_detections:
                self.ai_files.append({
                    "file": str(file_path.relative_to(self.project_path)),
                    "frameworks": list(set(file_detections)),
                    "source": "code",
                })
        except Exception as e:
            logger.debug("Error scanning %s: %s", file_path, e)

    def _scan_config_file(self, file_path: Path):
        self.files_scanned += 1
        try:
            content = file_path.read_text(encoding="utf-8", errors="ignore")
            file_detections = []
            for framework, patterns in CONFIG_DEPENDENCY_PATTERNS.items():
                for pattern in patterns:
                    if re.search(pattern, content, re.IGNORECASE):
                        file_detections.append(framework)
                        self.detected_models.setdefault(framework, []).append(
                            str(file_path.relative_to(self.project_path))
                        )
                        break
            if file_detections:
                self.ai_files.append({
                    "file": str(file_path.relative_to(self.project_path)),
                    "frameworks": list(set(file_detections)),
                    "source": "dependency_file",
                })
        except Exception as e:
            logger.debug("Error scanning config %s: %s", file_path, e)

    def _enrich_findings(self) -> List[Dict[str, Any]]:
        framework_files: Dict[str, List[Dict[str, str]]] = {}
        seen: set = set()
        for entry in self.ai_files:
            file_path = entry["file"]
            source = entry.get("source", "code")
            for framework in entry["frameworks"]:
                key = (framework, file_path)
                if key not in seen:
                    seen.add(key)
                    framework_files.setdefault(framework, []).append({"file": file_path, "source": source})

        findings = []
        for framework, files_info in framework_files.items():
            info = FRAMEWORK_COMPLIANCE_INFO.get(framework, {})
            sources = sorted(set(f["source"] for f in files_info))
            findings.append({
                "framework": framework,
                "files": [f["file"] for f in files_info],
                "sources": sources,
                "risk_level": info.get("risk_level", "medium"),
                "article_reference": info.get("article_reference", "Art. 6 + Annex III (assess use case)"),
                "article_urls": info.get("article_urls", [f"{_ART_URL_BASE}/6/"]),
                "eur_lex_url": info.get("eur_lex_url", _EUR_LEX_BASE),
                "remediation": info.get("remediation", "Document this AI framework usage and assess risk category per Art. 6."),
            })
        return findings

    def check_compliance(self, risk_category: str = "limited") -> Dict[str, Any]:
        """Check EU AI Act compliance for a given risk category."""
        if risk_category not in RISK_CATEGORIES:
            return {"error": f"Invalid risk category: {risk_category}. Valid: {list(RISK_CATEGORIES.keys())}"}

        if not self.detected_models:
            return {
                "risk_category": risk_category,
                "no_ai_detected": True,
                "compliance_status": {},
                "compliance_score": "N/A",
                "compliance_percentage": None,
                "recommendations": [],
                "note": "No AI frameworks detected. Run scan() first.",
            }

        category_info = RISK_CATEGORIES[risk_category]
        compliance_checks = {
            "risk_category": risk_category,
            "description": category_info["description"],
            "requirements": category_info["requirements"],
            "compliance_status": {},
        }

        readme_exists = (self.project_path / "README.md").exists()

        if risk_category == "high":
            compliance_checks["compliance_status"] = {
                "technical_documentation": self._check_technical_docs(),
                "risk_management": self._check_doc_content("RISK_MANAGEMENT.md", ["risk", "mitigation", "impact"]),
                "transparency": self._check_doc_content("TRANSPARENCY.md", ["ai", "model", "disclosure"]) or self._check_ai_disclosure(),
                "data_governance": self._check_doc_content("DATA_GOVERNANCE.md", ["data", "source", "quality"]),
                "human_oversight": self._check_doc_content("HUMAN_OVERSIGHT.md", ["oversight", "human", "intervention"]),
                "robustness": self._check_doc_content("ROBUSTNESS.md", ["test", "security", "accuracy"]),
            }
        elif risk_category == "limited":
            compliance_checks["compliance_status"] = {
                "transparency": readme_exists or self._check_file_exists("TRANSPARENCY.md"),
                "user_disclosure": self._check_ai_disclosure(),
                "content_marking": self._check_content_marking(),
            }
        elif risk_category == "minimal":
            compliance_checks["compliance_status"] = {
                "basic_documentation": readme_exists,
            }

        total = len(compliance_checks["compliance_status"])
        passed = sum(1 for v in compliance_checks["compliance_status"].values() if v)
        compliance_checks["compliance_score"] = f"{passed}/{total}"
        compliance_checks["compliance_percentage"] = round((passed / total) * 100, 1) if total > 0 else 0
        compliance_checks["recommendations"] = self._generate_recommendations(compliance_checks)

        return compliance_checks

    def suggest_risk_category(self, description: str = "") -> str:
        """Suggest a risk category based on detected frameworks and optional description."""
        if description:
            desc_lower = description.lower()
            for category in ["unacceptable", "high", "limited", "minimal"]:
                for kw in RISK_CATEGORY_INDICATORS.get(category, {}).get("keywords", []):
                    if kw in desc_lower:
                        return category

        # Determine from detected frameworks
        risk_levels = set()
        for framework in self.detected_models:
            info = FRAMEWORK_COMPLIANCE_INFO.get(framework, {})
            risk_levels.add(info.get("risk_level", "medium"))

        if "high" in risk_levels:
            return "limited"  # Default to limited; high requires explicit use-case assessment
        elif "medium" in risk_levels:
            return "limited"
        return "minimal"

    def generate_report(self, scan_results: Dict, compliance_results: Dict) -> Dict[str, Any]:
        """Generate a complete compliance report."""
        from datetime import datetime, timezone
        return {
            "report_date": datetime.now(timezone.utc).isoformat(),
            "project_path": str(self.project_path),
            "scan_summary": {
                "files_scanned": scan_results.get("files_scanned", 0),
                "ai_files_detected": len(scan_results.get("ai_files", [])),
                "frameworks_detected": list(scan_results.get("detected_models", {}).keys()),
            },
            "compliance_summary": {
                "risk_category": compliance_results.get("risk_category", "unknown"),
                "compliance_score": compliance_results.get("compliance_score", "0/0"),
                "compliance_percentage": compliance_results.get("compliance_percentage", 0),
            },
            "detailed_findings": {
                "detected_models": scan_results.get("detected_models", {}),
                "findings": scan_results.get("findings", []),
                "compliance_checks": compliance_results.get("compliance_status", {}),
            },
            "recommendations": compliance_results.get("recommendations", []),
        }

    def _check_technical_docs(self) -> bool:
        docs = ["README.md", "ARCHITECTURE.md", "API.md", "docs/"]
        return any((self.project_path / doc).exists() for doc in docs)

    def _check_file_exists(self, filename: str) -> bool:
        return (self.project_path / filename).exists() or (self.project_path / "docs" / filename).exists()

    def _check_doc_content(self, filename: str, required_keywords: list) -> bool:
        for path in [self.project_path / filename, self.project_path / "docs" / filename]:
            if path.exists():
                try:
                    content = path.read_text(encoding="utf-8", errors="ignore").strip()
                    if len(content) < 100:
                        return False
                    content_lower = content.lower()
                    return any(kw in content_lower for kw in required_keywords)
                except Exception:
                    return False
        return False

    def _check_ai_disclosure(self) -> bool:
        readme_path = self.project_path / "README.md"
        if readme_path.exists():
            content = readme_path.read_text(encoding="utf-8", errors="ignore").lower()
            keywords = ["ai", "artificial intelligence", "machine learning", "deep learning", "gpt", "claude", "llm"]
            return any(kw in content for kw in keywords)
        return False

    def _check_content_marking(self) -> bool:
        markers = ["generated by ai", "ai-generated", "machine-generated"]
        for dirpath, dirnames, filenames in os.walk(self.project_path, topdown=True):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for fname in filenames:
                if not any(fname.endswith(ext) for ext in CODE_EXTENSIONS):
                    continue
                file_path = Path(dirpath) / fname
                try:
                    content = file_path.read_text(encoding="utf-8", errors="ignore").lower()
                    if any(marker in content for marker in markers):
                        return True
                except Exception:
                    pass
        return False

    def _generate_recommendations(self, compliance_results: Dict) -> List[Dict[str, Any]]:
        recommendations = []
        for check, passed in compliance_results.get("compliance_status", {}).items():
            if not passed:
                guidance = ACTIONABLE_GUIDANCE.get(check, {})
                recommendations.append({
                    "check": check,
                    "status": "FAIL",
                    "what": guidance.get("what", f"Missing: {check.replace('_', ' ')}"),
                    "why": guidance.get("why", "Required by EU AI Act"),
                    "how": guidance.get("how", [f"Create {check}.md documentation"]),
                    "eu_article": guidance.get("eu_article", ""),
                    "effort": guidance.get("effort", "medium"),
                })
            else:
                recommendations.append({"check": check, "status": "PASS"})
        return recommendations
