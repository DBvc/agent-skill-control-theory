# 九条设计定律

ASCT 的设计定律是工程设计定律，不是自然定律。它们从五条基础假设推出，用来指导 skill authoring。

## 1. 触发边界定律

**skill 的第一质量是正确激活。**

因为 skill 是选择性加载的。如果它在错误任务中触发，内部 workflow 越强，干扰越强。

实践：`description` 应包含 use when、not for、near-miss 和相邻 skill 路由。

## 2. 任务编译定律

**skill 把用户原话编译成任务框架和运行模式。**

用户说“检查一下”，可能是 review、debug、design、release check、rewrite 或 decision support。skill 要选择最小充分模式，而不是直接执行表面文字。

实践：定义 quick、standard、deep、clarification、safety_redirect 等模式。

## 3. 上下文经济定律

**`SKILL.md` 里的每个 token 都应该买到行为改变。**

上下文和注意力有限。长文档不等于高可靠性。

实践：核心触发和 workflow 放 `SKILL.md`；长 rubric、示例、API 细节放 `references/`；确定性检查放 `scripts/`。

## 4. 证据外部化定律

**当前事实应来自外部证据，而不是模型隐式记忆。**

当前文件、diff、官方文档、日志、测试结果、截图和渲染产物通常比模型记忆更可靠。

实践：定义 source hierarchy，区分事实、假设、判断和未知。

## 5. 轨迹约束定律

**workflow 的意义是让坏路径更难发生。**

“Be careful” 很弱。“没有 pass/fail signal 不准改代码” 才是控制。

实践：使用 hard gates、stop conditions、fallback、handoff。

## 6. 自由度风险定律

**任务风险越高，agent 自由度越应降低。**

创意任务需要自由度，发布、删除、安全 verdict、格式敏感 artifact 需要 gates、dry-runs、validation 和 approvals。

## 7. 确定性外包定律

**模型负责判断，工具负责确定性执行。**

解析、计数、格式校验、渲染、schema validation、公式重算、危险命令拦截都更适合脚本或工具。

## 8. 完成证明定律

**done = 输出 + 证据 + 验证 + 限制条件。**

核心约束：

```text
final_claims ⊆ validated_evidence
```

没有验证就不能说“已验证”；无法验证要显式说明。

## 9. 漂移回归定律

**skill 是会漂移的控制器，需要 eval、版本和回归用例。**

每次重要修改都应说明：目标失败、拟议变更、预期收益、预期成本、更新哪些 eval、回滚条件。

## 总表

| 定律 | 主要目标 |
|---|---|
| 触发边界 | 错误激活 |
| 任务编译 | 误解用户意图 |
| 上下文经济 | 上下文膨胀 |
| 证据外部化 | 过期或想象事实 |
| 轨迹约束 | 看似合理的坏路径 |
| 自由度风险 | 风险与自由度错配 |
| 确定性外包 | 脆弱的自由文本执行 |
| 完成证明 | 完成幻觉 |
| 漂移回归 | 长期衰减 |
