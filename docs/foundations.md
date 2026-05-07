# Foundations: Definitions, Postulates, Design Laws, and Formulas

ASCT uses several terms that sound mathematical: definition, postulate, law, theorem, corollary, and formula. This document fixes the level of each term so the theory stays precise without pretending to be physics.

## 1. Levels of claim

| Term | Meaning in ASCT | Example |
|---|---|---|
| Definition | A stipulated meaning used inside the theory | “A skill is a selectively loaded policy controller.” |
| Postulate | A foundational assumption about current LLM agents and skill systems | “Context, attention, and safety budget are finite.” |
| Derived claim | A claim that follows from definitions and postulates | “A skill with poor activation can reduce reliability even if its workflow is good.” |
| Design law | A stable engineering rule derived from the theory and supported by practice | “Models judge; tools execute deterministically.” |
| Corollary | A practical consequence of a design law | “Parse-heavy validation belongs in scripts, not prose.” |
| Formula | A compact evaluation model, usually approximate | `SkillValue = SuccessGain - Cost - Risk` |

ASCT does not claim natural-law precision. A design law is not like the speed of light. It is a durable engineering rule under the current agent model: context-conditioned LLMs, finite context, tool use, external files, non-zero error rates, and evolving environments.

## 2. Why postulates, not axioms

The word “axiom” suggests a formal mathematical system. ASCT is an engineering theory. Its basic assumptions are better called **postulates**: claims we treat as true for the purpose of designing skills.

If future agents have infinite context, perfect grounding, zero wrong-trigger rate, deterministic execution, and no safety risk, ASCT will no longer be the right theory. That is acceptable. ASCT is designed for the agents we actually build with: context-conditioned models that operate with files, tools, resources, and fallible action trajectories.

## 3. The object of the theory

ASCT studies skills, not all prompts or all agent applications.

A skill is a special kind of control artifact because it is:

1. **Packaged**: usually a directory with `SKILL.md` and optional resources.
2. **Selectable**: it is not always active.
3. **Contextual**: it changes behavior by entering the agent context.
4. **Portable**: it can be installed, shared, reviewed, and versioned.
5. **Composable**: it may coexist with other skills, commands, hooks, and repo-level instructions.

These properties make skill design different from ordinary prompt writing. A prompt can be useful once. A skill must work repeatedly across a task distribution.

## 4. The minimal formal model

ASCT models an agent as a context-conditioned policy:

```text
Agent = π(action | context, tools, observations, memory)
```

A skill changes the conditions under which the agent selects actions:

```text
Base agent:
  π0(action | C)

Skill-activated agent:
  πs(action | C + I_s + R_s + T_s + V_s)
```

Where:

- `C` is the original context.
- `I_s` is skill instruction, usually `SKILL.md`.
- `R_s` is references, assets, or project memory.
- `T_s` is tool or script affordance.
- `V_s` is validation policy.

The goal is not to maximize instruction. The goal is to improve task success under acceptable cost and risk.

## 5. Definitions

### Agent

A context-conditioned system that selects actions using the current prompt, installed tools, observations, and available memory.

### Skill

A selectively loaded policy controller that changes an agent’s behavior for a recurring class of tasks.

### Task distribution

A recurring set of tasks with similar inputs, constraints, desired outputs, success criteria, and failure modes.

A task distribution is not a single prompt. For example, “review this PR” is one task instance. “Review completed frontend diffs before merge for correctness, rendering, accessibility, performance, and maintainability risk” is a task distribution.

### Failure mode

A high-probability path by which the base agent fails on the task distribution.

A failure mode should be operational, not ornamental. “The agent is not careful enough” is weak. “The agent patches symptoms before establishing a reproducible pass/fail signal” is a useful failure mode.

### Control surface

A part of agent behavior that a skill can influence: activation, intent, state, trajectory, execution, completion, or evolution.

### Evidence

Externally observable support for a claim. Evidence may include file contents, diffs, logs, official documentation, command output, tests, screenshots, rendered artifacts, user-provided documents, issue history, or persistent project memory.

### Completion proof

The evidence and validation required before the agent may claim a task is done.

### Placement decision

The decision of where a control should live: skill, command, hook, script, reference, asset, project memory, global instruction, or collection-level routing.

This is a first-class design decision. Not every useful rule should become skill prose.

## 6. The five postulates

### P1. Conditional Policy

Agent behavior changes with context, instructions, tools, observations, and resources.

If agent behavior were not conditionable, skills could not work. A skill matters because it changes what the agent sees, what it treats as relevant, what actions it considers, and what claims it is allowed to make.

### P2. Bounded Resources

Context, attention, tool calls, execution time, user patience, monetary budget, and safety budget are finite.

Therefore, a skill is not better because it is longer. The best skill is the smallest controller that reliably reduces the target failure modes.

### P3. Non-zero Fallibility

Agents have non-zero error rates in activation, intent inference, state grounding, trajectory selection, execution, and completion claims.

Therefore, skill design should be failure-mode first. The author should ask “how does the base agent fail here?” before asking “what should the skill say?”

### P4. External Groundability

Many task-relevant facts and deterministic operations can be handled more reliably by external evidence and tools than by model generation alone.

Therefore, a mature skill moves current facts out of latent model memory and moves deterministic work out of free-form language generation.

### P5. Drift

Models, tools, APIs, repositories, organizations, task distributions, and user habits change over time.

Therefore, skills are not static documents. They are drifting controllers that need evaluation, versioning, compatibility notes, and regression cases.

## 7. From postulates to design laws

The nine design laws are not arbitrary best practices. They follow from the postulates.

- Because behavior is conditionable and skills are selectively loaded, activation matters.
- Because resources are bounded, context economy matters.
- Because agents are fallible, workflow must constrain bad paths.
- Because external evidence can be stronger than latent memory, state grounding matters.
- Because deterministic tools can outperform generation on certain operations, scripts matter.
- Because agents can claim completion without evidence, completion proof matters.
- Because the environment drifts, regression matters.

This chain is what makes ASCT a theory rather than a checklist.

## 8. The role of formulas

The SkillValue formula is not a calculator. It is a reasoning scaffold.

```text
SkillValue(s, D) =
  E_t~D[Success(agent_with_skill, t) - Success(base_agent, t)]
  - Cost(s, D)
  - Risk(s, D)
```

Its purpose is to make hidden trade-offs visible. A skill can increase success on one task while reducing reliability elsewhere through wrong triggers, context crowding, user friction, unsafe tool use, or maintenance drift.

The safety constraint is not merely a cost term:

```text
SafetyRisk(s, D) <= SafetyBudget
```

A skill can be high-performing and still inadmissible if it requires unacceptable risk.

## 9. What would falsify or weaken ASCT

ASCT would need revision if one of these assumptions becomes false:

- Skills no longer work by selective context and resource loading.
- Agent behavior no longer depends meaningfully on runtime instructions.
- Context and attention become effectively unbounded.
- Agents become perfectly grounded and deterministic on the relevant tasks.
- External tools no longer provide reliability advantages.
- Skill environments stop drifting.

These conditions do not hold for current skill systems. Until they do, ASCT should remain useful.
