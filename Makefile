up:
	docker-compose up --build

build:
	docker-compose build

migrate:
	docker-compose run --rm migrate

worker:
	docker-compose run --rm worker

logs:
	docker-compose logs -f

down:
	docker-compose down -v

shell:
	docker-compose run --rm backend /bin/bash

# Generate an Alembic migration locally (developer convenience)
# Usage: make alembic-rev NAME="add_field_to_user"
alembic-rev:
	python -m pip install -r backend/requirements.txt
t	# ensure backend package is importable
t	python -m pip install -e backend
t	alembic -c backend/alembic.ini revision --autogenerate -m "${NAME}"
seed-plans:
	python -m pip install -r backend/requirements.txt
	python -m pip install -e backend
	python backend/scripts/seed_plans.py
