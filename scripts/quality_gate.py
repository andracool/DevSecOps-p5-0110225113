"""Quality Gate: gagalkan pipeline bila hasil Bandit melewati ambang batas.

Aturan: 0 temuan HIGH dan 0 temuan MEDIUM. Temuan LOW diperbolehkan (warning).
"""
import json
import sys

MAX_HIGH = 0
MAX_MEDIUM = 0


def evaluate(report_path):
    with open(report_path, "r", encoding="utf-8") as fh:
        report = json.load(fh)
    counts = {"HIGH": 0, "MEDIUM": 0, "LOW": 0}
    for issue in report.get("results", []):
        counts[issue["issue_severity"]] += 1
    passed = counts["HIGH"] <= MAX_HIGH and counts["MEDIUM"] <= MAX_MEDIUM
    return passed, counts


if __name__ == "__main__":
    ok, c = evaluate(sys.argv[1] if len(sys.argv) > 1 else "bandit-report.json")
    print(f"Quality Gate -> HIGH={c['HIGH']} MEDIUM={c['MEDIUM']} LOW={c['LOW']}")
    if not ok:
        print("QUALITY GATE FAILED: temuan HIGH/MEDIUM melebihi ambang batas.")
        sys.exit(1)
    print("QUALITY GATE PASSED")
