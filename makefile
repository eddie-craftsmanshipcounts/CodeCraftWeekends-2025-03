.PHONY: test

test:
	uv run python -m unittest discover -s src

run:
	python -m your_package_name