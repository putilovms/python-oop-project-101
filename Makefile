.PHONY: install
install:
	poetry install

.PHONY: lint
lint:
	poetry run flake8 validator

.PHONY: test
test:
	poetry run pytest

.PHONY: build
build:
	poetry build

.PHONY: test-coverage
test-coverage:
	poetry run pytest --cov=validator --cov-report xml
