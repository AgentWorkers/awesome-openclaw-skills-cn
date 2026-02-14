# AGENTS.md

This file provides guidance to agents when working with code in this repository.

## 项目性质

这是一个中文翻译仓库，fork 自上游英文仓库 [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)。

## 同步上游更新

**不要直接 merge 上游**：由于译文与原文差异大，直接 merge 会产生大量冲突。

同步方法：
1. 获取上游最新 commit id：`git fetch upstream && git log upstream/main --oneline -1`
2. 对比翻译基准版本 `95fb437` 与最新版本的差异
3. 将差异翻译并应用到中文版本
4. 更新 `SYNC.md` 中的 commit id 和同步历史

## 翻译规范

- 技能名称保持英文原文
- 描述翻译为中文
- 保持 Markdown 格式和链接地址不变

## 关键文件

- `SYNC.md` - 追踪译文与上游 commit 的对应关系
- `README.md` - 主翻译文件（约 40 万字符）
- `CONTRIBUTING.md` - 贡献指南翻译
