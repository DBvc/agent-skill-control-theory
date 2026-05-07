# 基础：定义、基础假设、设计定律和公式

ASCT 使用了一些听起来比较数学化的词：定义、基础假设、定律、推论、公式。为了让理论严谨但不过度宣称，本文件先固定这些词在本仓库中的层级。

## 1. 概念层级

| 术语 | 在 ASCT 中的含义 | 示例 |
|---|---|---|
| 定义 | 规定一个词在本理论中的含义 | “skill 是选择性加载的策略控制器” |
| 基础假设 | 关于当前 LLM agent 和 skill 系统的基础前提 | “上下文、注意力和安全预算是有限的” |
| 派生命题 | 从定义和基础假设推出的结论 | “触发不清会让好 skill 变成坏控制” |
| 设计定律 | 从理论推出并被工程实践反复支持的稳定规则 | “模型负责判断，工具负责确定性执行” |
| 推论 | 设计定律的具体实践结论 | “parse-heavy 的验证应放进 scripts，而不是 prose” |
| 公式 | 用符号表达评价关系，通常是近似模型 | `SkillValue = SuccessGain - Cost - Risk` |

ASCT 不把这些定律包装成自然科学定律。它们是当前 agent 范式下的工程定律：上下文条件化模型、有限上下文、工具使用、外部文件、非零错误率和不断变化的运行环境。

## 2. 为什么用“基础假设”，不用“公理”

“公理”容易让人联想到严格数学系统。ASCT 是工程理论，所以更稳妥的说法是 **postulates / 基础假设**。

如果未来 agent 拥有无限上下文、完美 grounding、零错误触发、确定性执行和无安全风险，那么 ASCT 就不是合适理论。但在当前系统里，这些前提并不成立。

## 3. 理论对象

ASCT 研究 skill，而不是所有 prompt 或所有 agent 应用。

skill 有几个特殊性质：

1. **可打包**：通常是带 `SKILL.md` 和可选资源的目录。
2. **可选择**：不是始终生效，而是按任务触发。
3. **上下文化**：通过进入 agent context 改变行为。
4. **可迁移**：可以安装、分享、评审和版本化。
5. **可组合**：可以和其他 skills、commands、hooks、repo rules 一起工作。

这些性质让 skill 设计不同于普通 prompt 写作。prompt 可以只服务一次回答，skill 必须在一个任务分布上重复可靠地工作。

## 4. 最小形式模型

ASCT 把 agent 抽象为上下文条件化策略：

```text
Agent = π(action | context, tools, observations, memory)
```

skill 改变 agent 选择动作的条件：

```text
Base agent:
  π0(action | C)

Skill-activated agent:
  πs(action | C + I_s + R_s + T_s + V_s)
```

其中：

- `C` 是原始上下文。
- `I_s` 是 skill instruction，通常是 `SKILL.md`。
- `R_s` 是 references、assets 或 project memory。
- `T_s` 是 tool 或 script affordance。
- `V_s` 是 validation policy。

skill 的目标不是最大化指令量，而是在可接受成本和风险下提升任务成功率。

## 5. 核心定义

### Agent

基于当前 prompt、工具、观测和记忆选择动作的上下文条件化系统。

### Skill

一个选择性加载的策略控制器，用于改变 agent 在一类重复任务中的行为。

### Task distribution，任务分布

一组具有相似输入、约束、期望输出、成功标准和失败模式的重复任务。

### Failure mode，失败模式

基础 agent 在该任务分布上高概率失败的路径。

### Control surface，控制面

skill 可以影响 agent 行为的某一方面：激活、意图、状态、轨迹、执行、完成或演化。

### Evidence，证据

支持某个声明的外部可观察信息，例如文件内容、diff、日志、官方文档、命令输出、测试、截图、渲染产物、用户文档、issue 历史或项目记忆。

### Completion proof，完成证明

agent 在声称任务完成前必须拥有的证据和验证。

### Placement decision，放置决策

决定一个控制应该放在哪里：skill、global instruction、command、hook、script、reference、asset、repo memory 或 collection routing。

## 6. 五条基础假设

### P1. 条件策略

agent 行为会随上下文、指令、工具、观测和资源变化。

如果这不成立，skill 就不会有用。

### P2. 资源有界

上下文、注意力、工具调用、执行时间、用户耐心、金钱成本和安全预算都是有限资源。

因此，最长的 skill 不等于最好的 skill。最好的 skill 是能可靠降低目标失败模式的最小充分控制器。

### P3. 非零错误率

agent 在触发、意图推断、状态 grounding、轨迹选择、执行和完成声明上都有非零错误率。

因此，skill 设计应该以失败模式为起点。

### P4. 外部可证据化

许多任务事实和确定性操作可以由外部证据和工具更可靠地处理。

因此，成熟 skill 会把当前事实从模型隐式记忆中移出，把确定性工作从自由文本生成中移出。

### P5. 漂移

模型、工具、API、代码库、组织、任务分布和用户习惯都会变化。

因此，skill 不是静态文档，而是需要 eval、版本、兼容性说明和回归用例的漂移控制器。

## 7. 从基础假设到设计定律

九条设计定律不是任意最佳实践，而是从基础假设自然推出：

- 因为行为可被条件化，skill 才能控制 agent。
- 因为 skill 是选择性加载，触发边界才是第一设计。
- 因为资源有界，上下文经济才重要。
- 因为 agent 有非零错误率，workflow 必须阻止坏路径。
- 因为外部证据更可靠，state grounding 才重要。
- 因为确定性工具能胜过自由生成，scripts 才重要。
- 因为 agent 会产生完成幻觉，completion proof 才重要。
- 因为环境会漂移，eval 和 regression 才重要。

这条推导链，是 ASCT 区别于 checklist 的地方。

## 8. 公式的角色

SkillValue 不是精确计算器，而是推理框架：

```text
SkillValue(s, D) =
  E_t~D[Success(agent_with_skill, t) - Success(base_agent, t)]
  - Cost(s, D)
  - Risk(s, D)
```

它的作用是让隐形 trade-off 变得可见。一个 skill 可能提高某个任务的成功率，同时因为错误触发、上下文拥挤、用户摩擦、脚本风险或维护漂移而降低整体可靠性。

安全不是普通成本项：

```text
SafetyRisk(s, D) <= SafetyBudget
```

高收益但越过安全预算的 skill 不可接受。
