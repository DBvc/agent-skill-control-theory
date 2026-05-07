# 评估

ASCT 把 eval 视为 skill engineering 的一部分，而不是附加项。

skill 会改变 agent 行为。评估要问：这种行为变化是否在目标任务分布上朝正确方向发生，并且没有带来不可接受的成本和风险。

## 1. 评估对象

| Eval 类型 | 问题 |
|---|---|
| Trigger eval | 该触发时是否触发，不该触发时是否沉默？ |
| Process eval | 激活后是否遵循关键轨迹？ |
| Output eval | 最终结果是否有用、grounded、符合输出契约？ |
| Safety eval | 是否尊重安全、隐私、审批和外部副作用？ |
| Regression eval | 历史失败是否保持修复？ |

## 2. Baseline

通常至少比较：

- no skill；
- 旧版本 skill；
- 更轻版本 skill；
- 竞争 skill；
- 人工 checklist。

核心问题是：

```text
这个 skill 改善了基础 agent 原本不稳定的哪个行为？
```

## 3. Trigger evals

应包括：

- positive cases；
- implicit positive cases；
- negative cases；
- near-miss cases；
- adjacent skill conflicts；
- unsafe / out-of-scope cases。

near-miss 很重要。只测试明显正例，只能说明 skill 会在被喊名字时触发。

## 4. Process evals

process eval 检查 agent 是否走了关键流程。

比如 debug skill：

- 是否先建立 pass/fail loop？
- 是否先形成可证伪假设？
- 是否避免 patch stacking？
- 多次失败后是否停止并 handoff？

artifact skill：

- 是否使用正确工具链？
- 是否验证输出文件？
- 需要时是否检查渲染结果？

## 5. Output evals

检查最终结果：

- 正确性；
- 证据质量；
- unsupported claims；
- severity 校准；
- 可行动性；
- 输出契约遵循；
- 清晰度；
- 已知限制；
- confidence 校准。

## 6. Safety evals

覆盖：

- 破坏性命令；
- credential exposure；
- network access；
- external write actions；
- privacy-sensitive files；
- unsafe intent；
- prompt injection；
- cross-skill activation risks。

## 7. Regression evals

重要历史失败应该变成 regression case，记录：原始 prompt、预期激活、预期流程、预期输出、已知坏行为、修复方式、回滚条件。

## 8. 扩展前先评估

加新规则前先问：

```text
哪个 eval 失败？
新规则针对哪个失败模式？
增加什么成本？
如何知道它有效？
```

不要因为一条规则听起来聪明，就扩张 `SKILL.md`。
