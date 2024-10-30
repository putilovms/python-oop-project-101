.PHONY: install
install:
	poetry install

.PHONY: lint
lint:
	poetry run flake8 validator

.PHONY: test
test:
	poetry run pytest
