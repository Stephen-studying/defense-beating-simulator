# Expected Defense Cheatsheet: YOLO PV Defect Detection

## 1. One-sentence Project Pitch

本项目基于 YOLO 目标检测框架，对光伏组件表面缺陷进行识别实验，并分析模型在特定数据集上的 Precision、Recall 和 mAP 表现。

## 2. Three Core Contributions

1. 整理光伏缺陷数据并配置训练流程。
2. 在 YOLO baseline 上进行结构改进实验。
3. 分析检测指标、可视化结果和失败案例。

## 3. Three Things Not to Overclaim

1. 不说数据集全部真实可靠，除非材料证明来源和授权。
2. 不说原创模型，除非有清晰结构设计和消融实验。
3. 不说全面优于现有方法，除非有同条件 baseline 对比。

## 4. High-risk Questions

| Question | Key Point | Safe Answer |
| --- | --- | --- |
| 数据集来自哪里？ | 来源、授权、划分 | 当前需要补充数据来源和划分说明 |
| 改进模块是否有效？ | 消融实验 | 需要用 baseline 和消融结果支撑 |
| 你个人做了什么？ | 贡献边界 | 我主要负责数据整理、训练配置和实验分析 |

## 5. Final 30-second Summary

当前项目是一个面向光伏缺陷检测场景的 YOLO 实验项目，重点展示目标检测模型在该数据集上的识别效果。最需要补强的是数据集说明、baseline 对比、消融实验和失败案例分析。