# Repository agent contract

## Precedence

- Issue-specific requirements override this file.
- An applicable nested `AGENTS.md` overrides this file for its paths.
- For unspecified details, follow the surrounding code and preserve its style.

## Scope and design

- Build only what the issue requires and preserve unrelated behavior.
- Include directly required tests, error handling, cleanup, and removal of superseded code.
- Do not add speculative options, hooks, wrappers, interfaces, extension points, services, or
  infrastructure.
- Introduce an abstraction only when at least two current callers require it.
- Do not replace working code only because another library or pattern exists.
- Do not make unrelated renames, formatting changes, upgrades, or documentation changes.

## Readability and source structure

- Use the configured formatter and lint rules.
- Write readable maintained source with clear, intent-revealing names.
- Keep related code together and use direct control flow with explicit side effects.
- Do not extract a one-use helper unless it removes meaningful complexity.
- Remove dead code, unused exports, unreachable branches, commented-out code, and superseded
  implementations.
- Comments explain non-obvious reasons, ordering, limits, or compatibility constraints.

## Errors and dependencies

- Validate at system boundaries and fail with useful context.
- Do not suppress errors or add untested fallback behavior.
- Do not add a dependency without issue approval. For issue #84 only, `voxcpm` and `soundfile`
  are approved server-generation dependencies.

## Tests and validation

- Add or update only tests required by the issue.
- Test observable behavior at the narrowest stable boundary and mock only external boundaries.
- Do not weaken or delete tests to make a change pass.
- Use repository-native commands and run focused checks during work and relevant local gates
  before pushing. CI is the authoritative full automated suite.
- Do not add a test framework, wrapper, coverage tool, Makefile, or speculative test
  infrastructure.

## Machine safety

- Do not launch or interact with an application or graphical interface.
- Do not use GUI or browser automation, simulated input, notifications, or desktop control.
- Do not start persistent services, watchers, or background processes.
- Run speech models and full audio generation only on the designated server.
- Use headless tests, lint, compilation, and non-interactive commands.

## Pull requests and executor responses

- One issue equals one branch and one pull request.
- A pull-request description contains exactly one `Fixes #N`.
- Requested changes stay on the same branch and pull request.
- Do not include unrelated changes.
- Completion or blocker handoff is one fenced block beginning with `EXECUTOR → ORCHESTRATOR`.
  Include only the repository, issue and pull-request numbers, branch, latest commit, CI state,
  unresolved feedback, uncovered requirements, human-verification state, queue state, and blocker
  when blocked.
