# Repository agent contract

## Precedence

For an executor, instructions apply in this order:

1. the latest explicit `HUMAN → EXECUTOR` instruction;
2. the current `ORCHESTRATOR → EXECUTOR` handoff;
3. the issue and unresolved review feedback;
4. applicable nested `AGENTS.md` files;
5. this root `AGENTS.md`;
6. surrounding repository conventions.

A more specific current instruction overrides a general lower-priority prohibition only for the
named action and task.

## Scope and design

- Apply YAGNI to messages, issues, work, evidence, and validation.
- Build only what the issue requires and preserve unrelated behavior.
- Include directly required tests, error handling, cleanup, and removal of superseded code.
- For content, require clear structure, consistent terminology, source accuracy, natural language,
  and suitable learner presentation.
- For data and configuration, require valid structure, clear naming, stable formatting, and
  appropriate validation.
- Do not add speculative options, hooks, wrappers, interfaces, extension points, services, or
  infrastructure, sections, sources, tools, or tests.
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

## Errors, evidence, dependencies, and external actions

- Validate at system boundaries and fail with useful context.
- Do not suppress errors or add untested fallback behavior.
- Produce the required evidence and use repository-native checks.
- Do not repeat expensive unaffected checks without a reason.
- Every new dependency or tool requires issue approval.
- External, interactive, destructive, publishing, installation, launch, upload, deployment,
  service, and graphical actions are prohibited by default.
- A current `HUMAN → EXECUTOR` or `ORCHESTRATOR → EXECUTOR` message can authorize one named
  action for the current task.
- Perform only the authorized action and stop on unexpected credentials, privileges, destructive
  steps, or security bypasses.

## Tests and validation

- The executor writes or updates only tests required by the issue.
- Test observable behavior at the narrowest stable boundary.
- Do not mock the unit under test.
- Mock external boundaries only when necessary.
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

## Human verification

- Use blocking human verification only when objective evidence cannot establish correctness,
  usability, accessibility, compatibility, or fitness for purpose.
- Defer low-risk subjective review until the related queue is complete.
- Do not ask the human to repeat automated checks.

## Pull requests and executor responses

- One issue equals one branch and one pull request.
- A pull-request description contains exactly one `Fixes #N`.
- Requested changes stay on the same branch and pull request.
- Do not include unrelated changes.
- Routine status begins with `EXECUTOR → HUMAN`.
- A blocking question begins with `EXECUTOR → HUMAN — ACTION REQUIRED`.
- Completion or blocker handoff is one fenced block beginning with `EXECUTOR → ORCHESTRATOR`.
  Include only the repository, issue and pull-request numbers, branch, latest commit, validation
  state, unresolved feedback, uncovered requirements, required human verification, deferred
  subjective-review items, authorized external-action state and result, queue state, and blocker
  when blocked.
