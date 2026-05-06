# Skill Review Rubric

Score each category from 1 to 5.

| Score | Meaning |
|---|---|
| 1 | Missing or actively harmful |
| 2 | Present but weak |
| 3 | Usable but incomplete |
| 4 | Strong |
| 5 | Production-grade |

## Rubric

| Dimension | Score | Notes |
|---|---:|---|
| Skill-worthiness: repeated, stable, evaluatable task distribution | | |
| Activation Control: clear description, use/not-for/near-miss | | |
| Intent Control: modes, input contract, non-goals | | |
| State Control: source of truth, evidence hierarchy, freshness policy | | |
| Trajectory Control: workflow, hard gates, stops, fallback | | |
| Execution Control: deterministic work delegated to tools/scripts | | |
| Completion Control: validation, proof fields, limitations | | |
| Evolution Control: evals, regression, patch hypothesis | | |
| Context Economy: main SKILL.md is smallest sufficient controller | | |
| Safety: fail-closed, approvals, no hidden risky behavior | | |

## Overall rating

- 45-50: Production-grade skill
- 38-44: Strong reusable skill
- 30-37: Usable but needs eval/resources
- 20-29: Prompt-like checklist
- <20: Do not publish as a full skill

## Review questions

1. What failure mode does this skill reduce?
2. What new costs does it introduce?
3. What new risks does it introduce?
4. What evidence proves it improves over baseline?
5. What should be moved out of `SKILL.md`?
6. What deterministic work should be scripted?
7. What claims must be forbidden unless validated?
8. What historical failure should become an eval?
