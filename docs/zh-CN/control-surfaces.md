# 七个控制面

ASCT 认为 skill 通过七个控制面影响 agent 行为。一个 skill 不需要全部七个控制面，应该根据任务分布和主要失败模式选择。

## 1. Activation Control

**问题：** 该不该使用这个 skill？

当误触发风险高时重点设计。

检查项：

- `description` 是否包含任务、触发关键词和上下文？
- 是否包含 not-for 或 near-miss 边界？
- 是否命名并路由相邻 skill？
- 是否有 positive、negative、near-miss trigger eval？

## 2. Intent Control

**问题：** 用户真正要的任务是什么？

当同一句用户表达可能对应多个任务时重点设计。

检查项：

- 是否有 mode routing？
- 是否定义 required inputs？
- 是否定义何时澄清？
- 是否定义 non-goals？

## 3. State Control

**问题：** 当前真实状态是什么？

当当前事实、代码库状态、API 版本或 artifact 状态重要时重点设计。

检查项：

- source of truth 是什么？
- 行动前必须检查哪些证据？
- 是否区分事实、假设和判断？
- 外部事实是否有 freshness policy？

## 4. Trajectory Control

**问题：** agent 应该走什么路径？

当 agent 容易修症状、跳步骤或硬往前冲时重点设计。

检查项：

- 是否有 hard gates？
- 是否有明确 stop conditions？
- 是否定义 fallback paths？
- 失败时是否有 handoff 格式？

## 5. Execution Control

**问题：** 哪些操作需要确定性工具？

当任务涉及解析、验证、渲染、格式、计算或高风险外部动作时重点设计。

检查项：

- 哪些步骤应该交给 scripts？
- 脚本是否自包含，并清楚说明依赖？
- 脚本输出是否简洁有用？
- 危险动作是否有确认或 dry-run？

## 6. Completion Control

**问题：** 什么时候可以声称 done？

当 agent 可能过度声称成功时重点设计。

检查项：

- 最终输出是否包含 validation？
- 是否禁止无证据 claim？
- 是否要求 known limitations？
- 未验证工作是否明确标注？

## 7. Evolution Control

**问题：** skill 如何避免漂移？

当 skill 重要到值得维护时重点设计。

检查项：

- 是否有 trigger eval？
- 是否有 output eval？
- 是否有 safety eval？
- 历史失败是否进入 regression cases？
- 每次改动是否有 patch hypothesis？
