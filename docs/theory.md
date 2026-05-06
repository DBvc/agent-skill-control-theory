# Agent Skill Control Theory

Agent Skill Control Theory (ASCT) is a first-principles framework for designing and evaluating LLM agent skills.

It is intentionally narrower than general agent architecture. It focuses on **skills**: filesystem-like packages that use `SKILL.md`, metadata, references, scripts, assets, and progressive disclosure to guide an agent on specific task distributions.

## 1. Why a theory is needed

Many skill repositories begin as collections of useful prompts. That works for a while, but prompt collections tend to drift into three failure modes:

1. **Overfitting to anecdotes**: every new failure adds one more rule.
2. **Context inflation**: the main skill file becomes a suitcase full of every possible concern.
3. **Unmeasured confidence**: authors believe a skill is better because it feels more complete.

ASCT starts from the agent, not from existing skill examples.

An LLM agent can be modeled as:

```text
Agent = π(action | context, tools, observations, memory)
```

The agent chooses actions under the influence of context, tools, observations, and memory. A skill matters because it changes those conditions.

## 2. Core definition

```text
Skill = a selectively loaded policy controller for an LLM agent.
```

A skill is not merely a knowledge bundle. It is a control layer that activates for a task distribution and changes the agent's action distribution.

The common skill structure maps naturally to control functions:

| Artifact | Control function |
|---|---|
| `description` | Activation classifier |
| `SKILL.md` | Runtime controller |
| `references/` | External semantic memory |
| `scripts/` | Deterministic executors |
| `assets/` | Material priors |
| `evals/` | Controller regression tests |

This mapping is not only stylistic. It follows from progressive disclosure: metadata is always visible, the full `SKILL.md` is loaded only after activation, and additional files are accessed only when needed.

## 3. Definitions

### Agent

A context-conditioned policy system that selects actions using the current prompt, tools, observations, and memory.

### Skill

A selectively loaded policy controller that changes an agent’s behavior for a class of tasks.

### Task distribution

A recurring set of tasks with similar inputs, constraints, desired outputs, and failure modes.

### Failure mode

A high-probability path by which the base agent fails on the task distribution.

### Control surface

A part of agent behavior that a skill can influence: activation, intent, state, trajectory, execution, completion, or evolution.

### Evidence

Any externally observable support for a claim: file contents, diffs, logs, official docs, command output, tests, screenshots, rendered artifacts, user statements, or persistent project memory.

### Completion proof

The evidence and validation needed before the agent may claim the task is done.

## 4. Postulates

### P1. Conditional Policy

Agent behavior changes with context, instructions, tools, observations, and resources.

If this were false, skills could not work. A skill is useful only because the agent’s policy is conditionable.

### P2. Bounded Resources

Context, attention, tool calls, execution time, user patience, and safety budget are finite.

Therefore, the right skill is not the longest skill. The right skill is the smallest sufficient controller.

### P3. Non-zero Fallibility

Agents have non-zero error rates in activation, intent inference, state grounding, trajectory selection, execution, and completion claims.

Therefore, skills should be failure-mode first.

### P4. External Groundability

Many task-relevant truths and deterministic operations can be handled more reliably by external evidence and tools than by model generation alone.

Therefore, a mature skill moves facts out of latent memory and moves deterministic work out of free-form language generation.

### P5. Drift

Models, tools, APIs, repositories, organizations, and task distributions change over time.

Therefore, skills are not static documents. They are drifting controllers that need evaluation and regression.

## 5. Seven control surfaces

### 5.1 Activation Control

Question: **Should this skill be used?**

Mechanisms:

- `name`
- `description`
- explicit invocation names
- not-for boundaries
- adjacent skill routing
- trigger evals

A bad activation classifier can make a good runtime controller harmful.

### 5.2 Intent Control

Question: **What task is the user actually asking for?**

Mechanisms:

- mode routing
- input contract
- clarification gates
- non-goals
- task frame selection

User utterances are often ambiguous. A skill compiles them into task frames.

### 5.3 State Control

Question: **What is true right now?**

Mechanisms:

- reading files
- inspecting diffs
- official docs
- logs and command output
- rendered screenshots
- project memory such as glossary, ADRs, issue history

State control prevents the agent from acting on stale or imagined facts.

### 5.4 Trajectory Control

Question: **What path should the agent follow?**

Mechanisms:

- workflow
- hard gates
- stop conditions
- fallback paths
- escalation rules
- handoff rules

Workflow is not a ceremony. It is a constraint on bad action paths.

### 5.5 Execution Control

Question: **Which operations require deterministic tools?**

Mechanisms:

- scripts
- validators
- renderers
- linters
- schema checks
- dry-run commands
- dangerous action guards

Models should judge; deterministic tools should execute.

### 5.6 Completion Control

Question: **When may the agent claim done?**

Mechanisms:

- validation commands
- proof fields
- claim-evidence mapping
- confidence levels
- known limitations
- unverified work disclosure

A skill should suppress completion hallucination.

### 5.7 Evolution Control

Question: **How does the skill avoid drift and regression?**

Mechanisms:

- trigger evals
- output evals
- safety evals
- versioning
- patch hypotheses
- regression suites
- compatibility notes

A skill without evaluation is an author belief, not an engineering asset.

## 6. Design laws

### Law 1: Trigger Boundary Law

A skill’s first quality is correct activation.

Wrong activation causes direct harm: wasted context, wrong workflow, unnecessary friction, or unsafe action.

### Law 2: Task Compilation Law

A skill compiles user utterances into task frames and runtime modes.

The user says “check this”; the skill must decide whether that means review, debug, design, release check, rewrite, or decision support.

### Law 3: Context Economy Law

Every token in `SKILL.md` should buy behavior change.

Long theory, exhaustive examples, and domain references belong in `references/` unless they are needed on every activation.

### Law 4: Evidence Externalization Law

Current facts should come from external evidence, not latent memory.

Repository state, official APIs, diffs, rendered artifacts, command output, and user-provided documents should outrank model memory.

### Law 5: Trajectory Constraint Law

Workflow exists to make bad paths harder to take.

“Be careful” is weak. “Do not edit code before establishing a reproducible pass/fail signal” is strong.

### Law 6: Freedom-Risk Law

Higher-risk tasks require lower agent freedom.

Creative tasks need room. Destructive actions, release operations, format-sensitive artifacts, and security-sensitive tasks need gates, dry-runs, and validation.

### Law 7: Deterministic Delegation Law

Models judge; tools execute deterministically.

If the same input should produce the same output, prefer a script, validator, parser, or renderer.

### Law 8: Completion Proof Law

Done means output plus evidence, validation, and limitations.

```text
final_claims ⊆ validated_evidence
```

If validation was not run, the final answer must say so.

### Law 9: Drift Regression Law

Skills are drifting controllers and need evals, versions, and regression tests.

Every skill change should state the failure it tries to reduce, the cost it adds, and the evals that will detect regressions.

## 7. SkillValue

A skill should be judged by net reliability gain:

```text
SkillValue(s, D) =
  E_t~D[Success(agent_with_skill, t) - Success(base_agent, t)]
  - Cost(s, D)
  - Risk(s, D)
```

Where:

- `s` is the skill.
- `D` is the task distribution.
- `Success` is measured by task-specific criteria.
- `Cost` includes trigger cost, context cost, tool cost, user friction, and maintenance cost.
- `Risk` includes safety risk, side-effect risk, privacy risk, and wrong-trigger risk.

A skill is admissible only if:

```text
SafetyRisk(s, D) <= SafetyBudget
```

A skill is worth keeping only if:

```text
SkillValue(s, D) > 0
```

## 8. The ASCT design loop

1. Define the task distribution.
2. Identify likely base-agent failure modes.
3. Choose control surfaces.
4. Write the activation classifier.
5. Write the runtime controller.
6. Externalize evidence and long memory.
7. Delegate deterministic work.
8. Define completion proof.
9. Add evals and regression cases.
10. Evolve through patch hypotheses.

## 9. What ASCT is not

ASCT is not:

- an official Agent Skills specification;
- a universal theory of all LLM applications;
- a claim that every skill needs every control surface;
- a reason to over-structure simple tasks;
- a substitute for domain expertise or evaluation.

ASCT is a design lens. It helps you ask what a skill controls, what it costs, what it risks, and whether it improves behavior on a real task distribution.
