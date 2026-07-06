# Engineering Simulation Defense Questions

Use this reference for energy systems, engineering simulation, EMS, PV, storage, source-grid-load-storage projects, and course-design calculation platforms.

## Model assumptions

- 模型边界条件是什么？
- 哪些参数来自真实资料，哪些参数是课程假设？
- 如果参数变化 20%，结论是否仍然成立？
- 结果能支撑工程结论，还是只能支撑趋势展示？
- 是否有物理约束、功率平衡或能量守恒检查？
- 是否考虑极端工况、设备容量限制和效率损耗？

## Energy system projects

- 光伏出力曲线如何得到？
- 负荷数据是实测、典型日、课程假设，还是人工构造？
- 储能 SOC 是否由功率积分计算，还是预设曲线？
- EMS 是否有优化算法，还是仅做展示逻辑？
- 源网荷储之间的功率平衡如何体现？
- 并网、弃光、充放电效率和约束条件是否说明？
- 成本、收益或节能量是否有计算依据？

## Common safe wording

- “本项目采用典型工况数据，主要用于展示系统运行逻辑和能量流关系。”
- “当前模型偏工程估算和方案验证，尚未达到实际工程部署级别。”
- “数据并非实测数据，因此结论更适合用于趋势分析，而不是直接工程设计。”
- “储能控制目前采用规则逻辑，后续可以接入优化调度模型。”
