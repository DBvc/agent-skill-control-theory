# 安全

skill 可以包含指令、脚本、references、assets、commands 和外部工具指引。它不仅改变 agent 说什么，也可能改变 agent 做什么。

ASCT 把安全视为准入约束，而不是普通成本项：

```text
SafetyRisk(skill, task_distribution) <= SafetyBudget
```

只有先满足安全约束，才讨论 SkillValue。

## 1. 风险类型

| 风险 | 描述 |
|---|---|
| Destructive action | 删除文件、重置 git、发布、关闭 issue、修改外部系统 |
| Credential exposure | 读取、打印、复制或传输 secrets |
| Network access | 调用外部服务、获取不可信内容、潜在泄露路径 |
| Script execution | 运行未审查代码、安装依赖、执行 shell 命令 |
| Supply chain | 未 pin 依赖、远程安装器、不可信包 |
| Privacy | 访问私人文件、用户数据、客户数据、日志、转录 |
| Prompt injection | 不可信 references 或文档要求 agent 覆盖规则 |
| Cross-skill activation | 一个 skill 推动另一个 skill 以不安全方式激活 |
| Overbroad permissions | skill 获得超过任务所需的工具或权限 |

## 2. 安全控制的放置

有些安全控制不应只写在 skill prose 里：

| 控制 | 更好位置 |
|---|---|
| 阻止危险 shell 命令 | hook 或 sandbox policy |
| 外部写操作前审批 | hook、command workflow、skill hard gate |
| 防止 secret 打印 | global rule、scanner、hook |
| 校验脚本依赖 | CI 和安全审查 |
| 限制网络访问 | sandbox 或 host policy |
| 记录外部副作用 | audit log |

高影响行为不应该只依赖模型记忆。

## 3. 外部动作契约

发布、创建 release、关闭 issue、发送邮件、修改 ticket、删除 branch、运行云任务、花费金钱等都属于外部动作。

这类 skill 应有显式 action contract：

```yaml
external_action:
  type: "publish | comment | close_issue | deploy | delete | spend_money | other"
  target: ""
  irreversible: true
  requires_user_approval: true
  dry_run_available: true
  approval_evidence: ""
  audit_output: ""
```

## 4. 脚本安全

脚本应像可执行代码一样被审查：

- 是否读取环境变量？
- 是否访问网络？
- 是否写文件？
- 是否删除或覆盖文件？
- 是否运行 shell 命令？
- 是否安装依赖？
- 是否处理异常输入？
- 是否打印敏感数据？
- 依赖是否 pin？
- 错误信息是否既有帮助又不泄露 secrets？

## 5. Collection 安全

大型 skill collection 有额外风险：安装过多、隐藏脚本、依赖冲突、不可信贡献、过期技能和跨 skill 工作流绕过安全门。

推荐控制：最小安装子集、脚本清单、网络和 credential policy、来源追踪、版本 pin、安全审查、废弃流程、兼容性说明、collection-level safety evals。
