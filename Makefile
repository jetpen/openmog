.PHONY: help install install-dev test test-cov lint format docs clean build

help: ## Show this help message
	@echo 'Usage: make [target]'
	@echo ''
	@echo 'Targets:'
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "  \033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install: ## Install the package
	pip install -e .

install-dev: ## Install the package with development dependencies
	pip install -e ".[dev]"

test: ## Run tests
	pytest

test-cov: ## Run tests with coverage
	pytest --cov=openmog --cov-report=html --cov-report=term-missing

lint: ## Run linting checks
	flake8 src/openmog tests
	mypy src/openmog

format: ## Format code with black and isort
	black src/openmog tests
	isort src/openmog tests

docs: ## Build documentation
	cd docs && make html

clean: ## Clean build artifacts
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .coverage
	rm -rf htmlcov/
	rm -rf .pytest_cache/
	rm -rf docs/_build/

build: ## Build the package
	python -m build

check: lint test ## Run all checks (linting and tests)

all: clean check build docs ## Run all tasks