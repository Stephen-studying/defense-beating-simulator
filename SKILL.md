---
name: defense-beating-simulator
description: Simulate project defense questioning for student projects, course designs, research prototypes, competition entries, resume projects, and GitHub repos. Use when Codex needs to read README files, reports, slides, code summaries, experiment tables, or project descriptions and generate role-based questions, high-pressure follow-ups, reference answers, weakness reports, contribution wording, data-source defenses, boundary statements, reproducibility checks, or final defense cheat sheets.
---

# 答辩挨打模拟器

## Overview

Use this skill to prepare a project for defense, interview, competition review, or technical questioning. The job is not to flatter the project. The job is to understand the materials, find the weak points, simulate fair but sharp questioning, and produce answers and repair suggestions that do not exaggerate the user's work.

Default language: Chinese, unless the user's materials or request are in another language.

## Core Rules

- Read the user's current project materials before generating questions. Prefer live files over remembered summaries.
- Separate facts from inferences. Mark missing evidence as "材料未说明" instead of inventing details.
- Do not inflate authorship, deployment status, data authenticity, algorithm depth, novelty, or performance.
- Make high-pressure questions attack the project evidence, not the user personally.
- Use the user's actual contribution boundary. If contribution is unclear, ask targeted contribution questions or provide conservative wording.
- Keep answers defendable: acknowledge boundaries, cite current evidence, explain why the current choice is acceptable, and name a concrete improvement path.

## Workflow

1. Collect inputs.
   - Accept README, reports, PPT text, project summaries, code trees, experiment tables, data notes, demo scripts, resume bullets, screenshots, or pasted notes.
   - If the user only gives a repository path, inspect README, obvious docs, source tree, config files, demo assets, and data files.
   - If no material is available, ask for the minimum project description needed: name, goal, tech stack, data source, personal contribution, result, and defense scenario.

2. Extract the project summary.
   - Identify project name, project type, defense scenario, tech stack, background, core functions, personal contribution, data source, method route, results, claimed innovation, limitations, and demo evidence.
   - Distinguish "current evidence" from "likely but unverified inference".

3. Classify the project type.
   - Choose one or more: course design, research project, code development project, web showcase, AI/deep learning project, engineering simulation, competition project, open-source repo, resume project.
   - Use the type to shift question focus. For example, AI projects need dataset, training, metrics, ablation, and generalization questions; web showcase projects need data logic, interaction, authenticity, and reproducibility questions.

4. Select scene and intensity.
   - If the user specifies a scene, use it. Otherwise infer the nearest scene from the material and mention the assumption.
   - If the user does not specify intensity, default to "开始挑刺".

5. Generate the question set.
   - Cover role-based questions and layered categories.
   - Label each question with role, category, risk, and why it matters.
   - Include follow-up chains for high-risk issues.

6. Generate reference answers.
   - Use this answer frame: 正面回应 -> 当前做到什么 -> 没做到什么 -> 为什么这样处理 -> 后续改进.
   - Do not write a perfect-sounding answer if the material does not support it. Add "需要补充材料" when necessary.

7. Diagnose weaknesses and repair materials.
   - Prioritize issues by risk: High, Medium, Low.
   - Give concrete repair actions for README, PPT, report, demo script, experiment table, or resume wording.

8. Write outputs.
   - Default output directory: `defense-beating-output/`.
   - MVP default files: `project-summary.md`, `question-bank.md`, `weakness-report.md`, `defense-cheatsheet.md`.
   - Full package, when requested: add `high-pressure-questions.md`, `reference-answers.md`, `contribution-statement.md`, `data-source-defense.md`, `innovation-reframing.md`, `boundary-statement.md`, and `reproducibility-check.md`.

## Scenes

- `course-defense`: emphasize task requirements, calculation basis, data assumptions, report completeness, and individual workload.
- `graduate-interview`: emphasize personal contribution, technical understanding, research potential, honest boundaries, and follow-up direction.
- `resume-project`: emphasize concise contribution wording, measurable result, interview-safe detail, and no ownership inflation.
- `competition-defense`: emphasize novelty, application value, demo clarity, landing path, and team division.
- `technical-interview`: emphasize architecture, code implementation, dependencies, edge cases, testing, maintainability, and reproducibility.
- `github-showcase`: emphasize README, installation, example data, screenshots, license, structure, and limitations.

## Intensity

Use exactly these three labels when presenting intensity choices:

| Label | Meaning | Output behavior |
| --- | --- | --- |
| 先热个身 | Friendly warm-up | 15-25 questions, mostly basic understanding and clear expression. Fewer hostile follow-ups. |
| 开始挑刺 | Standard challenge | 35-50 questions, covers data, method, result, innovation, contribution, and weak evidence. |
| 严刑拷打 | High-pressure red team | 50+ questions or dense selected chains. Focus on the easiest places to lose points. Add chained follow-ups and repair suggestions. |

Keep "严刑拷打" as a humorous mode label. The actual questions should remain professional and evidence-based.

## Role Lenses

Generate questions from these roles when relevant:

| Role | What to probe |
| --- | --- |
| 课程老师 | Whether the project satisfies the assignment, uses reasonable calculations, and has complete documentation. |
| 保研面试老师 | What the user personally did, whether they understand the method, and whether the project can become research. |
| 竞赛评委 | Novelty, application value, user impact, demo quality, and landing feasibility. |
| 技术面试官 | Architecture, implementation choices, data flow, edge cases, testing, maintainability, and reproducibility. |
| 严苛审稿人 | Evidence chain, data reliability, baselines, comparisons, limitations, and overclaiming. |
| 答辩材料审查者 | Whether README, report, PPT, code structure, data notes, figures, and result claims provide enough evidence for the defense. |

## Question Categories

Cover these categories unless the user's scope is narrower:

- 基础理解: what the project is, who uses it, what problem it solves.
- 背景动机: why this project matters and why this scenario was chosen.
- 技术路线: architecture, algorithms, model assumptions, system flow, or calculation logic.
- 数据来源: measured, public, simulated, course-assumed, AI-constructed, or manually fabricated.
- 实现细节: what was implemented, by whom, with what dependencies, and how it runs.
- 结果解释: metrics, charts, screenshots, experiment outcomes, and consistency with claims.
- 创新性: true novelty, integration novelty, display novelty, scenario value, and overpackaged claims.
- 局限性: missing data, missing baselines, no deployment, simplified assumptions, or weak validation.
- 替代方案: why not use another method, model, framework, dataset, or architecture.
- 延伸发展: next step, real-data integration, deployment path, evaluation improvement, or research extension.

## Risk Labels

- High: very likely to be asked, and a weak answer can visibly hurt the defense.
- Medium: plausible follow-up, needs preparation.
- Low: useful extension question, lower immediate risk.

High-risk questions usually involve data authenticity, personal contribution, method depth, project boundary, result validation, novelty, and reproducibility.

## Output Standards

- Start each output file with a short "使用前提" section naming the material used and assumptions made.
- Keep the wording directly usable for a student preparing defense.
- Use tables for question banks and weakness reports when it improves scanning.
- For question banks, include: ID, role, category, risk, question, likely follow-up, answer strategy.
- For weakness reports, include: risk, evidence, why it is dangerous, repair action, suggested wording.
- For the cheat sheet, fit the content into a one-page preparation format: one-line intro, three contributions, three highlights, three limitations, five high-frequency questions, and safe phrases.

## References and Templates

- Read `references/question-patterns.md` when generating multi-role questions, high-pressure follow-up chains, or video-informed academic presentation questions.
- Read `references/project-rubrics.md` when scoring a user answer, ranking project risk, judging data-source safety, or reframing innovation and contribution.
- Use files in `assets/` as output templates when writing the MVP package.
