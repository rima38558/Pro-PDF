#!/usr/bin/env python3
"""Pre-commit hook: ensure Alembic migration is staged when SQLAlchemy models change.

Heuristic: if any staged file is under `backend/app/` and looks like a models file,
require that at least one staged file exists under `backend/alembic/versions/`.

This is a simple safety check and not a substitute for human review.
"""
import sys
import subprocess


def get_staged_files():
    res = subprocess.run(["git", "diff", "--name-only", "--cached"], capture_output=True, text=True)
    if res.returncode != 0:
        print("Unable to get staged files", file=sys.stderr)
        sys.exit(0)
    return [p.strip() for p in res.stdout.splitlines() if p.strip()]


def main():
    staged = get_staged_files()
    if not staged:
        sys.exit(0)

    # Patterns to consider as model changes
    model_paths = [p for p in staged if p.startswith("backend/app/") and ("model" in p or p.endswith("models.py"))]
    if not model_paths:
        sys.exit(0)

    # Check if any alembic version file is staged (new or modified)
    alembic_staged = [p for p in staged if p.startswith("backend/alembic/versions/")]
    if alembic_staged:
        sys.exit(0)

    print("\nERROR: Detected changes to models but no Alembic migration staged.")
    print("If you changed SQLAlchemy models, generate and stage a migration before committing.")
    print("")
    print("Run locally: make alembic-rev NAME=\"short-description\"")
    print("Then review the generated file under backend/alembic/versions/ and stage it.")
    print("")
    sys.exit(1)


if __name__ == '__main__':
    main()
