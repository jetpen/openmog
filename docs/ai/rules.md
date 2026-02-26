```markdown
# AI / Agent Rules (docs/ai/rules.md)

## 0) Scope and precedence
These rules apply to any AI coding agent (Cline, Codex, etc.) operating in this repository.

Precedence (highest to lowest):
1. Oracle/company security, privacy, legal, and compliance requirements
2. This file (`docs/ai/rules.md`)
3. Repo documentation (README, `docs/`, ADRs), codebase patterns, and CI checks
4. Tool defaults

If instructions conflict, stop and ask for clarification.

---

## 1) Security, privacy, and data handling (non-negotiable)
- **Do not introduce secrets** into code, config, tests, logs, or documentation.
  - No API keys, passwords, tokens, private certificates, or internal hostnames.
  - Use `.env.example` for placeholders and documented env var names.
- **Do not exfiltrate sensitive data**.
  - Do not paste proprietary source code or confidential data into external third-party tools/services unless explicitly approved per internal policy.
- **Logging**: never log credentials, tokens, PII, customer data, or sensitive payloads by default.
- **Input handling**: validate untrusted inputs. Avoid unsafe patterns such as `eval`, `exec`, `pickle` on untrusted data, or shell injection.
- **Crypto**: use well-established libraries and patterns; do not implement custom cryptography.

If a task touches authentication/authorization, encryption, or sensitive data flows, ask for review/confirmation before proceeding.

---

## 2) Dependency management and licensing
- Minimize new dependencies; prefer the standard library or existing repo dependencies.
- If adding a dependency:
  - justify why it’s needed and why existing deps aren’t sufficient,
  - pin/lock as per repo tooling (pip-tools/poetry/uv/conda),
  - consider security posture (maintenance, CVEs) and license suitability for enterprise use.
- Do not add dependencies that require downloading or running untrusted binaries/scripts during install.

---

## 3) Python code quality rules
- Match existing project structure and conventions.
- Prefer:
  - small, testable functions,
  - explicit error handling,
  - clear exceptions/messages,
  - type hints for new/modified code when practical.
- Avoid behavior changes in unrelated code (“drive-by refactors”).
- Keep public APIs stable unless explicitly requested.

---

## 4) Testing and verification (required)
- For any functional change, add or update tests.
- Keep tests deterministic:
  - no real network calls unless explicitly requested (use mocks),
  - control time/randomness where needed,
  - avoid reliance on execution order.
- Run the repo’s standard checks (as available): tests, lint, format, type checks.
- If you cannot run commands, state that clearly and provide alternative validation (static reasoning, focused code review notes).

---

## 5) Documentation rules
- Update documentation when behavior, configuration, or usage changes.
- Keep README accurate and concise; deeper docs belong under `docs/`.

### Cline-specific README rule
If CLI usage/parameter parsing changes, update `README.md` accordingly and keep any “Entity Types” and “Usage” sections synchronized with actual behavior. [1]

---

## 6) Change management and reviewability
- Prefer small, coherent diffs with clear commit messages (or a single coherent changeset if commits aren’t used).
- Include a brief change summary and testing notes with every delivery/PR:
  - what changed,
  - why,
  - how it was verified,
  - risks/rollout notes if relevant.

---

## 7) Agent behavior and tool usage
- Ask clarifying questions when requirements are ambiguous or when multiple repo patterns exist.
- Do not fabricate files, APIs, or test results. If unsure, say so and propose a safe next step.

### Cline-specific operating rules (when using terminal)
Before executing terminal commands, `cd` to repo root using an absolute path (`/cygdrive/c/...` on Windows/Cygwin, `/...` otherwise) and use repo-relative paths for arguments. [1]

### Cline Memory Bank (if enabled in this repo)
If the repository uses `memory-bank/`, follow its workflow:
- read all memory bank files at the start of tasks,
- and on “update memory bank”, review all memory bank files and append to the changelog. [1]

---

## 8) Prohibited actions
- Introducing secrets or sensitive data into repo content.
- Disabling security checks or weakening authentication/authorization without explicit approval.
- Adding “temporary” backdoors, debug endpoints, or hidden flags.
- Copying code with unclear licensing.

---

## 9) Escalation / when to stop
Stop and ask for guidance if:
- a request could violate security/privacy/compliance,
- production data access is required,
- dependency/license risk is unclear,
- the requested change is large and requirements are not well-defined.
```

If you tell me whether this repo uses **ruff/black/mypy/pytest** (and whether you have a `pyproject.toml`), I can tune the rules to name your exact commands and quality gates.