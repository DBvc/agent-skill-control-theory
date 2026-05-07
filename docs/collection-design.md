# Skill Collection Design

A skill collection is not just a folder of skills. At collection scale, new problems appear: routing, composition, conflicts, installation scope, security review, versioning, and deprecation.

ASCT handles this by applying the same seven control surfaces at collection level.

## 1. Why collection design matters

A single skill can be well written and still behave poorly in a collection.

Common collection failures:

- multiple skills trigger for the same request;
- no skill triggers because descriptions are too narrow;
- commands bypass intended safety checks;
- skill A produces output skill B cannot use;
- large catalogs create installation and audit risk;
- human-facing metadata differs from agent-facing metadata;
- deprecated skills remain discoverable;
- community skills introduce scripts, network calls, or dependency risks.

Collection design prevents the skill system from becoming a prompt swamp with better folder names.

## 2. Collection-level control surfaces

| Control surface | Collection-level expression |
|---|---|
| Activation Control | catalog, generated index, priority, conflict rules |
| Intent Control | commands, task taxonomy, routing questions |
| State Control | shared references, project memory, shared indexes |
| Trajectory Control | skill graph, required order, handoff contracts |
| Execution Control | shared scripts, tool policy, hook policy |
| Completion Control | cross-skill proof requirements and output contracts |
| Evolution Control | release process, eval suites, deprecation, compatibility |

## 3. Human discovery vs agent activation

A marketplace description is for humans. A skill `description` is for agent activation. These should not be confused.

Human discovery metadata may say:

```text
A set of skills for building high-quality web scraping workflows.
```

Agent activation metadata should say:

```text
Use when the user asks to select, configure, run, or validate an Apify Actor for a web scraping or automation task. Not for generic browser automation unrelated to Apify.
```

A collection may need both.

## 4. Skill graph

A skill graph describes how skills relate.

Useful relationships:

```text
precedes: A should run before B
requires: B depends on output from A
competes: A and B are alternatives
fallback: use B if A cannot proceed
handoff: A produces a contract for B
```

Skill graphs are especially useful for methodology packs, product workflows, multi-tool ecosystems, and research pipelines.

## 5. Conflict resolution

When two skills might trigger, the collection should define precedence.

Example:

```text
If the user asks to debug an actively broken behavior, prefer debug-skill over code-review-skill.
If the user asks to review a completed diff, prefer code-review-skill over debug-skill.
If the user asks for release notes prose, prefer writing-skill over release-action-skill.
If the user asks to publish or tag a release, prefer release-action-skill.
```

Without conflict resolution, overlapping skills create inconsistent behavior.

## 6. Installation scope

Large catalogs should not be installed wholesale by default.

Consider:

- user scope vs repo scope vs organization scope;
- trusted vs untrusted skills;
- script permissions;
- network access;
- dependency installation;
- environment variable access;
- sensitive domain risk;
- marketplace provenance.

Least privilege applies to skills too.

## 7. Collection safety

Collection-level risks include:

- cross-skill activation promotion;
- hidden scripts across many skills;
- unpinned dependencies;
- network access through unexpected paths;
- credential leakage;
- stale skills that retain high permissions;
- malicious or unreviewed community contributions.

Recommended controls:

- provenance tracking;
- script inventory;
- network policy;
- credential policy;
- dependency pinning policy;
- installation subsets;
- security review before release;
- deprecation process;
- compatibility matrix.

## 8. Collection evaluation

Evaluate collections at two levels.

### Skill-level eval

- trigger correctness;
- output quality;
- safety behavior;
- process adherence.

### Collection-level eval

- routing correctness;
- conflict resolution;
- command behavior;
- cross-skill handoff;
- install subset behavior;
- performance under many installed skills;
- regression when a skill is added or removed.

## 9. Collection IR

Use [templates/collection-ir.yaml](../templates/collection-ir.yaml) to design a collection before building it.
