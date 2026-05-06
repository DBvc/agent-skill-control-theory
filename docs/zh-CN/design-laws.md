# 设计定律

这些是工程设计定律，不是自然科学定律。它们从 ASCT 的基础假设推出，用来指导 skill 写作。

## 1. 触发边界定律

Skill 的第一质量是正确激活。

### 为什么

Skill 是选择性加载的。如果它在错误任务里激活，所有 workflow 都会变成错用的控制。

### 实践

Description 应包含：

- use when；
- not for；
- near-miss cases；
- adjacent skill routing。

## 2. 任务编译定律

Skill 把用户原话编译成任务框架和运行模式。

### 为什么

用户语言经常模糊。Skill 必须选择最小充分模式。

### 实践

定义模式，例如：

- quick；
- standard；
- deep；
- clarification；
- safety redirect。

## 3. 上下文经济定律

`SKILL.md` 里的每个 token 都应该买到行为改变。

### 为什么

上下文和注意力有限。

### 实践

保持 `SKILL.md` 精炼。长 rubric、案例和参考资料放进 `references/`。确定性检查放进 `scripts/`。

## 4. 证据外部化定律

当前事实应该来自外部证据，而不是模型潜在记忆。

### 为什么

模型记忆可能过期、不完整或幻觉。

### 实践

定义 source hierarchy：

```text
直接工具输出 > 当前文件/diff > 官方文档 > 用户声明 > 推断 > 猜测
```

## 5. 轨迹约束定律

Workflow 的作用是让坏路径更难发生。

### 为什么

Agent 总能生成一个看似合理的下一步。Skill 必须阻止坏的“看似合理”。

### 实践

使用：

- hard gates；
- stop conditions；
- fallback paths；
- handoff format。

## 6. 自由度风险定律

风险越高的任务，agent 自由度越应降低。

### 为什么

动作越高风险、越不可逆、越有外部副作用，错误行动代价越高。

### 实践

- 创意设计：高自由度，taste rubric。
- 技术决策：中等自由度，assumptions 和 trade-offs。
- Debug：受控自由度，feedback loop 和 hypothesis gate。
- Artifact 生成：低自由度，validators 和 render checks。
- 发布/删除/外部写操作：极低自由度，approval 和 dry-run。

## 7. 确定性外包定律

模型做判断，工具做确定性执行。

### 为什么

重复、解析密集、数值敏感或格式敏感任务不应依赖自由文本生成。

### 实践

脚本用于：

- 解析；
- 验证；
- 渲染；
- 计数；
- 格式化；
- schema check；
- dangerous command guard。

## 8. 完成证明定律

Done = output + evidence + validation + limitations。

### 为什么

Agent 可以生成完成叙事，但实际没完成。

### 实践

要求：

- 改了什么；
- 跑了什么验证；
- 验证结果；
- 已知限制；
- 未验证事项。

## 9. 漂移回归定律

Skill 是会漂移的控制器，需要 eval、版本和 regression cases。

### 为什么

环境会变化。好行为也会退化。

### 实践

每次重要 skill 改动都应包含：

- target failure；
- proposed change；
- expected benefit；
- expected cost；
- evals updated；
- rollback condition。
