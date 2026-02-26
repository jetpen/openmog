# AGENTS.md

## Purpose
This repository supports AI coding agents (starting with **Cline** and **Codex**) to implement Python changes safely, consistently, and with good documentation. This file defines the shared working agreement for any agent operating in this repo.

## Source of Truth (Cline Memory Bank)
If you are running as **Cline**, you must follow the repo’s Cline rules and Memory Bank workflow:

- Read **all** files in `memory-bank/` at the start of every task. [1]
- Maintain and update the Memory Bank as you work (see “Memory Bank Updates”). [1]

For **Codex** (and other agents), treat `memory-bank/` as authoritative project context when present.

## Python Project Conventions (assumed defaults)
Unless this repo explicitly indicates otherwise (in `pyproject.toml`, `setup.cfg`, `requirements*.txt`, `Pipfile`, `poetry.lock`, etc.), follow these defaults:

- Use a virtual environment (venv/poetry/uv/conda as defined by the repo).
- Keep changes compatible with the Python version stated in project config (e.g., `pyproject.toml`).
- Prefer type hints in new/modified code where practical.
- Add/maintain tests for behavior changes.

If tooling is unclear, stop and ask (don’t guess).

## Operating Principles
1. **Small, reviewable diffs**
   - Avoid drive-by refactors.
   - Keep changes scoped to the request.

2. **Security and privacy first**
   - Never add secrets to source control.
   - Do not log sensitive data.
   - Be careful with deserialization, shelling out, filesystem operations, and dependency additions.

3. **Reproducible workflows**
   - Prefer documented, single-command workflows (make targets/scripts).
   - Run commands from the repo root.

## Standard Workflow (All Agents)

### 1) Understand the task
- Restate the goal and acceptance criteria.
- Identify impacted modules/files and edge cases.
- Identify validation needed (tests, lint, type checks).

### 2) Gather context
- Read relevant docs (README, `docs/`, inline module docs).
- Inspect Python tooling configuration:
  - `pyproject.toml` (preferred)
  - `setup.cfg`
  - `requirements.txt` / `requirements-dev.txt`
  - `tox.ini`
- For Cline: read the entire `memory-bank/` folder first. [1]

### 3) Plan before changing code
Provide a short plan that includes:
- Steps to implement
- Files to change
- Tests/checks to run
- Any risks or migration concerns

### 4) Implement
- Match existing code style and patterns.
- Keep public interfaces stable unless explicitly requested.
- Prefer clear exceptions and error messages.
- For new modules/functions, include docstrings if that’s the repo norm.

### 5) Verify (run what exists in the repo)
Run the repo’s established checks. Common Python checks include:
- Unit tests: `pytest`
- Linting: `ruff` / `flake8`
- Formatting: `ruff format` / `black`
- Type checking: `mypy` / `pyright`
- Packaging checks: `python -m build`

If the repo has `tox`, prefer running via `tox` because it encodes the project’s supported environments.

If you can’t run commands (or the environment isn’t available), say so explicitly and provide the next best verification (e.g., reasoning, targeted static review).

### 6) Document
- Update documentation if behavior or usage changes.
- For Cline: update Memory Bank (see below). [1]

## Dependency Changes (Python)
- Prefer using the project’s existing dependency manager (pip-tools/poetry/uv/conda).
- Minimize new dependencies; justify why they’re needed.
- If adding a dependency, ensure it is:
  - maintained,
  - license-appropriate for enterprise use,
  - and added to the correct dependency group (runtime vs dev/test).

## Tests (Python)
- Add tests for bug fixes and new behavior.
- Prefer `pytest`-style tests if the repo uses pytest.
- Keep tests deterministic:
  - avoid network calls unless mocked,
  - avoid reliance on system time unless controlled/freezed,
  - avoid ordering dependencies.

## Memory Bank Updates (Cline)
Update the Memory Bank when any of the following occur:
- You learned a new project pattern.
- You implemented significant changes.
- The user requests **“update memory bank”** (special handling below).
- Context needs clarification or time-based updates are needed. [1]

When triggered by **update memory bank**:
- Review **every** Memory Bank file, even if some don’t change. [1]
- Focus particularly on `memory-bank/activeContext.md` and `memory-bank/progress.md`. [1]
- Append an entry to `memory-bank/changelog.md` following a standard version/date header format. [1]

## README Update Rule
Update `README.md` when usage and/or command-line parsing changes. Keep any **Entity Types** list and **Usage** section synchronized with actual behavior. [1]

## Terminal / Command Execution Rule (Cline)
Before executing terminal commands:
- `cd` to the repo root using an **absolute path** (`/cygdrive/c/...` on Windows/Cygwin, `/...` on Unix). [1]
- Use repo-root-relative paths for commands that accept file arguments. [1]

(Other agents: follow the same spirit—run commands from repo root to ensure reproducibility.)

## Quality Bar Checklist
Before declaring work “done”, ensure:
- The change matches the requested behavior and constraints.
- Tests/checks were run (or you clearly stated why not).
- No secrets/sensitive data were added.
- Any new dependencies are justified and properly declared.
- Documentation is updated where necessary.
- For Cline: Memory Bank is current and consistent with the change. [1]

## When to Ask Questions Instead of Guessing
Stop and ask for clarification when:
- Requirements are ambiguous.
- A change might impact security/compliance, authentication/authorization, or data handling.
- Tooling is unclear (poetry vs pip vs uv; ruff vs flake8; mypy vs pyright; etc.).
- There are multiple competing patterns in the repo.

## Recommended Repo Files (Optional but Helpful)
To make agent-driven changes more reliable, consider adding:
- `pyproject.toml` with standardized tooling configuration (ruff/black/mypy/pytest)
- `tox.ini` (single entry point for lint/test across environments)
- `Makefile` or `scripts/` with:
  - `make test`, `make lint`, `make format`, `make typecheck`

## Testing (pytest)

Preferred commands (run from repo root):

- Run all tests:
  - `pytest`

- Run a subset (fast iteration):
  - `pytest -q`
  - `pytest path/to/test_file.py`
  - `pytest path/to/test_file.py::test_name`

- Stop on first failure:
  - `pytest -x`

- Show local variables in tracebacks (useful for debugging):
  - `pytest -l`

- Re-run only failures from last run (if enabled by pytest cache):
  - `pytest --lf`

Notes:
- Keep tests deterministic (no real network; mock external services).
- If you cannot run tests in your environment, state that explicitly and describe how you validated the change.
```

If you want, share whether you use any common pytest plugins (e.g., `pytest-cov`, `pytest-xdist`, `pytest-mock`) and I’ll tailor this to your repo’s exact setup (including coverage and parallelization conventions).

