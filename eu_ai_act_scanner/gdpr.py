"""GDPR compliance scanner — detects personal data processing and checks GDPR compliance."""

import os
import re
from pathlib import Path
from typing import Dict, List, Any
from datetime import datetime, timezone

from eu_ai_act_scanner.patterns import (
    GDPR_CODE_PATTERNS, GDPR_CONFIG_PATTERNS,
    CODE_EXTENSIONS, CONFIG_FILE_NAMES, SKIP_DIRS,
    MAX_FILES, MAX_FILE_SIZE,
)
from eu_ai_act_scanner.guidance import GDPR_REQUIREMENTS, GDPR_GUIDANCE


class GDPRScanner:
    """Scan a project for personal data processing patterns and check GDPR compliance."""

    def __init__(self, project_path: str):
        self.project_path = Path(project_path).resolve()
        self.detected_patterns: Dict[str, List[str]] = {}
        self.files_scanned = 0
        self.flagged_files: List[Dict[str, Any]] = []

    def scan(self) -> Dict[str, Any]:
        """Scan the project for personal data processing patterns."""
        if not self.project_path.exists():
            return {"error": f"Path does not exist: {self.project_path}", "detected_patterns": {}}

        for dirpath, dirnames, filenames in os.walk(self.project_path, topdown=True):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            if self.files_scanned >= MAX_FILES:
                break
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
                    self._scan_code(file_path)
                elif file_path.name in CONFIG_FILE_NAMES:
                    self._scan_config(file_path)

        return {
            "files_scanned": self.files_scanned,
            "flagged_files": self.flagged_files,
            "detected_patterns": self.detected_patterns,
            "processing_summary": self._summarize_processing(),
        }

    def _scan_code(self, file_path: Path):
        self.files_scanned += 1
        try:
            content = file_path.read_text(encoding="utf-8", errors="ignore")
            rel = str(file_path.relative_to(self.project_path))
            detections = []
            for category, patterns in GDPR_CODE_PATTERNS.items():
                for pattern in patterns:
                    if re.search(pattern, content, re.IGNORECASE):
                        detections.append(category)
                        self.detected_patterns.setdefault(category, []).append(rel)
                        break
            if detections:
                self.flagged_files.append({"file": rel, "categories": list(set(detections))})
        except Exception:
            pass

    def _scan_config(self, file_path: Path):
        self.files_scanned += 1
        try:
            content = file_path.read_text(encoding="utf-8", errors="ignore")
            rel = str(file_path.relative_to(self.project_path))
            detections = []
            for category, patterns in GDPR_CONFIG_PATTERNS.items():
                for pattern in patterns:
                    if re.search(pattern, content, re.IGNORECASE):
                        detections.append(category)
                        self.detected_patterns.setdefault(category, []).append(rel)
                        break
            if detections:
                self.flagged_files.append({"file": rel, "categories": list(set(detections)), "source": "config"})
        except Exception:
            pass

    def _summarize_processing(self) -> Dict[str, Any]:
        has_pii = "pii_fields" in self.detected_patterns or "database_queries" in self.detected_patterns
        has_tracking = "user_tracking" in self.detected_patterns or "analytics" in self.detected_patterns
        has_consent = "consent_mechanism" in self.detected_patterns
        has_deletion = "data_deletion" in self.detected_patterns or "data_export" in self.detected_patterns
        has_encryption = "encryption_usage" in self.detected_patterns or "encryption" in self.detected_patterns
        has_geo = "geolocation" in self.detected_patterns
        has_uploads = "file_uploads" in self.detected_patterns

        risk_factors = sum([has_pii, has_tracking, has_geo, has_uploads, not has_consent and has_pii])
        if risk_factors >= 3:
            risk_level = "high"
        elif risk_factors >= 1:
            risk_level = "medium"
        else:
            risk_level = "low"

        positive = []
        if has_consent:
            positive.append("Consent mechanism detected")
        if has_deletion:
            positive.append("Data deletion/export capability detected")
        if has_encryption:
            positive.append("Encryption usage detected")

        return {
            "processes_personal_data": has_pii or has_tracking,
            "risk_level": risk_level,
            "risk_factors": risk_factors,
            "positive_signals": positive,
            "processing_role": "controller" if has_pii else ("processor" if has_tracking else "minimal_processing"),
        }

    def check_compliance(self, processing_role: str = "controller") -> Dict[str, Any]:
        """Check GDPR compliance for a given processing role."""
        if processing_role not in GDPR_REQUIREMENTS:
            return {"error": f"Invalid role: {processing_role}. Valid: {list(GDPR_REQUIREMENTS.keys())}"}

        role_info = GDPR_REQUIREMENTS[processing_role]
        status = {
            "privacy_policy": self._check_file("PRIVACY_POLICY.md") or self._check_file("privacy-policy.md"),
            "consent_mechanism": "consent_mechanism" in self.detected_patterns,
            "data_subject_rights": "data_deletion" in self.detected_patterns or "data_export" in self.detected_patterns,
            "security_measures": "encryption_usage" in self.detected_patterns or "encryption" in self.detected_patterns,
            "records_of_processing": self._check_file("RECORDS_OF_PROCESSING.md"),
        }

        if processing_role == "controller":
            status["dpia"] = self._check_file("DPIA.md")
            status["data_breach_procedure"] = self._check_file("DATA_BREACH_PROCEDURE.md")
            status["dpa"] = self._check_file("DATA_PROCESSING_AGREEMENT.md") or self._check_file("DPA.md")

        total = len(status)
        passed = sum(1 for v in status.values() if v)

        recommendations = []
        for check, check_passed in status.items():
            if not check_passed:
                guidance = GDPR_GUIDANCE.get(check, {})
                recommendations.append({
                    "check": check,
                    "status": "FAIL",
                    "what": guidance.get("what", f"Missing: {check.replace('_', ' ')}"),
                    "why": guidance.get("why", "Required by GDPR"),
                    "gdpr_article": guidance.get("gdpr_article", ""),
                    "effort": guidance.get("effort", "medium"),
                })
            else:
                recommendations.append({"check": check, "status": "PASS"})

        return {
            "processing_role": processing_role,
            "description": role_info["description"],
            "requirements": role_info["requirements"],
            "compliance_status": status,
            "compliance_score": f"{passed}/{total}",
            "compliance_percentage": round((passed / total) * 100, 1) if total > 0 else 0,
            "recommendations": recommendations,
        }

    def generate_report(self, scan_results: Dict, compliance_results: Dict) -> Dict[str, Any]:
        return {
            "report_date": datetime.now(timezone.utc).isoformat(),
            "regulation": "GDPR",
            "project_path": str(self.project_path),
            "scan_summary": {
                "files_scanned": scan_results.get("files_scanned", 0),
                "flagged_files": len(scan_results.get("flagged_files", [])),
                "processing_categories": list(scan_results.get("detected_patterns", {}).keys()),
            },
            "processing_summary": scan_results.get("processing_summary", {}),
            "compliance_summary": {
                "processing_role": compliance_results.get("processing_role", "unknown"),
                "compliance_score": compliance_results.get("compliance_score", "0/0"),
                "compliance_percentage": compliance_results.get("compliance_percentage", 0),
            },
            "recommendations": compliance_results.get("recommendations", []),
        }

    def _check_file(self, filename: str) -> bool:
        return (self.project_path / filename).exists() or (self.project_path / "docs" / filename).exists()
