# Placement Decisions

A mature skill author does not ask only “what should this skill say?” They ask:

```text
Where should this control live?
```

ASCT treats placement as a first-class design decision. Many useful controls should not be written into `SKILL.md`.

## 1. Why placement matters

Putting a control in the wrong place creates cost and risk.

- A rule that should be always-on becomes unreliable if hidden inside a rarely triggered skill.
- A deterministic check becomes fragile if written as prose.
- A long reference becomes noisy if pasted into `SKILL.md`.
- A dangerous action guard becomes unsafe if it relies on the model remembering a rule.
- A multi-skill workflow becomes confusing if no command or routing layer coordinates it.

The goal is to put each control where it reduces failure with the least cost and risk.

## 2. Placement options

| Placement | Best for | ASCT role |
|---|---|---|
| Skill | Selectively loaded workflow for a recurring task distribution | Local policy controller |
| Global instruction | Always-on norms and constraints | Global policy controller |
| Command | Explicit macro workflow or multi-skill orchestration | Activation and trajectory controller |
| Hook | Lifecycle gate, state refresh, dangerous action block | Host-level trajectory, state, or safety controller |
| Script | Deterministic or repeatable operation | Execution controller |
| Reference | Long or conditional knowledge | External semantic memory |
| Asset | Template, schema, data file, example, starter artifact | Material prior |
| Repo memory | Project glossary, ADR, issue brief, known constraint | Persistent state controller |
| Collection routing | Skill priority, conflict resolution, install scope | Collection-level activation controller |

## 3. Decision procedure

Use this sequence.

### Step 1: Is the control always relevant?

If yes, prefer global instruction, repo instruction, or hook.

Examples:

- “Do not run destructive git commands without explicit approval.”
- “Do not edit unrelated files.”
- “Always protect secrets.”

These are not task-specific skills. They are global operating constraints.

### Step 2: Is the control deterministic?

If yes, prefer a script, validator, linter, renderer, schema check, or hook.

Examples:

- Validate JSON shape.
- Recalculate spreadsheet formulas.
- Detect forbidden shell commands.
- Render slides to images.
- Count missing required sections.

The model can decide when to run the check. The check itself should not be improvised.

### Step 3: Is the control long or conditional knowledge?

If yes, prefer `references/`.

Examples:

- API usage details.
- Domain rubric.
- Style guide.
- Common gotchas.
- Detailed examples.

The main `SKILL.md` should point to references rather than swallow them.

### Step 4: Is the control persistent project state?

If yes, prefer repo memory.

Examples:

- Project glossary.
- Architecture decision records.
- Agent briefs.
- Out-of-scope records.
- Known constraints.
- Design system master file.

This reduces future state uncertainty and future context cost.

### Step 5: Does the control orchestrate several skills?

If yes, prefer a command, collection routing rule, or explicit workflow layer.

Examples:

- Run `/plan`, then `/implement`, then `/review`.
- Choose a skill based on issue type.
- Chain read, research, and writing skills.

A single skill may not be the right abstraction for a multi-stage system.

### Step 6: Is the control a task-specific recurring workflow?

If yes, a skill is appropriate.

Examples:

- Debug a frontend runtime regression.
- Verify a suspected security finding.
- Generate a structured release checklist.
- Build an artifact with validation.
- Convert a user request into a PRD.

## 4. Placement anti-patterns

### Everything in `SKILL.md`

The skill becomes long, brittle, and hard to trigger precisely.

### Everything as a skill

Always-on norms, deterministic checks, and dangerous action guards are hidden behind selective activation.

### Everything as a hook

The system becomes rigid and surprising. Hooks should enforce lifecycle constraints, not replace task reasoning.

### Everything as references

The agent has knowledge, but no runtime control.

### Everything as scripts

The system has deterministic tools, but no judgment layer for when and why to use them.

## 5. Placement examples

### Example: “Do not claim tests passed unless they were run”

Best placement:

- Global instruction for general honesty.
- Skill completion contract for task-specific proof.
- Eval for regression.

Not enough:

- A buried sentence in a long reference.

### Example: “Block `git reset --hard`”

Best placement:

- Hook or command guard.
- Skill reminder only as secondary documentation.

Not enough:

- Asking the model to remember not to run it.

### Example: “Use the current official SDK docs”

Best placement:

- Skill state policy.
- Reference links.
- Tool or docs-fetch procedure.
- Eval case for outdated API hallucination.

### Example: “Project term X means Y”

Best placement:

- Repo memory or reference.
- Skill state policy may instruct the agent to read it.

## 6. Template

Use [templates/placement-decision.md](../templates/placement-decision.md) for concrete decisions.
