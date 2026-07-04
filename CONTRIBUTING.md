# 贡献于精选 OpenClaw 技能

这是一个精选的 OpenClaw 技能列表。我们整理发布在 [ClawHub](https://clawhub.ai)（OpenClaw 的公共技能注册表）上的技能链接。

> 此仓库只是一个精选的链接列表 — 仅此而已。此处列出的每个技能**必须已经发布在** [ClawHub](https://clawhub.ai) 上。如果您的技能不在那里，我们无法接受。请先将您的技能发布到 ClawHub，然后再回来提交 PR 添加链接。

## 添加技能

### 条目格式

在 `README.md` 的相应分类末尾添加您的技能：

```markdown
- [skill-name](https://clawhub.ai/author/skill-name) - 简短描述它的功能。
```

如果同一作者在同一领域有多个技能，请不要逐个添加。相反，链接到最具代表性的技能并写一段通用描述。这样可以保持列表整洁，避免不必要的杂乱。

### 添加位置

- 在 `README.md` 中找到匹配的分类，在该部分末尾添加您的条目。
- 如果没有合适的分类，添加到最接近的分类，或在 PR 描述中建议一个新分类。

### 要求

- **技能必须已经发布在 [ClawHub](https://clawhub.ai)（OpenClaw 的公共技能注册表）上。** 我们不接受托管在其他地方的技能 — 不接受个人仓库、gist 或外部链接。如果它不在 ClawHub 上，就不属于这里。
- **技能在 ClawHub 上的测试必须通过**，且安全状态必须是干净的（未被标记为可疑）。
- 有文档（SKILL.md）
- 描述必须简洁 — 10 个词以内
- 技能必须有真实的社区使用量。我们专注于社区采用的、经过验证的技能，这些技能由开发团队发布并在实际使用中得到验证。不接受全新的技能 — 在提交之前，请给您的技能时间成熟并获得用户。
- 暂不接受加密货币、区块链、DeFi 或金融相关的技能

### PR 描述

在 PR 描述中包含您技能的 ClawHub 链接，例如：
- `https://clawhub.ai/steipete/slack`

### PR 标题

`Add skill: author/skill-name`

## 更新现有条目

- 通过 PR 修复失效链接、错别字或过时的描述
- 如果技能已被移除或弃用，请提交 issue 或提交 PR 将其移除

## 安全策略

我们只包含在 [ClawHub](https://www.clawhub.ai/) 上安全状态**未被标记为可疑**的技能。在 ClawHub 上被标记为可疑的技能不会被接受到此列表中。

如果您认为此列表中的某个技能存在安全问题或应该被标记，请[提交 issue](https://github.com/VoltAgent/awesome-clawdbot-skills/issues)，以便我们审核并将其移除。

## 重要事项

- 此仓库仅整理链接。每个技能都位于 ClawHub（OpenClaw 的公共技能注册表）上。
- 技能条目链接到技能的 ClawHub 页面 `https://clawhub.ai/author/skill-name`。在您的 PR 中分享相同的 ClawHub 页面，以便我们验证它已发布。
- **不要提交指向 `https://clawskills.sh/` URL 的链接。** 始终使用 ClawHub 链接（`https://clawhub.ai/author/skill-name`）。clawskills.sh 的列表由我们单独管理和部署 — 您不需要在那里添加任何内容。
- 提交前请验证链接可用。
- 我们会审核所有提交，可能会拒绝未达到质量标准的技能。
- 不要提交与现有条目功能相同的重复技能。

## 帮助

- 先查看现有的 [issues](https://github.com/VoltAgent/awesome-openclaw-skills/issues) 和 PR
- 有疑问时提交新 issue
- 访问技能的 SKILL.md 获取特定技能的帮助
