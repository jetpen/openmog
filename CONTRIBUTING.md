# Contributing to OpenMog

Thank you for your interest in contributing to OpenMog! This document provides guidelines for contributing to this project.

## Development Environment

### Prerequisites

- Python 3.9 or higher
- pip (Python package installer)
- git

### Setup

1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/your-username/openmog.git
   cd openmog
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install -e ".[dev]"
   ```

5. Install pre-commit hooks (optional but recommended):
   ```bash
   pre-commit install
   ```

## Development Workflow

### Code Style

This project uses:
- **Black** for code formatting
- **isort** for import sorting
- **flake8** for linting
- **mypy** for type checking

Run all checks:
```bash
make lint
```

Format code:
```bash
make format
```

### Testing

Run tests:
```bash
make test
```

Run tests with coverage:
```bash
make test-cov
```

### Documentation

Build documentation:
```bash
make docs
```

## Project Structure

```
openmog/
├── src/openmog/          # Source code
│   ├── __init__.py
│   ├── cli.py           # Command-line interface
│   ├── core/            # Core agent logic
│   ├── config/          # Configuration handling
│   ├── skills/          # Agent skills
│   └── utils/           # Utilities
├── tests/               # Test files
├── docs/                # Documentation
├── pyproject.toml       # Project configuration
├── requirements.txt     # Dependencies
└── README.md           # Project documentation
```

## AI Agent Guidelines

This project is designed to be AI-agent friendly. When contributing:

### Code Standards
- Use type hints for all function parameters and return values
- Write docstrings for all public functions and classes
- Keep functions small and focused on a single responsibility
- Use descriptive variable and function names

### Commit Messages
- Use clear, descriptive commit messages
- Start with a verb (Add, Fix, Update, etc.)
- Reference issue numbers when applicable

### Pull Requests
- Create descriptive PR titles and descriptions
- Include tests for new functionality
- Update documentation as needed
- Ensure CI checks pass

### Skills Development
When adding new skills to the agent:
- Place skill implementations in `src/openmog/skills/`
- Include skill metadata and configuration
- Add comprehensive tests
- Update skill documentation

## Communication

- Use GitHub Issues for bug reports and feature requests
- Use GitHub Discussions for general questions
- Join our community chat for real-time discussion

## License

By contributing to OpenMog, you agree that your contributions will be licensed under the same license as the project (MIT License).

Thank you for contributing to OpenMog! 🚀