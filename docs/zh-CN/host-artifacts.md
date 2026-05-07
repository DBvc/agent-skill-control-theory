# 宿主相关构件

不同 agent 宿主支持不同构件：commands、hooks、statusline、plugin metadata、generated indexes、repo instructions、persistent planning files。

ASCT 不把这些视为新的基础概念，而是映射到七个控制面。

## 1. 角色与机制分离

标准 skill 核心通常是：

```text
SKILL.md
references/
scripts/
assets/
evals/
```

真实系统还会有：

```text
commands/
hooks/
statusline
AGENTS.md
CLAUDE.md
llms.txt
marketplace metadata
plugin manifests
planning files
project memory
```

它们很重要，但问题应该是：

```text
这个构件实现了哪个控制面？
```

## 2. 映射表

| 构件 | 典型 ASCT 角色 |
|---|---|
| Slash command | 显式激活或宏工作流 |
| Command file | 激活控制和轨迹控制 |
| Hook | 生命周期状态、轨迹、完成或安全控制 |
| Statusline | 用户可见状态或模式反馈 |
| `AGENTS.md` | repo-level 或 global policy controller |
| `CLAUDE.md` | repo-level 或宿主相关 policy controller |
| `llms.txt` | agent-facing discovery 和 routing index |
| Marketplace metadata | human discovery 和安装元数据 |
| Plugin manifest | 分发和能力元数据 |
| Planning file | 持久状态控制和轨迹控制 |
| Progress file | 持久状态控制和完成控制 |
| Project glossary | 持久状态控制 |
| ADR | 持久状态控制和演化控制 |
| Agent brief | handoff contract 和未来意图控制 |

## 3. 设计原则

不要把机制当理论。

```text
角色：Completion Control
某个宿主的机制：stop hook
另一个宿主的机制：validation command
第三个宿主的机制：SKILL.md 中的显式 checklist
```

理论关心的是控制功能，宿主决定具体机制。
