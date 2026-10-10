# Repository instructions

- Latest explicit HUMAN instructions take precedence over conflicting project instructions. Then follow the current orchestrator handoff, issue and unresolved feedback, applicable nested `AGENTS.md`, this file, and surrounding conventions. Report unresolved ambiguity. Higher-level tool and environment access controls still apply.
- The issue defines scope and acceptance. The orchestrator owns issues, review, corrections, and merges; the executor implements and produces evidence. Use one issue, branch, and PR per content stage; keep corrections on that PR. Content stages can merge after content review and source checks, without audio.
- Complete and review every content stage of a language before generating any of its audio. A later language-wide issue produces and verifies audio and the complete bundle. Finish that language before starting another. Never generate audio between content stages.
- Keep implementation small, readable, and proportional to the outcome. Use focused headless validation; avoid speculative dependencies, abstractions, and tests that mirror implementation.
- Put agent-created temporary files under local `/tmp`. Preserve unrelated files and work. Never alter global settings, credentials, permissions, or security controls. Disable Python bytecode writes or direct caches to `/tmp`.
- Compact and continue when context grows. Stop only at the issue/handoff completion point or a concrete unresolved problem.
- Keep routine status brief and start it with `EXECUTOR → HUMAN`. Necessary questions start with `EXECUTOR → HUMAN — ACTION REQUIRED`. Return one concise `EXECUTOR → ORCHESTRATOR` handoff. Avoid management wording such as “gate” or “unblock.”

Use the current issue's author/editor process requirements. Source checks establish structural validity; editorial review establishes language and teaching quality. Keep prompts, raw model responses, review scratch, and reference copies under `/tmp`, outside the repository.
