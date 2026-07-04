<div align="center">

# 答辩挨打模拟器

一个专门帮你提前发现项目答辩漏洞的 Agent Skill。

它读取 README、报告、PPT 文案、代码结构和数据说明，然后直接在对话里给出追问、薄弱点、稳妥回答和修改建议。

`defense-beating-simulator` · 可安装到 Codex，也可安装到其他支持本地指令/技能目录的 Agent

</div>

<details>
<summary>English Overview</summary>

**Defense Beating Simulator** is a portable Agent Skill for project defense preparation. It can be installed into Codex or into a generic local agent skill directory. It reads project materials such as README files, reports, slide text, code structure, data notes, and experiment results, then returns an in-chat defense review: role-based questions, high-pressure follow-ups, weakness diagnosis, safe answer strategies, and material repair suggestions. Markdown files are generated only when the user explicitly asks for an exported package.

</details>

## 这是什么

答辩挨打模拟器不是普通的“生成几个问题”，也不是演讲稿润色工具。它更像一个提前上岗的答辩评委：先读你的项目材料，再判断哪些说法站得住、哪些证据不够、哪些地方最容易被老师继续追问。

它默认直接在聊天里反馈结果，不会一上来就生成一堆文件。这样用户可以马上看到重点问题，直接修改 README、PPT、报告或答辩口径。

## 不只支持 Codex

这个仓库按“可移植 Skill”设计，不绑定单一 Agent：

- **Codex**：读取 `SKILL.md` 和 `agents/openai.yaml`，按 Codex Skill 方式调用。
- **其他本地 Agent**：读取 `AGENTS.md` 作为通用入口，再按需参考 `SKILL.md`、`references/` 和 `assets/`。
- **不支持自动发现 Skill 的 Agent**：把 `AGENTS.md` 作为项目级指令，把 `SKILL.md` 作为详细工作流说明即可。

通用安装模式会把整个技能目录复制到 `AGENT_SKILLS_HOME`，如果没有设置这个环境变量，则默认使用 `~/.agent-skills`。

## 适合什么项目

- 课程设计项目：检查任务完成度、数据来源、计算依据和个人贡献
- 科研或竞赛原型：检查创新性、实验设计、结果可信度和落地边界
- Web 或系统展示项目：检查功能真实性、数据逻辑、交互演示和复现性
- AI 或算法项目：检查数据集、训练过程、指标解释、对比实验和泛化能力
- 简历项目或 GitHub 仓库：检查项目表述、技术细节、安装说明和面试追问风险

## 默认怎么反馈

使用这个 Skill 后，默认返回一份结构化的文字反馈，而不是创建多个 Markdown 文件。

一次常规输出通常包括：

1. **项目定位判断**：这个项目到底应该怎么说，哪些词容易说大。
2. **材料支撑情况**：README、报告、PPT、代码结构分别支撑了什么，缺了什么。
3. **高风险追问**：最可能被问、答不好会扣分的问题。
4. **参考回答策略**：按“正面回应、承认边界、说明依据、强调贡献、后续改进”来组织。
5. **薄弱点修复建议**：告诉你该补数据来源、运行说明、截图、对比实验还是贡献边界。
6. **答辩速查卡**：一句话介绍、三点贡献、三个亮点、三个局限和高频追问。

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

## 使用方式

Codex 中可以这样调用：

```text
请用 $defense-beating-simulator 分析我的项目 README，场景为保研面试，强度选择“严刑拷打”。
```

其他 Agent 中可以直接要求它按本仓库的 `AGENTS.md` / `SKILL.md` 工作：

```text
请按照 defense-beating-simulator 的规则分析我的项目材料，重点拷问数据来源、个人贡献和创新点，不要生成文件，直接在对话里反馈。
```

## 实际案例

假设用户提供的项目是：**校园综合能源系统仿真展示平台**。

材料摘要：

```text
项目使用 HTML/CSS/JavaScript 实现校园源网荷储可视化页面，展示光伏出力、负荷变化、储能 SOC 和能量流动画。数据来自典型日场景和课程设计假设，暂未接入真实校园运行数据。
```

调用方式：

```text
请用 $defense-beating-simulator 分析这个课程设计项目，强度选择“严刑拷打”。
```

直接反馈片段：

```text
项目定位判断：
这个项目更适合表述为“面向课程设计场景的源网荷储运行展示平台”，不要直接说成“真实校园能源仿真系统”。目前材料能支撑可视化展示和典型工况分析，但还不足以支撑工程级实时仿真或优化调度。

高风险追问 1：
你的数据是实测数据还是构造数据？如果是构造数据，为什么结论还有意义？

稳妥回答策略：
可以先明确数据属性：当前数据基于课程设计假设和典型日工况构造，主要用于展示源网荷储之间的运行关系。然后承认边界：它不能替代真实校园实测数据。最后说明改进方向：后续可以接入校园电表、光伏逆变器或公开负荷数据进行校准。

材料修复建议：
README 里需要新增“数据来源与假设”小节；PPT 中不要只放能量流动画，要补一页说明 SOC 曲线、负荷曲线和光伏曲线是如何得到的；个人贡献不要写“负责整个系统”，应改为“负责前端界面、场景切换、数据结构和能量流可视化”。
```

## 仓库结构

```text
defense-beating-simulator/
├── SKILL.md                  # Codex/OpenAI Skill 入口，也是完整工作流说明
├── AGENTS.md                 # 通用 Agent 入口，适合非 Codex Agent 先读取
├── agents/
│   └── openai.yaml           # Codex 技能列表中的展示名称、简介和默认提示
├── references/
│   ├── question-patterns.md  # 多角色追问、高压追问链和问题分类模式
│   └── project-rubrics.md    # 风险等级、回答评分、创新点和贡献边界规则
├── assets/
│   ├── project-summary.template.md
│   ├── question-bank.template.md
│   ├── weakness-report.template.md
│   └── defense-cheatsheet.template.md
│                              # 仅在用户要求导出文件时使用的 Markdown 模板
├── scripts/
│   ├── __init__.py
│   └── validate_skill.py      # 无第三方依赖的技能包校验脚本
├── tests/
│   └── test_skill_package.py  # 基础测试，确认入口、规则和模板存在
├── install.ps1                # Windows / PowerShell 安装脚本，支持 codex 和 generic
├── install.sh                 # macOS / Linux shell 安装脚本，支持 codex 和 generic
├── pyproject.toml             # 项目元信息
└── README.md                  # 仓库主页
```

## 安装

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

## 校验

不需要安装第三方依赖。

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests
```