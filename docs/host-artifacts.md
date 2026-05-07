# Host-Specific Artifacts

Different agent hosts support different artifacts: commands, hooks, status lines, plugin metadata, generated indexes, repo instructions, and persistent planning files.

ASCT does not treat these as new primitives. It maps them to the same seven control surfaces.

## 1. Why this document exists

The portable Agent Skills core is usually:

```text
SKILL.md
references/
scripts/
assets/
evals/
```

Real systems often add:

```text
commands/
hooks/
statusline
AGENTS.md
CLAUDE.md
llms.txt
marketplace metadata
plugin manifests
planning files
project memory
```

These are important, but they should not make the theory grow a new layer for every host artifact. The right question is:

```text
Which control surface does this artifact implement?
```

## 2. Artifact mapping

| Artifact | Typical ASCT role |
|---|---|
| Slash command | Explicit activation or macro workflow |
| Command file | Activation Control and Trajectory Control |
| Hook | Lifecycle State, Trajectory, Completion, or Safety Control |
| Statusline | User-visible state or mode feedback |
| `AGENTS.md` | Repo-level or global policy controller |
| `CLAUDE.md` | Repo-level or host-specific policy controller |
| `llms.txt` | Agent-facing discovery and routing index |
| Marketplace metadata | Human discovery and installation metadata |
| Plugin manifest | Distribution and capability metadata |
| Planning file | Persistent State Control and Trajectory Control |
| Progress file | Persistent State Control and Completion Control |
| Project glossary | Persistent State Control |
| ADR | Persistent State Control and Evolution Control |
| Agent brief | Handoff contract and future Intent Control |
| Out-of-scope record | Future Intent Control and State Control |

## 3. Commands

Commands are best when the user wants explicit invocation of a workflow.

They are useful when:

- the workflow spans multiple skills;
- the user should decide when it starts;
- the workflow is a macro action;
- activation by `description` would be too ambiguous.

Commands usually implement Activation Control and Trajectory Control.

## 4. Hooks

Hooks are best when the system must enforce a lifecycle rule without relying on the model's memory.

They are useful for:

- blocking dangerous commands;
- refreshing project state before tool use;
- checking required files before stop;
- reminding the agent to update progress;
- enforcing audit logs.

Hooks are powerful and can surprise users. Use them for constraints, not for hidden task reasoning.

## 5. Status lines and visible state

Persistent modes can create user confusion. A status line can show:

- current mode;
- active workflow;
- compressed-output mode;
- pending validation;
- blocked external action.

Status lines are not core skill primitives. They help users observe the controller state.

## 6. Repo-level instructions

Files such as `AGENTS.md` and `CLAUDE.md` are appropriate for always-on repo rules, not task-specific skill workflows.

Good uses:

- coding style norms;
- safety constraints;
- repository conventions;
- prohibited operations;
- preferred package manager;
- project-wide validation commands.

Bad uses:

- long task workflows that should be selectively activated;
- large domain references that should be loaded conditionally;
- deterministic checks that should be scripts.

## 7. Generated indexes

Large skill collections may need generated indexes, such as `llms.txt` or a skill inventory.

Indexes support:

- Activation Control;
- human discovery;
- agent discovery;
- routing;
- collection governance.

They should summarize trigger boundaries, not duplicate full skill instructions.

## 8. Planning and memory files

Planning files, progress files, ADRs, glossaries, and agent briefs are external state. They help with:

- long tasks;
- context window limits;
- handoff;
- future task cost reduction;
- repeated terminology alignment;
- preserving decisions.

ASCT maps them to State Control, Completion Control, and Evolution Control.

## 9. Host portability rule

A portable theory should distinguish role from mechanism.

```text
Role: Completion Control
Mechanism in one host: stop hook
Mechanism in another host: validation command
Mechanism in a third host: explicit checklist in SKILL.md
```

Do not make the mechanism the theory.
