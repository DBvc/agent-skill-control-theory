# Patch Hypothesis

用于影响 trigger boundary、workflow、evidence policy、output contract、tools 或 safety behavior 的 skill 改动。

## 改动摘要

**Skill：**

**当前版本 / commit：**

**计划改动：**

## 目标失败

这个 patch 要减少哪种失败？

- [ ] Wrong trigger
- [ ] Missed trigger
- [ ] Intent confusion
- [ ] State hallucination
- [ ] Bad trajectory
- [ ] Fragile execution
- [ ] Unsupported completion claim
- [ ] Safety overreach
- [ ] Context bloat
- [ ] Maintenance drift
- [ ] Other:

## 假设

如果我们修改：

```text
<change>
```

那么：

```text
<expected behavior improvement>
```

因为：

```text
<mechanism>
```

## 预期成本

- Context cost:
- User friction:
- Runtime/tool cost:
- Maintenance cost:
- New risk:

## 需要更新的 eval

- [ ] Trigger evals
- [ ] Near-miss evals
- [ ] Output evals
- [ ] Safety evals
- [ ] Historical regression cases

## 回滚条件

如果出现以下情况则回滚：

```text
<condition>
```

## 评审结果

- [ ] Accept
- [ ] Revise
- [ ] Reject

Notes:
