# Agent 技能控制论

Agent Skill Control Theory（ASCT，Agent 技能控制论）是一套用于设计和评估 LLM agent skills 的第一性原理框架。

它不是泛泛讨论所有 agent 架构，而是聚焦 **skills**：使用 `SKILL.md`、metadata、references、scripts、assets 和 progressive disclosure 的文件系统型能力包。

## 1. 为什么需要一套理论

很多 skill 仓库一开始只是有用 prompt 的集合。短期可用，但容易出现三个问题：

1. **被案例牵着走**：每遇到一个失败就加一条规则。
2. **上下文膨胀**：主 skill 文件变成装满所有顾虑的行李箱。
3. **无法测量的自信**：作者觉得更完整就是更好。

ASCT 不从现有 skill 样本出发，而是从 agent 的运行方式出发。

一个 LLM agent 可以抽象成：

```text
Agent = π(action | context, tools, observations, memory)
```

Agent 会在当前上下文、工具、观测和记忆条件下选择动作。Skill 之所以有效，是因为它改变了这些条件。

## 2. 核心定义

```text
Skill = 一个选择性加载的 LLM agent 策略控制器。
```

Skill 不只是知识包。它是在某类任务上被激活的控制层，用来改变 agent 的动作分布。

常见 skill 结构可以映射到控制功能：

| 构件 | 控制功能 |
|---|---|
| `description` | 激活分类器 |
| `SKILL.md` | 运行时控制器 |
| `references/` | 外部语义记忆 |
| `scripts/` | 确定性执行器 |
| `assets/` | 素材先验 |
| `evals/` | 控制器回归测试 |

这种映射不是文风问题，而是来自 progressive disclosure：metadata 常驻，完整 `SKILL.md` 触发后才加载，其它文件按需读取或执行。

## 3. 定义

### Agent

基于上下文、工具、观测和记忆选择动作的策略系统。

### Skill

选择性加载的策略控制器，用来改变 agent 在某类任务中的行为。

### Task distribution

一组重复出现、输入、约束、期望输出和失败模式相似的任务。

### Failure mode

没有该 skill 时，base agent 在该任务分布中高概率出现的失败路径。

### Control surface

Skill 可以影响的行为面：激活、意图、状态、轨迹、执行、完成或演化。

### Evidence

支持某个声明的外部可观察信息，例如文件内容、diff、日志、官方文档、命令输出、测试结果、截图、渲染产物、用户声明或项目记忆。

### Completion proof

Agent 声称任务完成前所需的证据和验证。

## 4. 五条基础假设

### P1. 条件策略

Agent 行为会被上下文、指令、工具、观测和资源改变。

如果这条不成立，skill 就不可能有效。Skill 有用，是因为 agent 的策略可以被条件化。

### P2. 资源有界

上下文、注意力、工具调用、执行时间、用户耐心和安全预算都是有限资源。

所以正确的 skill 不是最长的 skill，而是最小充分控制器。

### P3. 非零错误率

Agent 在激活、意图推断、状态落地、轨迹选择、执行和完成声明上都有非零错误率。

所以 skill 应该从失败模式出发设计。

### P4. 外部可证据化

许多任务相关事实和确定性操作，可以通过外部证据和工具比模型生成更可靠地处理。

所以成熟 skill 会把事实从模型潜在记忆中移出来，把确定性工作从自由文本生成中移出来。

### P5. 漂移

模型、工具、API、代码库、组织和任务分布都会随时间变化。

所以 skill 不是静态文档，而是会漂移的控制器，需要评估和回归。

## 5. 七个控制面

### 5.1 Activation Control

问题：**该不该使用这个 skill？**

机制：

- `name`
- `description`
- 显式调用名
- not-for 边界
- 相邻 skill 路由
- trigger evals

坏的激活分类器会让好的运行时控制器变成干扰。

### 5.2 Intent Control

问题：**用户真正要的任务是什么？**

机制：

- mode routing
- input contract
- clarification gates
- non-goals
- task frame selection

用户话语经常含糊。Skill 要把它们编译成任务框架。

### 5.3 State Control

问题：**当前真实状态是什么？**

机制：

- 读取文件
- 检查 diff
- 官方文档
- 日志和命令输出
- 渲染截图
- 项目记忆，例如 glossary、ADR、issue history

State control 防止 agent 基于过期或想象的事实行动。

### 5.4 Trajectory Control

问题：**agent 应该走什么行动路径？**

机制：

- workflow
- hard gates
- stop conditions
- fallback paths
- escalation rules
- handoff rules

Workflow 不是仪式，而是对坏行动路径的约束。

### 5.5 Execution Control

问题：**哪些操作需要确定性工具？**

机制：

- scripts
- validators
- renderers
- linters
- schema checks
- dry-run commands
- dangerous action guards

模型负责判断，确定性工具负责执行。

### 5.6 Completion Control

问题：**什么时候可以声称 done？**

机制：

- validation commands
- proof fields
- claim-evidence mapping
- confidence levels
- known limitations
- unverified work disclosure

Skill 应该压制“完成幻觉”。

### 5.7 Evolution Control

问题：**skill 如何避免漂移和回归？**

机制：

- trigger evals
- output evals
- safety evals
- versioning
- patch hypotheses
- regression suites
- compatibility notes

没有评估的 skill 只是作者信念，不是工程资产。

## 6. 设计定律

### Law 1：触发边界定律

Skill 的第一质量是正确激活。

错误激活会直接产生伤害：浪费上下文、套错 workflow、增加摩擦，甚至触发不安全动作。

### Law 2：任务编译定律

Skill 把用户原话编译成任务框架和运行模式。

用户说“帮我看看”，skill 要判断这到底是 review、debug、design、release check、rewrite 还是 decision support。

### Law 3：上下文经济定律

`SKILL.md` 里的每个 token 都应该买到行为改变。

长理论、详尽案例和领域参考应该放进 `references/`，除非每次激活都需要它们。

### Law 4：证据外部化定律

当前事实应该来自外部证据，而不是模型潜在记忆。

代码库状态、官方 API、diff、渲染产物、命令输出和用户文档应优先于模型记忆。

### Law 5：轨迹约束定律

Workflow 的作用是让坏路径更难发生。

“请谨慎”很弱。“改代码前必须先建立可复现 pass/fail 信号”很强。

### Law 6：自由度风险定律

风险越高的任务，agent 自由度越应降低。

创意任务需要空间。破坏性动作、发布操作、格式敏感产物和安全敏感任务需要 gates、dry-run 和验证。

### Law 7：确定性外包定律

模型做判断，工具做确定性执行。

如果同样输入应该得到同样输出，优先使用脚本、验证器、解析器或渲染器。

### Law 8：完成证明定律

Done = output + evidence + validation + limitations。

```text
final_claims ⊆ validated_evidence
```

如果没有运行验证，最终输出必须明确说明。

### Law 9：漂移回归定律

Skill 是会漂移的控制器，需要 eval、版本和回归测试。

每次修改 skill 都应该说明：它要减少哪种失败，增加了什么成本，哪些 eval 能发现回归。

## 7. SkillValue

Skill 应该按净可靠性收益评价：

```text
SkillValue(s, D) =
  E_t~D[Success(agent_with_skill, t) - Success(base_agent, t)]
  - Cost(s, D)
  - Risk(s, D)
```

其中：

- `s` 是 skill。
- `D` 是任务分布。
- `Success` 由任务特定标准衡量。
- `Cost` 包括触发成本、上下文成本、工具成本、用户摩擦和维护成本。
- `Risk` 包括安全风险、副作用风险、隐私风险和误触发风险。

Skill 可被接受的前提：

```text
SafetyRisk(s, D) <= SafetyBudget
```

Skill 值得保留的前提：

```text
SkillValue(s, D) > 0
```

## 8. ASCT 设计循环

1. 定义任务分布。
2. 识别 base agent 可能出现的失败模式。
3. 选择控制面。
4. 写激活分类器。
5. 写运行时控制器。
6. 外部化证据和长记忆。
7. 委托确定性工作。
8. 定义完成证明。
9. 加 eval 和 regression case。
10. 通过 patch hypothesis 演进。

## 9. ASCT 不是什么

ASCT 不是：

- 官方 Agent Skills 规范；
- 所有 LLM 应用的统一理论；
- 每个 skill 都必须具备每个控制面的要求；
- 让简单任务过度结构化的理由；
- 领域专业知识或评估的替代品。

ASCT 是一个设计镜片。它帮助你判断一个 skill 控制了什么、成本是什么、风险是什么，以及它是否真的改善了真实任务分布上的 agent 行为。
