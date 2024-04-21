set -e

exec uvicorn main:app --log-level info --host 0.0.0.0 --port 8094 --reload