# Safety Constraints

ASCT treats safety as an admissibility constraint, not just another cost.

```text
A skill is admissible only if:
  SafetyRisk(skill, task_distribution) <= SafetyBudget
```

If a skill exceeds the safety budget, it should not be published or installed even if it improves task success.

## Safety risks specific to skills

Skills can include instructions, scripts, assets, and references. That makes them more powerful than ordinary prompt snippets.

Common risks:

- executing destructive commands;
- reading or exposing secrets;
- writing to external systems without approval;
- making hidden network calls;
- overriding user intent or consent;
- enabling fraud, evasion, coercion, or privacy invasion;
- bundling malicious or unclear scripts;
- instructing agents to ignore higher-priority policies or system rules.

## Safe skill design rules

1. **Fail closed** when authorization is unclear.
2. **Ask for explicit approval** before external, irreversible, or public actions.
3. **Prefer dry-run** for destructive or state-changing operations.
4. **Declare dependencies** and environment assumptions.
5. **Keep scripts auditable** and self-contained.
6. **Do not bundle secrets** or private local paths.
7. **Separate private presets** from public reusable skills.
8. **Expose known limitations** in final output.
9. **Avoid hidden network behavior** unless explicitly required and documented.
10. **Do not instruct the agent to bypass higher-priority policies.**

## External action contract

For skills that can create, update, publish, delete, close, push, deploy, comment, or label, require an action contract:

```yaml
external_action:
  action_type: create_issue | update_label | post_comment | close_issue | push | publish | deploy | delete | none
  target:
  irreversible: true | false
  public_visible: true | false
  requires_user_approval: true
  approval_text:
  dry_run_available: true | false
  preflight_checks:
    -
  blocked_by:
    -
```

## Final answer disclosure

When a skill performs or prepares a risky action, the final answer should include:

- what action was taken or prepared;
- who approved it;
- what target was affected;
- what validation or dry-run was performed;
- what risks remain.
