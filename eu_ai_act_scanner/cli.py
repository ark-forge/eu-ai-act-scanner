"""CLI interface for eu-ai-act-scanner."""

import argparse
import json
import sys
from pathlib import Path

from eu_ai_act_scanner import __version__


# ANSI colors (disabled if not a TTY)
_USE_COLOR = sys.stdout.isatty()


def _c(code: str, text: str) -> str:
    return f"\033[{code}m{text}\033[0m" if _USE_COLOR else text


def _red(t: str) -> str: return _c("31", t)
def _green(t: str) -> str: return _c("32", t)
def _yellow(t: str) -> str: return _c("33", t)
def _blue(t: str) -> str: return _c("34", t)
def _bold(t: str) -> str: return _c("1", t)
def _dim(t: str) -> str: return _c("2", t)


def _risk_color(level: str) -> str:
    colors = {"high": "31", "medium": "33", "low": "32"}
    return _c(colors.get(level, "0"), level.upper())


def _print_banner():
    print(_bold("EU AI Act Scanner") + f" v{__version__}")
    print(_dim("Scan your project for AI framework usage and EU AI Act / GDPR compliance"))
    print()


def _print_scan_results(results: dict):
    if "error" in results:
        print(_red(f"Error: {results['error']}"))
        return

    print(_bold("Scan Results"))
    print(f"  Files scanned: {results['files_scanned']}")
    print(f"  AI files found: {len(results.get('ai_files', []))}")
    print()

    models = results.get("detected_models", {})
    if not models:
        print(_green("  No AI frameworks detected."))
        return

    print(_bold("  Detected Frameworks:"))
    for framework, files in models.items():
        print(f"    {_blue(framework)} ({len(files)} file{'s' if len(files) != 1 else ''})")

    print()
    findings = results.get("findings", [])
    if findings:
        print(_bold("  Risk Assessment:"))
        for f in findings:
            risk = _risk_color(f["risk_level"])
            print(f"    [{risk}] {f['framework']}: {f['article_reference']}")
            print(f"           {_dim(f['remediation'])}")
        print()


def _print_compliance_results(results: dict):
    if "error" in results:
        print(_red(f"Error: {results['error']}"))
        return

    if results.get("no_ai_detected"):
        print(_yellow("  No AI frameworks detected — compliance checks not applicable."))
        return

    score = results.get("compliance_score", "?")
    pct = results.get("compliance_percentage", 0)
    category = results.get("risk_category", "?")

    color = "32" if pct >= 80 else ("33" if pct >= 50 else "31")
    print(_bold(f"  Compliance: {_c(color, f'{score} ({pct}%)')} for {category}-risk"))
    print()

    for rec in results.get("recommendations", []):
        if rec["status"] == "PASS":
            print(f"    {_green('PASS')} {rec['check']}")
        else:
            print(f"    {_red('FAIL')} {rec['check']}")
            print(f"         {rec.get('what', '')}")
            print(f"         {_dim(rec.get('why', ''))}")
            for step in rec.get("how", []):
                print(f"           - {step}")
    print()


def _print_gdpr_results(scan_results: dict, compliance_results: dict):
    summary = scan_results.get("processing_summary", {})
    if summary.get("processes_personal_data"):
        print(f"  Personal data processing: {_yellow('YES')}")
        print(f"  Risk level: {_risk_color(summary.get('risk_level', 'unknown'))}")
        print(f"  Suggested role: {summary.get('processing_role', '?')}")
        for sig in summary.get("positive_signals", []):
            print(f"    {_green('+')} {sig}")
    else:
        print(f"  Personal data processing: {_green('Not detected')}")

    print()
    score = compliance_results.get("compliance_score", "?")
    pct = compliance_results.get("compliance_percentage", 0)
    color = "32" if pct >= 80 else ("33" if pct >= 50 else "31")
    print(_bold(f"  GDPR Compliance: {_c(color, f'{score} ({pct}%)')}"))
    print()

    for rec in compliance_results.get("recommendations", []):
        if rec["status"] == "PASS":
            print(f"    {_green('PASS')} {rec['check']}")
        else:
            print(f"    {_red('FAIL')} {rec['check']}: {rec.get('what', '')}")
    print()


def cmd_scan(args):
    from eu_ai_act_scanner.scanner import EUAIActScanner

    _print_banner()
    project_path = args.path
    print(f"Scanning: {_bold(project_path)}")
    print()

    scanner = EUAIActScanner(project_path)
    scan_results = scanner.scan()

    _print_scan_results(scan_results)

    if scan_results.get("detected_models") and not args.scan_only:
        risk = args.risk or scanner.suggest_risk_category()
        compliance = scanner.check_compliance(risk)
        _print_compliance_results(compliance)

        if args.json:
            report = scanner.generate_report(scan_results, compliance)
            print(json.dumps(report, indent=2))
    elif args.json:
        print(json.dumps(scan_results, indent=2))

    # GDPR scan
    if args.gdpr:
        from eu_ai_act_scanner.gdpr import GDPRScanner
        print(_bold("GDPR Scan"))
        gdpr = GDPRScanner(project_path)
        gdpr_scan = gdpr.scan()
        role = gdpr_scan.get("processing_summary", {}).get("processing_role", "controller")
        gdpr_compliance = gdpr.check_compliance(role)
        _print_gdpr_results(gdpr_scan, gdpr_compliance)

        if args.json:
            gdpr_report = gdpr.generate_report(gdpr_scan, gdpr_compliance)
            print(json.dumps(gdpr_report, indent=2))

    # CTA for hosted MCP scanner
    if not args.json:
        print(_dim("─" * 60))
        print(f"  {_bold('Hosted MCP scanner available')} — scan without installing anything.")
        print(f"  Works with Claude, Cursor, Windsurf, and any MCP client.")
        print(f"  {_blue('https://arkforge.fr/mcp')}")
        print()


def main():
    parser = argparse.ArgumentParser(
        prog="eu-ai-act-scanner",
        description="Scan projects for AI framework usage and check EU AI Act / GDPR compliance",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")

    subparsers = parser.add_subparsers(dest="command")

    # scan command
    scan_parser = subparsers.add_parser("scan", help="Scan a project directory")
    scan_parser.add_argument("path", nargs="?", default=".", help="Project directory to scan (default: current directory)")
    scan_parser.add_argument("--risk", choices=["high", "limited", "minimal"], help="Risk category for compliance check")
    scan_parser.add_argument("--gdpr", action="store_true", help="Also run GDPR compliance scan")
    scan_parser.add_argument("--json", action="store_true", help="Output full report as JSON")
    scan_parser.add_argument("--scan-only", action="store_true", help="Only detect frameworks, skip compliance check")
    scan_parser.set_defaults(func=cmd_scan)

    args = parser.parse_args()
    if not args.command:
        # Default to scan current directory
        args.command = "scan"
        args.path = "."
        args.risk = None
        args.gdpr = False
        args.json = False
        args.scan_only = False
        args.func = cmd_scan

    args.func(args)
