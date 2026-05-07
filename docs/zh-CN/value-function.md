# SkillValue：成功、成本、风险

ASCT 用净可靠性收益评估 skill：

```text
SkillValue(s, D) =
  E_t~D[Success(agent_with_skill, t) - Success(base_agent, t)]
  - Cost(s, D)
  - Risk(s, D)
```

其中：

- `s` 是 skill。
- `D` 是任务分布。
- `Success` 由任务定义。
- `Cost` 包括上下文、摩擦、运行、金钱、审计和维护成本。
- `Risk` 包括安全、隐私、副作用、安全工程、错误触发和漂移风险。

首先必须满足：

```text
SafetyRisk(s, D) <= SafetyBudget
```

然后才讨论：

```text
SkillValue(s, D) > 0
```

## 1. 为什么需要价值函数

skill 作者容易优化错指标：

- `SKILL.md` 长度；
- 规则数量；
- 语气严格程度；
- 结构优雅程度；
- 作者自信；
- 个别成功案例；
- 文件数量。

skill 可以变长但变差，可以更严格但更低效，也可以加入 scripts 后因为安全和维护成本变高而净价值下降。

价值函数要求我们问：

```text
这个 skill 是否以可接受成本和风险提升了任务成功率？
```

## 2. Success

Success 必须按任务分布定义。

代码审查 skill 的 success 可以包括：发现重要缺陷、避免 false positives、证据充分、severity 校准、fix direction 可用。

debug skill 的 success 可以包括：建立反馈循环、先定位 root cause 再 patch、修复通过验证、必要时添加 regression test。

artifact skill 的 success 可以包括：文件可打开、格式有效、渲染正确、公式或字段正确、验证命令通过。

教学型 skill 的 success 还可以包括：用户理解框架、未来独立性提升。

项目记忆型 skill 的 success 还可以包括：未来任务上下文成本下降、术语更稳定、决策更容易恢复。

## 3. Cost

成本不只是 token：

| 成本 | 含义 |
|---|---|
| Context cost | 激活前后加载的 token |
| Trigger cost | installed skills 列表拥挤、description 歧义、错误触发成本 |
| User friction cost | 澄清、审批、额外仪式、长输出 |
| Tool/runtime cost | shell、browser、tests、API、依赖 |
| Monetary cost | 付费 API、云服务、CI、外部平台成本 |
| Audit cost | 审查 scripts、依赖、网络访问、权限 |
| Maintenance cost | 维护 references、scripts、evals、兼容性说明 |
| Opportunity cost | skill 阻碍更简单充分的回答 |

## 4. Risk

风险不只是成本。有些风险会让 skill 不可接受。

| 风险 | 示例 |
|---|---|
| Safety risk | 有害、欺骗、未授权行为 |
| Security risk | secret 泄露、恶意脚本、依赖污染 |
| Privacy risk | 读取或传输敏感文件 |
| Side-effect risk | 发布、删除、关闭 issue、修改外部系统 |
| Wrong-trigger risk | 在相邻任务中误触发 |
| Over-control risk | 压制合理判断或创造性 |
| Under-control risk | 危险自由度未被约束 |
| Drift risk | 旧规则、过时文档、失效脚本 |
| Collection conflict risk | 多个 skill 互相矛盾或绕过安全门 |

## 5. 如何测量

不需要精确数字，但需要结构化对比：

```text
base agent
old skill
new skill
```

覆盖：

- positive trigger cases；
- negative trigger cases；
- near-miss trigger cases；
- happy path；
- edge cases；
- historical failures；
- safety cases。

指标包括：触发正确性、输出质量、流程遵循、验证强度、不支持声明、运行成本、用户摩擦、安全姿态。
