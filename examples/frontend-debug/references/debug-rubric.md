# Frontend Debug Rubric

Use this reference only when deeper diagnosis is needed.

## Bug classes

- State transition bug
- Stale closure or stale cache bug
- Async race condition
- Rendering or layout bug
- Hydration mismatch
- Event propagation bug
- Accessibility interaction bug
- Browser compatibility bug
- Environment or config bug
- Data contract mismatch

## Root-cause hypothesis shape

A useful hypothesis has this form:

```text
Because <specific condition> occurs in <specific code path>,
<state or DOM or request> becomes <wrong value>,
which explains <symptom A> and <symptom B>.
This can be falsified by <probe>.
```

## Bad hypotheses

Avoid hypotheses like:

- “The state management is broken.”
- “Probably a race condition.”
- “The component did not re-render.”
- “The CSS is wrong.”

These may be starting intuitions, but they are not root-cause hypotheses until they name a condition, path, mechanism, and falsifying probe.
