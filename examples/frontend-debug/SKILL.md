---
name: frontend-debug
description: Use when diagnosing an actively broken frontend behavior, regression, rendering bug, flaky UI interaction, or state/timing problem. Not for reviewing a completed diff, designing new UI, writing commit messages, or subjective visual taste critique without broken behavior.
---

# Frontend Debug

Use this skill to diagnose and fix active frontend failures with evidence, feedback loops, and completion proof.

This is a synthetic example built with Agent Skill Control Theory. It is intentionally not tied to any specific framework.

## Purpose

The goal is to move from observed broken behavior to a verified fix.

The goal is not to redesign the feature, review unrelated code, or make broad quality improvements.

## Mode selection

Choose the smallest sufficient mode.

- `quick`: small, reproducible bug with obvious scope.
- `standard`: normal runtime, rendering, state, or interaction bug.
- `deep`: flaky behavior, cross-browser issue, production regression, data loss, security-sensitive UI, or repeated failed attempts.
- `clarification`: required reproduction details or access are missing.
- `safety_redirect`: the request asks for unsafe, deceptive, or unauthorized behavior.

## Required inputs

Identify:

- observed symptom;
- expected behavior;
- reproduction path or missing reproduction information;
- environment if relevant;
- current files, diff, logs, test output, or screenshots available;
- validation commands available in the repository.

If the reproduction path is missing but can be discovered by inspecting tests, routes, stories, logs, or code, inspect before asking the user.

## Hard gates

Do not edit code until one of these exists:

- a reproducible pass/fail signal;
- a failing test;
- a browser or interaction script;
- a minimal manual reproduction path;
- a clear log or trace that maps to the symptom.

Do not propose a fix until you can state a falsifiable root-cause hypothesis.

Do not claim success unless validation evidence supports the claim.

## Workflow

1. **Symptom inventory**
   - Restate the observed behavior and expected behavior.
   - List all known symptoms.
   - Note uncertainty and missing inputs.

2. **Feedback loop**
   - Establish the fastest reliable pass/fail signal.
   - Prefer existing test commands, focused tests, Playwright or browser checks, storybook states, curl/API fixtures, or small reproduction scripts.
   - If no automated loop is available, document the manual reproduction path.

3. **State grounding**
   - Inspect current files, diff, logs, tests, screenshots, and config.
   - Do not rely on framework or package behavior from memory when local evidence or docs are available.

4. **Hypothesis**
   - Generate one to three ranked hypotheses.
   - Each hypothesis must explain all known symptoms.
   - Each hypothesis must be falsifiable by a probe.

5. **Probe**
   - Test one variable at a time.
   - Prefer evidence-producing probes over broad edits.
   - If a hypothesis fails, record why.

6. **Fix**
   - Make the smallest fix that addresses the root cause.
   - Avoid unrelated refactors.
   - Add or update regression coverage when there is a correct seam.

7. **Validate**
   - Run the feedback loop again.
   - Run relevant repository validation when practical.
   - If validation cannot run, state why.

8. **Handoff or completion**
   - If fixed and validated, provide completion proof.
   - If not fixed after three failed hypotheses, stop and provide handoff.

## Stop conditions

Stop and hand off when:

- three root-cause hypotheses fail;
- required environment access is unavailable;
- validation cannot be established;
- the fix requires product or design judgment outside the bug;
- external credentials or production access are required;
- continuing would likely cause unrelated changes.

## Evidence policy

Use this source hierarchy unless the task suggests otherwise:

```text
focused reproduction or failing test
> current logs and browser evidence
> current files and diff
> repository config and validation commands
> official docs or installed package types
> user statement
> inference
```

Separate facts, assumptions, and judgments.

## Output contract

Final output must include:

- Symptom:
- Root cause:
- Evidence:
- Fix:
- Validation:
- Not validated:
- Remaining risk:

For handoff, include:

- Known symptoms:
- Feedback loop attempted:
- Hypotheses tested:
- Evidence collected:
- Current best hypothesis:
- Blocker:
- Recommended next probe:

## Common failure modes to avoid

Avoid:

- patching symptoms before root cause;
- changing unrelated files;
- relying on framework behavior from memory when local evidence exists;
- treating subjective visual taste as a bug;
- declaring success without rerunning the pass/fail signal;
- continuing indefinitely after failed hypotheses.
