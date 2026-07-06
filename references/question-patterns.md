# Question Patterns

Use this reference when generating role-based questions, high-pressure follow-up chains, and Claim-Evidence Matrix driven defense reviews.

## Core principle

Start from evidence, not from questions.

```text
Claim -> Evidence -> Gap -> Risk -> Follow-up chain -> Safe answer -> Repair action
```

A good question should point to a concrete material gap: README section missing, PPT claim unsupported, code tree unclear, data source unstated, result metric unexplained, or contribution boundary vague.

## Universal question chain builders

### Data authenticity chain

1. 数据是实测、公开、模拟、课程假设，还是构造出来的？
2. 材料中哪一处说明了数据来源？
3. 如果不是实测，哪些结论只能算趋势展示？
4. 如果换成真实数据，需要重新计算哪些参数？
5. 当前代码或平台能否接入真实数据？需要改哪里？

### Personal contribution chain

1. 这个项目中你独立完成了哪一部分？
2. 哪些部分是团队完成、开源复用、课程模板或 AI 辅助生成的？
3. 材料中是否能证明你的具体贡献？
4. 如果现场要求你改一个功能，你能改哪里？
5. 如果去掉团队或模板部分，你自己的技术贡献还剩什么？

### Project boundary chain

1. 你说的“系统”“平台”“仿真”“优化”分别指什么？
2. 是否有真实模型、动态计算、后端服务或优化算法支撑？
3. 哪些数据是预设曲线，哪些是运行时计算？
4. 如果只是展示平台，为什么仍然有答辩价值？
5. 要变成工程级系统，下一步必须补什么？

### Result reliability chain

1. 你的结果指标是什么？
2. 这些指标如何计算，和项目目标是否一致？
3. 有没有对比实验、基线、消融或人工检查？
4. 哪些结果只是演示效果，不能代表真实部署表现？
5. 如果结果被质疑，材料里最有力的证据是什么？

### Innovation chain

1. 你的创新点属于方法、工程集成、展示方式、应用场景、流程，还是工具？
2. 哪个创新点最有材料证据？
3. 哪个创新点只是包装，不能说太满？
4. 和普通课程设计、常规页面或开源 baseline 相比，差异在哪里？
5. 如果评委认为创新不足，如何转向完整度、可解释性或工程组织价值？

## Claim-Evidence prompts

Use these prompts before writing hard questions:

- 材料中具体说了什么？
- 这个说法对应 README、PPT、报告、代码或结果图的哪一处？
- 证据是明确支持、间接暗示、完全缺失，还是仅仅推断出的风险？
- 如果老师抓住这个说法追问，最危险的连续问题是什么？
- 用户应该补哪一段材料，才能把风险降下来？

## Role phrasing

- 课程老师: “这个计算依据来自哪里？和任务书哪一条对应？”
- 保研面试老师: “你在这个项目里最能体现专业能力的工作是什么？材料中能看出来吗？”
- 技术面试官: “这个功能的数据流从哪里进来，到哪里渲染？异常情况怎么处理？”
- 竞赛评委: “相比现有方案，你的优势是效果、成本、体验，还是集成度？”
- 严苛审稿人: “如果数据来源不清，你的结论还能成立到什么程度？”
- 答辩材料审查者: “README、报告或 PPT 里哪一段能支撑这个结论？”

## High-pressure wording rules

- Be sharp about evidence: “材料里没有看到...” is better than vague criticism.
- Ask for mechanism, not labels: ask “SOC 曲线如何计算” instead of only “有没有算法”.
- Convert broad doubts into answerable questions: data, method, contribution, result, boundary, reproducibility.
- Do not use insults or personal attacks, even in “严刑拷打” mode.
