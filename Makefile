export DOCKER_DEFAULT_PLATFORM=linux/amd64

up:
	docker compose -f docker-compose.yml up -d

down:
	docker compose -f docker-compose.yml down --remove-orphans

up_ci:
	docker compose -f docker-compose-ci.yaml up -d

up_ci_rebuild:
	docker compose -f docker-compose-ci.yaml up --build -d

down_ci:
	docker compose -f docker-compose-ci.yaml down --remove-orphans
