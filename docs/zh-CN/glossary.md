# 术语表

## Agent

基于当前提示、工具、观测和记忆选择动作的上下文条件化策略系统。

## Skill

选择性加载的 LLM agent 策略控制器。

## Task distribution

输入、约束、输出和失败模式相似的一类重复任务。

## Activation classifier

帮助 agent 判断 skill 是否适用的部分，通常是 `description`。

## Runtime controller

Skill 激活后塑造 agent 行为的完整 `SKILL.md` 指令。

## Control surface

Skill 可以控制的行为维度：激活、意图、状态、轨迹、执行、完成或演化。

## Failure mode

Base agent 在某类任务中常见的失败路径。

## Evidence

支持某个声明的外部可观察信息，例如文件、diff、日志、测试、文档、截图、渲染产物、用户声明、issue 历史。

## Completion proof

Agent 声称任务完成前所需的证据、验证和限制说明。

## Deterministic executor

比自由文本生成更可靠的重复操作工具，例如脚本、验证器、解析器、渲染器、linter。

## Progressive disclosure

一种分层加载模式：agent 先看到轻量 metadata，相关时再加载完整 skill，需要时再加载资源。

## Drift

随着模型、工具、API、代码库、组织或任务分布变化，skill 可靠性下降的趋势。

## SkillValue

一个用于评价 skill 是否以可接受成本和风险改善任务成功率的启发式价值函数。
