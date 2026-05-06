# The Seven Control Surfaces

ASCT says a skill controls agent behavior through seven surfaces. A skill does not need all seven. The relevant surfaces depend on the task distribution and dominant failure modes.

## 1. Activation Control

**Question:** Should this skill be used?

Use this when wrong-trigger risk is high.

Checklist:

- Does `description` include the task, trigger keywords, and context?
- Does it include not-for or near-miss boundaries?
- Are adjacent skills named and routed?
- Are there trigger evals for positive, negative, and near-miss cases?

## 2. Intent Control

**Question:** What is the user actually asking for?

Use this when the same user phrase can mean multiple tasks.

Checklist:

- Does the skill have mode routing?
- Does it define required inputs?
- Does it define when to ask clarification?
- Does it define non-goals?

## 3. State Control

**Question:** What is true right now?

Use this when current facts, repository state, API versions, or artifact state matter.

Checklist:

- What is the source of truth?
- What evidence must be inspected before action?
- Are facts separated from assumptions and judgments?
- Is there a freshness policy for external facts?

## 4. Trajectory Control

**Question:** What path should the agent follow?

Use this when agents tend to patch symptoms, skip steps, or over-proceed.

Checklist:

- Are there hard gates?
- Are stop conditions explicit?
- Are fallback paths defined?
- Is handoff defined for failure?

## 5. Execution Control

**Question:** Which operations need deterministic tools?

Use this when the task involves parsing, validation, rendering, formatting, calculation, or risky external actions.

Checklist:

- What should be delegated to scripts?
- Are scripts self-contained and clear about dependencies?
- Do scripts produce concise, useful outputs?
- Are dangerous actions guarded by approval or dry-run?

## 6. Completion Control

**Question:** When may the agent claim done?

Use this when agents may overclaim success.

Checklist:

- Does final output include validation?
- Are unsupported claims forbidden?
- Are known limitations required?
- Is unverified work explicitly labeled?

## 7. Evolution Control

**Question:** How does this skill avoid drift?

Use this when the skill is important enough to maintain.

Checklist:

- Are trigger evals present?
- Are output evals present?
- Are safety evals present?
- Are historical failures captured as regression cases?
- Does each change have a patch hypothesis?
