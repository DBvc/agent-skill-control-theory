# Skill Collection 设计

skill collection 不只是多个 skill 文件的集合。一旦进入 collection 层，会出现路由、组合、冲突、安装范围、安全审计、版本和废弃等问题。

ASCT 通过把七个控制面应用到 collection 层来处理这些问题。

## 1. 为什么需要 collection design

单个 skill 写得很好，放进 collection 后仍可能表现很差：

- 多个 skills 对同一请求同时触发。
- 没有 skill 触发，因为 description 过窄。
- command 绕过安全检查。
- skill A 的输出 skill B 不能接。
- 大型 catalog 增加安装和审计风险。
- human-facing metadata 和 agent-facing metadata 混淆。
- deprecated skill 仍然可见。

## 2. Collection 层的控制面

| 控制面 | collection 层表现 |
|---|---|
| 激活控制 | catalog、generated index、priority、conflict rules |
| 意图控制 | commands、任务分类、路由问题 |
| 状态控制 | 共享 references、project memory、shared indexes |
| 轨迹控制 | skill graph、required order、handoff contracts |
| 执行控制 | 共享 scripts、tool policy、hook policy |
| 完成控制 | 跨 skill 证明要求和输出契约 |
| 演化控制 | release、eval suites、deprecation、compatibility |

## 3. 人类发现 vs agent 激活

marketplace description 面向人类；skill `description` 面向 agent 激活。两者不应混淆。

人类发现元数据可以写得概括。agent 激活元数据必须写清 use when、not for 和 trigger terms。

## 4. Skill graph

skill graph 描述 skill 之间的关系：

```text
precedes: A 应在 B 前运行
requires: B 依赖 A 的输出
competes: A 和 B 是替代关系
fallback: A 无法继续时使用 B
handoff: A 为 B 生成交接契约
```

## 5. 冲突解决

当两个 skill 可能触发时，collection 应定义优先级。

示例：

```text
active broken behavior -> debug skill
completed diff review -> code review skill
release prose -> writing skill
release publish/tag -> release action skill
```

## 6. 安装范围和安全

大型 catalog 不应默认整包安装。需要考虑：

- user / repo / organization scope；
- trusted vs untrusted skills；
- script permissions；
- network access；
- dependency installation；
- environment variables；
- marketplace provenance。

最小权限原则也适用于 skills。

使用 [templates/zh-CN/collection-ir.yaml](../../templates/zh-CN/collection-ir.yaml) 设计 collection。
