# Expected Weakness Report: Campus Energy System

## 1. Overall Risk Level

- Overall risk: High
- Main reason: 数据来源、仿真边界和 EMS 算法深度容易被连续追问。
- Priority repair area: 数据来源与项目边界声明。

## 2. Weakness Table

| Risk | Weak Point | Material Evidence | Why It Is Dangerous | Repair Action | Safer Wording |
| --- | --- | --- | --- | --- | --- |
| High | 数据不是实测但可能被误解为真实运行数据 | 输入材料说明典型日和课程假设 | 会影响结论可信度 | 新增数据来源与假设 | 数据基于典型工况构造，主要用于趋势展示 |
| High | 仿真平台表述偏大 | 材料未见后端仿真服务或优化模型 | 容易被质疑只是网页展示 | 改为展示与辅助分析平台 | 当前版本更接近课程设计展示平台 |
| Medium | 个人贡献证据不足 | 只说明负责前端和可视化 | 面试中可能被追问具体代码 | 补模块截图和目录说明 | 我主要负责前端界面、数据结构和能量流可视化 |

## 3. Top Repair Actions

1. README 新增数据来源与假设。
2. PPT 补 SOC、负荷、光伏曲线来源。
3. 统一项目边界表述，避免真实部署和工程级仿真说法。
