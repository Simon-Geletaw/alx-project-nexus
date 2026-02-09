FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y \
        build-essential \
        libpq-dev \
        gcc \
        python3-dev \
        musl-dev \
        netcat-openbsd \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt /app/requirements.txt
RUN python - <<'PY'
from pathlib import Path

p = Path("/app/requirements.txt")
p.write_bytes(p.read_bytes().replace(b"\x00", b""))
PY
RUN python -m pip install --upgrade pip \
    && python -m pip install --no-cache-dir -r /app/requirements.txt

COPY . /app/
RUN find /app -name '__pycache__' -type d -prune -exec rm -rf {} + \
    && python - <<'PY'
from pathlib import Path

for path in Path("/app").rglob("*.py"):
        data = path.read_bytes()
        if b"\x00" in data:
                path.write_bytes(data.replace(b"\x00", b""))
PY

RUN chmod +x /app/scripts/entrypoint.sh

ENV PORT=8000
EXPOSE 8000
CMD python -m gunicorn E_Commerce.wsgi:application --bind 0.0.0.0:${PORT}