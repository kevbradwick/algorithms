.PHONY: test
test:
	poetry run python -m pytest --doctest-modules -s

.PHONY: fmt
fmt:
	poetry run black .
	poetry run isort .