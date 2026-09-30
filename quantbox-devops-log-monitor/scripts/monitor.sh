#!/usr/bin/env bash
set -euo pipefail

LOG_FILE="${1:-sample/app.log}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

echo "[monitor] Checking ${LOG_FILE}"
python3 "${SCRIPT_DIR}/log_analyzer.py" "${LOG_FILE}"
