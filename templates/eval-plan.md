# Skill Eval Plan

## Skill

**Name:**

**Version / commit:**

**Task distribution:**

## Baseline

Compare against:

- [ ] no skill
- [ ] previous version
- [ ] competing skill
- [ ] human rubric only

## Trigger evals

| Case ID | User prompt | Expected trigger? | Expected mode | Notes |
|---|---|---:|---|---|
| pos-001 | | yes | | |
| neg-001 | | no | | |
| near-001 | | no or different skill | | |
| safety-001 | | safety redirect | | |

## Process evals

| Case ID | Required behavior | Pass criteria |
|---|---|---|
| proc-001 | | |

Examples:

- Reads actual diff before summarizing.
- Establishes pass/fail loop before debugging.
- Does not perform external action without approval.
- Stops after repeated failed hypotheses.

## Output evals

| Case ID | Expected output property | Pass criteria |
|---|---|---|
| out-001 | | |

Examples:

- Each finding has evidence.
- Final claims map to validation.
- Unknowns are labeled.
- No process chatter in public artifact.

## Safety evals

| Case ID | Risk | Expected behavior |
|---|---|---|
| safe-001 | | |

## Metrics

| Metric | Measurement |
|---|---|
| Trigger precision | |
| Trigger recall | |
| Near-miss false positive rate | |
| Output quality | |
| Unsupported claims | |
| Validation rate | |
| Token/context cost | |
| User friction | |
| Safety incidents | |

## Decision

- [ ] Keep
- [ ] Revise
- [ ] Deprecate
- [ ] Split
- [ ] Merge

**Rationale:**
