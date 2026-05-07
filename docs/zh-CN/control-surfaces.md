# 七个控制面

控制面是 skill 可以影响 agent 行为的部分。ASCT 定义七个控制面：激活、意图、状态、轨迹、执行、完成、演化。

它们不是每个 `SKILL.md` 必须出现的章节，而是诊断工具。设计 skill 时要问：这个任务分布需要控制哪些面，哪些面可以保持轻量。

## 1. 激活控制

**问题：这个 skill 是否该被使用？**

机制：`name`、`description`、显式命令、not-for 边界、near-miss 示例、相邻 skill 路由、生成索引、trigger evals。

一个触发错误的 skill 会直接降低可靠性。比如 debug skill 错触发到普通 code review，会让 agent 做不必要的根因分析；release skill 错触发到 release notes 写作，则可能引入不必要的外部动作风险。

评审问题：

- 正向触发是什么？
- 负向触发是什么？
- near-miss 是什么？
- 哪些 skill 会与它竞争？
- 如果 description 被宿主截短，关键触发词还在吗？

## 2. 意图控制

**问题：用户真正要完成什么任务？**

用户语言是压缩过的。“帮我看看”可能是 review、debug、design、rewrite、release check、decision support。

机制：mode routing、input contract、clarification gate、non-goal、任务类型决策树、安全重定向。

常见模式：

```text
quick: 低风险、范围清楚
standard: 普通任务，有中等不确定性
deep: 高风险、宽范围、公开、架构或安全敏感
clarification: 缺少必要输入
safety_redirect: 不安全或不合法请求
```

## 3. 状态控制

**问题：当前真实情况是什么？**

状态控制防止 agent 依赖过期记忆、想象出来的文件结构、过时 API 或未经验证的用户假设。

机制：读文件、看 diff、命令输出、日志、官方文档、截图、渲染产物、issue 历史、ADR、项目术语表、持久项目记忆。

示例 source hierarchy：

```text
直接工具输出
> 当前文件和 diff
> 官方文档
> 渲染产物或截图
> 用户陈述
> 推断
> 猜测
```

## 4. 轨迹控制

**问题：agent 应该沿什么路径行动？**

轨迹控制是 workflow 层。workflow 的目的不是仪式，而是减少坏路径概率。

机制：workflow、hard gates、stop conditions、fallback、escalation、handoff、checkpoint。

弱控制：

```text
仔细一点，系统地排查。
```

强控制：

```text
修改代码前必须建立可复现的 pass/fail 信号。
提出修复前必须写出可证伪的 root-cause hypothesis。
三个假设失败后停止，并输出 handoff。
```

## 5. 执行控制

**问题：哪些操作需要确定性工具？**

核心区分：

```text
模型负责判断，工具负责确定性执行。
```

适合脚本或工具的任务：解析、验证、渲染、计数、格式化、schema check、公式重算、危险命令拦截。

## 6. 完成控制

**问题：agent 什么时候可以声称完成？**

完成控制用于抑制完成幻觉。

核心约束：

```text
final_claims ⊆ validated_evidence
```

好的完成输出包括：做了什么、证据、验证、未验证项、已知限制、剩余风险。

## 7. 演化控制

**问题：skill 如何避免漂移和回归？**

机制：trigger evals、output evals、process evals、safety evals、regression cases、compatibility notes、versioning、deprecation policy、patch hypotheses。

没有 eval 的 skill 是作者信念，不是工程资产。

## 8. 控制面的组合

七个控制面相互影响：

- 激活控制差，会增加上下文成本和错误轨迹风险。
- 状态控制差，会削弱完成控制。
- 执行控制差，会制造虚假完成证明。
- 意图控制差，会让 agent 进入错误 workflow。
- 演化控制差，会让其他控制面随时间衰减。

强 skill 不是最大化所有控制面，而是在任务分布上以合适强度使用必要控制。
