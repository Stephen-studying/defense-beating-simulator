# Expected Chat Output: GitHub Skill Review

## 项目一句话定位

这是一个面向项目答辩材料的可移植 Agent Skill，核心价值是证据链审查、连续追问、防守型回答和材料修复。

## Claim-Evidence Matrix

| Claim / 项目说法 | Evidence / 材料依据 | Evidence status / 证据状态 | Gap / 缺口 | Risk basis / 风险依据 | Risk |
| --- | --- | --- | --- | --- | --- |
| Skill 用于审查答辩材料并生成追问、回答和修复建议 | 输入 README 第 2 段 | Material-missing | 只有 README 自述，需由 SKILL.md 的强制输出契约佐证 | Material-derived | High |
| 可用于课程设计、保研面试、竞赛答辩和 GitHub 展示 | 输入 README 第 3 段 | Material-implied | 场景已列出，但未提供角色路由和对应示例 | Material-derived | Medium |
| 仓库包含多 Agent 入口、参考资料、模板和测试 | 输入 README 第 3 段 | Material-missing | 未提供目录清单或实际文件供本次输入核对 | Material-derived + Risk-inferred | High |

## 高风险缺口（最多 5 项）

1. “多 Agent”必须对应真实支持的安装目录，不能只写通用路径。
2. Evals 需要检查真实输出结构，而不只是文件存在。
3. Claim-Evidence Matrix 必须区分证据状态和风险推断。

## 连续追问链

- 哪些 Agent 能自动发现这个 Skill，各自目录是什么？
- CI 是否验证安装脚本和示例输出，而不只是关键词？
- 如果 Agent 跳过证据矩阵，仓库如何发现行为退化？

## 防守型回答策略

将项目定位为“兼容 Agent Skills 标准及可读取 Markdown 指令的 Agent”，并逐个平台给出经过验证的路径。不要声称所有 Agent 都能自动发现同一个目录。

## 材料修复清单

- 在 README 中列出 Codex、Claude、Gemini、Copilot 和共享目录。
- 给安装脚本增加平台模式并只复制运行文件。
- 在测试中校验矩阵结构、名称一致性、示例顺序和安装结果。

## 答辩速查卡

- 核心差异：先审证据，再生成追问。
- 兼容边界：支持 Agent Skills 标准或显式读取 Markdown 的 Agent。
- 不能夸大：不能保证所有 Agent 自动发现、不能保证答辩通过。
