# AGENTS.md

This file provides guidance to agents when working with code in this repository.

## 项目性质

这是一个中文翻译仓库，fork 自上游英文仓库 [VoltAgent/awesome-openclaw-skills](https://github.com/VoltAgent/awesome-openclaw-skills)。

## 同步上游更新

**不要直接 merge 上游**：由于译文与原文差异大，直接 merge 会产生大量冲突。

### 同步步骤（详细版）

#### 步骤 1：获取上游最新 commit id

```bash
git fetch upstream
git log upstream/main --oneline -1
```

记下输出的 commit id（例如：`6ee3d5efa6d92f5c2b41bee86a3663a5ed690288`）

#### 步骤 2：查看上次同步的 commit id

打开 `SYNC.md` 文件，查看"当前状态"表格中 README.md 对应的上游 Commit。

例如当前是：`f200dd7f6cf500740ebc420da298b97c58700f78`

#### 步骤 3：对比差异

在本地获取上游两个版本的 README.md：

```bash
# 获取上次同步的版本
git show f200dd7f6cf500740ebc420da298b97c58700f78:README.md > /tmp/old_readme.md

# 获取最新版本
git show 6ee3d5efa6d92f5c2b41bee86a3663a5ed690288:README.md > /tmp/new_readme.md

# 对比差异
diff /tmp/old_readme.md /tmp/new_readme.md
```

#### 步骤 4：分析差异

diff 输出格式说明：
- `>` 开头的行 = 新增内容
- `<` 开头的行 = 删除内容
- 数字 `a` = 在某行之后添加
- 数字 `d` = 在某行之后删除
- 数字 `c` = 某行被修改

常见变更类型：
1. **新增技能**：在列表中添加新的技能条目
2. **删除技能**：从列表中移除某个技能
3. **修改内容**：更新技能的描述或链接
4. **结构调整**：添加新的章节或修改现有结构

#### 步骤 5：应用变更

1. 打开中文版 `README.md`
2. 使用搜索功能找到需要修改的位置
3. 添加新技能或删除旧技能
4. 翻译新增内容的描述（技能名称保持英文）

#### 步骤 6：更新 SYNC.md

1. 更新"当前状态"表格中的 commit id 和同步时间
2. 在"同步历史"部分添加新的同步记录

格式：
```markdown
### 2026-02-20
- 同步到 `6ee3d5efa6d92f5c2b41bee86a3663a5ed690288`
- 变更说明:
  - 新增技能: xxx, yyy
  - 删除技能: zzz
```

### 翻译规范

- 技能名称保持英文原文
- 描述翻译为中文
- 保持 Markdown 格式和链接地址不变

### 验证同步正确

1. 检查 README.md 语法正确
2. 确认所有新增技能都有中文描述
3. 确认已删除的技能不再存在

### 常见问题

**Q: 找不到要修改的位置怎么办？**
A: 使用 diff 中的行号作为参考，在中文版中搜索相关的上下文来定位。

**Q: 如何确定技能应该放在哪个类别？**
A: 参考上游版本中的顺序，保持相同的分类位置。

**Q: 技能描述怎么翻译？**
A: 翻译时保持简洁准确，使用中文常见术语。

## 关键文件

- `SYNC.md` - 追踪译文与上游 commit 的对应关系
- `README.md` - 主翻译文件（约 40 万字符）
- `CONTRIBUTING.md` - 贡献指南翻译
