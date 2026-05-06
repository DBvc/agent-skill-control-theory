# Design Laws

These are engineering design laws, not natural laws. They follow from ASCT’s postulates and are meant to guide skill authorship.

## 1. Trigger Boundary Law

A skill’s first quality is correct activation.

### Why

A skill is selectively loaded. If it activates in the wrong task, all of its workflow becomes misapplied control.

### Practice

Write descriptions that include:

- use when;
- not for;
- near-miss cases;
- adjacent skill routing.

## 2. Task Compilation Law

A skill compiles user utterances into task frames and modes.

### Why

User language is ambiguous. The skill must choose the smallest sufficient mode.

### Practice

Define modes such as:

- quick;
- standard;
- deep;
- clarification;
- safety redirect.

## 3. Context Economy Law

Every token in `SKILL.md` should buy behavior change.

### Why

Context and attention are finite.

### Practice

Keep `SKILL.md` lean. Move long rubrics, examples, and references to `references/`. Move deterministic checks to `scripts/`.

## 4. Evidence Externalization Law

Current facts should come from external evidence, not latent memory.

### Why

Agent memory may be stale, incomplete, or hallucinated.

### Practice

Define source hierarchy:

```text
direct tool output > current files/diff > official docs > user statement > inference > guess
```

## 5. Trajectory Constraint Law

Workflow exists to make bad paths harder to take.

### Why

Agents can always produce a plausible next step. The skill must prevent bad plausible steps.

### Practice

Use:

- hard gates;
- stop conditions;
- fallback paths;
- handoff format.

## 6. Freedom-Risk Law

Higher-risk tasks require lower agent freedom.

### Why

The cost of a bad action rises with risk, irreversibility, and external side effects.

### Practice

- Creative design: high freedom, taste rubric.
- Technical decision: moderate freedom, assumptions and trade-offs.
- Debug: controlled freedom, feedback loop and hypothesis gate.
- Artifact generation: low freedom, validators and render checks.
- Release/delete/external write: very low freedom, approval and dry-run.

## 7. Deterministic Delegation Law

Models judge; tools execute deterministically.

### Why

Repeated, parse-heavy, numerical, or format-sensitive tasks should not rely on free-form generation.

### Practice

Use scripts for:

- parsing;
- validation;
- rendering;
- counting;
- formatting;
- schema checks;
- dangerous command guards.

## 8. Completion Proof Law

Done means output plus evidence, validation, and limitations.

### Why

Agents can generate completion narratives without completing the task.

### Practice

Require:

- what changed;
- validation run;
- validation result;
- known limitations;
- unverified items.

## 9. Drift Regression Law

Skills are drifting controllers and need evals, versions, and regression cases.

### Why

The environment changes. Good behavior can regress.

### Practice

Every important skill change should include:

- target failure;
- proposed change;
- expected benefit;
- expected cost;
- evals updated;
- rollback condition.
