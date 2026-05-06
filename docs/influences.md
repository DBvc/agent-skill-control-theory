# Influences and Sources

ASCT is not an official standard and does not claim ownership over the Agent Skills format.

It is a working theory built from:

1. The public Agent Skills specification.
2. Official OpenAI Codex skill documentation.
3. Official Anthropic Agent Skills documentation.
4. Public skill repositories and real skill-authoring patterns.
5. General observations about LLM agents, tool use, bounded context, hallucination, evaluation, and software engineering workflows.

## Why there are no repository rankings here

This repository intentionally avoids ranking or critiquing specific public skill repositories in the core theory.

Reasons:

- Public repositories change quickly.
- Repository-specific judgments become stale.
- This project is meant to be a theory and design toolkit, not a review archive.
- The same repository can improve, pivot, or reorganize after this theory is published.

If case studies are added, they should be:

- dated;
- separated from core theory;
- scoped to one question;
- explicit about what version or commit was observed;
- treated as examples, not permanent judgments.

## Public sources worth reading

- Agent Skills specification: https://agentskills.io/specification
- OpenAI Codex skills docs: https://developers.openai.com/codex/skills
- Anthropic Agent Skills article: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- Claude Agent Skills docs: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- OpenAI skills repository: https://github.com/openai/skills
- Anthropic skills repository: https://github.com/anthropics/skills

## Suggested case-study policy

If you want to analyze a repository, create a dated file:

```text
case-studies/2026-05-06-repo-name.md
```

Use this structure:

```markdown
# Repository case study: <repo>

Observed at: <date>
Commit or tag: <commit/tag if available>
Question: <what this case study tests>

## ASCT mapping

- Activation Control:
- Intent Control:
- State Control:
- Trajectory Control:
- Execution Control:
- Completion Control:
- Evolution Control:

## What the repository teaches

## What appears missing

## What changed in the theory, if anything
```

Most case studies should not change ASCT’s core theory. They should map new examples to existing control surfaces unless they reveal a new class of failure that ASCT cannot explain.
