FROM python:3.12-slim

WORKDIR /app
COPY scripts/ ./scripts/
COPY sample/ ./sample/

RUN chmod +x scripts/monitor.sh scripts/log_analyzer.py

CMD ["python", "scripts/log_analyzer.py", "sample/app.log"]
