# Seven Control Surfaces

A control surface is a part of agent behavior that a skill can influence.

The seven ASCT control surfaces are:

1. Activation Control
2. Intent Control
3. State Control
4. Trajectory Control
5. Execution Control
6. Completion Control
7. Evolution Control

They are not mandatory sections for every skill. They are diagnostic lenses. A skill author should ask which surfaces matter for the task distribution and which ones can be safely left light.

## 1. Activation Control

**Question:** Should this skill be used?

A skill that triggers incorrectly can reduce reliability even if its internal workflow is excellent. Because skills are selectively loaded, the activation layer is the first point of control.

### Mechanisms

- `name`
- `description`
- explicit invocation names
- slash commands or command aliases
- not-for boundaries
- near-miss examples
- adjacent skill routing
- generated indexes such as `llms.txt`
- trigger evals

### Good activation description

```yaml
description: Use when reviewing a completed frontend diff before merge for correctness, rendering, accessibility, performance, and maintainability risks. Not for debugging active broken behavior, designing new UI, or writing commit messages.
```

### Failure modes

- Activates for adjacent tasks.
- Fails to activate for implicit but valid requests.
- Uses broad words such as “quality”, “improve”, or “help” without boundaries.
- Hides trigger information in the body of `SKILL.md` where the agent cannot see it before activation.

### Review questions

- What are the positive trigger cases?
- What are the negative trigger cases?
- What are the near-miss cases?
- What other skill might compete with this one?
- If descriptions are shortened by the host, will the key trigger terms survive?

## 2. Intent Control

**Question:** What task is the user actually asking for?

User language is often ambiguous. A skill must compile utterances into task frames.

### Mechanisms

- mode routing
- clarification gates
- input contracts
- non-goals
- task-type decision tree
- safety redirects
- smallest-sufficient-mode rule

### Example modes

```text
quick: small, low-risk, clear task
standard: ordinary task with moderate ambiguity
deep: high-risk, broad, public-facing, or architecture-sensitive task
clarification: required inputs are missing
safety_redirect: unsafe, illegitimate, deceptive, or privacy-invasive request
```

### Failure modes

- Treats every request as deep mode.
- Treats high-risk tasks as quick mode.
- Answers the literal phrasing while missing the underlying job.
- Asks for clarification when repo or document inspection could answer the question.
- Proceeds despite missing required inputs.

### Review questions

- What inputs are required?
- What task modes exist?
- What is the smallest sufficient mode?
- When should the skill ask the user?
- When should the skill inspect the environment instead of asking?

## 3. State Control

**Question:** What is true right now?

State Control prevents the agent from acting on stale memory, imagined file structure, outdated API knowledge, or unverified user assumptions.

### Mechanisms

- reading files
- inspecting diffs
- command output
- logs
- official docs
- screenshots
- rendered artifacts
- issue history
- ADRs
- project glossary
- persistent project memory
- source hierarchy

### Source hierarchy example

```text
direct tool output
> current repository files and diffs
> official documentation
> rendered artifacts or screenshots
> user statements
> inference
> guess
```

The hierarchy is task-dependent. For a product decision, user goals may rank above repo files. For a code review, diff evidence usually ranks above conversation history.

### Failure modes

- Cites files not read.
- Assumes API signatures from memory.
- Uses old project context after the repo changed.
- Treats user guesses as facts.
- Ignores current test output or logs.

### Review questions

- What is the source of truth?
- What evidence must be read before action?
- What should happen when evidence conflicts?
- What can be inferred, and how should uncertainty be labeled?
- Which state should become persistent project memory?

## 4. Trajectory Control

**Question:** What path should the agent follow?

Trajectory Control is the workflow layer. Its purpose is not ceremony. Its purpose is to make bad plausible paths harder to take.

### Mechanisms

- ordered workflow
- hard gates
- stop conditions
- fallback paths
- escalation rules
- handoff format
- checkpoints
- phase boundaries

### Weak workflow

```text
Think carefully. Be systematic. Check your work.
```

### Strong trajectory control

```text
Before editing code, establish a reproducible pass/fail signal.
Before proposing a fix, write a falsifiable root-cause hypothesis.
After three failed hypotheses, stop and produce a handoff.
Do not claim success without validation evidence.
```

### Failure modes

- Patches symptoms before diagnosis.
- Jumps to implementation before deciding scope.
- Runs broad changes when a narrow edit is needed.
- Continues after repeated failed attempts.
- Performs external side effects before approval.

### Review questions

- Which bad path is this workflow designed to block?
- What must happen before implementation?
- What causes a hard stop?
- What causes a handoff?
- What fallback is used when a tool fails?

## 5. Execution Control

**Question:** Which operations require deterministic tools?

Execution Control separates judgment from deterministic execution.

```text
Models judge. Tools execute deterministically.
```

### Mechanisms

- scripts
- validators
- parsers
- renderers
- linters
- typecheckers
- schema checks
- formula recalculation
- dry-run commands
- dangerous command guards

### Use scripts when the operation is

- repetitive;
- parse-heavy;
- numerical;
- format-sensitive;
- expected to produce the same output for the same input;
- easy to validate mechanically;
- risky enough to require dry-run or guardrails.

### Failure modes

- Asks the model to count, parse, or validate by inspection.
- Produces artifact files without opening or rendering them.
- Claims formulas work without recalculation.
- Uses broad shell commands without dry-run.
- Lets model prose substitute for structured validation.

### Review questions

- Which steps are deterministic?
- Which scripts are needed?
- What are script inputs and outputs?
- What dependencies or permissions are required?
- Should scripts be run, read, or both?

## 6. Completion Control

**Question:** When may the agent claim done?

Completion Control suppresses completion hallucination. It ensures final claims do not exceed evidence.

```text
final_claims ⊆ validated_evidence
```

### Mechanisms

- validation commands
- proof fields
- claim-evidence mapping
- confidence levels
- known limitations
- unverified item disclosure
- completion checklist
- rendered artifact inspection

### Good completion output

```text
Implemented:
- Changed the pending-state handling in LoginForm.

Evidence:
- Diff inspected in src/components/LoginForm.tsx.
- Reproduction test added for double submit.

Validation:
- npm test passed.
- npm run build not run because dependency install failed.

Remaining risk:
- Backend idempotency was not inspected.
```

### Failure modes

- Says “done” without validation.
- Hides unverified claims.
- Confuses implementation with correctness.
- Treats absence of visible error as proof.
- Omits remaining risks.

### Review questions

- What claims does the final answer make?
- What evidence supports each claim?
- What validation was run?
- What was not validated?
- What risks remain?

## 7. Evolution Control

**Question:** How does the skill avoid drift and regression?

Skills drift because the world around them changes: models, tools, APIs, repositories, user habits, and platform behavior.

### Mechanisms

- trigger evals
- output evals
- process evals
- safety evals
- regression cases
- compatibility notes
- versioning
- deprecation policy
- patch hypotheses
- baseline comparison

### Failure modes

- Skill grows by anecdote without eval.
- Trigger behavior changes silently.
- New instructions improve one case and regress another.
- References become stale.
- Scripts assume old tools or old directory structure.
- Safety posture weakens as capabilities expand.

### Review questions

- What is the baseline?
- Which failure does this change target?
- Which evals should detect success?
- Which evals should detect regression?
- What is the rollback condition?
- When should the skill be deprecated?

## 8. Using the surfaces together

The surfaces are interconnected.

- Poor Activation Control increases context cost and wrong trajectory risk.
- Poor State Control weakens Completion Control.
- Poor Execution Control creates fake completion proof.
- Poor Intent Control sends the agent into the wrong workflow.
- Poor Evolution Control lets all other controls decay.

A strong skill is not one that maximizes every control surface. It is one that applies the right controls at the right strength for its task distribution.
