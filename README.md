# Agent Skill Control Theory

**Agent Skill Control Theory (ASCT)** is a first-principles framework for designing, reviewing, and evolving **LLM agent skills**.

A skill is not just a longer prompt. In ASCT, a skill is a **selectively loaded policy controller**: it changes how an agent behaves in a specific task distribution by adding instructions, resources, tools, scripts, and validation rules.

> Short version: ASCT studies how to control LLM agent failure modes with skills.

中文版本见 [README.zh-CN.md](README.zh-CN.md).

## Status

This is a working theory, not an official standard.

It builds on the public Agent Skills format and the progressive disclosure model described by the Agent Skills specification, OpenAI Codex skills documentation, and Anthropic’s Agent Skills documentation:

- Agent Skills specification: https://agentskills.io/specification
- OpenAI Codex skills: https://developers.openai.com/codex/skills
- Anthropic Agent Skills overview: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- Claude Agent Skills docs: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview

ASCT is intended to be portable across Claude, Codex, and other filesystem-based skill implementations, while staying grounded in the common `SKILL.md + references/scripts/assets` structure.

## Core definition

```text
Skill = a selectively loaded policy controller for an LLM agent.
```

More explicitly:

```text
A skill is a packaged control layer that is activated for a class of tasks.
It changes an agent's action distribution by supplying runtime instructions,
external context, deterministic executors, reusable materials, and validation rules.
```

ASCT maps common skill files to control functions:

| Skill artifact | ASCT role |
|---|---|
| `description` | Activation classifier |
| `SKILL.md` | Runtime controller |
| `references/` | External semantic memory |
| `scripts/` | Deterministic executors |
| `assets/` | Reusable material priors |
| `evals/` | Controller regression tests |

## Five postulates

1. **Conditional Policy**: Agent behavior changes with context, instructions, tools, observations, and resources.
2. **Bounded Resources**: Context, attention, tool calls, time, user patience, and safety budget are finite.
3. **Non-zero Fallibility**: Agents have non-zero error rates in activation, intent inference, state grounding, trajectory selection, execution, and completion claims.
4. **External Groundability**: Many task-relevant facts and deterministic operations can be handled more reliably by external evidence and tools than by model generation alone.
5. **Drift**: Models, tools, APIs, repositories, organizations, and task distributions change over time.

## Seven control surfaces

| Control surface | Question it controls |
|---|---|
| Activation Control | Should this skill be used? |
| Intent Control | What task is the user actually asking for? |
| State Control | What is true right now? |
| Trajectory Control | What path should the agent follow? |
| Execution Control | Which operations require deterministic tools? |
| Completion Control | When may the agent claim done? |
| Evolution Control | How does the skill avoid drift and regression? |

## Nine design laws

1. **Trigger Boundary Law**: A skill’s first quality is correct activation.
2. **Task Compilation Law**: A skill compiles user utterances into task frames and modes.
3. **Context Economy Law**: Every token in `SKILL.md` should buy behavior change.
4. **Evidence Externalization Law**: Current facts should come from external evidence, not latent memory.
5. **Trajectory Constraint Law**: Workflow exists to make bad paths harder to take.
6. **Freedom-Risk Law**: Higher-risk tasks require lower agent freedom.
7. **Deterministic Delegation Law**: Models judge; tools execute deterministically.
8. **Completion Proof Law**: Done means output plus evidence, validation, and limitations.
9. **Drift Regression Law**: Skills are drifting controllers and need evals, versioning, and regression tests.

## Value function

ASCT evaluates skills by **net reliability gain**, not instruction length or elegance.

```text
SkillValue(s, D) =
  E_t~D[Success(agent_with_skill, t) - Success(base_agent, t)]
  - Cost(s, D)
  - Risk(s, D)
```

A skill is worth keeping only when:

```text
SkillValue > 0
SafetyRisk <= acceptable_threshold
```

## Repository contents

```text
docs/
  theory.md                 Full ASCT theory
  glossary.md               Core terms
  control-surfaces.md       Seven control surfaces
  design-laws.md            Nine design laws
  value-function.md         SkillValue model
  safety.md                 Safety constraints
  influences.md             Public sources and design influences
  zh-CN/                    Chinese versions

templates/
  skill-ir.yaml             Internal representation for designing skills
  skill-design-brief.md     Scenario and failure map template
  skill-review-rubric.md    Review rubric for existing skills
  eval-plan.md              Trigger/output/safety eval planning template
  patch-hypothesis.md       Change proposal template

templates/zh-CN/              Chinese template versions

examples/
  frontend-debug/           A synthetic example skill built with ASCT

scripts/
  check_repo.py             Lightweight repository checks
```

## Should this repository mention public skill repositories?

The core theory intentionally does **not** rank or critique specific public repositories.

This keeps the theory stable and prevents it from becoming stale when those repositories evolve. The public repositories that informed the framework are mentioned only in [docs/influences.md](docs/influences.md), without repository-specific judgments.

If you want case studies, add them as separate, dated essays under `case-studies/`, not inside the core theory.

## How to use ASCT

When designing a new skill:

1. Define the task distribution.
2. Map the agent’s likely failure modes.
3. Choose the relevant control surfaces.
4. Write the activation classifier in `description`.
5. Write the runtime controller in `SKILL.md`.
6. Move long references to `references/`.
7. Move deterministic checks to `scripts/`.
8. Define completion proof.
9. Add trigger, output, and safety evals.
10. Evolve through patch hypotheses, not author confidence.

## Quick start

```bash
python3 scripts/check_repo.py
```

To design a skill, start from:

```text
templates/skill-ir.yaml
templates/skill-design-brief.md
templates/skill-review-rubric.md
```

## License

MIT. See [LICENSE](LICENSE).
