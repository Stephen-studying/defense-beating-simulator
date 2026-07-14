<div align="center">

# 针对性答辩模拟器

**项目答辩证据链审查与连续追问 Agent Skill**

先核对“项目说法有没有证据”，再模拟评委追问，最后给出稳妥回答和材料修复动作。

[![许可证](https://img.shields.io/badge/许可证-MIT-111827)](LICENSE)
[![类型](https://img.shields.io/badge/类型-Agent%20Skill-2563eb)](SKILL.md)
[![兼容](https://img.shields.io/badge/兼容-Codex%20%7C%20Claude%20%7C%20Gemini%20%7C%20Copilot-16a34a)](#兼容性)
[![验证](https://img.shields.io/badge/验证-Python%20标准库-0f766e)](#项目验证)

[核心能力](#核心能力) · [实际案例](#实际案例) · [快速开始](#快速开始) · [安装](#安装) · [仓库结构](#仓库结构) · [English](README.en.md)

</div>

---

## 30 秒看懂

`defense-beating-simulator` 不是普通的“答辩问题生成器”。它先审查 README、PPT、报告、代码结构、数据说明和结果图中的证据链，再决定哪些问题值得追问。

```text
项目说法 → 材料证据 → 证据缺口 → 答辩风险 → 连续追问 → 稳妥回答 → 材料修复
```

默认结果直接在对话中反馈，不会擅自生成一批 Markdown 文件。只有用户明确要求导出时，才使用 `assets/` 中的模板生成材料包。

## 核心能力

| 能力 | 具体作用 |
| --- | --- |
| Claim-Evidence Matrix | 逐条核对项目说法与 README、PPT、报告、代码或图表证据 |
| 高风险缺口 | 找出最容易被追问的数据、贡献、创新、边界与复现问题 |
| 连续追问链 | 围绕同一缺口连续追问 2–4 层，而不是堆一串散题 |
| 防守型回答 | 承认真实边界、说明已有依据、突出本人贡献，不替用户编造事实 |
| 材料修复 | 明确应该补 README、PPT、报告、演示脚本还是简历表述 |
| 回答评分 | 按正面回应、技术细节、证据、贡献边界和表达清晰度评分 |

完整审查固定按以下顺序输出：

1. 项目一句话定位
2. Claim-Evidence Matrix
3. 高风险缺口（最多 5 项）
4. 连续追问链
5. 防守型回答策略
6. 材料修复清单
7. 答辩速查卡

### 证据标签

| 维度 | 标签 | 含义 |
| --- | --- | --- |
| 证据状态 | `Material-supported` | 材料明确支持 |
| 证据状态 | `Material-implied` | 材料仅间接暗示 |
| 证据状态 | `Material-missing` | 材料出现了该说法，但没有给出支撑 |
| 风险依据 | `Material-derived` | 风险直接来自材料矛盾、遗漏或限制 |
| 风险依据 | `Risk-inferred` | 根据答辩经验推断，不能当作材料事实 |

### 提问强度

| 等级 | 适合阶段 | 提问方式 |
| --- | --- | --- |
| 先热个身 | 初次梳理项目 | 先确认定位、材料和基础理解 |
| 开始挑刺 | 常规答辩准备 | 系统追问数据、方法、结果、贡献和边界 |
| 严刑拷打 | 正式答辩前压测 | 集中攻击最高风险缺口，进行多层连续追问 |

“严刑拷打”只提高问题锋利度，不降低证据标准，也不包含人身攻击。

## 实际案例

以“校园综合能源系统源网荷储展示平台”为例。材料说明网页展示光伏、负荷、储能 SOC 和能量流，数据来自典型工况与课程假设，尚未提供真实校园数据、后端接口或优化模型。

| Claim / 项目说法 | Evidence / 材料依据 | Evidence status / 证据状态 | Gap / 缺口 | Risk basis / 风险依据 | Risk |
| --- | --- | --- | --- | --- | --- |
| 网页能够展示源网荷储典型日运行状态 | 项目摘要中的功能说明 | `Material-missing` | 只有功能自述，缺少运行截图与复现步骤 | `Material-derived` | Medium |
| 项目属于“仿真平台” | 项目名称与简介 | `Material-missing` | 未说明 SOC、功率平衡和调度结果如何计算 | `Material-derived` | High |
| 数据来自典型工况与课程假设 | 项目摘要中的数据说明 | `Material-supported` | 缺少参数来源表和构造规则 | `Material-derived` | High |

连续追问会从“数据是不是实测”继续追到“构造数据能支持什么结论”“换成真实数据需要重算哪些参数”“当前架构能否接入真实接口”。稳妥口径会明确：当前版本是课程设计场景下的运行展示与辅助分析平台，适合说明系统关系和典型趋势，不等同于工程级实时调度系统。

[查看完整校园能源示例](examples/campus-energy-system/expected-output-chat.md) · [查看 YOLO 缺陷检测示例](examples/yolo-pv-defect-detection/expected-output-chat.md)

## 快速开始

基础审查：

```text
请使用 defense-beating-simulator 审查我的项目答辩材料。
重点检查：项目定位、数据来源、个人贡献、创新点，以及 README / PPT / 报告中缺少的证据。
默认直接在对话中反馈，不要生成文件。
```

高压审查：

```text
请用“严刑拷打”强度模拟答辩老师。
先做 Claim-Evidence Matrix，再指出高风险缺口，并围绕每个缺口连续追问 3 层。
最后给出稳妥回答和材料修改建议，不要替我编造材料中没有的信息。
```

回答评分：

```text
下面是老师的问题和我的回答。请先指出回答依赖了哪些材料证据，再按 100 分制评分，
标出夸大或回避问题的句子，给出一版更稳妥的回答，并补一个最可能的追问。
```

## 适用范围

适合：

- 课程设计、毕业设计、综合实践项目
- 科研原型、竞赛项目、算法实验项目
- 保研复试、简历项目、技术面试
- GitHub 项目展示、README 和可复现性检查

不适合：

- 单纯润色演讲稿或生成通用面试题
- 没有项目材料的职业规划建议
- 与项目证据链无关的学术科普
- 替代导师、老师或真实评委的最终判断

## 兼容性

这是一个可移植的 `SKILL.md` 项目，不绑定单一 Agent。只要 Agent 支持技能目录，或能够按要求读取本地指令文件，就可以使用。

| Agent / 方式 | 默认目录 | 安装参数 |
| --- | --- | --- |
| Codex | `~/.codex/skills` | `codex` |
| 共享 Agent Skills | `~/.agents/skills` | `agents` |
| Claude Code | `~/.claude/skills` | `claude` |
| Gemini CLI | `~/.gemini/skills` | `gemini` |
| GitHub Copilot CLI | `~/.copilot/skills` | `copilot` |
| 项目内共享 | `<项目>/.agents/skills` | `project` |

目录依据可查阅 [Claude Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)、[Gemini CLI Agent Skills](https://geminicli.com/docs/cli/using-agent-skills/) 和 [GitHub Copilot Agent Skills](https://docs.github.com/en/copilot/concepts/agents/about-agent-skills) 官方文档。

不同 Agent 的自动发现规则仍可能随版本变化。如果技能没有被自动触发，请明确提到 `defense-beating-simulator`，或让 Agent 依次读取：

```text
AGENTS.md → SKILL.md → references/中与项目类型对应的文件
```

`generic` 参数作为旧命令兼容别名保留，实际与 `agents` 一样安装到 `~/.agents/skills`。

## 安装

先克隆仓库并进入目录：

```bash
git clone https://github.com/Stephen-studying/defense-beating-simulator.git
cd defense-beating-simulator
```

Windows PowerShell：

```powershell
# Codex
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent codex -Force

# Claude Code；也可改为 agents / gemini / copilot
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent claude -Force
```

macOS / Linux：

```bash
# Codex
sh install.sh --agent codex --force

# 共享 Agent Skills；也可改为 claude / gemini / copilot
sh install.sh --agent agents --force
```

Gemini CLI 也可以使用原生命令从仓库安装：

```bash
gemini skills install https://github.com/Stephen-studying/defense-beating-simulator
```

项目内安装必须显式指定另一个项目的技能目录：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 `
  -Agent project -Destination "D:\YourProject\.agents\skills" -Force
```

安装脚本只复制运行所需的 `SKILL.md`、Agent 入口、`references/`、`assets/` 和许可证，不会把测试、示例、CI 或开发缓存复制到用户技能目录。

## 仓库结构

```text
defense-beating-simulator/
├── SKILL.md                   # 唯一规范：触发、流程、证据标签和安全边界
├── AGENTS.md                  # 通用 Agent 入口与安装目录说明
├── CLAUDE.md                  # Claude Code 薄入口
├── GEMINI.md                  # Gemini CLI 薄入口
├── agents/openai.yaml         # Codex 展示与默认调用信息
├── references/                # 通用规则与五类项目专用追问库
├── assets/                    # 用户明确要求导出时使用的模板
├── examples/                  # 校园能源、YOLO 和 GitHub 审查示例
├── evals/                     # 触发、结构与防夸大回归用例
├── scripts/                   # 包结构验证与回答结果检查
├── tests/                     # 标准库单元测试
├── install.ps1               # Windows 安装器
└── install.sh                 # macOS / Linux 安装器
```

## 项目验证

仓库验证不依赖第三方 Python 包：

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests
```

保存一次 Agent 回答后，可用回归规则检查输出结构：

```bash
python scripts/evaluate_response.py --eval-id explicit_01 --response response.md
```

GitHub Actions 会在 Linux 和 Windows 上验证 Skill 结构、Python 打包、单元测试与安装脚本的实际复制结果。

## 安全边界

- 不编造数据来源、实验结果、代码功能或部署状态。
- 不把展示型 Demo 说成真实部署系统。
- 不把课程假设数据说成实测数据。
- 不把团队成果全部说成个人成果。
- 不把模型微调或模块替换包装成原创模型。
- 不保证答辩通过，输出只是准备辅助，不能替代导师反馈和真实评委判断。

## GitHub 信息建议

建议 About 描述：

```text
A portable Agent Skill for evidence-first project defense review, follow-up questioning, answer scoring, and material repair.
```

建议 Topics：

```text
agent-skills  academic-defense  defense-preparation  project-review
interview-prep  red-team  codex  claude-code  gemini-cli  github-copilot
```

## 许可证

[MIT License](LICENSE)
