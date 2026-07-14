# Expected Weakness Report: Campus Energy System

## 1. Overall Risk Level

- Overall risk: High
- Main reason: 数据来源、仿真边界和 EMS 算法深度容易被连续追问。
- Priority repair area: 数据来源与项目边界声明。

## 2. Weakness Table

| Risk | Weak Point | Material Evidence | Evidence status | Risk basis | Why It Is Dangerous | Repair Action | Safer Wording |
| --- | --- | --- | --- | --- | --- | --- | --- |
| High | 数据不是实测但可能被误解为真实运行数据 | 输入材料说明典型日和课程假设 | Material-supported | Risk-inferred | 会影响结论可信度 | 新增数据来源与假设 | 数据基于典型工况构造，主要用于趋势展示 |
| High | “能耗优化计算”缺少模型证据 | 材料主题包含优化，但未见目标函数或算法 | Material-implied | Material-derived | 容易被连续追问优化机制 | 改为展示与辅助分析，或补模型 | 当前版本主要进行典型工况辅助分析 |
| Medium | 个人贡献证据不足 | 只说明负责前端和可视化 | Material-supported | Risk-inferred | 面试中可能被追问具体代码 | 补模块截图和目录说明 | 我主要负责前端界面、数据结构和能量流可视化 |

## 3. Top Repair Actions

1. README 新增数据来源与假设。
2. PPT 补 SOC、负荷、光伏曲线来源。
3. 统一项目边界表述，避免真实部署和工程级仿真说法。
