# Nine Design Laws

The ASCT design laws are engineering laws, not natural laws. They are derived from the five postulates and are meant to guide skill authorship.

They are stable enough to be useful, but not sacred. If a future agent architecture invalidates one of the postulates, the corresponding laws should be revised.

## 1. Trigger Boundary Law

**A skill's first quality is correct activation.**

### Why

A skill is selectively loaded. If it activates in the wrong task, all of its internal workflow becomes misapplied control. Wrong activation wastes context, adds friction, and may push the agent toward unsafe or irrelevant actions.

### Derived from

- Conditional Policy
- Bounded Resources
- Non-zero Fallibility

### Practice

A good `description` should contain:

- what the skill does;
- when to use it;
- important trigger words;
- not-for boundaries;
- near-miss cases;
- adjacent-skill routing.

### Weak version

```yaml
description: Helps with code quality.
```

### Stronger version

```yaml
description: Use when reviewing a completed frontend diff before merge for correctness, rendering, accessibility, performance, and maintainability risks. Not for debugging active broken behavior, designing new UI, or writing commit messages.
```

### Corollaries

- Do not hide trigger rules only inside the body of `SKILL.md`.
- If many skills overlap, add a resolver or collection routing rule.
- Evaluate near-miss prompts, not just obvious positive cases.

## 2. Task Compilation Law

**A skill compiles user utterances into task frames and runtime modes.**

### Why

User language is ambiguous. “Can you check this?” may mean review, debug, design, release validation, rewrite, or decision support.

A skill should not blindly execute the user's surface phrase. It should infer the task frame, choose the smallest sufficient mode, and ask for clarification only when required.

### Derived from

- Conditional Policy
- Non-zero Fallibility
- Bounded Resources

### Practice

Define modes such as:

```text
quick: low-risk task with clear scope
standard: ordinary task with moderate ambiguity
deep: high-risk, broad, public-facing, security-sensitive, or architecture-sensitive task
clarification: required inputs are missing
safety_redirect: unsafe or illegitimate request
```

### Corollaries

- A skill without mode routing tends to over-handle small tasks and under-handle risky tasks.
- Clarification is a tool, not a reflex. Inspect available evidence before asking the user for information the environment can provide.
- Non-goals are part of task compilation.

## 3. Context Economy Law

**Every token in `SKILL.md` should buy behavior change.**

### Why

Context and attention are finite. Progressive disclosure exists because not every piece of knowledge should be loaded on every task.

A long `SKILL.md` can be worse than a short one if it dilutes the agent's attention, increases activation cost, or mixes rare edge cases into the main path.

### Derived from

- Bounded Resources

### Practice

Put content where it belongs:

| Content type | Suggested placement |
|---|---|
| Core trigger and workflow | `SKILL.md` |
| Long rubric | `references/` |
| Detailed examples | `references/` |
| API or domain reference | `references/` |
| Deterministic validation | `scripts/` |
| Templates, schemas, static resources | `assets/` |
| Regression cases | `evals/` |

### Corollaries

- Main skill files should be navigational, not encyclopedic.
- Long examples are valuable, but often belong in references.
- If a rule does not change behavior, remove it or demote it.

## 4. Evidence Externalization Law

**Current facts should come from external evidence, not latent memory.**

### Why

LLM latent memory may be stale, incomplete, or overgeneralized. Current repository state, official documentation, command output, and rendered artifacts usually provide stronger grounding.

### Derived from

- Non-zero Fallibility
- External Groundability

### Practice

Define a task-specific source hierarchy.

Example for code review:

```text
current diff
> current repository files
> test output and CI logs
> project docs
> user statement
> inference
```

Example for API migration:

```text
official current docs
> installed package types or source
> local codebase usage
> user statement
> model memory
```

### Corollaries

- The final answer should distinguish facts, assumptions, judgments, and unknowns.
- If freshness matters, use official or current sources.
- Do not claim to have inspected evidence that was not inspected.

## 5. Trajectory Constraint Law

**Workflow exists to make bad paths harder to take.**

### Why

Agents can always generate a plausible next step. Many failures are not caused by lack of ideas, but by choosing a plausible bad path: patching symptoms, skipping validation, widening scope, or continuing after repeated failure.

### Derived from

- Conditional Policy
- Non-zero Fallibility

### Practice

Use:

- hard gates;
- stop conditions;
- fallback paths;
- escalation rules;
- handoff formats;
- phase boundaries.

### Weak instruction

```text
Be careful and debug systematically.
```

### Strong control

```text
Do not edit code until a reproducible pass/fail signal exists.
Do not propose a fix until you can state a falsifiable root-cause hypothesis.
After three failed hypotheses, stop and produce a handoff.
```

### Corollaries

- Workflow steps should correspond to failure modes.
- Stop conditions are as important as action steps.
- Handoff is a success path when continuing would increase risk.

## 6. Freedom-Risk Law

**Higher-risk tasks require lower agent freedom.**

### Why

The cost of a bad action rises with irreversibility, external side effects, safety impact, public visibility, format sensitivity, and security sensitivity.

A creative UI exploration should not be controlled like a production release. A destructive shell operation should not be controlled like a writing task.

### Derived from

- Non-zero Fallibility
- External Groundability
- Bounded Resources

### Practice

| Task type | Freedom level | Control style |
|---|---:|---|
| Creative design | High | taste rubric, examples, anti-patterns |
| Technical decision | Medium-high | assumptions, trade-offs, reversibility |
| Debug | Medium | feedback loop, hypothesis gate, stop conditions |
| Artifact generation | Low | scripts, validators, render checks |
| Release, delete, publish, external write | Very low | approval, dry-run, audit trail |
| Security verdict | Very low | evidence class, counterargument, gate review |

### Corollaries

- Creative skills should parameterize freedom rather than eliminate it.
- High-risk skills should fail closed.
- Approval is not a substitute for evidence, but it is required for external side effects.

## 7. Deterministic Delegation Law

**Models judge; tools execute deterministically.**

### Why

Some operations are poor fits for free-form generation: parsing, counting, rendering, schema validation, formula recalculation, linting, and file-format checks.

A model can decide which check is relevant. The check itself should often be a script or tool.

### Derived from

- External Groundability
- Bounded Resources

### Practice

Use scripts for:

- parsing;
- validation;
- rendering;
- counting;
- formula recalculation;
- schema checks;
- formatting;
- dependency inspection;
- dangerous command guards.

### Corollaries

- Deterministic work hidden inside prose is fragile.
- A good skill tells the agent when to run a script and what the result means.
- A script should produce clear failure messages, not just exit codes.

## 8. Completion Proof Law

**Done means output plus evidence, validation, and limitations.**

### Why

Agents can generate completion narratives without completing the task. The final answer may sound confident while validation was not run, artifact files are broken, or risks remain undisclosed.

### Derived from

- Non-zero Fallibility
- External Groundability

### Practice

Require final outputs to include:

- what changed or what was decided;
- evidence inspected;
- validation run;
- validation result;
- known limitations;
- unverified items;
- remaining risks.

Central constraint:

```text
final_claims ⊆ validated_evidence
```

### Corollaries

- “Should work” is not a completion claim.
- If validation was not run, say so explicitly.
- Confidence should track evidence strength.

## 9. Drift Regression Law

**Skills are drifting controllers and need evals, versions, and regression cases.**

### Why

Models change. Tool behavior changes. APIs change. Repositories change. User behavior changes. A skill that works today can regress tomorrow.

### Derived from

- Drift
- Non-zero Fallibility

### Practice

Every important skill change should state:

- target failure;
- proposed change;
- expected benefit;
- expected cost;
- evals updated;
- rollback condition.

### Corollaries

- A skill without evals is an author belief.
- A skill should have trigger evals before its trigger boundary becomes complex.
- A skill should have output evals before it is called production-grade.
- Historical failures should become regression cases.

## Summary table

| Law | Main target |
|---|---|
| Trigger Boundary | Wrong activation |
| Task Compilation | Misread user intent |
| Context Economy | Context bloat |
| Evidence Externalization | Stale or imagined facts |
| Trajectory Constraint | Bad plausible action paths |
| Freedom-Risk | Unsafe or overfree behavior |
| Deterministic Delegation | Fragile free-form execution |
| Completion Proof | Completion hallucination |
| Drift Regression | Long-term decay |
