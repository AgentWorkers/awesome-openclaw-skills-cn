# 译文同步追踪

本文件用于追踪中文译文与上游仓库的对应关系。

## 当前状态

| 文件            | 上游 Commit                                | 同步时间   |
| --------------- | ------------------------------------------ | ---------- |
| README.md       | `6ee3d5efa6d92f5c2b41bee86a3663a5ed690288` | 2026-02-20 |
| CONTRIBUTING.md | `ce7b4e400ef794bddce66eb64719dd7550b23101` | 2026-02-14 |

## 上游仓库信息

- **仓库地址**: https://github.com/VoltAgent/awesome-openclaw-skills

## 同步历史

### 2026-02-20
- 同步到 `6ee3d5efa6d92f5c2b41bee86a3663a5ed690288`
- 变更说明:
  - 更新安全通知 (Security Notice) 部分，添加更详细的安全警告和推荐工具
  - 新增技能:
    - `eachlabs-face-swap` - 使用 EachLabs AI 进行图像换脸
    - `eachlabs-fashion-ai` - 生成时尚图像、虚拟试穿、秀场视频
    - `eachlabs-image-edit` - 使用 200+ AI 模型编辑、转换、放大图像
    - `eachlabs-image-generation` - 使用 Flux、GPT Image、Gemini、Imagen 生成图像
    - `eachlabs-video-edit` - 编辑视频，包括唇形同步、翻译、字幕
    - `eachlabs-video-generation` - 使用 AI 模型从文本/图像生成视频
    - `eachlabs-music` - 使用 Mureka AI 生成歌曲、配乐、歌词、播客
    - `eachlabs-voice-audio` - 使用 ElevenLabs、Whisper、RVC 进行语音合成、语音识别、声音转换
    - `eachlabs-product-visuals` - 生成电商产品摄影和视频
    - `desearch` - 通过 Desearch 进行 Web、X、AI 搜索和页面抓取
    - `goodreads` - 搜索书籍、获取评论并管理阅读列表
    - `redline` - 针对 Claude.ai 和 OpenAI 的实时速率限制感知
    - `criticaster` - 查找具有综合评论的产品，标准化为单一评分
  - 删除技能: `agentledger`, `skillguard`

### 2026-02-19
- 同步到 `f200dd7f6cf500740ebc420da298b97c58700f78`
- 变更说明:
  - 删除技能: `deeps`, `gorger`, `ouyang` (ttboy 的技能被移除)
  - 新增技能: `openclaw-validate` - AI 代理响应的实时人工评估基准

### 2026-02-18
- 同步到 `030c62d60c942e2fd614992893ade8f0df246d86`
- 变更说明:
  - README.md 和 CONTRIBUTING.md 无变化
  - 上游仅进行了 skills 目录下的文件操作（创建、重命名、删除 skill.md/SKILL.md）

### 2026-02-17
- 同步到 `7483209cfb71f5e7d8259b8b4c8b9864058b779d`
- 新增技能:
  - `capmetro-skill` - 奥斯汀 CapMetro 公交实时查询
  - `openclaw-backup-safe` - 加固的 OpenClaw 备份和安全恢复回滚

### 2026-02-16
- 同步到 `e4f76b7cc09399eaf52a8a0acfd0bc6271efd1f2`
- 新增技能:
  - `token-panel-ultimate` - 实时追踪 AI 使用情况
  - `agent-memory-ultimate` - 生产级内存系统
  - `whatsapp-ultimate` - 完整 WhatsApp 集成
  - `appraisal-ai` - 房地产评估报告
  - `agent-boundaries-ultimate` - 安全与伦理框架
  - `shell-security-ultimate` - Shell 命令安全分类

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
