# SkillValue

ASCT 用净可靠性收益评价 skill。

```text
SkillValue(s, D) =
  E_t~D[Success(agent_with_skill, t) - Success(base_agent, t)]
  - Cost(s, D)
  - Risk(s, D)
```

## 术语

- `s`：skill。
- `D`：任务分布。
- `agent_with_skill`：skill 激活后的 agent。
- `base_agent`：没有 skill 的同一 agent。
- `Success`：任务特定成功指标。
- `Cost`：skill 引入的摩擦。
- `Risk`：安全、隐私、副作用和误触发风险。

## 成本项

| 成本 | 含义 |
|---|---|
| Trigger cost | 选择和加载 skill 的成本。 |
| Context cost | skill 指令消耗的 token 和注意力。 |
| Tool cost | 工具和脚本的时间与运行成本。 |
| User friction | 额外问题、确认或输出重量。 |
| Maintenance cost | 未来保持 skill 正确的维护成本。 |
| Opportunity cost | 被这个 skill 挤掉的其它上下文或 skill。 |

## 风险项

| 风险 | 含义 |
|---|---|
| Wrong-trigger risk | skill 在错误任务上激活。 |
| Safety risk | skill 促成不安全或不正当行为。 |
| Privacy risk | skill 读取或暴露敏感信息。 |
| Side-effect risk | skill 执行外部或不可逆动作。 |
| Over-constraint risk | skill 限制了有用的创造性或适应性。 |
| Drift risk | skill 随环境变化而过期。 |

## 接受条件

Skill 可接受的前提：

```text
SafetyRisk(s, D) <= SafetyBudget
```

Skill 值得保留的前提：

```text
SkillValue(s, D) > 0
```

## 实用评分

无法精确测量时，用 1-5 分 rubric：

| 维度 | 1 | 5 |
|---|---|---|
| Success gain | 几乎无改善 | 相比 baseline 明显改善 |
| Trigger precision | 经常误触发 | 正例和 near-miss 都准确 |
| Context cost | 臃肿 | 最小充分控制器 |
| Validation strength | claim 无证据 | claim 映射到 evidence |
| Safety posture | 风险模糊 | fail-closed 且有显式确认 |
| Maintainability | 难维护 | 有 eval 和 patch hypothesis |

实用判断规则：

```text
当 SuccessGain + ValidationStrength + Maintainability
明显超过 ContextCost + Friction + Risk 时，保留。
```
