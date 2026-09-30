#!/usr/bin/env python3
"""Analyze a Linux-style log file and return an incident summary."""

import re
import sys
from pathlib import Path

PATTERNS = {
    "errors": re.compile(r"\\bERROR\\b", re.I),
    "critical": re.compile(r"\\bCRITICAL\\b", re.I),
    "failed_logins": re.compile(r"(failed password|authentication failure)", re.I),
}

def analyze(path: Path) -> dict[str, int]:
    counts = {"lines": 0, "errors": 0, "critical": 0, "failed_logins": 0}
    with path.open("r", encoding="utf-8") as log:
        for line in log:
            counts["lines"] += 1
            for key, pattern in PATTERNS.items():
                if pattern.search(line):
                    counts[key] += 1
    return counts

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: log_analyzer.py <log-file>", file=sys.stderr)
        return 1

    path = Path(sys.argv[1])
    if not path.is_file():
        print(f"Log file not found: {path}", file=sys.stderr)
        return 1

    result = analyze(path)
    print("=== Log Monitor Report ===")
    for key, value in result.items():
        print(f"{key.replace('_', ' ').title()}: {value}")

    if result["critical"] or result["errors"]:
        print("Status: ATTENTION - error events detected")
        return 2

    print("Status: OK")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
