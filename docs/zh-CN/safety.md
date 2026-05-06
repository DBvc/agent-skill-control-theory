# 安全约束

ASCT 把安全视为可接受性约束，而不只是成本项之一。

```text
Skill 可接受的前提：
  SafetyRisk(skill, task_distribution) <= SafetyBudget
```

如果 skill 超过安全预算，即使它能提升任务成功率，也不应该发布或安装。

## Skill 特有安全风险

Skill 可以包含指令、脚本、资源和参考资料，所以它比普通 prompt snippet 更强，也更有风险。

常见风险：

- 执行破坏性命令；
- 读取或暴露 secrets；
- 未经确认写入外部系统；
- 隐藏网络调用；
- 覆盖用户意图或同意；
- 促成欺诈、规避、胁迫或隐私侵犯；
- 捆绑恶意或不清楚的脚本；
- 指示 agent 忽略更高优先级规则或系统指令。

## 安全 skill 设计规则

1. 授权不清时 **fail closed**。
2. 外部、不可逆或公开动作前要求显式批准。
3. 破坏性或状态变更操作优先 dry-run。
4. 声明依赖和环境假设。
5. 脚本要可审计、自包含。
6. 不捆绑 secrets 或私人本地路径。
7. 私人 preset 和公共可复用 skill 分离。
8. 最终输出暴露 known limitations。
9. 除非明确需要并记录，不做隐藏网络行为。
10. 不指示 agent 绕过更高优先级规则。

## 外部动作契约

对可能 create、update、publish、delete、close、push、deploy、comment、label 的 skill，要求 action contract：

```yaml
external_action:
  action_type: create_issue | update_label | post_comment | close_issue | push | publish | deploy | delete | none
  target:
  irreversible: true | false
  public_visible: true | false
  requires_user_approval: true
  approval_text:
  dry_run_available: true | false
  preflight_checks:
    -
  blocked_by:
    -
```

## 最终输出披露

当 skill 执行或准备高风险动作时，最终输出应包含：

- 执行或准备了什么动作；
- 谁批准了它；
- 影响了哪个目标；
- 做了什么验证或 dry-run；
- 还剩什么风险。
