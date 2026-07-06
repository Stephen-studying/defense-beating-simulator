# Project Rubrics

Use this reference for risk ranking, evidence labeling, answer scoring, safe wording, data-source defense, innovation reframing, and contribution statements.

## Evidence labels

| Label | Meaning | How to use |
| --- | --- | --- |
| Material-supported | The material explicitly supports the claim. | Cite the README section, PPT page, report paragraph, code directory, data table, screenshot, or result figure. |
| Material-implied | The material suggests the claim but does not state it clearly. | Treat it as uncertain and ask for clarification or repair. |
| Material-missing | The material does not provide evidence. | Do not present the claim as true; propose a material repair. |
| Risk-inferred | The risk is inferred from defense experience. | Mark it as a likely defense risk, not a fact from the material. |

## Risk rubric

| Risk | Criteria |
| --- | --- |
| High | Likely to be asked and damaging if weak. Usually about data authenticity, personal contribution, project boundary, method depth, validation, novelty, or reproducibility. |
| Medium | Plausible follow-up. The user should prepare a short answer and one concrete example. |
| Low | Extension or curiosity question. Useful for polish but not the first preparation priority. |

## Weakness dimensions

Check these dimensions in every review:

1. 项目定位: 是否说清楚项目到底是什么，是否存在“仿真”“优化”“实时”“部署”等说法过大。
2. 技术深度: 是否有算法、模型、计算逻辑、工程依据，还是主要是展示和集成。
3. 数据支撑: 数据来源、构造逻辑、可信边界、可替换真实数据的路径。
4. 结果展示: 是否有图表、截图、指标、对比、误差、失败案例。
5. 个人贡献: 是否能区分本人工作、团队工作、开源复用、AI 辅助。
6. 创新表达: 哪些是真创新，哪些是工程集成或展示方式优化。
7. 可复现性: README、运行命令、依赖、示例数据、截图、Demo、许可证。
8. 风险表述: 是否有夸大、模糊、偷换概念、不严谨表述。
9. 答辩安全性: 哪些问题最容易引出连续追问。

## Reference answer frame

Use this structure for most answers:

1. 正面回应问题。
2. 说明当前版本实际做到了什么。
3. 承认当前没有做到什么。
4. 解释为什么这样处理，最好连接课程要求、数据条件、原型阶段或资源限制。
5. 给出后续改进方向，并说明先改哪一步。

Avoid:

- “完全实现了...”
- “真实部署了...”
- “效果大幅领先...”
- “最优控制...”
- “高精度预测...”
- “全部由我完成...”

Prefer:

- “当前版本主要实现...”
- “面向课程设计场景...”
- “基于典型工况或课程假设...”
- “用于趋势展示和方案说明...”
- “后续可以接入...”
- “我主要负责...”

## Data-source defense logic

1. 明确数据属性: 实测、公开数据、课程假设、模拟、构造、AI 生成、人工整理。
2. 说明使用目的: 趋势展示、方案计算、教学演示、初步验证、界面联调。
3. 说明合理性依据: 典型工况、公开范围、工程估算、任务书要求、可解释参数。
4. 承认局限: 不能替代真实工程实测或严格实验结论。
5. 提出改进: 接入真实数据、公开数据集、传感器、日志、更多场景或对比实验。

## Innovation rubric

| Type | Safe framing |
| --- | --- |
| 方法创新 | Only claim when there is a new algorithm, model, training design, optimization method, or clear method adaptation. |
| 工程集成创新 | Multiple modules are integrated into a usable system or workflow. This is common and often defensible. |
| 展示方式创新 | Static report results become interactive visualization, dashboard, demo, or explainable interface. |
| 应用场景创新 | Existing method is adapted to a specific scenario with meaningful constraints. |
| 流程创新 | The workflow itself improves preparation, validation, review, or collaboration. |
| 工具创新 | A reusable script, app, template, or skill is produced and can be used beyond one report. |

If novelty is weak, shift from “创新性很强” to “完整性、可解释性、展示效果、可扩展性较好”.

## Answer scoring rubric

When the user provides their own answer, score out of 100:

| Dimension | Points |
| --- | ---: |
| 正面回答问题 | 20 |
| 有技术或材料细节 | 20 |
| 承认项目边界 | 15 |
| 突出个人贡献 | 15 |
| 避免夸大 | 15 |
| 表达清晰 | 15 |

Output format:

```text
得分：78/100
主要问题：...
建议补充：...
更稳妥版本：...
```

## Contribution statement frame

Produce five forms when requested:

- 一句话贡献。
- 三条核心贡献。
- 可放简历的表达。
- 可在答辩中说的表达。
- 面对追问时的防守回答。

Always keep contribution conservative. If the user says “参与完成”, ask or infer carefully before saying “独立负责”.
