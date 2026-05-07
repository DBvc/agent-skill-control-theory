# 来源和设计影响

ASCT 不是官方标准，而是一套用于解释和指导 LLM agent skill 设计的工作理论。

## 主要公开来源

- [Agent Skills specification](https://agentskills.io/specification)
- [OpenAI Codex skills documentation](https://developers.openai.com/codex/skills)
- [Anthropic Agent Skills overview](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

这些来源定义或解释了常见 skill 结构：`SKILL.md`、frontmatter metadata、可选 `scripts/`、`references/`、`assets/` 以及 progressive disclosure。

## 公开仓库影响

ASCT 也受多种公开 skill 仓库启发，包括：官方 skill 仓库、个人工程工作流 skills、安全审计 skills、设计和 taste skills、科学和领域型 skill catalogs、产品和规划 skills、工具生态 skills、持久文件记忆 skills、压缩交互模式 skills。

核心理论不排名也不点评具体仓库。仓库级观察会随时间过期，因此 ASCT 默认使用合成案例。若要写具体案例，应单独标明日期、commit 和观察范围。

## 更广背景

ASCT 与以下领域相容：工具型 agents、检索增强生成、prompt/agent eval、软件工程反馈循环、workflow design、安全建模和人机交互。

本仓库刻意保持在 skill authoring 范围内，不扩张成完整 agent architecture 理论。
