# Agent 技能控制论

Agent Skill Control Theory，简称 ASCT，是一套用于设计和评估 LLM agent skills 的第一性原理框架。

它刻意比完整 agent 架构窄。它聚焦的是 skill：一种围绕 `SKILL.md`、metadata、references、scripts、assets 和 progressive disclosure 构建的可移植行为包。

## 1. 中心命题

ASCT 的中心命题是：

```text
Skill = 一个选择性加载的 LLM agent 策略控制器。
```

这句话的每个词都有含义：

- **Skill**：用于一类重复任务的可复用行为包。
- **选择性加载**：它不是始终生效，而是通过显式调用、隐式匹配或宿主路由被选中。
- **策略控制器**：它改变 agent 的动作分布，让某些路径更可能、某些路径更不可能、某些路径被禁止。
- **LLM agent**：目标不是静态文本生成器，而是可以读文件、调工具、执行代码、检查结果、修改环境的 agent。

因此，skill 不是 prompt。prompt 请求一次回答；skill 控制一种可重复的 agent 行为模式。

## 2. 为什么 prompt collection 不够

prompt collection 可以局部改善回答，但 skill system 必须处理更复杂的问题：

1. **激活**：agent 要知道什么时候用这个 skill，什么时候不用。
2. **歧义**：agent 要把模糊用户请求编译成任务框架。
3. **状态**：agent 要 grounding 到当前代码库、文档、工具和环境。
4. **轨迹**：agent 要避免看似合理但错误的下一步。
5. **执行**：agent 要把确定性工作交给工具。
6. **完成**：agent 不能在没有证据时声称完成。
7. **演化**：skill 要随着模型、工具、API 和工作流变化而维护。

prompt collection 主要包含建议。skill system 包含控制。

## 3. 最小 agent 模型

ASCT 把 LLM agent 建模为：

```text
Agent = π(action | context, tools, observations, memory)
```

agent 在上下文、工具、观测和记忆影响下选择动作。skill 改变这些条件。

```text
Base agent:
  π0(action | C)

Skill-activated agent:
  πs(action | C + I_s + R_s + T_s + V_s)
```

其中：

- `I_s`：运行时指令，通常是 `SKILL.md`。
- `R_s`：references、assets、project memory 或其他外部上下文。
- `T_s`：skill 让 agent 注意到的工具或脚本。
- `V_s`：验证和完成规则。

skill 不替代 agent。skill 塑形 agent。

## 4. 标准 skill 结构为什么重要

公开 Agent Skills 格式把 skill 定义为至少包含 `SKILL.md` 的目录，`SKILL.md` 包含 YAML frontmatter 和 Markdown body。可选目录包括 `scripts/`、`references/` 和 `assets/`。

ASCT 把这些文件解释为控制功能：

| Artifact | 控制功能 |
|---|---|
| `description` | 激活分类器 |
| `SKILL.md` | 运行时控制器 |
| `references/` | 外部语义记忆 |
| `scripts/` | 确定性执行器 |
| `assets/` | 可复用素材先验 |
| `evals/` | 控制器回归测试 |

这个映射来自 progressive disclosure。metadata 在激活前可见，完整 `SKILL.md` 只在激活后加载，references/scripts/assets 按需使用。

## 5. 五条基础假设

ASCT 建立在五条基础假设上：

1. **条件策略**：agent 行为会受上下文、指令、工具、观测和资源影响。
2. **资源有界**：上下文、注意力、工具调用、时间、用户耐心、金钱成本和安全预算有限。
3. **非零错误率**：agent 在触发、意图推断、状态 grounding、轨迹选择、执行和完成声明上都有非零错误率。
4. **外部可证据化**：许多任务事实和确定性操作可以由外部证据和工具更可靠地处理。
5. **漂移**：模型、工具、API、代码库、组织、任务分布和用户习惯都会变化。

## 6. 七个控制面

### 6.1 激活控制

问题：**这个 skill 是否该使用？**

机制包括 `name`、`description`、显式命令、not-for 边界、相邻 skill 路由、生成索引和 trigger evals。

错误激活会让好 skill 变成坏控制。

### 6.2 意图控制

问题：**用户真正要完成什么任务？**

用户说“帮我看看”，可能是 review、debug、design、release check、rewrite 或 decision support。skill 要把自然语言编译成任务框架和运行模式。

### 6.3 状态控制

问题：**当前真实情况是什么？**

状态控制防止 agent 依赖过期记忆或想象事实。它使用当前文件、diff、日志、官方文档、测试输出、截图、渲染产物、issue 历史、ADR、术语表和项目记忆。

### 6.4 轨迹控制

问题：**agent 应该沿什么路径行动？**

workflow 不是仪式，而是减少坏路径概率的约束层。好的轨迹控制包含 hard gates、stop conditions、fallback、escalation 和 handoff。

### 6.5 执行控制

问题：**哪些操作需要确定性工具？**

核心区分：

```text
模型负责判断，工具负责确定性执行。
```

### 6.6 完成控制

问题：**agent 什么时候可以声称完成？**

完成控制用于抑制完成幻觉，要求 proof fields、validation results、claim-evidence mapping、confidence、known limitations 和 unverified-work disclosure。

核心约束：

```text
final_claims ⊆ validated_evidence
```

### 6.7 演化控制

问题：**skill 如何避免漂移和回归？**

机制包括 trigger evals、output evals、safety evals、regression suites、versioning、compatibility notes 和 patch hypotheses。

没有 eval 的 skill 是作者信念，不是工程资产。

## 7. 放置决策

ASCT 不认为每条有用控制都应该成为 skill。它要求每条控制放到能以最低成本和风险减少失败的位置。

可能的位置：

| 位置 | 适合什么 |
|---|---|
| Skill | 选择性加载的重复任务 workflow |
| Global instruction | 始终适用的规范和约束 |
| Command | 显式宏工作流或多 skill 编排 |
| Hook | 生命周期 gate、状态刷新、危险动作拦截 |
| Script | 确定性、重复、格式敏感的工作 |
| Reference | 长内容或条件性知识 |
| Asset | 模板、schema、数据文件、示例 |
| Repo memory | 项目术语、ADR、agent brief、已知约束 |
| Collection routing | skill 优先级、冲突解决、安装范围 |

成熟 skill 作者不会只问“这个 skill 该写什么”，还会问“这个控制应该放在哪里”。

## 8. Skill collection

真实 skill system 往往包含多个 skills、commands、hooks、indexes、marketplace metadata、global instructions 和 repo memory。ASCT 把这看成 collection-level design，而不是新基础概念。

在 collection 层面，七个控制面再次出现：

- 激活控制变成 routing 和 discovery。
- 意图控制变成 command design 和任务拆解。
- 状态控制变成共享项目记忆和生成索引。
- 轨迹控制变成 skill graph。
- 执行控制变成共享 scripts、hooks 和 tool policy。
- 完成控制变成跨 skill handoff contract。
- 演化控制变成版本、回归、废弃和发布治理。

理论不变，作用范围扩大。

## 9. 九条设计定律

1. **触发边界定律**：skill 的第一质量是正确激活。
2. **任务编译定律**：skill 把用户原话编译成任务框架和运行模式。
3. **上下文经济定律**：`SKILL.md` 里的每个 token 都应该买到行为改变。
4. **证据外部化定律**：当前事实应来自外部证据，而不是模型隐式记忆。
5. **轨迹约束定律**：workflow 的意义是让坏路径更难发生。
6. **自由度风险定律**：任务风险越高，agent 自由度越应降低。
7. **确定性外包定律**：模型负责判断，工具负责确定性执行。
8. **完成证明定律**：done = 输出 + 证据 + 验证 + 限制条件。
9. **漂移回归定律**：skill 是会漂移的控制器，需要 eval、版本和回归测试。

## 10. 价值与安全

ASCT 用净可靠性收益评估 skill：

```text
SkillValue(s, D) =
  E_t~D[Success(agent_with_skill, t) - Success(base_agent, t)]
  - Cost(s, D)
  - Risk(s, D)
```

首先必须满足：

```text
SafetyRisk(s, D) <= SafetyBudget
```

然后才讨论：

```text
SkillValue(s, D) > 0
```

## 11. 设计循环

1. 定义任务分布。
2. 识别基础 agent 的失败模式。
3. 做放置决策。
4. 选择控制面。
5. 写激活分类器。
6. 写运行时控制器。
7. 外部化证据和长记忆。
8. 外包确定性工作。
9. 定义完成证明。
10. 增加 eval 和 regression。
11. 通过 patch hypothesis 演化。

## 12. ASCT 不是什么

ASCT 不是：

- 官方 Agent Skills 规范；
- 所有 LLM 应用的统一理论；
- 每个 skill 都必须包含所有控制面的理由；
- 把简单任务过度结构化的借口；
- 领域知识的替代品；
- 实证评估的替代品；
- 把每条有用规则都塞进 `SKILL.md` 的理由。

ASCT 是一个设计透镜。它帮助作者判断 skill 控制了什么、花费什么、冒什么风险，以及是否在真实任务分布上改善行为。
