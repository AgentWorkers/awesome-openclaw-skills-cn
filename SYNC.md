# 译文同步追踪

本文件用于追踪中文译文与上游仓库的对应关系。

## 当前状态

| 文件 | 上游 Commit | 同步时间 |
|------|-------------|----------|
| README.md | `b0f21bbe051ed3463b3edda59b953326c1c64ab0` | 2026-02-14 |
| CONTRIBUTING.md | `ce7b4e400ef794bddce66eb64719dd7550b23101` | 2026-02-14 |

## 上游仓库信息

- **仓库地址**: https://github.com/VoltAgent/awesome-openclaw-skills
- **翻译基准版本**: `95fb437` (翻译前的原始英文版本)

## 同步历史

### 2026-02-14
- 同步到 `b0f21bbe051ed3463b3edda59b953326c1c64ab0`
- 新增技能:
  - `static-app` - 将静态网站部署到 static.app 托管。
  - `prometheus` - 查询 Prometheus 监控数据以检查服务器指标、资源使用情况和系统健康状况。
  - `douban-sync-skill` - 导出并同步豆瓣书籍/电影/音乐/游戏收藏。

---

# 同步更新说明

## 概述

由于中文译文与英文原文差异较大，无法直接通过 git merge 合并上游更新。本文档说明如何手动同步上游更新到中文版本。

## 同步方法

### 方法一：提供最新 commit id（推荐）

1. 获取上游最新 commit id：
   ```bash
   git fetch upstream
   git log upstream/main --oneline -1
   ```

2. 将 commit id 提供给 AI 助手，AI 会：
   - 对比翻译前的原始版本与最新版本
   - 识别所有新增、修改、删除的内容
   - 将差异翻译并应用到中文版本

### 方法二：查看多个 commit 的变化

如果有多个 commit 需要同步，只需提供**最新的 commit id**即可。AI 会对比翻译前的原始版本与最新版本，自动捕获所有累积的变化。

### 方法三：手动同步

1. 获取上游原始版本（翻译前）：
   ```bash
   git show 95fb437:README.md > /tmp/original.md
   ```

2. 获取上游最新版本：
   ```bash
   git show <latest-commit>:README.md > /tmp/latest.md
   ```

3. 对比差异：
   ```bash
   diff /tmp/original.md /tmp/latest.md
   ```

4. 将差异内容翻译并应用到中文版本

## 注意事项

1. **不要直接 merge 上游**：由于译文与原文差异大，直接 merge 会产生大量冲突

2. **保持翻译基准版本不变**：`95fb437` 是翻译前的原始版本，用于对比差异的基准，不要修改

3. **更新本文件**：每次同步后，请更新"当前状态"表格中的 commit id 和同步时间

4. **记录同步历史**：在"同步历史"部分记录每次同步的具体变化

## 翻译规范

- 技能名称保持英文原文
- 描述翻译为中文
- 保持 Markdown 格式不变
- 链接地址保持原样
