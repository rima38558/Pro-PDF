Contributing to Pro PDF
======================

Thanks for contributing! This file contains quick guidelines to make contributions smooth.

Getting started
- Create an issue to discuss larger changes before implementing.
- Fork the repo and create a branch with a descriptive name: `feature/xxx` or `fix/yyy`.

Code style and tests
- Follow the existing code style (Black/Flake8 where configured).
- Add tests for new behavior and run `pytest` locally.
- Install dev hooks: `python -m pip install --user pre-commit && pre-commit install`.

Database migrations
- If you change models, generate an Alembic revision: `make alembic-rev NAME="desc"`.
- Review the generated migration under `backend/alembic/versions/` and commit it with your change.
- CI will fail if models change without committed migrations.

PR process
- Open a pull request from your branch to the main branch.
- CI runs tests and migration checks; address failures before merge.
- Request at least one reviewer and squash/merge when approved.

Security
- Do not commit secrets. Use environment variables and secrets in CI.
