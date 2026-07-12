# Expected Chat Output: GitHub Skill Review

## 项目一句话定位

这是一个面向项目答辩材料的可移植 Agent Skill，核心价值是证据链审查、高压追问、防守型回答和材料修复。

## Claim-Evidence Matrix

| Claim / 项目说法 | Evidence / 材料依据 | Evidence label | Gap / 缺口 | Risk |
| --- | --- | --- | --- | --- |
| 不是普通问题生成器 | README 需要明确 Claim-Evidence Matrix | Material-implied | 顶部定位必须强化 | High |
| 可用于 Codex 和其他 Agent | 仓库有 SKILL.md 和 AGENTS.md | Material-supported | 安装路径需要说明 | Medium |
| 默认聊天反馈 | README 提到不要生成一堆文件 | Material-supported | Skill 规则需要同步 | High |

## 修复建议

- README 顶部用一句话说明 Project Defense Red-Team Skill。
- SKILL.md 强制要求 Claim-Evidence Matrix。
- AGENTS.md 写明通用 Agent 入口。
- evals 增加触发和非触发示例。