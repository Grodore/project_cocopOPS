.PHONY: frontend
frontend:
		docker build -f Dockerfile.advancedv2 -t frontend:0.0.5 .

.PHONY: tests
tests:
		python -m pytest -v tests/
