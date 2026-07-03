<div align="center">

# 答辩挨打模拟器

把 README、报告、PPT 和代码结构变成一场提前发生的答辩压力测试。

`defense-beating-simulator` · Codex 技能 · 面向学生项目、课程设计、科研原型与开源仓库

</div>

## 它解决什么问题

很多项目不是不能讲，而是材料里有漏洞：数据来源没说清楚、个人贡献太模糊、创新点说得过满、结果缺少证据。这个技能会围绕答辩材料本身追问，提前暴露这些风险。

重点检查：

- README 是否支撑项目定位
- 报告、PPT、图表和结论是否互相对应
- 代码结构是否能证明真实实现
- 数据来源、模型假设、结果指标是否说清楚
- 个人贡献、项目边界和风险表述是否稳妥

## 核心能力

- 提取项目摘要：项目类型、技术栈、功能、数据、结果、贡献与局限
- 生成分层问题库：基础理解、技术路线、数据来源、结果解释、创新性和改进方向
- 模拟多角色追问：课程老师、保研导师、竞赛评委、技术面试官和严苛审稿人
- 输出高压追问链：专门针对最容易扣分的问题连续追问
- 给出稳妥回答：承认边界、说明依据、突出贡献、补充改进方向
- 诊断材料薄弱点：指出 README、报告、PPT、演示和简历表述该怎么补

## 默认产物

- `project-summary.md`：项目摘要与材料支撑情况
- `question-bank.md`：分角色、分层级、带风险标注的问题库
- `weakness-report.md`：高风险薄弱点与修复建议
- `defense-cheatsheet.md`：答辩前一页速查卡

## 提问强度

```text
先热个身 / 开始挑刺 / 严刑拷打
```

| 强度 | 适合场景 | 输出特点 |
| --- | --- | --- |
| 先热个身 | 第一次梳理项目 | 先确认项目能不能讲清楚，问题相对友好 |
| 开始挑刺 | 常规答辩准备 | 系统追问数据、方法、结果、贡献和创新 |
| 严刑拷打 | 正式答辩前压测 | 集中攻击最容易扣分的薄弱点，并生成追问链 |

## 安装

PowerShell：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent codex -Force
```

类 Unix shell：

```bash
sh install.sh --agent codex --force
```

安装后重启 Codex，然后这样调用：

```text
请用 $defense-beating-simulator 分析我的项目 README，场景为保研面试，强度选择“严刑拷打”。
```

## 校验

不需要安装第三方依赖。

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests
```

## 目录结构

```text
SKILL.md                 Codex 技能入口
AGENTS.md                通用智能体入口
agents/openai.yaml       Codex 展示元信息
references/              问题模式与评分规则
assets/                  输出模板
scripts/validate_skill.py 无依赖校验脚本
tests/                   基础测试
```