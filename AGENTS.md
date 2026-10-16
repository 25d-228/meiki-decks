# Execution rules

HUMAN is the human authority; a message headed `HUMAN` needs no recipient suffix.
ORCHESTRATOR assigns bounded issues and reviews/merges their results. EXECUTOR
implements the assigned issue and stops with one draft PR and a concise
`EXECUTOR → ORCHESTRATOR` handoff. Keep HUMAN-facing reports short; put concrete
requirements and evidence in issues and PRs. Do not merge or begin the next stage
as EXECUTOR.

ORCHESTRATOR status begins `ORCHESTRATOR → HUMAN`, normally in one to three short
sentences. Forward assignments in one concise `ORCHESTRATOR → EXECUTOR` block.

Follow the assigned issue, roadmap #1, the relevant language plan, and its pinned
guide. Preserve all guides, accepted source IDs, and unrelated work. Start from
verified current main after dependencies merge; inspect checkout, branch, dirty
state, applicable instructions, and installed tools before writes. Do not reset,
stash, force-push, or discard concurrent work.

Every child launched by EXECUTOR must use **Sol 6.1**, with the exact authorized
CLI identifier verified in the designated environment. Spanish 01 verified
`gpt-6.1-sol`; this is evidence for that environment, not permission to guess or
fall back elsewhere. Use sequential fresh Codex CLI processes with high reasoning,
`--ephemeral`, read-only sandbox, and structured JSON. No session reuse, nested
agents, or child repository edits. Report missing capability precisely; do not
install tools, change credentials/global settings, or weaken the sandbox.

Enumerate actual senses/contrasts and prerequisites before each batch. Use one
fresh author and separate editor, ordinarily 40 cards per batch. EXECUTOR reads
all outputs, resolves findings, and alone saves accepted cards and synchronized
coverage. Apply cheap checks to new/changed records during ingestion. After all
cards, do one complete final editorial pass in consecutive partitions of at most
400, apply verified corrections together, then one consolidated source/count/
coverage/preservation check. Add review rounds only for concrete unresolved
defects. Run focused local implementation tests and use exact-head CI as the
authoritative repository suite; do not repeat full tests/hashes per batch.

Normally make one implementation commit/push per completed issue, and one
correction commit/push per requested review round on the same PR. No setup-only,
batch, audit-partition, or evidence-only commits. PR evidence must identify actual
base/head, process counts/settings, reviewed ranges, findings, checks/CI, and final
source/coverage SHA-256. Use exactly one closing reference for the execution issue;
link parent plans without closing them.

All nine languages' text must be accepted before any audio. Text validation checks
logical audio paths without MP3 files. No audio/runtime preparation, archive
export, application work, model/dependency installations/downloads/upgrades, GUI
automation, persistent services, or publication without a later explicit assignment.

Keep temporary prompts, outputs, scripts, reference copies, logs, and caches in
local `/tmp` (Spanish 01: `/tmp/meiki-decks-es-01/`); disable Python bytecode or
direct caches there. Never repurpose HOME. Keep normal source in the designated
checkout. Do not commit raw model logs, secrets, models, binaries, or archives.

Source contract and text-only commands: [docs/authoring-v1.md](docs/authoring-v1.md).
