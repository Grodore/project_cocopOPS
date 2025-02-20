.PHONY: build
build:
	# Assurez-vous d'utiliser une tabulation ici
	docker compose -f docker-compose.dev.yaml build

.PHONY: up
up:
	# Assurez-vous d'utiliser une tabulation ici
	docker compose -f docker-compose.dev.yaml up