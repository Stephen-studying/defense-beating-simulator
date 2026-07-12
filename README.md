<div align="center">

# 项目答辩红队审查器

**面向多 Agent 的项目答辩证据链审查 Skill**

先查项目材料有没有证据，再模拟老师连续追问，最后给出稳妥回答和材料修复建议。

![license](https://img.shields.io/badge/license-MIT-111827)
![skill](https://img.shields.io/badge/type-Agent%20Skill-2563eb)
![agent](https://img.shields.io/badge/install-Codex%20%7C%20Generic%20%7C%20Project-16a34a)
![language](https://img.shields.io/badge/language-%E4%B8%AD%E6%96%87%20%7C%20English-0f766e)

[立即安装](#立即安装) ·
[使用示例](#使用示例) ·
[核心工作流](#核心工作流) ·
[仓库结构](#仓库结构) ·
[English](README.en.md)

</div>

---

- 项目答辩红队审查器不是普通的“答辩问题生成器”，而是一个面向学生项目、课程设计、科研原型、竞赛项目和 GitHub 展示项目的答辩红队 Skill。
- 它会先审查 README、报告、PPT、代码结构、数据说明和结果图中的“说法 - 证据 - 缺口 - 风险”，再生成高风险追问链。
- 它不会替用户编造数据、实验结果、部署状态或个人贡献，只帮助用户把项目边界讲清楚、讲稳妥。
- 默认产物是直接在对话中反馈，不会一上来生成一堆零散 Markdown 文件；只有用户明确要求导出时才会写文件。

## 核心定位

项目答辩红队审查器的重点不是“多问几个问题”，而是先判断材料能不能支撑用户的说法。

```text
项目说法 -> 材料证据 -> 缺口定位 -> 风险分级 -> 连续追问 -> 稳妥回答 -> 材料修复
```

这让它更适合真实答辩准备：用户不只知道老师可能问什么，还知道答辩前应该补哪些证据、哪些话不能说满。

## 主要能力

| 能力 | 解决的问题 |
| --- | --- |
| 证据链矩阵 | 检查项目说法是否有 README、报告、PPT、代码或图表支撑 |
| 高风险追问链 | 围绕数据来源、个人贡献、创新点、项目边界和可复现性连续追问 |
| 防守型回答 | 用“承认边界 + 说明依据 + 强调贡献 + 后续改进”的方式组织回答 |
| 材料修复清单 | 指出 README、PPT、报告、演示脚本和简历表述应该怎么补 |
| 答辩速查卡 | 整理一句话定位、三点贡献、三个亮点、三个局限和高频追问 |

## 适合场景

- 课程设计、毕业设计、综合实践项目
- 科研原型、创新创业项目、竞赛项目
- 简历项目、保研复试项目经历、技术面试项目追问
- GitHub 仓库展示、README 可复现性检查、项目说明优化

## 不适合场景

- 单纯润色演讲稿
- 没有项目材料的泛泛模拟面试
- 与项目证据链无关的职业规划问答
- 替代导师、老师或评委的最终判断

## 核心工作流

1. **项目一句话定位**：先把项目说成最稳妥的版本，避免夸大。
2. **证据链矩阵**：逐条标注 `Material-supported`、`Material-implied`、`Material-missing`、`Risk-inferred`。
3. **高风险缺口 Top 5**：优先指出最容易扣分的问题。
4. **连续追问链**：围绕每个高风险点连续追问 2 到 4 层。
5. **防守型回答策略**：给出能承认边界、又不显得项目很弱的回答。
6. **材料修复清单**：明确该补 README、PPT、报告、数据说明还是简历表述。
7. **答辩速查卡**：最后整理成答辩前可快速复习的一页内容。

## 提问强度

```text
先热个身 / 开始挑刺 / 严刑拷打
```

| 强度 | 适合阶段 | 追问方式 |
| --- | --- | --- |
| 先热个身 | 刚开始梳理项目 | 先确认项目能不能讲清楚，问题较友好 |
| 开始挑刺 | 常规答辩准备 | 系统追问数据、方法、结果、贡献和创新 |
| 严刑拷打 | 正式答辩前压测 | 集中攻击最容易扣分的薄弱点，并给出连续追问链 |

## 使用示例

基础用法：

```text
请使用 defense-beating-simulator 帮我审查这个项目答辩材料。
重点检查：
1. 项目定位是否清楚
2. 数据来源是否可信
3. 个人贡献是否说得清楚
4. 创新点是否容易被质疑
5. README / PPT / 报告中还缺哪些证据
```

高压用法：

```text
请严厉模拟答辩老师，先做证据链矩阵，再指出高风险缺口，
并围绕每个缺口连续追问 3 层。最后给出稳妥回答和材料修改建议。
不要替我编造材料中没有的信息。
```

Codex 中可以这样调用：

```text
请用 $defense-beating-simulator 分析我的项目 README，
场景为保研面试，强度选择“严刑拷打”。
```

其他 Agent 可以让它先读 `AGENTS.md`，再读 `SKILL.md`：

```text
请按照 defense-beating-simulator 的规则分析我的项目材料，
重点拷问数据来源、个人贡献和创新点，直接在对话里反馈。
```

## 实际案例

<details>
<summary>校园综合能源系统仿真展示平台</summary>

输入摘要：

```text
项目使用 HTML/CSS/JavaScript 实现校园源网荷储可视化页面，
展示光伏出力、负荷变化、储能 SOC 和能量流动画。
数据来自典型日场景和课程设计假设，暂未接入真实校园运行数据。
```

输出片段：

```text
项目一句话定位：
更稳妥的说法是“面向课程设计场景的校园源网荷储运行展示与辅助分析平台”，
不要直接说成“真实校园能源仿真系统”。

证据链矩阵：
| 项目说法 | 材料依据 | 证据标签 | 缺口 | 风险 |
| --- | --- | --- | --- | --- |
| 平台展示光伏、负荷、储能 SOC | README 功能描述和前端页面截图 | Material-supported | 需要补数据生成逻辑 | Medium |
| 系统可用于校园真实能源优化 | 未看到真实数据、优化模型或部署证据 | Material-missing | 容易被追问是否夸大 | High |

高风险追问：
你的数据是实测数据还是构造数据？
如果是构造数据，为什么结论还有意义？
SOC 曲线是功率积分算出来的，还是预设曲线？

稳妥回答：
当前数据基于课程设计假设和典型日工况构造，主要用于展示源网荷储运行关系。
它不能替代真实校园实测数据，也不能直接支撑工程部署结论。
后续可以接入电表、光伏逆变器或公开负荷数据进行校准。
```

</details>

## 立即安装

### Codex

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent codex -Force
```

```bash
sh install.sh --agent codex --force
```

### 通用本地 Agent

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent generic -Force
```

```bash
sh install.sh --agent generic --force
```

### 项目级 Agent

如果某个 Agent 会读取项目内的 `.agents/skills`，可以把本仓库安装到项目目录：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent project -Destination "D:\YourProject\.agents\skills" -Force
```

```bash
sh install.sh --agent project --dest "$HOME/your-project/.agents/skills" --force
```

注意：`project` 模式的目标目录应该是“另一个项目”的 `.agents/skills`，不要指向本仓库自己的子目录。

默认安装位置：

```text
Codex:   ~/.codex/skills/defense-beating-simulator
Generic: ~/.agent-skills/defense-beating-simulator
Project: <your-project>/.agents/skills/defense-beating-simulator
```

如果你的 Agent 使用 `.agents/skills`，也可以手动复制到：

```text
$HOME/.agents/skills/defense-beating-simulator
项目目录/.agents/skills/defense-beating-simulator
```

如果 Agent 不支持自动发现，只要让它按顺序读取：

```text
AGENTS.md -> SKILL.md -> references/按项目类型选择
```

## 仓库结构

```text
defense-beating-simulator/
├── SKILL.md                  # Skill 入口和完整工作流
├── AGENTS.md                 # 通用 Agent 入口
├── CLAUDE.md                 # Claude 类 Agent 的薄入口
├── GEMINI.md                 # Gemini 类 Agent 的薄入口
├── agents/openai.yaml        # Codex 展示信息
├── references/               # 追问模式、评分规则和领域问题库
├── assets/                   # 用户要求导出时使用的模板
├── examples/                 # 校园能源、YOLO 检测等示例
├── evals/                    # 触发与输出结构回归提示集
├── scripts/                  # 无第三方依赖的验证脚本
├── tests/                    # 基础测试
├── install.ps1               # Windows 安装脚本
├── install.sh                # macOS / Linux 安装脚本
└── README.md                 # GitHub 主页
```

## 验证

本仓库不需要第三方 Python 依赖。

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests
```

## 项目边界

- 不能保证答辩一定通过。
- 不能验证材料里没有提供的事实。
- 不应编造数据来源、实验结果、部署状态或个人贡献。
- 输出是答辩准备辅助，不替代导师反馈或真实评委判断。

## 推荐仓库信息

建议 GitHub About 描述：

```text
A portable Agent Skill for project defense review: evidence-gap audit, high-pressure follow-up questions, safe answer strategies, and material repair suggestions.
```

建议 Topics：

```text
codex
agent-skills
defense-preparation
academic-defense
interview-prep
project-review
red-team
student-projects
```
