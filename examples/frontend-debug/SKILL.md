---
name: frontend-debug
description: Diagnose and fix active frontend bugs, regressions, rendering issues, flaky UI behavior, or broken user interactions. Use when the user reports something is currently broken, failing, visually regressed, flaky, or inconsistent in a web UI. Not for general code review, new feature design, subjective visual taste, or writing PR descriptions.
---

# Frontend Debug

Use this skill to diagnose active frontend failures and produce a minimal, verified fix.

The goal is not to make broad improvements. The goal is to establish a reliable feedback loop, identify a falsifiable root cause, make the smallest sufficient change, and verify the result.

## Mode selection

Choose the smallest sufficient mode:

- `quick`: obvious local bug, existing failing test or clear reproduction.
- `standard`: normal broken UI behavior, regression, or rendering issue.
- `deep`: flaky behavior, race condition, cross-browser issue, hydration issue, release-critical bug, or repeated failed fix.
- `clarification`: the symptom or reproduction is missing.
- `safety_redirect`: user asks for unsafe, deceptive, or unauthorized behavior.

## Required inputs

Before changing code, identify:

- symptom;
- reproduction path;
- expected behavior;
- actual behavior;
- affected route/component/browser/device when available;
- whether this is a regression;
- available validation command or UI check.

If the reproduction is missing, ask for it or construct the smallest observable feedback loop from available evidence.

## Hard gates

Do not edit production code until you have at least one pass/fail feedback signal:

- failing test;
- browser reproduction;
- console/log assertion;
- screenshot comparison;
- CLI or API fixture;
- minimal reproduction script;
- user-confirmed reproduction steps.

Do not claim root cause unless the hypothesis explains all observed symptoms.

Do not claim success unless validation was run or the limitation is explicitly stated.

## Workflow

1. **Classify the failure**
   - runtime error;
   - state/data bug;
   - rendering/layout bug;
   - interaction bug;
   - hydration or server/client mismatch;
   - async/race/flaky behavior;
   - environment/config issue.

2. **Establish feedback**
   - Prefer existing test or reproduction.
   - If absent, create the smallest temporary harness or manual browser check.
   - Write down what signal means fail and what signal means pass.

3. **Gather current evidence**
   - Inspect relevant files, not remembered paths.
   - Read recent diff if this is a regression.
   - Check logs, console output, failing assertions, screenshots, or DOM evidence.
   - Separate observed facts from assumptions.

4. **Form hypotheses**
   - Generate 2-4 ranked hypotheses.
   - Each hypothesis must predict an observable result.
   - Probe one variable at a time.

5. **Fix minimally**
   - Change the smallest surface that explains the root cause.
   - Avoid broad rewrites, unrelated cleanup, or style drift.
   - Prefer preserving public interfaces unless the interface itself is the cause.

6. **Validate**
   - Run the feedback loop again.
   - Run relevant existing tests or build checks when available.
   - For visual bugs, check at least the affected viewport and one narrow mobile viewport when feasible.

7. **Stop or hand off**
   - If the same symptom remains after a fix, stop and re-evaluate the hypothesis.
   - After three failed hypotheses, stop and produce a handoff instead of stacking patches.

## Evidence policy

Use this source hierarchy:

1. direct tool output, failing tests, browser reproduction;
2. current files and diffs;
3. logs, screenshots, DOM evidence;
4. official framework docs;
5. user statements;
6. inference.

Do not rely on memory for file paths, framework behavior, package versions, or project conventions when they can be inspected.

## Output contract

Return:

- **Symptom**: what was broken.
- **Feedback loop**: how failure/pass was observed.
- **Root cause**: one falsifiable explanation.
- **Fix**: what changed and why.
- **Validation**: commands or browser checks run, with results.
- **Unverified**: anything not checked.
- **Remaining risk**: if any.

For handoff, return:

- observed facts;
- hypotheses tried;
- probes and results;
- files inspected;
- likely next probe;
- why continuing would risk patch stacking.
