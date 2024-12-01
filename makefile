.PHONY: build start stop all migrate-db seed

build:
	docker-compose -f docker/docker-compose.yml up --build

start:
	docker-compose -f docker/docker-compose.yml up -d app db && docker attach docker_app_1

stop:
	docker-compose -f docker/docker-compose.yml down

migrate-db:
	docker-compose -f docker/docker-compose.yml exec app alembic upgrade head

seed:
	docker-compose -f docker/docker-compose.yml exec app python alembic/seed/seed.py

all: start migrate-db seed