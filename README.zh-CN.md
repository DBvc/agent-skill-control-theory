# Agent 技能控制论

**Agent Skill Control Theory（ASCT，Agent 技能控制论）** 是一套用于设计、评审和演进 **LLM agent skills** 的第一性原理框架。

Skill 不只是更长的 prompt。在 ASCT 里，skill 是一个**选择性加载的策略控制器**：它通过指令、资源、工具、脚本和验证规则，改变 agent 在某类任务中的行为分布。

> 一句话：ASCT 研究如何用 skills 控制 LLM agent 的失败模式。

English version: [README.md](README.md).

## 状态

这是一套工作理论，不是官方标准。

它基于公开的 Agent Skills 格式和 progressive disclosure 机制，并参考以下公开资料：

- Agent Skills specification: https://agentskills.io/specification
- OpenAI Codex skills: https://developers.openai.com/codex/skills
- Anthropic Agent Skills overview: https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills
- Claude Agent Skills docs: https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview

ASCT 主要讨论 `SKILL.md + references/scripts/assets` 这类文件系统型 skill，尽量兼容 Claude、Codex 和其它 agent skill 实现。

## 核心定义

```text
Skill = 一个选择性加载的 LLM agent 策略控制器。
```

更完整地说：

```text
Skill 是针对某类任务被激活的控制层。
它通过运行时指令、外部上下文、确定性执行器、可复用素材和验证规则，
改变 agent 的动作分布。
```

ASCT 把常见 skill 文件映射到控制功能：

| Skill 构件 | ASCT 角色 |
|---|---|
| `description` | 激活分类器 |
| `SKILL.md` | 运行时控制器 |
| `references/` | 外部语义记忆 |
| `scripts/` | 确定性执行器 |
| `assets/` | 可复用素材先验 |
| `evals/` | 控制器回归测试 |

## 五条基础假设

1. **条件策略**：agent 行为会被上下文、指令、工具、观测和资源条件化。
2. **资源有界**：上下文、注意力、工具调用、时间、用户耐心和安全预算都是有限资源。
3. **非零错误率**：agent 在触发、意图理解、状态落地、轨迹选择、执行和完成声明上都有非零错误率。
4. **外部可证据化**：很多任务事实和确定性操作，外部证据与工具比模型生成更可靠。
5. **漂移**：模型、工具、API、代码库、组织和任务分布都会随时间变化。

## 七个控制面

| 控制面 | 它控制的问题 |
|---|---|
| Activation Control | 该不该使用这个 skill？ |
| Intent Control | 用户真正要的任务是什么？ |
| State Control | 当前真实状态是什么？ |
| Trajectory Control | agent 应该沿什么路径行动？ |
| Execution Control | 哪些操作要交给确定性工具？ |
| Completion Control | 什么时候可以说 done？ |
| Evolution Control | skill 如何避免漂移和回归？ |

## 九条设计定律

1. **触发边界定律**：skill 的第一质量是正确激活。
2. **任务编译定律**：skill 把用户原话编译成任务框架和运行模式。
3. **上下文经济定律**：`SKILL.md` 里的每个 token 都应该买到行为改变。
4. **证据外部化定律**：当前事实应来自外部证据，而不是模型潜在记忆。
5. **轨迹约束定律**：workflow 的作用是让坏路径更难发生。
6. **自由度风险定律**：风险越高的任务，agent 自由度越应降低。
7. **确定性外包定律**：模型负责判断，工具负责确定性执行。
8. **完成证明定律**：done = output + evidence + validation + limitations。
9. **漂移回归定律**：skill 是会漂移的控制器，需要 eval、版本和回归测试。

## 价值函数

ASCT 评价 skill 时看的是**净可靠性收益**，不是指令长度或形式优雅。

```text
SkillValue(s, D) =
  E_t~D[Success(agent_with_skill, t) - Success(base_agent, t)]
  - Cost(s, D)
  - Risk(s, D)
```

一个 skill 值得保留，当且仅当：

```text
SkillValue > 0
SafetyRisk <= acceptable_threshold
```

## 仓库结构

```text
docs/
  theory.md                 ASCT 完整理论，英文
  glossary.md               核心术语，英文
  control-surfaces.md       七个控制面，英文
  design-laws.md            九条设计定律，英文
  value-function.md         SkillValue 模型，英文
  safety.md                 安全约束，英文
  influences.md             公开资料和设计来源，英文
  zh-CN/                    中文版本

templates/
  skill-ir.yaml             skill 内部表示模板
  skill-design-brief.md     场景和失败地图模板
  skill-review-rubric.md    评审现有 skill 的 rubric
  eval-plan.md              触发、输出、安全 eval 模板
  patch-hypothesis.md       skill 修改假设模板

templates/zh-CN/              中文模板版本

examples/
  frontend-debug/           用 ASCT 设计的合成示例 skill

scripts/
  check_repo.py             轻量仓库检查
```

## 范围

核心理论不排名或点评具体公开 skill 仓库。

这样可以让 ASCT 聚焦相对稳定的控制原则，而不是容易随着外部项目演进而过期的仓库级判断。

启发过本框架的公开仓库只在 [docs/influences.md](docs/influences.md) 中作为资料来源和设计影响列出。

## 如何使用 ASCT

设计一个新 skill 时：

1. 定义任务分布。
2. 画出 agent 的高概率失败模式。
3. 选择相关控制面。
4. 在 `description` 里写激活分类器。
5. 在 `SKILL.md` 里写运行时控制器。
6. 长资料放进 `references/`。
7. 确定性检查放进 `scripts/`。
8. 定义完成证明。
9. 增加触发、输出和安全 eval。
10. 用 patch hypothesis 演进，不靠作者信心。

## 快速检查

```bash
python3 scripts/check_repo.py
```

设计 skill 时从这里开始：

```text
templates/skill-ir.yaml
templates/skill-design-brief.md
templates/skill-review-rubric.md
```

## License

MIT. See [LICENSE](LICENSE).
