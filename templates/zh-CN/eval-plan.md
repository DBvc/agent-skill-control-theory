# Skill Eval 计划

## Skill

**名称：**

**版本 / commit：**

**任务分布：**

## Baseline

比较对象：

- [ ] 无 skill
- [ ] 旧版本
- [ ] 竞争 skill
- [ ] 只有人类 rubric

## Trigger evals

| Case ID | 用户 prompt | 是否应触发 | 期望 mode | 备注 |
|---|---|---:|---|---|
| pos-001 | | yes | | |
| neg-001 | | no | | |
| near-001 | | no or different skill | | |
| safety-001 | | safety redirect | | |

## Process evals

| Case ID | 必须行为 | 通过标准 |
|---|---|---|
| proc-001 | | |

示例：

- 总结前读取真实 diff。
- debug 前建立 pass/fail loop。
- 未批准不执行外部动作。
- 多次假设失败后停止。

## Output evals

| Case ID | 期望输出属性 | 通过标准 |
|---|---|---|
| out-001 | | |

示例：

- 每个 finding 有 evidence。
- 最终 claim 映射到 validation。
- Unknowns 被标注。
- 公共产物不包含过程闲聊。

## Safety evals

| Case ID | 风险 | 期望行为 |
|---|---|---|
| safe-001 | | |

## Metrics

| 指标 | 测量方式 |
|---|---|
| Trigger precision | |
| Trigger recall | |
| Near-miss false positive rate | |
| Output quality | |
| Unsupported claims | |
| Validation rate | |
| Token/context cost | |
| User friction | |
| Safety incidents | |

## 决策

- [ ] Keep
- [ ] Revise
- [ ] Deprecate
- [ ] Split
- [ ] Merge

**理由：**
