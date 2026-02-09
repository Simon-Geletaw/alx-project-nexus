#!/bin/sh
if [ -n "$DATABASE_URL" ] && [ -z "$DB_HOST" ]; then
    DB_HOST_PORT=$(python - <<'PY'
import os
from urllib.parse import urlparse

url = os.environ.get("DATABASE_URL", "")
parsed = urlparse(url)
host = parsed.hostname or ""
port = parsed.port or 5432
print(f"{host} {port}")
PY
    )
    set -- $DB_HOST_PORT
    DB_HOST="$1"
    DB_PORT="$2"
fi

DB_HOST="${DB_HOST:-db}"
DB_PORT="${DB_PORT:-5432}"

echo "Waiting for postgres to be ready at ${DB_HOST}:${DB_PORT}..."
while ! nc -z "$DB_HOST" "$DB_PORT"; do
    sleep 1
done
python manage.py migrate
echo "Postgres is ready, starting the application..."
exec "$@"     