# Agent Skill Control Theory

Agent Skill Control Theory (ASCT) is a first-principles framework for designing and evaluating LLM agent skills.

It is intentionally narrower than general agent architecture. It focuses on skills: portable, filesystem-like packages that use `SKILL.md`, metadata, references, scripts, assets, and progressive disclosure to guide an agent on specific task distributions.

## 1. The central claim

The central claim of ASCT is:

```text
A skill is a selectively loaded policy controller for an LLM agent.
```

This definition is compact, but each word matters.

- **Skill**: a reusable package that changes agent behavior on a recurring task distribution.
- **Selectively loaded**: the skill is not always active. It is chosen through explicit invocation, implicit matching, or host-specific routing.
- **Policy controller**: the skill changes the agent's action distribution. It makes some paths more likely, some paths less likely, and some paths forbidden.
- **LLM agent**: the target is not a static text generator. The agent may read files, call tools, execute code, inspect outputs, revise plans, and affect external state.

This is why a skill is not merely a prompt. A prompt asks for a response. A skill controls a recurring agent behavior pattern.

## 2. Why prompt collections are not enough

A prompt collection can improve local behavior. But a skill system must solve harder problems:

1. **Activation**: the agent must know when to use the skill and when not to use it.
2. **Ambiguity**: the agent must interpret vague user requests as task frames.
3. **State**: the agent must ground itself in the current repository, document, tool, or environment.
4. **Trajectory**: the agent must avoid plausible but wrong next steps.
5. **Execution**: the agent must delegate deterministic operations to tools.
6. **Completion**: the agent must not claim success without evidence.
7. **Evolution**: the skill must avoid drift as models, tools, APIs, and workflows change.

A prompt collection usually contains advice. A skill system contains controls.

## 3. The minimal agent model

ASCT models an LLM agent as:

```text
Agent = π(action | context, tools, observations, memory)
```

The agent selects actions under the influence of context, installed tools, observations, and memory. A skill changes these conditions.

```text
Base agent:
  π0(action | C)

Skill-activated agent:
  πs(action | C + I_s + R_s + T_s + V_s)
```

Where:

- `I_s`: runtime instructions, usually `SKILL.md`.
- `R_s`: references, assets, project memory, or other external context.
- `T_s`: tools or scripts made salient by the skill.
- `V_s`: validation and completion rules.

The skill does not replace the agent. It shapes the agent.

## 4. Why the standard skill structure matters

The public Agent Skills format defines a skill as a directory containing at minimum a `SKILL.md` file with YAML frontmatter and Markdown body. Optional directories include `scripts/`, `references/`, and `assets/`.

ASCT interprets these files as control functions:

| Artifact | Control function |
|---|---|
| `description` | Activation classifier |
| `SKILL.md` | Runtime controller |
| `references/` | External semantic memory |
| `scripts/` | Deterministic executors |
| `assets/` | Reusable material priors |
| `evals/` | Controller regression tests |

This mapping follows from progressive disclosure. Metadata is visible before activation. The full `SKILL.md` is loaded only after activation. References, scripts, and assets are used only when needed.

Progressive disclosure is not just a packaging convenience. It is a theory of context economy. It lets the skill author decide what must be visible for selection, what must be visible after activation, and what should remain available but not loaded by default.

## 5. The five postulates

ASCT rests on five postulates.

### P1. Conditional Policy

Agent behavior changes with context, instructions, tools, observations, and resources.

A skill works only because the agent's behavior is conditionable. If instructions, examples, scripts, references, and validation rules did not change the policy, skill authoring would be pointless.

### P2. Bounded Resources

Context, attention, tool calls, execution time, user patience, monetary budget, and safety budget are finite.

This means a longer skill is not automatically a better skill. Overly broad instructions can crowd out task evidence. Too many installed skills can weaken activation. Too many validation steps can create friction. Too many scripts can increase audit cost.

### P3. Non-zero Fallibility

Agents have non-zero error rates in activation, intent inference, state grounding, trajectory selection, execution, and completion claims.

Therefore, skill design should begin with failure modes. A skill is justified when it reduces a repeated, meaningful failure mode at acceptable cost.

### P4. External Groundability

Many task-relevant facts and deterministic operations can be handled more reliably by external evidence and tools than by model generation alone.

This is the basis for reading files, inspecting diffs, using official docs, running tests, rendering artifacts, validating schemas, and using scripts.

### P5. Drift

Models, tools, APIs, repositories, organizations, task distributions, and user habits change over time.

Therefore, a skill should be evaluated and maintained. Its trigger behavior, output quality, safety posture, and maintenance cost can all regress.

## 6. The seven control surfaces

ASCT names seven places where a skill can control agent behavior.

### 6.1 Activation Control

Question: **Should this skill be used?**

Activation Control is implemented through `name`, `description`, explicit commands, not-for boundaries, adjacent skill routing, generated indexes, and trigger evals.

A bad activation classifier can make a good skill harmful. If a debugging skill activates for ordinary code review, it may force unnecessary root-cause analysis. If a release skill activates for release-note writing, it may introduce unsafe external action assumptions.

### 6.2 Intent Control

Question: **What task is the user actually asking for?**

User utterances are compressed. “Check this” may mean review, debug, redesign, rewrite, test, release, explain, or decide. A skill compiles this utterance into a task frame and a runtime mode.

Mechanisms include mode routing, input contracts, clarification gates, non-goals, and safety redirects.

### 6.3 State Control

Question: **What is true right now?**

State Control prevents the agent from relying on stale memory or imagined facts. It uses current files, diffs, logs, official docs, test output, screenshots, rendered artifacts, issue history, ADRs, glossaries, and project memory.

The core rule is: current facts should be externalized.

### 6.4 Trajectory Control

Question: **What path should the agent follow?**

Trajectory Control is the skill's workflow layer. But workflow is not ceremony. It exists to reduce the probability of bad action paths.

Good trajectory control includes hard gates, stop conditions, fallback paths, escalation rules, handoff formats, and validation checkpoints.

### 6.5 Execution Control

Question: **Which operations require deterministic tools?**

Execution Control decides which parts of the task should be handled by scripts, validators, renderers, parsers, linters, dry-runs, or other tools.

The guiding distinction is:

```text
Models judge. Tools execute deterministically.
```

### 6.6 Completion Control

Question: **When may the agent claim done?**

Completion Control suppresses completion hallucination. It requires proof fields, validation results, claim-evidence mapping, confidence levels, known limitations, and unverified-work disclosure.

The central constraint is:

```text
final_claims ⊆ validated_evidence
```

### 6.7 Evolution Control

Question: **How does the skill avoid drift and regression?**

Evolution Control uses trigger evals, output evals, safety evals, regression suites, versioning, compatibility notes, and patch hypotheses.

A skill without evaluation is an author belief, not an engineering asset.

## 7. Placement decisions

ASCT does not say that every useful control should become a skill. It says every control should be placed where it reduces failure with the least cost and risk.

Possible placements include:

| Placement | Best for |
|---|---|
| Skill | Selectively loaded workflow for a recurring task distribution |
| Global instruction | Always-on norms and engineering discipline |
| Command | Explicit macro workflow or multi-skill orchestration |
| Hook | Lifecycle gate, dangerous action block, or automatic state refresh |
| Script | Deterministic, parse-heavy, numerical, repeatable, or format-sensitive work |
| Reference | Long or conditional knowledge |
| Asset | Reusable templates, schemas, data files, or examples |
| Repo memory | Project glossary, ADRs, agent briefs, known constraints, out-of-scope records |
| Collection routing | Priority, conflict resolution, installation scope, and skill graph design |

A mature skill author does not ask only “what should this skill say?” They ask “where should this control live?”

## 8. Skill collections

Real-world skill systems often contain multiple skills plus commands, hooks, indexes, marketplace metadata, global instructions, and repo memory. ASCT treats this as collection-level design, not a new primitive.

At collection scale, the same control surfaces appear again:

- Activation Control becomes routing and discovery.
- Intent Control becomes command design and task decomposition.
- State Control becomes shared project memory and generated indexes.
- Trajectory Control becomes skill graph design.
- Execution Control becomes shared scripts, hooks, and tool policies.
- Completion Control becomes cross-skill handoff contracts.
- Evolution Control becomes versioning, regression, deprecation, and release governance.

The theory stays the same. The scope changes.

## 9. The design laws

The nine design laws translate ASCT into authoring practice.

1. **Trigger Boundary Law**: a skill's first quality is correct activation.
2. **Task Compilation Law**: a skill compiles user utterances into task frames and runtime modes.
3. **Context Economy Law**: every token in `SKILL.md` should buy behavior change.
4. **Evidence Externalization Law**: current facts should come from external evidence, not latent memory.
5. **Trajectory Constraint Law**: workflow exists to make bad paths harder to take.
6. **Freedom-Risk Law**: higher-risk tasks require lower agent freedom.
7. **Deterministic Delegation Law**: models judge; tools execute deterministically.
8. **Completion Proof Law**: done means output plus evidence, validation, and limitations.
9. **Drift Regression Law**: skills are drifting controllers and need evals, versions, and regression tests.

These laws are developed in [design-laws.md](design-laws.md).

## 10. Value and safety

ASCT evaluates a skill by net reliability gain:

```text
SkillValue(s, D) =
  E_t~D[Success(agent_with_skill, t) - Success(base_agent, t)]
  - Cost(s, D)
  - Risk(s, D)
```

A skill is admissible only if:

```text
SafetyRisk(s, D) <= SafetyBudget
```

Then it is worth keeping only if:

```text
SkillValue(s, D) > 0
```

This prevents two common mistakes:

1. Treating more rules as more reliability.
2. Treating task success as sufficient even when safety or maintenance risk is unacceptable.

## 11. The ASCT design loop

A practical design loop:

1. Define the task distribution.
2. Identify base-agent failure modes.
3. Decide placement.
4. Choose control surfaces.
5. Write activation classifier.
6. Write runtime controller.
7. Externalize evidence and long memory.
8. Delegate deterministic work.
9. Define completion proof.
10. Add evals and regression cases.
11. Evolve through patch hypotheses.

## 12. What ASCT is not

ASCT is not:

- an official Agent Skills specification;
- a universal theory of all LLM applications;
- a claim that every skill needs every control surface;
- a reason to over-structure simple tasks;
- a substitute for domain expertise;
- a substitute for empirical evaluation;
- an excuse to put every useful rule into `SKILL.md`.

ASCT is a design lens. It helps skill authors ask what a skill controls, what it costs, what it risks, and whether it improves behavior on a real task distribution.
