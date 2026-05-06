# Glossary

## Agent

A context-conditioned policy system that selects actions using the current prompt, tools, observations, and memory.

## Skill

A selectively loaded policy controller for an LLM agent.

## Task distribution

A recurring class of tasks with similar inputs, constraints, outputs, and failure modes.

## Activation classifier

The part of a skill, usually the `description`, that helps the agent decide whether the skill applies.

## Runtime controller

The full `SKILL.md` instructions that shape the agent’s behavior after activation.

## Control surface

A behavior dimension a skill can control: activation, intent, state, trajectory, execution, completion, or evolution.

## Failure mode

A common path by which the base agent fails on a task distribution.

## Evidence

Externally observable support for a claim. Examples: files, diffs, logs, tests, docs, screenshots, rendered artifacts, user statements, issue history.

## Completion proof

The evidence, validation, and limitations required before the agent may claim the task is complete.

## Deterministic executor

A script, validator, parser, renderer, linter, or other tool that performs a repeatable operation more reliably than free-form generation.

## Progressive disclosure

A loading pattern where the agent first sees lightweight metadata, then loads the full skill only when relevant, and loads resources only when needed.

## Drift

The tendency of skills to become less reliable as models, tools, APIs, repositories, organizations, or task distributions change.

## SkillValue

A heuristic value function for evaluating whether a skill improves task success enough to justify its costs and risks.
