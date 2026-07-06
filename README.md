<div align="center">

# 答辩挨打模拟器

**Defense Beating Simulator**  
A project defense red-team skill for evidence-gap review, high-pressure questioning, and safe answer preparation.

答辩挨打模拟器不是普通的“答辩问题生成器”，而是面向 README、报告、PPT、代码结构、数据说明和结果图的答辩证据链审查 Skill。它会先判断项目材料中哪些说法有证据支撑、哪些地方存在缺口，再生成高风险追问链、防守型回答策略和具体材料修复建议。

`defense-beating-simulator` · 可安装到 Codex，也可安装到其他支持本地指令/技能目录的 Agent

</div>

<details>
<summary>English Overview</summary>

**Defense Beating Simulator** is a portable Project Defense Red-Team Skill. It reviews project defense materials for claim-evidence gaps, high-risk follow-up questions, safe answer strategies, and concrete material repair actions. It is designed for course defenses, graduate interviews, competition defenses, resume project interviews, and GitHub project reviews. It returns structured in-chat feedback by default and exports Markdown files only when explicitly requested.

</details>

## What it does

1. **Claim-Evidence Matrix**: 逐条检查项目说法与材料证据是否匹配。
2. **High-risk Question Chains**: 围绕数据来源、个人贡献、项目边界、创新性和可复现性生成连续追问。
3. **Safe Answer Strategies**: 给出稳妥回答，不夸大项目、不编造数据、不虚构个人贡献。
4. **Material Repair Actions**: 告诉用户应该修改 README、PPT、报告、演示脚本还是简历表述。
5. **Defense Cheatsheet**: 整理一句话介绍、三点贡献、三个亮点、三个局限和高频追问。

## Why this is different

Most defense-preparation prompts start by generating questions. This skill starts by checking whether the project materials can actually support the claims.

```text
Claims -> Evidence -> Gaps -> Risks -> Follow-up questions -> Safe answers -> Material repairs
```

This makes the output more useful for real defense preparation because it tells the user not only what may be asked, but also what should be fixed before the defense.

## Best for

- 课程设计 / 毕设 / 综合实践项目
- 科研原型 / 竞赛项目 / 算法实验项目
- 简历项目 / GitHub 项目展示
- 保研、复试、项目面试中的项目经历准备

## Not for

- 单纯演讲稿润色
- 无材料输入的泛泛模拟面试
- 与项目证据链无关的职业规划问答
- 替代真实老师或评委的最终判断

## Quick Start

```text
请使用 defense-beating-simulator 帮我审查这个项目答辩材料。
重点检查：
1. 项目定位是否清楚
2. 数据来源是否可信
3. 个人贡献是否说得清楚
4. 创新点是否容易被质疑
5. README / PPT / 报告中还缺哪些证据
```

更强的红队模式：

```text
请严厉模拟答辩老师，先做 Claim-Evidence Matrix，再指出高风险缺口，并围绕每个缺口连续追问 3 层。最后给出稳妥回答和材料修改建议。不要替我编造材料中没有的信息。
```

Codex 中也可以这样调用：

```text
请用 $defense-beating-simulator 分析我的项目 README，场景为保研面试，强度选择“严刑拷打”。
```

其他 Agent 中可以直接要求它按本仓库的 `AGENTS.md` / `SKILL.md` 工作：

```text
请按照 defense-beating-simulator 的规则分析我的项目材料，重点拷问数据来源、个人贡献和创新点，不要生成文件，直接在对话里反馈。
```

## 默认反馈结构

默认返回一份结构化的文字反馈，而不是创建多个 Markdown 文件：

1. 项目一句话定位
2. Claim-Evidence Matrix
3. 高风险缺口 Top 5
4. 连续追问链
5. 防守型回答策略
6. 材料修复清单
7. 答辩速查卡

只有当用户明确说“导出文件”“生成材料包”“保存为 Markdown”时，才会生成 `project-summary.md`、`question-bank.md`、`weakness-report.md` 等文件。

## 提问强度

```text
先热个身 / 开始挑刺 / 严刑拷打
```

| 强度 | 适合场景 | 追问特点 |
| --- | --- | --- |
| 先热个身 | 刚开始梳理项目 | 先确认项目能否讲清楚，问题相对友好 |
| 开始挑刺 | 常规答辩准备 | 系统追问数据、方法、结果、贡献和创新 |
| 严刑拷打 | 正式答辩前压测 | 集中攻击最容易扣分的薄弱点，并给出连续追问链 |

## 实际案例

假设用户提供的项目是：**校园综合能源系统仿真展示平台**。

材料摘要：

```text
项目使用 HTML/CSS/JavaScript 实现校园源网荷储可视化页面，展示光伏出力、负荷变化、储能 SOC 和能量流动画。数据来自典型日场景和课程设计假设，暂未接入真实校园运行数据。
```

直接反馈片段：

```text
项目一句话定位：
更稳妥的说法是“面向课程设计场景的校园源网荷储运行展示与辅助分析平台”，不要直接说成“真实校园能源仿真系统”。

Claim-Evidence Matrix：
| Claim | Evidence | Evidence label | Gap | Risk |
| --- | --- | --- | --- | --- |
| 平台展示光伏、负荷、储能 SOC | README 功能描述和前端页面截图 | Material-supported | 需要补数据生成逻辑 | Medium |
| 系统可用于校园真实能源优化 | 材料未看到真实数据、优化模型或部署证据 | Material-missing | 容易被追问是否夸大 | High |

高风险追问：
你的数据是实测数据还是构造数据？如果是构造数据，为什么结论还有意义？SOC 曲线是功率积分算出来的，还是预设曲线？

稳妥回答策略：
当前数据基于课程设计假设和典型日工况构造，主要用于展示源网荷储运行逻辑和能量流关系。它不能替代真实校园实测数据，也不能直接支撑工程部署结论。后续可以接入电表、光伏逆变器或公开负荷数据进行校准。

材料修复建议：
README 新增“数据来源与假设”；PPT 补一页说明 SOC、负荷、光伏曲线来源；个人贡献改为“负责前端界面、场景切换、数据结构和能量流可视化”。
```

## 仓库结构

```text
defense-beating-simulator/
├── SKILL.md                  # Codex/OpenAI Skill 入口，也是完整工作流说明
├── AGENTS.md                 # 通用 Agent 入口，适合非 Codex Agent 先读取
├── agents/
│   └── openai.yaml           # Codex 技能列表中的展示名称、简介和默认提示
├── references/
│   ├── question-patterns.md  # 通用追问链和角色提问模式
│   ├── project-rubrics.md    # 风险等级、回答评分和安全表达规则
│   └── domain-*.md           # 不同项目类型的专用追问库
├── assets/                   # 用户要求导出 Markdown 时使用的模板
├── examples/                 # 真实使用场景示例
├── evals/                    # 维护者回归提示集
├── scripts/                  # 无第三方依赖的校验脚本
├── tests/                    # 基础测试
├── install.ps1               # Windows / PowerShell 安装脚本，支持 codex 和 generic
├── install.sh                # macOS / Linux shell 安装脚本，支持 codex 和 generic
└── README.md                 # 仓库主页
```

## Installation

### 安装到 Codex

PowerShell：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent codex -Force
```

macOS / Linux：

```bash
sh install.sh --agent codex --force
```

安装后重启 Codex，让新的 Skill 被重新加载。

### 安装到其他 Agent

PowerShell：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent generic -Force
```

macOS / Linux：

```bash
sh install.sh --agent generic --force
```

默认安装位置：

```text
Windows: %USERPROFILE%\.agent-skills\defense-beating-simulator
macOS/Linux: ~/.agent-skills/defense-beating-simulator
```

安装后，让你的 Agent 读取下面任意一个入口：

```text
AGENTS.md  # 通用入口，适合大多数本地 Agent
SKILL.md   # 完整工作流，适合支持 Skill/工具说明的 Agent
```

### 自定义安装目录

PowerShell：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent generic -Destination "D:\AgentSkills" -Force
```

macOS / Linux：

```bash
sh install.sh --agent generic --dest "$HOME/agent-skills" --force
```

## Compatibility Notes

Different agents may discover skills from different directories.

- Codex users can use the installation script provided in this repository.
- If your agent uses `.agents/skills` as the default skill directory, you can manually copy this repository to:
  - `$HOME/.agents/skills/defense-beating-simulator`
  - `.agents/skills/defense-beating-simulator` inside a project repository
- If the skill is not automatically discovered, explicitly mention `defense-beating-simulator` or ask the agent to read `SKILL.md`.
- If your agent only supports project-level instructions, point it to `AGENTS.md` first.

## Limitations

- This skill cannot guarantee defense success.
- It cannot verify facts that are not present in the provided materials.
- It should not invent data sources, experimental results, deployment status, or personal contributions.
- Its output is a preparation aid, not a replacement for advisor feedback or real committee evaluation.

## Suggested GitHub Topics

```text
codex
agent-skills
skill
defense-preparation
academic-defense
interview-prep
project-review
red-team
github-readme
student-projects
```

Suggested repository description:

```text
A portable Agent Skill for project defense review: evidence-gap audit, high-pressure follow-up questions, safe answer strategies, and material repair suggestions.
```

## Validation

No third-party dependency is required.

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests
```
