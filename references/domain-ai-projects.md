# AI / Machine Learning Project Defense Questions

Use this reference for AI, machine learning, deep learning, YOLO, detection, classification, prediction, and algorithm projects.

## Dataset

- 数据集来自哪里？
- 是否公开？
- 是否有授权？
- 训练集、验证集、测试集如何划分？
- 是否存在数据泄漏？
- 数据类别是否均衡？
- 样本量是否足够？
- 标注是谁做的？有没有标注一致性检查？
- 数据增强是否只用于训练集？

## Model

- 为什么选择这个模型？
- 和 baseline 相比提升在哪里？
- 是否做过消融实验？
- 是否只是换了一个模块名字？
- 参数量、计算量、推理速度如何？
- 改进模块是否真正改变了网络结构或训练策略？
- 代码是自己写的、复现论文的，还是基于开源项目修改？

## Metrics

- 为什么使用 Precision / Recall / F1 / mAP？
- 指标是否能反映实际应用效果？
- 有没有失败案例？
- 有没有误检和漏检分析？
- 是否只报告了最好结果？
- 是否在同一数据划分上比较 baseline？

## Contribution

- 你个人负责了哪些部分？
- 模型结构是你设计的还是引用的？
- 训练脚本、数据清洗、可视化、实验记录分别是谁完成的？
- 你真正解决了什么问题？
- 如果删除开源框架，你自己的贡献还剩什么？

## Safe wording

- “当前改进主要是在公开模型基础上的结构调整和实验验证。”
- “数据集规模有限，因此结论更适合说明该数据集上的趋势，而不是泛化到所有场景。”
- “我主要负责数据整理、训练配置、实验对比和结果分析。”