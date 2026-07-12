# Expected Question Bank: Campus Energy System

## High-risk Question Chains

### Chain 1: Data Source

- Q1: 你的负荷数据和光伏数据是实测的吗？
- Q2: 如果是典型工况构造，为什么还能用于课程设计？
- Q3: 哪些结论不能推广到真实校园？
- Risk: High
- Safe answer: 数据用于趋势展示和运行逻辑说明，不替代实测工程结论。
- Required material repair: README 增加数据来源、参数表和假设说明。

### Chain 2: Simulation Boundary

- Q1: 你说的仿真具体包含哪些计算？
- Q2: 储能 SOC 是积分计算还是预设曲线？
- Q3: EMS 是优化算法还是展示逻辑？
- Risk: High
- Safe answer: 当前版本偏展示与辅助分析，后续可接入优化调度模型。
- Required material repair: PPT 补模型边界图和当前/未来功能区分。