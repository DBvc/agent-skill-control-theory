# 放置决策

成熟 skill 作者不会只问“这个 skill 该写什么”，而会问：

```text
这个控制应该放在哪里？
```

ASCT 把放置决策作为一等设计问题。很多有用控制不应该写进 `SKILL.md`。

## 1. 为什么放置重要

错误放置会增加成本和风险：

- 始终适用的规则如果藏在很少触发的 skill 里，就不可靠。
- 确定性检查如果写成 prose，就脆弱。
- 长参考资料如果塞进 `SKILL.md`，就污染上下文。
- 危险动作拦截如果依赖模型记忆，就不安全。
- 多 skill workflow 如果没有 command 或 routing 层，就容易混乱。

目标是：把控制放到能以最低成本和风险减少失败的位置。

## 2. 可选位置

| 位置 | 适合什么 |
|---|---|
| Skill | 选择性加载的重复任务 workflow |
| Global instruction | 始终适用的规范和约束 |
| Command | 显式宏工作流或多 skill 编排 |
| Hook | 生命周期 gate、状态刷新、危险动作拦截 |
| Script | 确定性或重复操作 |
| Reference | 长知识或条件性知识 |
| Asset | 模板、schema、数据、示例 |
| Repo memory | 项目术语、ADR、agent brief、已知约束 |
| Collection routing | skill 优先级、冲突解决、安装范围 |

## 3. 决策流程

1. 控制是否始终相关？如果是，优先 global instruction、repo instruction 或 hook。
2. 控制是否确定性？如果是，优先 script、validator、linter、renderer 或 hook。
3. 控制是否是长知识或条件性知识？如果是，优先 `references/`。
4. 控制是否是持久项目状态？如果是，优先 repo memory。
5. 控制是否编排多个 skills？如果是，优先 command 或 collection routing。
6. 控制是否是任务特定、重复出现的 workflow？如果是，适合 skill。

## 4. 反模式

- 所有东西都塞进 `SKILL.md`。
- 所有好规则都做成 skill。
- 所有约束都靠 hook。
- 所有知识都放 reference，但没有 runtime control。
- 所有事情都脚本化，但没有判断层。

## 5. 示例

“不要声称测试通过，除非真的运行过”：

- global instruction 处理一般诚实原则；
- skill completion contract 处理具体任务证明；
- eval 做回归检查。

“阻止 `git reset --hard`”：

- 最好用 hook 或命令 guard；
- skill 文案只能作为二级提醒。

“项目术语 X 表示 Y”：

- 放到 repo memory 或 reference；
- skill 可以要求读取它。

使用 [templates/zh-CN/placement-decision.md](../../templates/zh-CN/placement-decision.md) 做具体决策。
