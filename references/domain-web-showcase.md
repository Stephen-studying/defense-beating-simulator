# Web Showcase / Frontend Demo Defense Questions

Use this reference for frontend demos, dashboards, visualization platforms, static sites, and web showcase projects.

## Function boundary

- 这个系统是真实运行平台，还是展示型 Demo？
- 数据是静态 JSON、前端 mock，还是后端接口返回？
- 用户操作是否会改变真实状态？
- 是否有真实数据库？
- 是否支持多用户？
- 是否有登录、权限、数据持久化和异常处理？
- 哪些功能只是演示逻辑，哪些功能有真实业务逻辑？

## Implementation

- 前端使用了什么技术栈？
- 状态管理如何实现？
- 页面切换后时间轴是否保持一致？
- 数据刷新逻辑如何实现？
- 是否做了响应式适配？
- 图表数据和页面交互之间如何绑定？
- 是否有构建、部署、测试或 lint 流程？

## Defense risk

- 如果只是展示平台，不能说成真实仿真平台。
- 如果没有后端，不能说成完整系统。
- 如果数据是构造的，必须说明是典型工况展示。
- 如果只是前端动画，不能暗示存在实时优化算法。
- 如果没有真实用户测试，不要说用户体验已被验证。

## Safe wording

- “当前版本主要是展示型 Demo，重点在交互逻辑和可视化表达。”
- “数据由静态文件或 mock 接口提供，用于演示页面流程。”
- “后续可以接入后端接口、数据库和真实日志，形成完整系统。”