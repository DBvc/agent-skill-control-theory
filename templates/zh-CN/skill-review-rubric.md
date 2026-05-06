# Skill 评审 Rubric

每项 1 到 5 分。

| 分数 | 含义 |
|---|---|
| 1 | 缺失或有害 |
| 2 | 存在但薄弱 |
| 3 | 可用但不完整 |
| 4 | 强 |
| 5 | 生产级 |

## Rubric

| 维度 | 分数 | 备注 |
|---|---:|---|
| Skill-worthiness：重复、稳定、可评估的任务分布 | | |
| Activation Control：清楚的 description、use/not-for/near-miss | | |
| Intent Control：modes、input contract、non-goals | | |
| State Control：source of truth、evidence hierarchy、freshness policy | | |
| Trajectory Control：workflow、hard gates、stops、fallback | | |
| Execution Control：确定性工作是否交给工具/scripts | | |
| Completion Control：validation、proof fields、limitations | | |
| Evolution Control：evals、regression、patch hypothesis | | |
| Context Economy：主 SKILL.md 是否最小充分 | | |
| Safety：fail-closed、approval、无隐藏风险行为 | | |

## 总体评级

- 45-50：生产级 skill
- 38-44：强可复用 skill
- 30-37：可用，但需要补 eval/resources
- 20-29：更像 prompt checklist
- <20：不应作为 full skill 发布

## 评审问题

1. 这个 skill 减少了哪种失败模式？
2. 它引入了什么新成本？
3. 它引入了什么新风险？
4. 什么证据证明它比 baseline 更好？
5. 哪些内容应该移出 `SKILL.md`？
6. 哪些确定性工作应该脚本化？
7. 哪些 claim 必须在验证前禁止？
8. 哪个历史失败应该成为 eval？
