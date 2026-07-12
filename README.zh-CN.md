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

- 项目答辩红队审查器不是普通的“答辩问题生成器”，而是面向学生项目、课程设计、科研原型、竞赛项目和 GitHub 展示项目的答辩红队 Skill。
- 它会先审查 README、报告、PPT、代码结构、数据说明和结果图中的“说法 - 证据 - 缺口 - 风险”，再生成高风险追问链。
- 它不会替用户编造数据、实验结果、部署状态或个人贡献，只帮助用户把项目边界讲清楚、讲稳妥。
- 默认产物是直接在对话中反馈；只有用户明确要求导出时才会生成 Markdown 文件。

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

## 核心工作流

1. **项目一句话定位**：先把项目说成最稳妥的版本，避免夸大。
2. **证据链矩阵**：逐条标注 `Material-supported`、`Material-implied`、`Material-missing`、`Risk-inferred`。
3. **高风险缺口 Top 5**：优先指出最容易扣分的问题。
4. **连续追问链**：围绕每个高风险点连续追问 2 到 4 层。
5. **防守型回答策略**：给出能承认边界、又不显得项目很弱的回答。
6. **材料修复清单**：明确该补 README、PPT、报告、数据说明还是简历表述。
7. **答辩速查卡**：整理成答辩前可快速复习的一页内容。

## 多 Agent 兼容

这个 Skill 是纯 Markdown 规则 + 可选模板，不依赖 Codex 专有运行时。

| Agent 类型 | 推荐入口 |
| --- | --- |
| Codex / OpenAI Skill | `SKILL.md` + `agents/openai.yaml` |
| 通用本地 Agent | `AGENTS.md` -> `SKILL.md` |
| Claude 类 Agent | `CLAUDE.md` -> `AGENTS.md` -> `SKILL.md` |
| Gemini 类 Agent | `GEMINI.md` -> `AGENTS.md` -> `SKILL.md` |
| 只支持自定义提示词的 Agent | 直接粘贴或附加 `SKILL.md` |
| 项目级 Agent | 放入目标项目的 `.agents/skills/defense-beating-simulator` |

如果 Agent 不支持自动发现，只要明确告诉它：

```text
请使用 defense-beating-simulator，并按 AGENTS.md -> SKILL.md -> references/ 的顺序读取规则。
```

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

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent project -Destination "D:\YourProject\.agents\skills" -Force
```

```bash
sh install.sh --agent project --dest "$HOME/your-project/.agents/skills" --force
```

注意：`project` 模式的目标目录应该是另一个项目的 `.agents/skills`，不要指向本仓库自己的子目录。

## 使用示例

```text
请使用 defense-beating-simulator 帮我审查这个项目答辩材料。
重点检查项目定位、数据来源、个人贡献、创新点和 README / PPT / 报告中缺少的证据。
```

高压模式：

```text
请严厉模拟答辩老师，先做证据链矩阵，再指出高风险缺口，
并围绕每个缺口连续追问 3 层。最后给出稳妥回答和材料修改建议。
不要替我编造材料中没有的信息。
```

## 仓库结构

```text
defense-beating-simulator/
├── SKILL.md                  # Skill 入口和完整工作流
├── AGENTS.md                 # 通用 Agent 入口
├── CLAUDE.md                 # Claude 类 Agent 薄入口
├── GEMINI.md                 # Gemini 类 Agent 薄入口
├── agents/openai.yaml        # Codex 展示信息
├── references/               # 追问模式、评分规则和领域问题库
├── assets/                   # 用户要求导出时使用的模板
├── examples/                 # 校园能源、YOLO 检测等示例
├── evals/                    # 触发与输出结构回归提示集
├── scripts/                  # 无第三方依赖的验证脚本
├── tests/                    # 基础测试
├── install.ps1               # Windows 安装脚本
└── install.sh                # macOS / Linux 安装脚本
```

## 验证

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests
```

## 项目边界

- 不能保证答辩一定通过。
- 不能验证材料里没有提供的事实。
- 不应编造数据来源、实验结果、部署状态或个人贡献。
- 输出是答辩准备辅助，不替代导师反馈或真实评委判断。
