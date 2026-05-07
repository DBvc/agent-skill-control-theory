---
name: frontend-debug
description: 当前端行为损坏、回归、渲染 bug、UI 交互 flaky、状态或时序问题需要诊断时使用。不要用于已完成 diff 的普通 review、新 UI 设计、commit message 写作，或没有 broken behavior 的主观视觉品味评价。
---

# Frontend Debug

这是一个用 ASCT 设计的合成示例 skill，用于展示如何把激活边界、反馈循环、轨迹约束、证据策略和完成证明组合起来。

## 目标

从可观察的前端异常出发，定位 root cause，做最小修复，并用证据证明修复有效。

不用于重新设计功能、审查无关代码或做泛泛质量提升。

## 模式选择

- `quick`：范围小、可复现、风险低。
- `standard`：普通 runtime、rendering、state、interaction bug。
- `deep`：flaky、跨浏览器、生产回归、数据丢失、安全敏感 UI 或多次失败。
- `clarification`：缺少必要复现信息。
- `safety_redirect`：请求不安全、不合法或未授权。

## Hard gates

没有以下任一条件前，不要修改代码：

- 可复现 pass/fail 信号；
- failing test；
- browser 或 interaction script；
- 最小手工复现路径；
- 能映射到症状的 log 或 trace。

不能写出可证伪 root-cause hypothesis 前，不要提出修复。

没有验证证据前，不要声称完成。

## Workflow

1. 症状盘点：复述 observed behavior 和 expected behavior。
2. 反馈循环：建立最快可靠的 pass/fail 信号。
3. 状态 grounding：检查当前文件、diff、logs、tests、screenshots、config。
4. 假设：生成一到三个排名假设，每个假设必须解释所有症状且可证伪。
5. Probe：一次只验证一个变量。
6. Fix：做最小修复，避免无关 refactor。
7. Validate：重新运行反馈循环和相关验证。
8. Completion 或 handoff：如果验证通过，输出完成证明；否则在多次失败后交接。

## Stop conditions

以下情况停止并交接：

- 三个 root-cause hypotheses 失败；
- 缺少必要环境访问；
- 无法建立验证；
- 需要产品或设计判断；
- 需要生产凭证或外部权限；
- 继续会导致无关修改。

## 证据策略

默认 source hierarchy：

```text
focused reproduction 或 failing test
> 当前 logs 和 browser evidence
> 当前 files 和 diff
> repo config 和 validation commands
> 官方文档或 installed package types
> 用户陈述
> 推断
```

## 输出契约

最终输出必须包含：

- Symptom
- Root cause
- Evidence
- Fix
- Validation
- Not validated
- Remaining risk

如果 handoff，包含：

- Known symptoms
- Feedback loop attempted
- Hypotheses tested
- Evidence collected
- Current best hypothesis
- Blocker
- Recommended next probe
