---
name: frontend-debug
description: Diagnose and fix active frontend bugs, regressions, rendering issues, flaky UI behavior, or broken user interactions. Use when the user reports something is currently broken, failing, visually regressed, flaky, or inconsistent in a web UI. Not for general code review, new feature design, subjective visual taste, or writing PR descriptions.
---

# Frontend Debug 中文说明

这是 `SKILL.md` 的中文阅读版。真正安装 skill 时请使用英文 `SKILL.md`。

使用这个 skill 诊断活跃的前端故障，并产出最小、已验证的修复。

目标不是做大范围优化，而是建立可靠反馈循环、识别可证伪根因、做最小充分改动并验证结果。

## 模式选择

选择最小充分模式：

- `quick`：明显局部 bug，已有失败测试或清晰复现。
- `standard`：普通 UI 故障、回归或渲染问题。
- `deep`：flaky 行为、竞态、跨浏览器问题、hydration 问题、发布关键 bug 或多次修复失败。
- `clarification`：症状或复现信息缺失。
- `safety_redirect`：用户要求不安全、欺骗性或未授权行为。

## 必要输入

改代码前识别：

- 症状；
- 复现路径；
- 期望行为；
- 实际行为；
- 受影响 route/component/browser/device；
- 是否是回归；
- 可用验证命令或 UI 检查。

如果复现缺失，先询问或根据已有证据构造最小可观察反馈循环。

## Hard gates

在至少有一个 pass/fail 反馈信号前，不修改生产代码：

- 失败测试；
- 浏览器复现；
- console/log assertion；
- 截图对比；
- CLI 或 API fixture；
- 最小复现脚本；
- 用户确认的复现步骤。

如果根因假设不能解释所有观察到的症状，不要声称找到 root cause。

如果没有运行验证，不能声称成功，除非明确说明限制。

## Workflow

1. 分类故障。
2. 建立反馈。
3. 收集当前证据。
4. 形成可证伪假设。
5. 最小修复。
6. 验证。
7. 必要时停止并 handoff。

## 输出契约

返回：

- **Symptom**：哪里坏了。
- **Feedback loop**：如何观察 fail/pass。
- **Root cause**：一个可证伪解释。
- **Fix**：改了什么以及为什么。
- **Validation**：运行的命令或浏览器检查及结果。
- **Unverified**：未检查项。
- **Remaining risk**：剩余风险。
