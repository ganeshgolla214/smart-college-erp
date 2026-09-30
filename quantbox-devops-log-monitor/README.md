# Linux Log Monitor & Incident Automation

A small DevOps/SRE practice project built around Linux log analysis and automated incident detection.

## What it does
- Parses Linux-style application/auth logs with Python.
- Detects ERROR, CRITICAL and failed-login patterns.
- Produces a compact incident summary and exit code suitable for automation.
- Includes a Bash wrapper for scheduled/cron-style execution.
- Runs consistently inside Docker.
- Includes GitHub Actions CI to validate the Python script and shell syntax.

## Stack
Linux/Unix • Python • Bash • Docker • GitHub Actions

## Run locally
```bash
python3 scripts/log_analyzer.py sample/app.log
```

Run the Bash automation:
```bash
bash scripts/monitor.sh sample/app.log
```

Run with Docker:
```bash
docker build -t linux-log-monitor .
docker run --rm linux-log-monitor
```

## Example output
The analyzer reports total lines, errors, critical events and failed logins. It exits with code 2 when critical/error events are detected, making it useful as a simple CI/cron health check.

## DevOps relevance
This project demonstrates basic production-support workflows: reading logs, identifying failure patterns, creating actionable summaries, using shell automation, containerizing a utility, and validating changes with CI.
