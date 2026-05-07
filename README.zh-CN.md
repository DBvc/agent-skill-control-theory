# Agent 技能控制论

**Agent Skill Control Theory**，简称 **ASCT**，是一套用于设计、评审、评估和演化 LLM agent skills 的第一性原理工程框架。

它的传播名可以叫 **Skill Mechanics，技能力学**。核心判断是：skill 不是更长的 prompt，不是人格，不是知识堆积。skill 是一种选择性加载的控制层，它改变 LLM agent 在一类重复任务中的行为方式。

```text
Skill = 一个选择性加载的 LLM agent 策略控制器。
```

更完整地说：

```text
Skill 是一个针对某类任务分布被激活的控制包。
它通过运行时指令、外部上下文、确定性执行器、可复用素材和验证规则，
改变 agent 的动作分布。
```

English version: [README.md](README.md).

## 状态

这是一套工作中的工程理论，不是官方标准。

ASCT 建立在公开 Agent Skills 格式和 progressive disclosure 模型之上，主要参考：

- [Agent Skills specification](https://agentskills.io/specification)
- [OpenAI Codex skills documentation](https://developers.openai.com/codex/skills)
- [Anthropic Agent Skills overview](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills)

这套理论刻意比完整 agent 架构窄。它聚焦的是以 `SKILL.md`、metadata、references、scripts、assets 和 evals 为核心的文件系统式 skill。

ASCT 的很多原则也适用于 agent workflow、prompt router、工具型 LLM 应用、多 agent 编排等场景。但在这个仓库里，我们先讨论 skill 这个明确对象。

## 为什么需要这套理论

很多 skill 仓库一开始都是有用的 prompt collection。短期没问题，长期会出现几类常见失败：

1. **经验堆积**：每遇到一个失败，就加一条规则。
2. **上下文膨胀**：`SKILL.md` 变成装满所有可能顾虑的大箱子。
3. **错误触发**：好 skill 被用在错误场景，变成坏控制。
4. **完成幻觉**：agent 因为答案写得完整，就声称任务完成。
5. **放置错误**：本该放到 scripts、hooks、references 或全局规则里的控制，被写成 skill 文案。
6. **未测量的信心**：作者觉得 skill 更完整，于是认为它更好。

ASCT 不从已有仓库归纳，而是从 agent 的运行结构出发。它问：

```text
基础 agent 在这个任务分布上会怎么失败？
skill 能控制 agent 行为的哪些面？
什么是最低成本、最低风险的有效控制器？
我们如何知道它真的改善了行为？
```

## 核心映射

ASCT 把常见 skill 构件映射成控制功能：

| Skill 构件 | ASCT 角色 | 控制的问题 |
|---|---|---|
| `description` | 激活分类器 | 这个 skill 是否该被使用？ |
| `SKILL.md` | 运行时控制器 | 激活后 agent 应该怎么做？ |
| `references/` | 外部语义记忆 | 哪些长内容或条件性知识应按需加载？ |
| `scripts/` | 确定性执行器 | 哪些事情不该靠自由文本生成完成？ |
| `assets/` | 可复用素材先验 | 哪些模板、示例、schema 或静态资源应被复用？ |
| `evals/` | 控制器回归测试 | 如何知道 skill 改善了行为并且没有回归？ |

commands、hooks、statusline、`AGENTS.md`、`CLAUDE.md`、`llms.txt`、marketplace metadata、generated indexes、planning files 和 project memory files 也都很有用。ASCT 把它们看成宿主环境相关的实现机制，并映射回相同的控制面，而不是把它们升格成新的基础概念。

## 五条基础假设

ASCT 使用五条基础假设：

1. **条件策略**：agent 行为会随上下文、指令、工具、观测和资源变化。
2. **资源有界**：上下文、注意力、工具调用、时间、用户耐心和安全预算都是有限资源。
3. **非零错误率**：agent 在触发、意图判断、状态 grounding、轨迹选择、执行和完成声明上都有非零错误率。
4. **外部可证据化**：很多任务事实和确定性操作，比起模型自由生成，更适合由外部证据和工具处理。
5. **漂移**：模型、工具、API、代码库、组织和任务分布都会随时间变化。

这些不是装饰性概念。它们解释了为什么 skill 需要触发边界、渐进加载、证据策略、确定性脚本、完成证明和回归测试。

## 七个控制面

skill 可能影响 agent 行为的七个方面：

| 控制面 | 控制的问题 |
|---|---|
| 激活控制 | 这个 skill 是否该使用？ |
| 意图控制 | 用户真正要完成什么任务？ |
| 状态控制 | 当前真实情况是什么？ |
| 轨迹控制 | agent 应该沿什么路径行动？ |
| 执行控制 | 哪些操作需要确定性工具？ |
| 完成控制 | agent 什么时候可以声称完成？ |
| 演化控制 | skill 如何避免漂移和回归？ |

不是每个 skill 都需要七个控制面。简单写作 skill 可能只需要激活和风格控制。发布类 skill 则可能需要激活、状态、轨迹、执行、完成、安全和演化控制。

## 九条设计定律

ASCT 从基础假设推出九条工程设计定律：

1. **触发边界定律**：skill 的第一质量是正确激活。
2. **任务编译定律**：skill 把用户原话编译成任务框架和运行模式。
3. **上下文经济定律**：`SKILL.md` 里的每个 token 都应该买到行为改变。
4. **证据外部化定律**：当前事实应来自外部证据，而不是模型隐式记忆。
5. **轨迹约束定律**：workflow 的意义是让坏路径更难发生。
6. **自由度风险定律**：任务风险越高，agent 自由度越应降低。
7. **确定性外包定律**：模型负责判断，工具负责确定性执行。
8. **完成证明定律**：done = 输出 + 证据 + 验证 + 限制条件。
9. **漂移回归定律**：skill 是会漂移的控制器，需要 eval、版本和回归测试。

## 价值函数

ASCT 评估 skill 时看净可靠性收益，而不是指令长度、优雅程度或作者自信。

```text
SkillValue(s, D) =
  E_t~D[Success(agent_with_skill, t) - Success(base_agent, t)]
  - Cost(s, D)
  - Risk(s, D)
```

一个 skill 必须先满足：

```text
SafetyRisk(s, D) <= SafetyBudget
```

然后才值得讨论：

```text
SkillValue(s, D) > 0
```

这个公式不是物理定律，而是评价框架。它的作用是防止我们把“更多指令”误认为“更高可靠性”。

## 仓库内容

```text
docs/
  theory.md                 完整 ASCT 理论
  foundations.md            定义、基础假设、定律、公式的层级
  control-surfaces.md       七个控制面
  design-laws.md            九条设计定律
  placement.md              判断控制应该放在哪里
  host-artifacts.md         commands、hooks、statusline、AGENTS.md、llms.txt 等宿主机制
  collection-design.md      skill collection 和 skill graph 设计
  value-function.md         success、cost、risk 和测量方法
  evaluation.md             trigger、output、process、safety 和 regression evals
  safety.md                 skill 和 skill collection 的安全约束
  glossary.md               术语表
  influences.md             公开来源和设计影响
  zh-CN/                    中文版本

templates/
  skill-ir.yaml             设计单个 skill 的内部表示
  collection-ir.yaml        设计 skill collection 的内部表示
  placement-decision.md     控制放置决策模板
  skill-design-brief.md     场景和失败模式模板
  skill-review-rubric.md    评审现有 skill 的 rubric
  eval-plan.md              eval 计划模板
  patch-hypothesis.md       skill 修改假设模板
  trigger-evals.json        trigger eval 示例
  output-eval-rubric.yaml   output eval rubric 示例
  zh-CN/                    中文模板版本

examples/
  frontend-debug/           一个用 ASCT 设计的合成示例 skill

scripts/
  check_repo.py             轻量仓库检查
```

## 如何使用 ASCT

设计新 skill 时：

1. 定义任务分布。
2. 识别基础 agent 的高概率失败模式。
3. 判断控制应该放在 skill、command、hook、script、reference、repo memory 还是 global instruction。
4. 选择相关控制面。
5. 在 `description` 中写激活分类器。
6. 在 `SKILL.md` 中写运行时控制器。
7. 把长内容和条件性知识移到 `references/`。
8. 把确定性检查移到 `scripts/`。
9. 定义完成证明。
10. 增加 trigger、output、process、safety 和 regression evals。
11. 用 patch hypothesis 演化，而不是靠作者自信演化。

评审现有 skill 时：

1. 它服务哪个任务分布？
2. 它减少哪些失败模式？
3. 它的构件分别映射到哪些控制面？
4. 它的上下文成本、摩擦成本、运行成本和安全风险是什么？
5. 它的最终声明是否绑定了证据？
6. 它有没有 near-miss trigger cases？
7. 哪些内容其实应该移出 `SKILL.md`？
8. 有没有 eval 证明它真的更好？

## 设计立场

ASCT 对理论扩张保持克制。

新的仓库、平台或宿主机制不应自动变成新基础概念。应该先尝试把它映射到五条基础假设、七个控制面和九条设计定律。只有当新案例暴露出当前理论无法解释的新失败类型时，才应该改变理论内核。

## 快速开始

运行检查：

```bash
python3 scripts/check_repo.py
```

设计单个 skill：

```text
templates/skill-ir.yaml
templates/skill-design-brief.md
templates/skill-review-rubric.md
templates/eval-plan.md
```

设计 skill collection：

```text
templates/collection-ir.yaml
```

做控制放置决策：

```text
templates/placement-decision.md
```

## License

MIT. See [LICENSE](LICENSE).
