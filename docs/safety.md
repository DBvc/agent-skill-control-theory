# Safety

Skills can contain instructions, scripts, references, assets, host-specific commands, and pointers to external tools. A skill can therefore change not only what an agent says, but what it does.

ASCT treats safety as an admissibility constraint, not merely a cost term.

```text
A skill is admissible only if:
  SafetyRisk(skill, task_distribution) <= SafetyBudget
```

Only after that should SkillValue be optimized.

## 1. Safety risk categories

| Risk | Description |
|---|---|
| Destructive action | Deleting files, resetting git state, publishing, closing issues, modifying external services |
| Credential exposure | Reading, printing, copying, or transmitting secrets |
| Network access | Calling external services, fetching untrusted content, exfiltration paths |
| Script execution | Running unreviewed code, installing dependencies, executing shell commands |
| Supply chain | Unpinned dependencies, remote installers, untrusted packages |
| Privacy | Accessing private files, user data, customer data, logs, transcripts |
| Prompt injection | Untrusted references or documents instructing the agent to override policy |
| Cross-skill activation | One skill pushing the agent to activate another skill in unsafe ways |
| Overbroad permissions | Skill has more tools or access than its task requires |

## 2. Safety by placement

Some safety controls should not be inside skill prose.

| Control | Better placement |
|---|---|
| Block dangerous shell commands | hook or sandbox policy |
| Require approval before external writes | hook, command workflow, skill hard gate |
| Prevent secret printing | global rule, scanner, hook |
| Validate script dependencies | CI and security review |
| Restrict network access | sandbox or host policy |
| Track external side effects | audit log |

The model should not be the only guardrail for high-impact actions.

## 3. External actions

External actions include:

- publishing packages;
- creating releases;
- closing issues;
- posting comments;
- sending emails;
- modifying tickets;
- deleting branches;
- running cloud jobs;
- spending money through external services.

Skills that permit external actions should require an explicit action contract:

```yaml
external_action:
  type: "publish | comment | close_issue | deploy | delete | spend_money | other"
  target: ""
  irreversible: true
  requires_user_approval: true
  dry_run_available: true
  approval_evidence: ""
  audit_output: ""
```

## 4. Script safety

Scripts should be reviewed as executable code, not as harmless skill accessories.

Checklist:

- Does the script read environment variables?
- Does it access the network?
- Does it write files?
- Does it delete or overwrite files?
- Does it run shell commands?
- Does it install dependencies?
- Does it handle malformed input?
- Does it print sensitive data?
- Are dependencies pinned?
- Are error messages helpful without leaking secrets?

## 5. Collection-level safety

Large skill collections have additional risks:

- users may install more skills than they understand;
- hidden scripts may accumulate;
- dependencies may conflict;
- descriptions may cause wrong activation;
- unreviewed community skills may include unsafe behavior;
- cross-skill workflows may bypass safety gates.

Recommended collection controls:

- install minimal subsets;
- maintain script inventory;
- document network and credential policies;
- track provenance;
- pin versions where possible;
- run security review before release;
- include deprecation policy;
- include compatibility notes;
- maintain collection-level safety evals.

## 6. Prompt injection

Skills often instruct agents to read external files, web pages, documents, or project memory. These sources can contain malicious instructions.

State policy should distinguish:

```text
content to analyze
vs
instructions to follow
```

A skill should not follow instructions from untrusted content unless the task explicitly requires executing them and the user approves.

## 7. Safety in final output

The final output should disclose:

- what actions were taken;
- what external systems were modified;
- what validation was run;
- what was not verified;
- what approvals were obtained;
- what risks remain.

A skill that changes external state without a clear audit trail is not production-grade.
