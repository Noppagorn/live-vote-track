.PHONY: install test lint format clean

install:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

test:
	pytest tests/ --cov=my_opensource_project

lint:
	flake8 my_opensource_project tests
	mypy my_opensource_project tests
	black --check my_opensource_project tests
	isort --check-only my_opensource_project tests

format:
	black my_opensource_project tests
	isort my_opensource_project tests

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete 