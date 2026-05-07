# Agent Skill Control Theory

**Agent Skill Control Theory** (ASCT) is a first-principles framework for designing, reviewing, evaluating, and evolving LLM agent skills.

The practical slogan is **Skill Mechanics**: a skill is not a longer prompt, a personality, or a knowledge dump. A skill is a selectively loaded control layer that changes how an LLM agent behaves on a recurring class of tasks.

```text
Skill = a selectively loaded policy controller for an LLM agent.
```

More explicitly:

```text
A skill is a packaged control layer that activates for a task distribution.
It changes an agent's action distribution by adding instructions, external context,
deterministic executors, reusable materials, and validation rules.
```

Chinese version: [README.zh-CN.md](README.zh-CN.md).

## Status

This is a working engineering theory, not an official standard.

ASCT is built on the public Agent Skills format and the progressive disclosure model described by:

- [Agent Skills specification](https://agentskills.io/specification)
- [OpenAI Codex skills documentation](https://developers.openai.com/codex/skills)
- [Anthropic Agent Skills overview](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

The theory is deliberately narrower than general LLM application architecture. It focuses on filesystem-like skills built around `SKILL.md`, metadata, references, scripts, assets, and skill-specific evaluation.

Many ASCT principles also apply to agents, prompt routers, workflow engines, and tool-using LLM systems. However, ASCT treats skills as a specific design object: a portable, selectively loaded behavior package.

## Why this theory exists

Skill repositories often begin as useful prompt collections. That works for a while. Then the collection tends to drift into recurring failure modes:

1. **Anecdote accumulation**: every new failure adds one more rule.
2. **Context inflation**: `SKILL.md` becomes a suitcase full of every possible concern.
3. **Wrong activation**: a good skill becomes harmful when loaded for the wrong task.
4. **Unverified completion**: the agent says the task is done because the answer sounds complete.
5. **Placement mistakes**: rules that should be scripts, hooks, references, or global instructions are written as skill prose.
6. **Unmeasured confidence**: the author believes the skill improved because it feels more complete.

ASCT starts from the agent, not from examples. It asks:

```text
What failure modes does the base agent have on this task distribution?
Which control surfaces can a skill influence?
What is the cheapest safe controller that reduces those failures?
How do we know it actually helped?
```

## Core mapping

ASCT maps common skill artifacts to control functions:

| Skill artifact | ASCT role | Main question |
|---|---|---|
| `description` | Activation classifier | Should this skill be used? |
| `SKILL.md` | Runtime controller | What should the agent do after activation? |
| `references/` | External semantic memory | What long or conditional knowledge should be loaded only when needed? |
| `scripts/` | Deterministic executors | What should not be done by free-form generation? |
| `assets/` | Reusable material priors | What templates, examples, schemas, or static resources should the agent reuse? |
| `evals/` | Controller regression tests | How do we know the skill improved behavior and did not regress? |

Host-specific artifacts such as commands, hooks, status lines, `AGENTS.md`, `CLAUDE.md`, `llms.txt`, marketplace metadata, generated indexes, planning files, and project memory files are also useful. ASCT treats them as implementation mechanisms that map back to the same control surfaces. They are not new primitives.

## Five postulates

ASCT uses five foundational assumptions.

1. **Conditional Policy**: Agent behavior changes with context, instructions, tools, observations, and resources.
2. **Bounded Resources**: Context, attention, tool calls, time, user patience, and safety budget are finite.
3. **Non-zero Fallibility**: Agents have non-zero error rates in activation, intent inference, state grounding, trajectory selection, execution, and completion claims.
4. **External Groundability**: Many task-relevant facts and deterministic operations can be handled more reliably by external evidence and tools than by model generation alone.
5. **Drift**: Models, tools, APIs, repositories, organizations, and task distributions change over time.

These are not philosophical decorations. They explain why skill design needs activation boundaries, progressive disclosure, evidence policies, deterministic scripts, completion proof, and regression tests.

## Seven control surfaces

A skill may influence seven parts of agent behavior:

| Control surface | Question it controls |
|---|---|
| Activation Control | Should this skill be used? |
| Intent Control | What task is the user actually asking for? |
| State Control | What is true right now? |
| Trajectory Control | What path should the agent follow? |
| Execution Control | Which operations require deterministic tools? |
| Completion Control | When may the agent claim done? |
| Evolution Control | How does the skill avoid drift and regression? |

A skill does not need every control surface. A small writing skill may need activation and style control. A release skill may need activation, state, trajectory, execution, completion, safety, and evolution control.

## Nine design laws

ASCT derives nine engineering design laws from the postulates.

1. **Trigger Boundary Law**: A skill's first quality is correct activation.
2. **Task Compilation Law**: A skill compiles user utterances into task frames and modes.
3. **Context Economy Law**: Every token in `SKILL.md` should buy behavior change.
4. **Evidence Externalization Law**: Current facts should come from external evidence, not latent memory.
5. **Trajectory Constraint Law**: Workflow exists to make bad paths harder to take.
6. **Freedom-Risk Law**: Higher-risk tasks require lower agent freedom.
7. **Deterministic Delegation Law**: Models judge; tools execute deterministically.
8. **Completion Proof Law**: Done means output plus evidence, validation, and limitations.
9. **Drift Regression Law**: Skills are drifting controllers and need evals, versions, and regression tests.

## Value function

ASCT evaluates skills by net reliability gain, not instruction length, elegance, or author confidence.

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

A skill is worth keeping only if:

```text
SkillValue(s, D) > 0
```

The equation is not a physical law. It is an evaluation frame. Its purpose is to prevent a common mistake: mistaking more instruction for more reliability.

## Repository contents

```text
docs/
  theory.md                 Full ASCT theory
  foundations.md            Definitions, postulates, laws, and formulas
  control-surfaces.md       The seven control surfaces
  design-laws.md            The nine design laws
  placement.md              Deciding where a control should live
  host-artifacts.md         Commands, hooks, status lines, AGENTS.md, llms.txt, and related mechanisms
  collection-design.md      Designing skill collections and skill graphs
  value-function.md         Success, cost, risk, and measurement
  evaluation.md             Trigger, output, process, safety, and regression evals
  safety.md                 Safety constraints for skills and skill collections
  glossary.md               Core terms
  influences.md             Public sources and design influences
  zh-CN/                    Chinese versions

templates/
  skill-ir.yaml             Internal representation for designing a skill
  collection-ir.yaml        Internal representation for designing a skill collection
  placement-decision.md     Template for deciding where a control belongs
  skill-design-brief.md     Scenario and failure-map template
  skill-review-rubric.md    Review rubric for existing skills
  eval-plan.md              Evaluation planning template
  patch-hypothesis.md       Skill change proposal template
  trigger-evals.json        Trigger eval fixture template
  output-eval-rubric.yaml   Output eval rubric template
  zh-CN/                    Chinese template versions

examples/
  frontend-debug/           A synthetic skill designed with ASCT

scripts/
  check_repo.py             Lightweight repository checks
```

## How to use ASCT

When designing a new skill:

1. Define the task distribution.
2. Identify likely base-agent failure modes.
3. Decide whether the control should be a skill, command, hook, script, reference, repo memory, or global instruction.
4. Choose the relevant control surfaces.
5. Write the activation classifier in `description`.
6. Write the runtime controller in `SKILL.md`.
7. Move long and conditional knowledge to `references/`.
8. Move deterministic checks to `scripts/`.
9. Define completion proof.
10. Add trigger, output, process, safety, and regression evals.
11. Evolve through patch hypotheses, not author confidence.

When reviewing an existing skill:

1. Ask which task distribution it claims to serve.
2. Ask which failure modes it reduces.
3. Map its artifacts to control surfaces.
4. Estimate context cost, friction cost, runtime cost, and safety risk.
5. Check whether final claims are tied to evidence.
6. Look for near-miss trigger cases.
7. Decide whether some content belongs outside `SKILL.md`.
8. Require evals before calling the change an improvement.

## Design stance

ASCT is intentionally disciplined about theory growth.

New repositories, platforms, or host artifacts should not automatically add new primitives. First map them to the five postulates, seven control surfaces, and nine design laws. Change the core only if the new case exposes a failure mode that cannot be explained by the current theory.

## Quick start

Run repository checks:

```bash
python3 scripts/check_repo.py
```

Start designing a skill from:

```text
templates/skill-ir.yaml
templates/skill-design-brief.md
templates/skill-review-rubric.md
templates/eval-plan.md
```

For collection-level design, start from:

```text
templates/collection-ir.yaml
```

For placement decisions, start from:

```text
templates/placement-decision.md
```

## License

MIT. See [LICENSE](LICENSE).
