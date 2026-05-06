# 启发来源和资料

ASCT 不是官方标准，也不声称拥有 Agent Skills 格式。

它是一套工作理论，来源包括：

1. 公开 Agent Skills specification。
2. OpenAI Codex skill 官方文档。
3. Anthropic Agent Skills 官方文档。
4. 公开 skill 仓库和真实 skill 写作模式。
5. 关于 LLM agent、工具使用、有界上下文、幻觉、评估和软件工程工作流的一般观察。

## 为什么核心理论不排名具体仓库

本仓库有意避免在核心理论里排名或点评具体公开 skill 仓库。

原因：

- 公开仓库变化很快。
- 仓库级判断容易过期。
- 本项目目标是理论和设计工具，而不是评论档案。
- 同一个仓库可能在发布后改进、转向或重组。

如果要增加案例分析，应当：

- 带日期；
- 和核心理论分离；
- 聚焦一个问题；
- 明确观察的是哪个版本或 commit；
- 把案例当例子，而不是永久判断。

## 推荐阅读资料

- Agent Skills specification: https://agentskills.io/specification
- OpenAI Codex skills docs: https://developers.openai.com/codex/skills
- Anthropic Agent Skills article: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- Claude Agent Skills docs: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview
- OpenAI skills repository: https://github.com/openai/skills
- Anthropic skills repository: https://github.com/anthropics/skills

## 推荐案例策略

如果要分析某个仓库，新建带日期的文件：

```text
case-studies/2026-05-06-repo-name.md
```

建议结构：

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

大多数案例不应该改变 ASCT 核心理论。除非它暴露出 ASCT 无法解释的新失败类型，否则应该优先映射到已有控制面。
