# Question Patterns

Use this reference when generating role-based questions, high-pressure follow-up chains, or academic-presentation style questions.

## Source-informed heuristics

The skill is shaped by patterns visible in public academic presentation and defense material:

- Short research-pitch formats such as 3MT can inform a small clarity check, but this skill should not turn into public-science communication coaching. Prioritize questions grounded in the user's README, report, PPT, code structure, data notes, figures, and result claims.
- Academic talk evaluation should not only check topic coverage; it should check whether the material connects project background, technical details, evidence, and the central contribution.
- Student presentation Q&A is often authentic and multi-turn, so hard questions should include follow-up chains instead of isolated prompts.
- Paper and project Q&A often asks information-seeking questions that require evidence across several parts of the material, not just a single fact.

## Universal question chain builders

### Data authenticity chain

1. 数据是实测、公开、模拟、课程假设，还是构造出来的？
2. 如果不是实测，为什么仍然可以支撑你的展示或结论？
3. 哪些结论只能算趋势展示，不能算工程结论？
4. 如果换成真实数据，需要重新计算哪些参数？
5. 当前代码或平台能否接入真实数据？需要改哪里？

### Personal contribution chain

1. 这个项目中你独立完成了哪一部分？
2. 哪些部分是团队完成、开源复用、课程模板或 AI 辅助生成的？
3. 你做的部分解决了什么具体问题？
4. 如果现场要求你改一个功能，你能改哪里？
5. 如果去掉别人的部分，你自己的技术贡献还剩什么？

### Simulation vs showcase chain

1. 你说的"仿真"具体指什么？
2. 是否有真实模型、动态计算或优化算法支撑？
3. 哪些数据是预设曲线，哪些是运行时计算？
4. 如果只是展示平台，为什么仍然有价值？
5. 为了变成工程级仿真平台，下一步要补什么？

### Result reliability chain

1. 你的结果指标是什么？
2. 这些指标如何计算，和项目目标是否一致？
3. 有没有对比实验、基线、消融或人工检查？
4. 哪些结果只是演示效果，不能代表真实部署表现？
5. 如果结果被质疑，你最有力的证据是什么？

### Innovation chain

1. 你的创新点属于方法、工程集成、展示方式、应用场景、流程，还是工具？
2. 哪个创新点最站得住？
3. 哪个说法可能只是包装，不能说太满？
4. 和普通课程设计或常规页面相比，区别在哪里？
5. 如果评委认为创新不足，你怎么把价值转到完整度、可解释性或工程组织上？

## Project-type focus

| Project type | Must ask |
| --- | --- |
| 课程设计 | 任务书覆盖、计算依据、参数来源、个人分工、报告规范、边界声明 |
| 科研项目 | 研究问题、创新性、实验设计、数据可信度、对比方法、局限和后续工作 |
| 代码开发 | 架构、模块边界、依赖、异常处理、测试、运行方式、可维护性 |
| 网页展示 | 数据来源、交互逻辑、是否真实计算、可视化是否误导、截图和 Demo |
| AI/深度学习 | 数据集、标注、训练策略、指标、对比、消融、泛化、失败案例 |
| 工程仿真 | 模型假设、边界条件、参数设置、验证方式、极端工况、工程可行性 |
| 竞赛项目 | 需求痛点、用户价值、创新等级、落地路径、团队分工、商业或社会价值 |
| 开源项目 | README、安装复现、示例数据、许可证、issue 风险、维护计划 |

## Role phrasing

- 课程老师: "这个计算依据来自哪里？和任务书哪一条对应？"
- 保研面试老师: "你在这个项目里最能体现专业能力的工作是什么？"
- 技术面试官: "这个功能的数据流从哪里进来，到哪里渲染？异常情况怎么处理？"
- 竞赛评委: "相比现有方案，你的优势是效果、成本、体验，还是集成度？"
- 严苛审稿人: "如果数据来源不清，你的结论还能成立到什么程度？"
- 答辩材料审查者: "你现在的 README、报告或 PPT 里，哪一页/哪一段能支撑这个结论？"

## High-pressure wording rules

- Be sharp about evidence: "材料里没有看到..." is better than vague criticism.
- Ask for mechanism, not labels: ask "SOC 曲线如何计算" instead of only "有没有算法".
- Convert broad doubts into answerable questions: data, method, contribution, result, boundary, reproducibility.
- Do not use insults or personal attacks, even in "严刑拷打" mode.
