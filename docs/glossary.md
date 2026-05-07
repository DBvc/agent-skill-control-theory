# Glossary

## Agent

A context-conditioned system that selects actions using the current prompt, tools, observations, and memory.

## Skill

A selectively loaded policy controller that changes an agent’s behavior for a recurring class of tasks.

## Task distribution

A recurring set of tasks with similar inputs, constraints, desired outputs, success criteria, and failure modes.

## Policy controller

An artifact that changes which actions the agent is likely to take, which evidence it considers, which tools it uses, which paths are forbidden, and what claims it may make.

## Activation classifier

The part of a skill that helps the agent decide whether to use it. In standard skills this is primarily the `description` field.

## Runtime controller

The part of a skill that controls behavior after activation. In standard skills this is primarily `SKILL.md`.

## External semantic memory

Long or conditional knowledge stored outside the main runtime controller, usually in `references/`, project memory, ADRs, glossaries, or issue briefs.

## Deterministic executor

A script or tool used for repeatable, parse-heavy, numerical, format-sensitive, or mechanically verifiable work.

## Material prior

A reusable asset such as a template, schema, data file, starter project, example, image, or design reference.

## Completion proof

The evidence and validation needed before the agent may claim the task is done.

## Control surface

A part of agent behavior a skill can influence: activation, intent, state, trajectory, execution, completion, or evolution.

## Failure mode

A high-probability path by which the base agent fails on the task distribution.

## Placement decision

The choice of where a control should live: skill, global instruction, command, hook, script, reference, asset, repo memory, or collection routing.

## Skill collection

A set of skills plus related artifacts such as commands, hooks, indexes, metadata, scripts, and shared references.

## Skill graph

A collection-level model of how skills relate: precedes, requires, competes, falls back, or hands off.

## Trigger eval

An evaluation that checks whether a skill activates when it should and stays inactive when it should not.

## Output eval

An evaluation that checks whether the final result is correct, useful, grounded, and properly shaped.

## Process eval

An evaluation that checks whether the agent followed the intended workflow.

## Safety eval

An evaluation that checks unsafe, privacy-sensitive, destructive, or unauthorized behavior.

## Regression eval

An evaluation that preserves fixes for historical failures.

## SkillValue

A conceptual evaluation model: expected task success gain minus cost and risk.
