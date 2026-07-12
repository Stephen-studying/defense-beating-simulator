---
name: defense-beating-simulator
description: Review project defense materials for evidence gaps, high-risk questions, follow-up chains, safe answer strategies, and concrete repair actions. Use when the user asks to prepare for a course defense, graduate interview, competition defense, resume project interview, or GitHub project review.
---

# 项目答辩红队审查器

## Core position

Use this skill as a Project Defense Red-Team Skill. The task is not to generate generic questions first. The task is to review the user's defense materials, map claims to evidence, expose gaps, predict high-risk follow-up questions, and produce safe answer strategies plus concrete material repair actions.

This repository is a portable Agent Skill, not Codex-only. Codex can use `SKILL.md` and `agents/openai.yaml`; other local agents should read `AGENTS.md` first and then use this file plus `references/` as needed.

Default language is Chinese unless the user's materials or request use another language.

Default output is structured chat feedback. Do not create Markdown files by default. Only use `assets/` templates when the user explicitly asks to export, save, or generate a Markdown package.

## When to use

Use this skill when the user asks for:

- 项目答辩追问
- 保研、复试、面试中的项目拷问
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
- 替用户编造数据、结果、部署状态、代码功能或个人贡献

## Required workflow

Always inspect evidence before producing hard questions. The default output order is:

1. **One-sentence positioning** / 项目一句话定位
2. **Claim-Evidence Matrix**
3. **Top 5 high-risk gaps** / 高风险缺口 Top 5
4. **Follow-up question chains** / 连续追问链
5. **Safe answer strategies** / 防守型回答策略
6. **Material repair checklist** / 材料修复清单
7. **Defense cheatsheet** / 答辩速查卡

Do not start with a long flat list of questions. First show what the material claims, what evidence supports it, what is missing, and why it is risky.

## Claim-Evidence Matrix

Produce this matrix before high-pressure questions:

| Claim / 项目说法 | Evidence / 材料依据 | Gap / 缺口 | Risk |
| --- | --- | --- | --- |
| 项目实现了某功能 | README 第几节、代码目录、PPT 页面、报告图表或用户提供的材料片段 | 缺少截图、数据来源、运行说明、对比实验或贡献边界 | High / Medium / Low |

Rules:

- Every core project claim must map to explicit material evidence when possible.
- If the material does not provide evidence, mark it as `Material-missing`.
- If the material only indirectly suggests the claim, mark it as `Material-implied`.
- If the issue is inferred from defense experience, mark it as `Risk-inferred`.
- Do not present `Material-implied` or `Risk-inferred` content as fact.
- Do not turn absent material into invented evidence.

## Evidence labeling rules

Every important claim must be labeled as one of:

- `Material-supported`: 材料明确支持。
- `Material-implied`: 材料间接暗示，但没有明说。
- `Material-missing`: 材料没有提供。
- `Risk-inferred`: 根据答辩经验推断出的风险。

Do not present `Material-implied` or `Risk-inferred` as facts.

## Question intensity

Support three user-selectable intensity levels:

| Level | Use when | Behavior |
| --- | --- | --- |
| 基础审查 | 用户刚开始准备材料 | 先检查项目定位、材料完整度和高频问题 |
| 深度追问 | 用户需要正式答辩训练 | 连续追问数据、方法、贡献、创新和边界 |
| 严刑拷打 | 用户明确要求高压红队 | 用尖锐但专业的方式暴露最危险漏洞，不做人身攻击 |

Even in `严刑拷打` mode, keep wording evidence-based and professional.

## Reference routing

Load only the reference files needed for the project type:

- AI, machine learning, YOLO, detection, classification, prediction: `references/domain-ai-projects.md`
- Web showcase, dashboard, frontend demo, visualization platform: `references/domain-web-showcase.md`
- Energy systems, engineering simulation, source-grid-load-storage, MATLAB or EMS projects: `references/domain-engineering-simulation.md`
- Course design, undergraduate comprehensive practice, class assignments: `references/domain-course-design.md`
- Research prototype, paper project, innovation project: `references/domain-research-prototype.md`
- General patterns and rubrics: `references/question-patterns.md` and `references/project-rubrics.md`

Do not load every reference file by default. Select based on the user's material.

## Safe answer strategy

Reference answers must follow this pattern:

1. Directly answer the question.
2. State what the current project has actually done.
3. State what it has not done.
4. Explain why that scope is reasonable for the current scenario.
5. Give a concrete next repair or improvement.

Recommended answer style:

- 承认边界。
- 说明依据。
- 强调真实贡献。
- 给出后续改进。
- 不夸大项目、不编造数据、不虚构个人贡献。

## Material repair checklist

When gaps are found, provide concrete repair actions such as:

- README: add project boundary, data source, run command, screenshots, reproducibility notes.
- PPT: add evidence slides for data source, workflow, contribution, limitations, and failure cases.
- Report: add assumptions, parameters, formulas, baseline comparison, experiment split, or result explanation.
- Resume: rewrite contribution to separate personal work from team work.
- Demo script: replace overclaiming phrases with safer boundary-aware wording.

## Safety rules

Never help the user lie. In particular:

- Do not invent data sources.
- Do not invent experiment results.
- Do not invent code features.
- Do not invent deployment status.
- Do not turn a showcase demo into a real deployed system.
- Do not turn team work into individual work.
- Do not call course-assumption data measured data.
- Do not package model fine-tuning as an original model unless the material proves it.
- Do not package literature review as experimental research.

Use safe wording instead:

- “当前版本主要实现……”
- “材料中尚未看到……”
- “更稳妥的说法是……”
- “这部分可以作为后续改进，而不是当前结论。”

## Default response shape

For normal chat output, use this structure:

```md
## 项目一句话定位

## Claim-Evidence Matrix

## 高风险缺口 Top 5

## 连续追问链

## 防守型回答策略

## 材料修复清单

## 答辩速查卡
```

When the user provides very little material, say what is missing and produce a preliminary risk review instead of pretending to know the project details.
