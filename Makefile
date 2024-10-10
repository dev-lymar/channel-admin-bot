lint:
	ruff check .
	flake8 .

run:
	pybabel compile -d locales -D messages
	python -m main