# 术语表

## Agent

基于当前 prompt、工具、观测和记忆选择动作的上下文条件化系统。

## Skill

一个选择性加载的策略控制器，用于改变 agent 在一类重复任务中的行为。

## Task distribution

具有相似输入、约束、期望输出、成功标准和失败模式的一组重复任务。

## Policy controller

改变 agent 行动概率、证据偏好、工具使用、禁止路径和最终声明边界的控制构件。

## Activation classifier

帮助 agent 判断是否使用某 skill 的部分。标准 skill 中主要是 `description` 字段。

## Runtime controller

skill 激活后控制行为的部分。标准 skill 中主要是 `SKILL.md`。

## External semantic memory

位于主 runtime controller 外的长知识或条件性知识，通常在 `references/`、项目记忆、ADR、术语表或 issue brief 中。

## Deterministic executor

用于重复、解析密集、数值敏感、格式敏感或机械可验证工作的脚本或工具。

## Material prior

可复用素材，例如模板、schema、数据文件、starter project、示例、图片或设计参考。

## Completion proof

agent 声称任务完成前必须拥有的证据和验证。

## Control surface

skill 可以影响 agent 行为的某一部分：激活、意图、状态、轨迹、执行、完成或演化。

## Failure mode

基础 agent 在任务分布上的高概率失败路径。

## Placement decision

决定一个控制应该放在哪里：skill、global instruction、command、hook、script、reference、asset、repo memory 或 collection routing。

## Skill collection

多个 skills 以及相关 commands、hooks、indexes、metadata、scripts 和共享 references 构成的集合。

## Skill graph

描述 skill 之间关系的图：precedes、requires、competes、fallback、handoff。

## Trigger eval

检查 skill 是否在应该触发时触发、不该触发时保持沉默的 eval。

## Output eval

检查最终结果是否正确、有用、有证据、符合输出契约的 eval。

## Process eval

检查 agent 是否遵循预期 workflow 的 eval。

## Safety eval

检查不安全、隐私敏感、破坏性或未授权行为的 eval。

## Regression eval

保护历史失败修复不回归的 eval。

## SkillValue

概念性评价模型：预期任务成功收益减去成本和风险。
