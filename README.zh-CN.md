# 答辩挨打模拟器

`defense-beating-simulator` 是一个用于项目答辩准备的 Codex Skill。它面向学生项目、课程设计、科研原型、竞赛项目、简历项目和 GitHub 仓库。

它会读取 README、报告、PPT 文案、代码结构、数据说明、实验结果表等材料，然后生成：

- 项目摘要
- 分角色答辩问题
- 高压追问链
- 项目薄弱点报告
- 个人贡献与边界声明
- 数据来源防守口径
- 答辩速查卡

## 重点

这个 Skill 的重点不是“让非专业观众听懂”，而是围绕答辩材料本身追问：

- README 是否支撑项目定位？
- 报告和 PPT 是否支撑结论？
- 代码结构是否能证明实现？
- 数据来源、模型假设、结果指标是否说清楚？
- 哪些表述容易被老师、评委、面试官继续追问？

## 提问强度

```text
先热个身 / 开始挑刺 / 严刑拷打
```

- `先热个身`：友好热身，检查项目是否能讲清楚。
- `开始挑刺`：常规质疑，追问数据、方法、结果、贡献和创新。
- `严刑拷打`：高压红队，集中攻击最容易扣分的薄弱点。

## 校验

无需安装 PyYAML 或其他第三方依赖。

```bash
python scripts/validate_skill.py
python -m unittest discover -s tests
```

## 安装到 Codex

PowerShell：

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\install.ps1 -Agent codex -Force
```

Shell：

```bash
sh install.sh --agent codex --force
```

安装后重启 Codex，然后这样调用：

```text
Use $defense-beating-simulator 分析我的课程设计 README，强度选择“严刑拷打”。
```
