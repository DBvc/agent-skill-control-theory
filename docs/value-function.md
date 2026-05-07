# SkillValue: Success, Cost, Risk

ASCT evaluates a skill by net reliability gain.

```text
SkillValue(s, D) =
  E_t~D[Success(agent_with_skill, t) - Success(base_agent, t)]
  - Cost(s, D)
  - Risk(s, D)
```

Where:

- `s` is the skill.
- `D` is the task distribution.
- `Success` is task-specific.
- `Cost` includes context, friction, runtime, monetary, audit, and maintenance costs.
- `Risk` includes safety, privacy, side-effect, security, wrong-trigger, and drift risk.

A skill is admissible only if:

```text
SafetyRisk(s, D) <= SafetyBudget
```

A skill is worth keeping only if:

```text
SkillValue(s, D) > 0
```

## 1. Why a value function is needed

Skill authors often optimize the wrong thing.

Common false proxies:

- length of `SKILL.md`;
- number of rules;
- strictness of tone;
- elegance of structure;
- author confidence;
- anecdotal success;
- novelty;
- number of files.

A skill can become longer and worse. It can become stricter and worse. It can add scripts and still be worse if the scripts are risky, slow, brittle, or unnecessary.

The value function forces a more disciplined question:

```text
Does this skill improve expected task success enough to justify its cost and risk?
```

## 2. Success

Success must be defined for the task distribution.

For a code review skill, success may include:

- important defects found;
- false positives avoided;
- findings backed by evidence;
- severity calibrated;
- fix directions useful;
- review not distracted by minor nits.

For a debug skill:

- reproducible feedback loop established;
- root cause identified before patching;
- fix passes validation;
- regression test added when appropriate;
- failed hypotheses handed off cleanly.

For an artifact skill:

- file opens;
- format is valid;
- visual/rendered output matches requirements;
- formulas or fields are correct;
- validation commands pass.

For a pedagogic skill:

- user learns the framework;
- output is correct;
- reasoning is understandable;
- future user independence improves.

For a project-memory skill:

- current task improves;
- future task context cost decreases;
- terminology becomes more stable;
- decisions are easier to recover.

`Success` is not always a single scalar. In practice, use a rubric.

## 3. Cost

Skill cost includes more than tokens.

| Cost type | Description |
|---|---|
| Context cost | Tokens loaded before and after activation |
| Trigger cost | Installed-skill list crowding, description ambiguity, wrong-trigger overhead |
| User friction cost | Clarification, approval, extra ceremony, longer final output |
| Tool/runtime cost | Shell commands, browser runs, tests, API calls, local dependencies |
| Monetary cost | Paid APIs, cloud services, actor runs, model usage, CI minutes |
| Audit cost | Reviewing scripts, dependencies, network access, permissions |
| Maintenance cost | Keeping references, scripts, evals, and compatibility notes current |
| Opportunity cost | The skill prevents or delays a simpler adequate response |

A skill with high cost can still be good if task risk and success gain are high. A low-risk task should usually have a lighter controller.

## 4. Risk

Risk is not merely cost. Some risks make a skill inadmissible even if it improves task success.

| Risk type | Example |
|---|---|
| Safety risk | Harmful, deceptive, or unauthorized behavior |
| Security risk | Secret leakage, malicious script, dependency compromise |
| Privacy risk | Reading or transmitting sensitive files |
| Side-effect risk | Publishing, deleting, closing issues, modifying external systems |
| Wrong-trigger risk | Skill activates in adjacent tasks and misguides the agent |
| Over-control risk | Skill suppresses useful agent judgment or creativity |
| Under-control risk | Skill leaves dangerous freedom unconstrained |
| Drift risk | Old rules, stale docs, broken scripts, outdated APIs |
| Collection conflict risk | Multiple skills contradict or bypass each other |

The safety constraint should be checked before optimizing value:

```text
SafetyRisk <= SafetyBudget
```

## 5. Measuring SkillValue

You rarely need exact numbers. Use structured comparison.

### Minimum evaluation

Compare:

```text
base agent
old skill, if any
new skill
```

Against:

```text
positive trigger cases
negative trigger cases
near-miss trigger cases
happy-path output cases
edge cases
historical failures
safety cases
```

Measure:

- trigger correctness;
- output quality;
- process adherence;
- validation strength;
- unsupported claims;
- runtime cost;
- user friction;
- safety posture.

## 6. Interpreting negative value

A skill may have negative SkillValue if it:

- triggers too often;
- adds too much context;
- forces a heavy workflow on small tasks;
- makes the agent overconfident;
- hides safety risk;
- increases false positives;
- requires maintenance beyond its benefit;
- solves a rare problem with a common burden.

Negative value does not mean the underlying idea is bad. It may mean the control is misplaced. Move it to a script, reference, command, hook, repo memory, or global instruction.

## 7. Practical scoring rubric

Use 1 to 5 for each dimension.

| Dimension | 1 | 5 |
|---|---|---|
| Task fit | Vague or one-off | Repeated, stable task distribution |
| Failure reduction | No clear failure target | Clear reduction of meaningful failures |
| Trigger precision | Broad and ambiguous | Clear positive, negative, near-miss boundaries |
| Context efficiency | Bloated | Smallest sufficient controller |
| Evidence grounding | Relies on model memory | Uses current sources and source hierarchy |
| Execution reliability | Free-form for deterministic work | Scripts/tools for deterministic work |
| Completion proof | Claims without validation | Claims mapped to evidence |
| Safety posture | Hidden or unsafe | Explicit budget, gates, approvals |
| Evaluation | None | Baseline, trigger, output, safety, regression evals |
| Maintenance | No owner or drift plan | Compatibility, review cadence, patch hypotheses |

A skill does not need a perfect score. It needs enough net value for its task distribution.
