# SkillValue

ASCT evaluates a skill by net reliability gain.

```text
SkillValue(s, D) =
  E_t~D[Success(agent_with_skill, t) - Success(base_agent, t)]
  - Cost(s, D)
  - Risk(s, D)
```

## Terms

- `s`: the skill.
- `D`: the task distribution.
- `agent_with_skill`: the agent after the skill is activated.
- `base_agent`: the same agent without the skill.
- `Success`: a task-specific success measure.
- `Cost`: friction introduced by the skill.
- `Risk`: safety, privacy, side-effect, and wrong-trigger risk.

## Cost components

| Cost | Meaning |
|---|---|
| Trigger cost | The cost of selecting and loading the skill. |
| Context cost | Tokens and attention consumed by skill instructions. |
| Tool cost | Time and runtime cost of tools and scripts. |
| User friction | Extra questions, confirmations, or output weight. |
| Maintenance cost | Future effort to keep the skill correct. |
| Opportunity cost | Other skills or context displaced by this skill. |

## Risk components

| Risk | Meaning |
|---|---|
| Wrong-trigger risk | Skill activates on the wrong task. |
| Safety risk | Skill enables unsafe or illegitimate behavior. |
| Privacy risk | Skill reads or exposes sensitive information. |
| Side-effect risk | Skill performs external or irreversible actions. |
| Over-constraint risk | Skill prevents useful agent creativity or adaptation. |
| Drift risk | Skill becomes stale as environment changes. |

## Acceptance conditions

A skill is admissible only if:

```text
SafetyRisk(s, D) <= SafetyBudget
```

A skill is worth keeping only if:

```text
SkillValue(s, D) > 0
```

## Practical scoring

When exact measurement is unavailable, use a 1-5 rubric for each dimension:

| Dimension | 1 | 5 |
|---|---|---|
| Success gain | No visible improvement | Major improvement over baseline |
| Trigger precision | Frequently wrong | Correct on positives and near-misses |
| Context cost | Bloated | Smallest sufficient controller |
| Validation strength | Claims unsupported | Claims mapped to evidence |
| Safety posture | Risky or vague | Fail-closed with explicit approvals |
| Maintainability | Hard to update | Has evals and patch hypotheses |

A practical decision rule:

```text
Keep if SuccessGain + ValidationStrength + Maintainability
     clearly exceeds ContextCost + Friction + Risk.
```
