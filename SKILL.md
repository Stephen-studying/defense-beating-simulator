---
name: defense-beating-simulator
description: Review project defense materials for evidence gaps, high-risk questions, follow-up chains, safe answer strategies, and concrete repair actions. Use when the user asks to prepare for a course defense, graduate interview, competition defense, resume project interview, or GitHub project review.
---

# 答辩挨打模拟器

## Core position

Use this skill as a Project Defense Red-Team Skill. The task is not to generate generic questions first. The task is to review the user's defense materials, map claims to evidence, expose gaps, predict high-risk follow-up questions, and produce safe answer strategies plus concrete material repair actions.

This repository is a portable Agent Skill, not Codex-only. Codex can use `SKILL.md` and `agents/openai.yaml`; other local agents should read `AGENTS.md` first and then use this file plus `references/` as needed.

Default language is Chinese unless the user's materials or request use another language.

Default output is structured chat feedback. Do not create Markdown files by default. Only use `assets/` templates when the user explicitly asks to export, save, or generate a Markdown package.

## When to use

Use this skill when the user asks for:

- 项目答辩追问
- 保研/面试项目拷问
- README、PPT、报告、代码结构的答辩风险检查
- 数据来源、个人贡献、创新点、项目边界的防守表达
- 答辩速查卡、问题库、薄弱点修复清单
- GitHub 项目展示、简历项目、课程设计、竞赛项目或科研原型的材料审查

## Do not use

Do not use this skill for:

- 单纯润色演讲稿
- 生成通用面试题
- 没有项目材料的职业规划建议
- 与项目证据链无关的学术科普问答
- 替用户编造数据、结果、部署、代码功能或个人贡献

## Safety rules

- Do not invent data sources.
- Do not invent experimental results.
- Do not invent code features.
- Do not describe a showcase demo as a real deployed system unless the material proves it.
- Do not turn team work into individual work.
- Do not describe course-assumption data as measured data.
- Do not package minor model tuning as an original model.
- Do not package a literature review as an experimental paper.
- Help the user state boundaries safely; do not help the user lie.

## Evidence labeling rules

Every important claim must be labeled as one of:

- `Material-supported`: the material explicitly supports the claim.
- `Material-implied`: the material indirectly suggests the claim but does not state it clearly.
- `Material-missing`: the material does not provide evidence for the claim.
- `Risk-inferred`: the risk is inferred from defense experience, not directly stated in the material.

Do not present `Material-implied` or `Risk-inferred` as facts. If evidence is absent, say `Material-missing` and propose a repair action.

## Required workflow

1. **Read materials**
   - Accept README, report text, PPT text, project summary, code tree, experiment table, data notes, demo script, resume bullet, screenshots, or pasted notes.
   - If the user gives a repository path, inspect README, docs, source tree, config files, example data, demo assets, screenshots, and tests.
   - If materials are insufficient, state what can and cannot be judged before asking for missing items.

2. **One-sentence positioning**
   - State the safest project positioning in one sentence.
   - Flag words that may overclaim, such as "真实仿真", "实时部署", "最优控制", "原创模型", "全部独立完成".

3. **Claim-Evidence Matrix**
   - Output this matrix before high-pressure questions.
   - Every core project claim must map to material evidence or a missing-evidence label.

```md
## Claim-Evidence Matrix

| Claim / 项目说法 | Evidence / 材料依据 | Evidence label | Gap / 缺口 | Risk |
| --- | --- | --- | --- | --- |
| 项目实现了某功能 | README section / code directory / PPT page | Material-supported | 缺少截图、数据、运行说明或结果解释 | High / Medium / Low |
```

4. **Top 5 high-risk gaps**
   - Rank the five most dangerous gaps. Typical high-risk gaps involve data authenticity, personal contribution, project boundary, method depth, result validation, innovation, and reproducibility.

5. **Follow-up chains**
   - For each High risk gap, generate 2-4 chained questions.
   - Ask about evidence and mechanism, not labels only.

6. **Safe answer strategies**
   - Use this frame: 正面回应 -> 当前做到什么 -> 没做到什么 -> 为什么这样处理 -> 后续怎么改.
   - Do not make the answer sound stronger than the material supports.

7. **Material repair checklist**
   - Give concrete edits for README, PPT, report, demo script, result table, code comments, or resume wording.
   - Prefer exact section names and safe wording.

8. **Defense cheatsheet**
   - Include one-sentence pitch, three contributions, three highlights, three limitations, five high-risk questions, and five safe phrases.

## Default output order

Use this order unless the user explicitly asks for a narrower output:

1. 项目一句话定位
2. Claim-Evidence Matrix
3. 高风险缺口 Top 5
4. 连续追问链
5. 防守型回答策略
6. 材料修复清单
7. 答辩速查卡

## Scene modes

- `course-defense`: task requirements, calculation basis, data assumptions, report completeness, individual workload.
- `graduate-interview`: personal contribution, technical understanding, research potential, honest boundary, next-step research.
- `resume-project`: concise contribution wording, measurable result, interview-safe detail, no ownership inflation.
- `competition-defense`: novelty, application value, demo clarity, landing path, team division.
- `technical-interview`: architecture, implementation, dependencies, edge cases, testing, maintainability, reproducibility.
- `github-showcase`: README, install command, example data, screenshots, license, project structure, limitations.

## Intensity labels

Use exactly these labels:

| 强度 | 含义 | 输出方式 |
| --- | --- | --- |
| 先热个身 | 友好热身 | 先检查项目能不能讲清楚，问题较基础。 |
| 开始挑刺 | 标准答辩压力 | 系统追问数据、方法、结果、贡献、创新和证据缺口。 |
| 严刑拷打 | 高压红队 | 集中攻击最容易扣分的薄弱点，增加连续追问和材料修复建议。 |

"严刑拷打" is a humorous label. The actual questions must remain professional, restrained, and evidence-based.

## Role lenses

Choose relevant roles based on the material; do not force every role every time.

| 角色 | 主要追问点 |
| --- | --- |
| 课程老师 | 是否符合任务要求，计算和报告是否规范。 |
| 保研面试老师 | 用户到底做了什么，是否真正理解项目，是否有继续研究潜力。 |
| 竞赛评委 | 创新性、应用价值、展示效果、落地可行性。 |
| 技术面试官 | 架构设计、代码实现、依赖、边界情况、测试和可扩展性。 |
| 严苛审稿人 | 数据可靠性、证据链、对比实验、结果解释和过度包装。 |
| 答辩材料审查者 | README、报告、PPT、代码结构、数据说明、图表和结论是否互相支撑。 |

## Project-type references

Load these files only when relevant:

- `references/domain-ai-projects.md` for AI, machine learning, YOLO, detection, classification, prediction, and algorithm projects.
- `references/domain-web-showcase.md` for web demos, dashboards, frontend visualizations, and showcase systems.
- `references/domain-engineering-simulation.md` for energy systems, engineering simulation, EMS, PV, storage, and source-grid-load-storage projects.
- `references/domain-course-design.md` for course design, undergraduate practice, and team coursework.
- `references/domain-research-prototype.md` for research prototypes, paper projects, innovation projects, and early-stage experiments.

Also use:

- `references/question-patterns.md` for universal chains and role phrasing.
- `references/project-rubrics.md` for risk ranking, safe wording, answer scoring, contribution framing, and innovation reframing.

## Optional exported package

Only when the user asks to export files, write:

- `project-summary.md`
- `question-bank.md`
- `weakness-report.md`
- `defense-cheatsheet.md`

When the user asks for a full package, add specialized files for high-pressure questions, reference answers, contribution statement, data-source defense, innovation reframing, boundary statement, and reproducibility check.
