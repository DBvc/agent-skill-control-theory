# Evaluation

ASCT treats evals as part of skill engineering, not an optional afterthought.

A skill changes agent behavior. Evaluation asks whether that behavior changed in the intended direction, on the intended task distribution, without unacceptable cost or risk.

## 1. Evaluation targets

Evaluate five behaviors.

| Eval type | Question |
|---|---|
| Trigger eval | Does the skill activate when it should and stay silent when it should not? |
| Process eval | After activation, does the agent follow the intended trajectory? |
| Output eval | Is the final result useful, grounded, and correctly shaped? |
| Safety eval | Does the skill respect safety, privacy, approvals, and external side effects? |
| Regression eval | Do historical failures stay fixed after changes? |

## 2. Baseline comparison

A skill should usually be compared against at least one baseline:

- no skill;
- old version of the skill;
- lighter version of the skill;
- competing skill;
- human-written checklist.

The basic question is:

```text
What does the skill improve that the base agent did not already do reliably?
```

If the base agent already performs the task reliably, a skill may add cost without value.

## 3. Trigger evals

Trigger evals should include:

- positive cases;
- implicit positive cases;
- negative cases;
- near-miss cases;
- adjacent skill conflicts;
- unsafe or out-of-scope cases.

Near-miss cases are the most valuable. Obvious positives only prove the skill can recognize itself when shouted at.

Example:

```json
{
  "positive": [
    {
      "prompt": "Review this completed React diff before merge.",
      "expected": "activate"
    }
  ],
  "near_miss": [
    {
      "prompt": "This button is broken in production. Find the root cause.",
      "expected": "do_not_activate",
      "prefer": "frontend-debug"
    }
  ]
}
```

## 4. Process evals

Process evals check whether the agent followed the critical trajectory.

For a debug skill:

- Did it establish a pass/fail loop before patching?
- Did it form a falsifiable hypothesis?
- Did it avoid patch stacking?
- Did it stop after repeated failed hypotheses?

For an artifact skill:

- Did it use the intended toolchain?
- Did it validate the output file?
- Did it inspect rendered output when needed?

For a release skill:

- Did it confirm target branch, version, artifacts, and approval?
- Did it avoid external side effects before user confirmation?

Process evals matter because the final answer can look good even when the process was unsafe.

## 5. Output evals

Output evals check the final result.

Useful criteria:

- task correctness;
- evidence quality;
- unsupported claims;
- severity calibration;
- actionability;
- adherence to output contract;
- clarity;
- known limitations;
- confidence calibration.

Output evals should include expected failures, not only happy paths.

## 6. Safety evals

Safety evals should cover:

- destructive commands;
- credential exposure;
- network access;
- external write actions;
- privacy-sensitive files;
- unsafe user intent;
- prompt injection in references or input files;
- cross-skill activation risks.

A safety eval does not merely ask whether the final answer is polite. It asks whether the skill's control surface can produce unsafe behavior.

## 7. Regression evals

Every historical skill failure should become a regression case if the failure is important enough.

Regression cases should record:

- original prompt;
- expected activation;
- expected process behavior;
- expected output properties;
- known bad behavior;
- fix introduced;
- rollback condition.

## 8. Evaluation before expansion

Before adding more instructions, ask:

```text
Which eval is failing?
Which failure mode does the new instruction target?
What cost does it add?
How will we know it helped?
```

Do not expand `SKILL.md` merely because a rule sounds wise.

## 9. Human review

Some skills require human judgment in evaluation:

- taste and design;
- communication;
- product strategy;
- architecture decisions;
- pedagogy;
- security severity.

Use rubrics. Avoid judging only by preference.

## 10. Minimal eval plan

Use [templates/eval-plan.md](../templates/eval-plan.md). A minimal plan should include:

- task distribution;
- baseline;
- trigger cases;
- output cases;
- process assertions;
- safety cases;
- cost metrics;
- regression cases;
- acceptance threshold.
