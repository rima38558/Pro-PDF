Pro PDF — dev README
=====================

This repository contains a FastAPI backend with Celery workers for PDF processing and a docker-compose setup for local development.

Quick start (Linux/macOS/Windows with Docker):

1. Ensure Docker and Docker Compose are installed.
2. (Optional) Copy `.env.example` to `.env` and set secrets (`DATABASE_URL`, `JWT_SECRET`, `USE_S3`, etc.).
3. Run migrations once:

```bash
make migrate
```

4. Start the stack:

```bash
make up
```

Useful targets:

- `make migrate` — run Alembic migrations (one-off service)
- `make up` — build and start containers
- `make worker` — run a Celery worker
- `make logs` — follow logs
- `make shell` — open a shell in the backend image

Notes
- Run `make migrate` before `make up` to ensure DB schema is applied.
- For S3/MinIO, set `USE_S3=true` and provide `S3_ENDPOINT`, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `S3_BUCKET` in `.env`.

Development
-----------

Recommended local development setup (Windows PowerShell example):

```powershell
cd "C:\xampp\htdocs\Pro PDF"
py -3.11 -m venv .venv
& ".\.venv\Scripts\Activate.ps1"
python -m pip install -U pip
python -m pip install -r backend/requirements.txt
python -m pip install -e backend
python -m pytest -q
```

Notes:
- Installing the backend in editable mode (`pip install -e backend`) lets tests import the `app` package without setting `PYTHONPATH`.
- If you prefer not to install editable, set `PYTHONPATH` to `backend` when running tests: `$env:PYTHONPATH = "C:\xampp\htdocs\Pro PDF\backend"`.

