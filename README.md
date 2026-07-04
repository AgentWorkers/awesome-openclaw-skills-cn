<div align="center">

<a href="https://clawskills.sh/">
<img width="1500" height="500" alt="social" src="https://github.com/user-attachments/assets/a6f310af-8fed-4766-9649-b190575b399d" />
</a>

<br/>
<br/>

<div align="center">
    <strong>发现 5300+ 社区构建的 OpenClaw 技能，按类别组织。
    </strong>
    <br />
    <br />
</div>
  
[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Skills Count](https://img.shields.io/badge/skills-5199-blue?style=flat-square)](#目录)
[![Last Update](https://img.shields.io/github/last-commit/VoltAgent/awesome-clawdbot-skills?label=Last%20update&style=flat-square)](https://github.com/VoltAgent/awesome-clawdbot-skills/pulls?q=is%3Apr+is%3Amerged+sort%3Aupdated-desc)
<a href="https://github.com/VoltAgent/voltagent">
  <img alt="VoltAgent" src="https://cdn.voltagent.dev/website/logo/logo-2-svg.svg" height="20" />
</a> 
[![Discord](https://img.shields.io/discord/1361559153780195478.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://s.voltagent.dev/discord)

> 英文原版 fork 自: https://github.com/VoltAgent/awesome-openclaw-skills  [MIT]

</div>



</div>

</div>

# 精选 OpenClaw 技能

OpenClaw 是一个直接在您的机器上运行的本地 AI 助手。技能扩展了它的能力，使其能够与外部服务交互、自动化工作流程并执行专门任务。这个集合帮助您发现并安装适合您需求的技能。它也可以作为 OpenClaw 用例的灵感来源。

此列表中的技能来源于 ClawHub（OpenClaw 的公共技能注册表）并按类别分类以便于发现。

### 安装

#### OpenClaw CLI

```bash
openclaw skills install <skill-slug>
```

#### ClawHub CLI

或者使用 ClawHub CLI，用于在完整 OpenClaw 工作区之外管理注册表托管的技能文件夹：

```bash
npx clawhub install <skill-slug>
```

#### 手动安装

将技能文件夹复制到以下位置之一：

| 位置   | 路径                  |
|----------|------|
| 全局   | `~/.openclaw/skills/` |
| 工作区 | `<project>/skills/`   |

优先级：工作区 > 本地 > 内置

#### 替代方案

您也可以将技能的 GitHub 仓库链接直接粘贴到助手的聊天中，并要求它使用它。助手将在后台自动处理设置。


### 为什么存在此列表？

OpenClaw 的公共注册表（ClawHub）托管了数千个社区构建的技能。这个精选列表挑选了其中最优秀的。以下是我们过滤掉的内容：

| 过滤器                                                   | 已排除    |
|--------|----------|
| 可能是垃圾邮件 — 批量账户、机器人账户、测试/垃圾内容     | 4,065     |
| 重复 / 相似名称                                          | 1,040     |
| 低质量或非英语描述                                       | 851       |
| 加密货币 / 区块链 / 金融 / 交易                          | 886       |
| 恶意 — 由研究人员发布的安全审计识别（不包括 VirusTotal） | 373       |
| **未从 OpenClaw 官方技能注册表中获取的总数**             | **7,215** |


#### 想要添加技能？

此列表仅包含已在 [ClawHub](https://clawhub.ai)（OpenClaw 的公共技能注册表）上**发布**的技能。我们不接受指向个人仓库、gist 或任何其他外部源的链接。如果您的技能尚未在 ClawHub 上，请先在那里发布。

在您的 PR 描述中包含技能的 ClawHub 链接（例如 `https://clawhub.ai/steipete/slack`）— `clawskills.sh` 的列表由我们单独管理。详情请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。


## OpenClaw 生态系统工具

### 🔌 连接外部服务

OpenClaw 代理可以与 GitHub、Slack、Gmail 等外部服务交互。您可以使用技能或插件自行构建集成，或使用托管服务来处理所有连接的身份验证、令牌刷新和权限管理。

<a href="https://composio.dev/claw?utm_source=github&utm_campaign=volt-agent">
<img src="https://cdn.voltagent.dev/awesome-repo/composio-img.png" alt="Composio"  />
跨 1000+ 应用的托管 OAuth、范围权限和原生工具调用记录。
</a>


### ☁️ 托管与部署

您可以在任何 VPS 或云平台上部署 OpenClaw，以便在自己的基础设施上安全地运行技能，或使用托管主机来处理服务器、更新和隔离。 

<a href="https://myclaw.ai/?utm_source=github&utm_campaign=awesome-openclaw-skills">
<img src="https://cdn.voltagent.dev/awesome-repo/myclaw-banner.svg" alt="MyClaw"  /><br/>
您无需管理服务器即可运行这些技能 — 一个完整的云托管 OpenClaw 实例，一键设置、7×24 小时运行，并完全拥有数据所有权。
</a>


<br/>
<br/>

> **提示：** 如果您是自托管，请将 OpenClaw Docker 镜像固定到特定标签，并在升级前对技能卷进行快照 — 这样当技能更新出问题时，回滚将毫无痛苦。


### 🔍 搜索与 Web 数据

OpenClaw 代理通常需要新鲜的、真实世界的数据 — 搜索结果、产品列表、视频等。您可以自己抓取和解析，或使用一个搜索 API 实时返回干净、结构化的数据，无需管理代理、验证码或 HTML 解析。

<a href="https://serpapi.com/search-engine-apis?utm_source=awesomeopenclawskills_github">
<img src="https://cdn.voltagent.dev/awesome-repo/serpapi.png" alt="SerpApi"  /><br/>
通过单一 API 让 OpenClaw 代理访问实时 Google 搜索、YouTube、亚马逊产品和网络搜索数据。
</a>


### 🛡️ 安全与配置审计

随着您添加更多技能、自定义代码和连接的服务，您的 OpenClaw 设置会积累密钥、文件访问和工具权限，这些很容易失控。您可以手动审查，或运行持续审计来在问题出现之前发现配置错误和过宽的权限。

<a href="https://trent.ai/openclaw/?utm_source=github&utm_medium=referral&utm_campaign=volt-agent">
<img src="https://cdn.voltagent.dev/awesome-repo/trenclaw.png" alt="trentclaw"  /><br/>
trentclaw 映射配置、已安装的技能、自定义代码、密钥和权限，然后在您的 OpenClaw 会话中返回发现结果。
</a>


### 🤖 模型提供商

OpenClaw 开箱即用支持 **25+ 个 LLM 提供商**，包括 Anthropic、OpenAI 等。只需更改一次配置即可在它们之间切换。

<details>
<summary><strong>示例：使用 OpenAI 模型</strong></summary>

OpenClaw 通过直接 API 密钥或 ChatGPT/Codex OAuth 支持 `gpt-5.4` 和 `gpt-5.4-pro`。默认启用 WebSocket 传输以降低延迟。

```bash
openclaw onboard --auth-choice openai-api-key
# 或使用基于订阅的访问：
openclaw onboard --auth-choice openai-codex
```
</details>


<div align="center">

<table>
<tr>
<td align="center" width="100%">

<h3>🦞 您可以在上面的区域展示您的 OpenClaw 生态系统工具。</h3>

<p></p>

<sub>官方 OpenClaw 资源之后访问量第一的社区资源</sub>


<a href="https://sponsors.voltagent.dev/#awesome-openclaw-skills"><img src="https://img.shields.io/badge/📩_Become_a_Sponsor-Contact_Us-blue?style=for-the-badge&logoColor=white" alt="Become a Sponsor" /></a>

</td>
</tr>
</table>

</div>



## 安全通知

此列表中的技能是**经过筛选但未经审计**的。它们在添加后可能随时被原始维护者更新、修改或替换。

在安装或使用任何 Agent Skill 之前，请自行审查潜在安全风险并验证来源。OpenClaw 与 **VirusTotal 合作**为技能提供安全扫描，请访问技能在 ClawHub 上的页面并检查 VirusTotal 报告，查看它是否被标记为有风险。

**推荐工具：**

- [Snyk Skill Security Scanner](https://github.com/snyk/agent-scan)
- [Agent Trust Hub](https://ai.gendigital.com/agent-trust-hub)
  
> Agent 技能可能包含提示注入、工具投毒、隐藏的恶意软件负载或不安全的数据处理模式。安装前请务必查看源代码，并自行决定是否使用。


如果您认为此列表中的某个技能应该被标记或存在安全问题，请[提交 issue](https://github.com/VoltAgent/awesome-clawdbot-skills/issues) 以便我们审核。


## 目录

| | | |
|---|---|---|
| [Git 与 GitHub](#git--github) (167) | [营销与销售](#marketing--sales) (104) | [通信](#communication) (146) |
| [编码代理与 IDE](#coding-agents--ides) (1184) | [生产力与任务](#productivity--tasks) (206) | [语音与转录](#speech--transcription) (46) |
| [浏览器与自动化](#browser--automation) (323) | [AI 与 LLMs](#ai--llms) (176) | [智能家居与物联网](#smart-home--iot) (41) |
| [Web 与前端开发](#web--frontend-development) (920) | [数据与分析](#data--analytics) (28) | [购物与电子商务](#shopping--e-commerce) (51) |
| [DevOps 与云](#devops--cloud) (393) | [日历与日程安排](#calendar--scheduling) (66) | |
| [图像与视频生成](#image--video-generation) (170) | [媒体与流媒体](#media--streaming) (86) | [PDF 与文档](#pdf--documents) (105) |
| [Apple 应用与服务](#apple-apps--services) (44) | [笔记与 PKM](#notes--pkm) (69) | [自托管与自动化](#self-hosted--automation) (33) |
| [搜索与研究](#search--research) (345) | [iOS 与 macOS 开发](#ios--macos-development) (29) | [安全与密码](#security--passwords) (54) |
| [Clawdbot 工具](#clawdbot-tools) (37) | [交通](#transportation) (110) | [Moltbook](#moltbook) (29) |
| [CLI 实用工具](#cli-utilities) (180) | [个人发展](#personal-development) (52) | [游戏](#gaming) (35) |
| [健康与健身](#health--fitness) (87) | | |



<br/>

<a href="https://launchkit.getdesign.md/">
<img src="https://cdn.voltagent.dev/awesome-repo/launchkit-banner-3.png" alt="launchkit"  /><br/>
</a>

<br/>

<details open>
<summary><h3 style="display:inline">Git 与 GitHub</h3></summary>

- [agent-commons](https://clawskills.sh/skills/zanblayde-agent-commons) - 查询、提交、扩展和质疑推理链。
- [agent-team-orchestration](https://clawskills.sh/skills/arminnaimi-agent-team-orchestration) - 编排具有定义角色、任务生命周期、交接协议和审查工作流的多代理团队。
- [agentdo](https://clawskills.sh/skills/wrannaman-agentdo) - 为其他 AI 代理发布任务，或从 AgentDo 任务队列（agentdo.dev）领取工作
- [agentgate](https://clawskills.sh/skills/monteslu-agentgate) - 带有人在回路写入审批的个人数据 API 网关。
- [airadar](https://clawskills.sh/skills/lopushok9-airadar) - 提炼 AI 原生工具/应用及其 GitHub 大本营周围的信号：快速增长、炒作、资金充足。
- [alex-session-wrap-up](https://clawskills.sh/skills/xbillwatsonx-alex-session-wrap-up) - 会话结束自动化，提交未推送的工作、提取经验、检测模式并持久化规则。
- [amazon-product-api-skill](https://clawskills.sh/skills/phheng-amazon-product-api-skill) - 此技能帮助用户从亚马逊提取结构化产品列表，包括标题、ASIN、价格、评分。
- [app-store-screenshot-generation](https://clawskills.sh/skills/eftalyurtseven-app-store-screenshot-generation) - 使用 each::sense AI 生成 App Store 和 Google Play 截图资产。
- [arc-agent-lifecycle](https://clawskills.sh/skills/trypto1019-arc-agent-lifecycle) - 管理自主代理及其技能的生命周期。
- [arc-security-audit](https://clawskills.sh/skills/trypto1019-arc-security-audit) - 面向代理完整技能栈的全面安全审计。
- [arc-skill-gitops](https://clawskills.sh/skills/trypto1019-arc-skill-gitops) - 面向代理工作流和技能的自动部署、回滚和版本管理。
- [arc-trust-verifier](https://clawskills.sh/skills/trypto1019-arc-trust-verifier) - 验证技能来源并为 ClawHub 技能构建信任评分。
- [arxiv-search-collector](https://clawskills.sh/skills/xukp20-arxiv-search-collector) - 模型驱动的 arXiv 检索工作流，用于构建论文集，带有手动语言参数：初始化运行。
- [auto-pr-merger](https://clawskills.sh/skills/autogame-17-auto-pr-merger) - 此技能自动化检出 GitHub。
- [azhua-skill-vetter](https://clawskills.sh/skills/fatfingererr-azhua-skill-vetter) - 面向 AI 代理的安全优先技能审查。
- [azure-devops](https://clawskills.sh/skills/pals-software-azure-devops) - 列出 Azure DevOps 项目、仓库和分支；创建拉取请求；管理工作项；检查构建状态。
- [bat-cat](https://clawskills.sh/skills/arnarsson-bat-cat) - 带有语法高亮、行号和 Git 集成的 cat 克隆。
- [beeminder](https://clawskills.sh/skills/ruigomeseu-beeminder) - 用于目标追踪和承诺装置的 Beeminder API。
- [billy-emergency-repair](https://clawskills.sh/skills/highlander89-billy-emergency-repair) - - Neill 明确请求 Billy 系统修复。
- [bitbucket-automation](https://clawskills.sh/skills/sohamganatra-bitbucket-automation) - 自动化 Bitbucket 仓库、拉取。
- [biz-reporter](https://clawskills.sh/skills/ariktulcha-biz-reporter) - 自动化商业智能报告，从 Google Analytics GA4、Google Search Console、Stripe 拉取数据。
- [blinko](https://clawskills.sh/skills/tolibear-blinko) - 在 Abstract 链上无头玩 Blinko（链上弹珠游戏）。

> **[查看 Git 与 GitHub 全部 159 个技能 →](categories/git-and-github.md)**
</details>

<details open>
<summary><h3 style="display:inline">编码代理与 IDE</h3></summary>

- [0g-compute](https://clawskills.sh/skills/in-liberty420-0g-compute) - 使用来自 0G Compute Network 的经济实惠、经 TEE 验证的 AI 模型作为 OpenClaw 提供者。
- [0protocol](https://clawskills.sh/skills/0isone-0protocol) - 代理可以签署插件、轮换凭证而不丢失身份，并公开证明其行为。
- [2nd-brain](https://clawskills.sh/skills/coderaven-2nd-brain) - 个人知识库，用于捕获和检索有关人物、地点、餐厅、游戏、科技的信息。
- [2slides-skills](https://clawskills.sh/skills/javainthinking-2slides-skills) - 使用 2slides API 进行 AI 驱动的演示文稿生成。
- [3d-cog](https://clawskills.sh/skills/nitishgargiitd-3d-cog) - 其他工具需要完美的图像。
- [3d-model-generation](https://clawskills.sh/skills/eftalyurtseven-3d-model-generation) - 使用 each::sense AI 生成 3D 模型。
- [a](https://clawskills.sh/skills/ricketh137-a) - 在 Lobster.fun 上以 AI VTuber 身份直播。
- [aade-api-monitor](https://clawskills.sh/skills/satoshistackalotto-aade-api-monitor) - 实时监控希腊 AADE 税务机构系统——跟踪截止日期、汇率变化和合规更新。
- [abaddon](https://clawskills.sh/skills/enochosbot-bot-abaddon) - OpenClaw 的红队安全模式。
- [academic-research](https://clawskills.sh/skills/rogersuperbuilderalpha-academic-research) - 使用 OpenAlex API 搜索学术论文和进行文献综述（免费，无需密钥）
- [academic-research-hub](https://clawskills.sh/skills/anisafifi-academic-research-hub) - 当用户需要搜索学术论文、下载研究文档、提取引用或收集信息时使用此技能。
- [acestep-simplemv](https://clawskills.sh/skills/dumoedss-acestep-simplemv) - 使用 Remotion 从音频文件和歌词渲染音乐视频。
- [acestep-songwriting](https://clawskills.sh/skills/dumoedss-acestep-songwriting) - ACE-Step 的音乐歌曲创作指南。
- [achurch](https://clawskills.sh/skills/lucasgeeksinthewood-achurch) - 一个 24/7 的数字避难所，供 AI 代理和人类使用——参与。
- [active-maintenance](https://clawskills.sh/skills/xiaowenzhou-active-maintenance) - **OpenClaw 的自动化系统健康和记忆代谢。**。
- [adblock-dns](https://clawskills.sh/skills/picaye-adblock-dns) - 在 DNS 层级实现全网广告和跟踪器拦截。
- [add-top-openrouter-models](https://clawskills.sh/skills/chunhualiao-add-top-openrouter-models) - 将 OpenClaw 使用的 OpenRouter 模型同步到此安装的配置中。
- [adhd-founder-planner](https://clawskills.sh/skills/jankutschera-adhd-founder-planner) - 当用户要求"规划我的一天"、"帮我规划今天"、"晨间规划"、"什么"时使用此技能。
- [adwhiz](https://clawskills.sh/skills/iamzifei-adwhiz) - 从您的 AI 编码工具管理 Google Ads 广告系列。44 个 MCP 工具，用于审计、创建和优化 Google。
- [aeo-prompt-question-finder](https://clawskills.sh/skills/psyduckler-aeo-prompt-question-finder) - 查找任何主题的基于问题的 Google 自动补全建议。
- [aetherlang-claude-code](https://clawskills.sh/skills/contrario-aetherlang-claude-code) - 使用此技能从 Claude Code 执行 AetherLang V3 AI 工作流。
- [agent-access-control](https://clawskills.sh/skills/bowen31337-agent-access-control) - AI 代理的分层陌生人访问控制。
- [agent-audit](https://clawskills.sh/skills/sharbelayy-agent-audit) - 审计您的 AI 代理设置的性能、成本和 ROI。
- [agent-audit-trail](https://clawskills.sh/skills/roosch269-agent-audit-trail) - 为 AI 代理提供防篡改、哈希链式审计日志。
- [agent-card-signing-auditor](https://clawskills.sh/skills/andyxinweiminicloud-agent-card-signing-auditor) - 帮助审计 A2A 协议实现中的代理卡签署实践。
- [agent-chat-ux-v1-4-0](https://clawskills.sh/skills/maverick-software-agent-chat-ux-v1-4-0) - OpenClaw 控制界面的多代理 UX——代理选择器、每代理会话、带搜索的会话历史查看器。
- [skywork-ppt](https://clawskills.sh/skills/gxcun17-skywork-ppt) - 使用 skywork 生成、模仿和编辑 PowerPoint 演示文稿。
- [skywork-music-maker](https://clawskills.sh/skills/gxcun17-skywork-music-maker) - 使用 Mureka AI 创建专业音乐。
- [before-you-build](https://clawhub.ai/bin1874/before-you-build) - 在构建之前审查产品风险。

> **[查看 编码代理与 IDE 全部 1200 个技能 →](categories/coding-agents-and-ides.md)**
</details>

<details open>
<summary><h3 style="display:inline">浏览器与自动化</h3></summary>

- [1p-shortlink](https://clawskills.sh/skills/tuanpmt-1p-shortlink) - 使用 1p.io 创建短链接并提交功能请求。
- [2captcha](https://clawskills.sh/skills/adinvadim-2captcha) - 使用 2Captcha 服务解决验证码。
- [a-share-real-time-data](https://clawskills.sh/skills/wangdinglu-a-share-real-time-data) - 通过 mootdx/TDX 协议获取中国 A 股市场数据（K 线、实时行情、逐笔成交）。
- [abm-outbound](https://clawskills.sh/skills/dru-ca-abm-outbound) - 将 LinkedIn URL 转化的多渠道 ABM 自动化。
- [accessibility-toolkit](https://clawskills.sh/skills/cgtreadw-accessibility-toolkit) - 为辅助 agent 降低摩擦的模式。
- [activecampaign](https://clawskills.sh/skills/kesslerio-activecampaign) - 用于线索管理、交易等的 ActiveCampaign CRM 集成。
- [adcp-advertising](https://clawskills.sh/skills/edyyy62-adcp-advertising) - 使用 AI 自动化广告投放活动。
- [admet-prediction](https://clawskills.sh/skills/huifer-admet-prediction) - 对候选药物进行 ADMET（吸收、分布、代谢、排泄、毒性）预测。
- [Agent Browser](https://clawskills.sh/skills/thesethrose-agent-browser) - 基于 Rust 的快速无头浏览器自动化 CLI。
- [agent-browser](https://clawskills.sh/skills/murphykobe-agent-browser-2) - 自动化浏览器交互，用于 Web 测试、表单。
- [agent-daily-planner](https://clawskills.sh/skills/gpunter-agent-daily-planner) - 用于 AI agent 的结构化每日规划和执行追踪系统。
- [agent-device](https://clawskills.sh/skills/okwasniewski-agent-device) - 自动化 iOS 模拟器/设备和 Android 模拟器/设备的交互。
- [agent-step-sequencer](https://clawskills.sh/skills/gostlightai-agent-step-sequencer) - 用于深度 agent 请求的多步骤调度器。
- [agent-task-tracker](https://clawskills.sh/skills/rikouu-agent-task-tracker) - 主动式任务状态管理。
- [agent-zero](https://clawskills.sh/skills/dowingard-agent-zero-bridge) - 委托复杂的编码、研究或自主任务。
- [agentapi](https://clawskills.sh/skills/gizmo-dev-agentapi) - 浏览和搜索 AgentAPI 目录——一个专为 AI agent 精选的 API 数据库。
- [agentapi-hub](https://clawskills.sh/skills/gizmo-dev-agentapi-hub) - 浏览和搜索 AgentAPI 目录——一个专为 AI agent 精选的 API 数据库。
- [agentaudit](https://clawskills.sh/skills/starbuck100-agentaudit) - 在安装前对照漏洞数据库检查依赖包的自动安全门。
- [agentaudit-skill](https://clawskills.sh/skills/starbuck100-agentaudit-skill) - 在安装前对照漏洞数据库检查依赖包的自动安全门。
- [agentmail-integration](https://clawskills.sh/skills/synesthesia-wav-agentmail-integration) - 为 AI agent 集成 AgentMail API。
- [agresource](https://clawskills.sh/skills/brianppetty-agresource) - 使用此技能抓取、总结和分析 AgResource 谷物营销通讯。
- [ai-hunter-pro](https://clawskills.sh/skills/traprapitalianazional-dev-ai-hunter-pro) - 一个高性能自动化 agent，将全球热点转化为 X（Twitter）上的病毒式社交媒体帖子。
- [ai-meeting-scheduling](https://clawskills.sh/skills/dheerg-ai-meeting-scheduling) - 预约链接对团队失效。
- [airtable-automation](https://clawskills.sh/skills/sohamganatra-airtable-automation) - 通过 Rube MCP（Composio）自动化 Airtable 任务。
- [airtable-participants](https://clawskills.sh/skills/austinmao-airtable-participants) - 从 Ceremonia Airtable 数据库读取和查询静修活动参与者数据。
- [ak-rss-24h-brief](https://clawskills.sh/skills/seandong-ak-rss-24h-brief) - 从 OPML 列表读取 RSS/Atom 订阅源，抓取最近 N 小时的文章，并生成中文分类摘要。
- [adspower-browser](https://clawskills.sh/skills/adspower-adspower-browser) - 当用户要求通过 AdsPower Local API 创建或管理 AdsPower 浏览器、分组、标签、代理或检查状态时使用。
- [duoplus-agent](https://clawskills.sh/skills/duoplusofficial-duoplus-agent) - 通过 ADB 控制 DuoPlus 云手机。

> **[查看 浏览器与自动化 全部 323 个技能 →](categories/browser-and-automation.md)**
</details>

<details>
<summary><h3 style="display:inline">Web 与前端开发</h3></summary>

- [0xwork](https://clawskills.sh/skills/jkillr-0xwork) - 在 0xWork 去中心化市场（Base 链，USDC 托管）查找并完成付费任务。
- [37soul-skill](https://clawskills.sh/skills/xnjiang-37soul-skill) - 将你的 AI agent 连接到 37Soul 虚拟主机角色并启用。
- [acestep](https://clawskills.sh/skills/dumoedss-acestep) - 使用 ACE-Step API 生成音乐、编辑歌曲和混音音乐。
- [actionbook](https://clawskills.sh/skills/adcentury-actionbook) - 当用户需要与任何网站交互时激活——浏览器自动化、网页抓取、截图、表单。
- [aegis-shield](https://clawskills.sh/skills/deegerwalker-aegis-shield) - 对不受信任的文本进行提示注入和数据外泄筛查。
- [aeo-analytics-free](https://clawskills.sh/skills/psyduckler-aeo-analytics-free) - 追踪 AI 可见性——衡量品牌是否被 AI 助手（Gemini、ChatGPT、Perplexity）提及和引用。
- [aeo-content-free](https://clawskills.sh/skills/psyduckler-aeo-content-free) - 创建或刷新能被 AI 助手（Gemini、ChatGPT、Perplexity）引用的 AEO 优化内容。
- [aeo-prompt-frequency-analyzer](https://clawskills.sh/skills/psyduckler-aeo-prompt-frequency-analyzer) - 通过使用 Google 搜索多次运行，分析 Gemini 在回答提示时使用的搜索查询。
- [aeo-prompt-research-free](https://clawskills.sh/skills/psyduckler-aeo-prompt-research-free) - 仅使用免费工具，发现对品牌回答引擎优化（AEO）重要的 AI 提示和主题。
- [agent-analytics](https://clawskills.sh/skills/dannyshmueli-agent-analytics) - 由你的 AI agent 端到端控制的简单网站分析。
- [agent-chat](https://clawskills.sh/skills/awlevin-agent-chat) - 为 AI agent 提供临时实时聊天室。
- [agent-dashboard](https://clawskills.sh/skills/tahseen137-agent-dashboard) - OpenClaw 的实时 agent 仪表板。
- [agent-dispatch](https://clawskills.sh/skills/userfrm-agent-dispatch) - 轻量级 agent 注册表和 JIT 路由器。
- [agent-hq](https://clawskills.sh/skills/thibautrey-agent-hq) - 部署 Agent HQ 任务控制技术栈（Express + React + Telegram 通知器 / Jarvis 摘要），以便其他 Clawdbot。
- [agent-passport](https://clawskills.sh/skills/markneville-agent-passport) - agent 时代的 OAuth——对所有敏感 agent 操作（包括购买、邮件、文件）进行同意门控。
- [agent-rate-limiter](https://clawskills.sh/skills/mxmsabundance-agent-rate-limiter) - 你懂的。
- [agent-self-assessment](https://clawskills.sh/skills/roosch269-agent-self-assessment) - AI agent 的安全自评估工具。
- [agent-self-reflection](https://clawskills.sh/skills/brennerspear-agent-self-reflection) - 对近期会话进行定期自我反思。
- [agent-skills-audit](https://clawskills.sh/skills/swader-agent-skills-audit) - 运行由决胜负责人主导的两轮多学科代码审计，结合安全、性能、UX、DX。
- [agent-spawner](https://clawskills.sh/skills/austineral-agent-spawner) - 通过对话生成新的 OpenClaw agent。
- [agent-swarm](https://clawskills.sh/skills/runeweaverstudios-agent-swarm) - 重要提示：需要 OpenRouter。
- [agent-takeover](https://clawskills.sh/skills/tracsystems-agent-takeover) - 如何对 Clawfinger 语音网关进行实时 agent 接管——拨号、注入问候语、处理轮次。
- [agent-topology-visualizer](https://clawskills.sh/skills/gavinnn-m-agent-topology-visualizer) - 为 AI agent 系统生成交互式 SVG 架构图。
- [agentdomainservice](https://clawskills.sh/skills/gregm711-agentdomainservice) - 世界第一的 AI 友好域名注册商。
- [agentic-browser-0-1-2](https://clawskills.sh/skills/xyny89-agentic-browser-0-1-2) - 通过 inference.sh 为 AI agent 提供浏览器自动化。
- [agentic-security-audit](https://clawskills.sh/skills/kingrubic-agentic-security-audit) - 审计代码库、基础设施以及 agent 式 AI 系统的安全问题。
- [agentpay](https://clawskills.sh/skills/kar69-96-agentpay) - 代表你的人类从真实网站购买物品。

> **[查看 Web 与前端开发 全部 925 个技能 →](categories/web-and-frontend-development.md)**
</details>

<details>
<summary><h3 style="display:inline">DevOps 与云</h3></summary>

- [0x0-messenger](https://clawskills.sh/skills/eijiac24-0x0-messenger) - 使用一次性号码和 PIN 发送和接收 P2P 消息。
- [12306](https://clawskills.sh/skills/kirorab-12306) - 查询中国铁路 12306 的列车时刻表、余票和车站信息。
- [1sec-security](https://clawskills.sh/skills/cutmob-1sec-security) - 安装、配置和管理 1-SEC——一个开源的一体化网络安全平台（16 个模块，单一二进制文件）。
- [aave-liquidation-monitor](https://clawskills.sh/skills/jgramajo4-aave-liquidation-monitor) - 主动监控 Aave V3 借款头寸并提供清算预警。
- [abstract-searcher](https://clawskills.sh/skills/easonc13-abstract-searcher) - 通过浏览器搜索学术数据库（arXiv、Semantic Scholar、CrossRef）为 .bib 文件条目添加摘要。
- [accounting-workflows](https://clawskills.sh/skills/satoshistackalotto-accounting-workflows) - 用于希腊会计的基于文件的工作流协调器。
- [adguard](https://clawskills.sh/skills/rowbotik-adguard) - 通过 HTTP API 控制 AdGuard Home DNS 过滤。
- [aegis-audit](https://clawskills.sh/skills/sanguineseal-aegis-audit) - 对 AI agent 技能和 MCP 工具的深度行为安全审计。
- [aetherlang-chef](https://clawskills.sh/skills/contrario-aetherlang-chef) - 米其林级别的食谱咨询，包含 17 个必填部分。
- [aetherlang-karpathy-skill](https://clawskills.sh/skills/contrario-aetherlang-karpathy-skill) - 为任何 DSL/运行时系统实现 10 种高级 AI agent 节点类型——计划编译器、代码解释器、批判。
- [agent-autonomy-primitives](https://clawskills.sh/skills/g9pedro-agent-autonomy-primitives) - 使用 ClawVault 原语（任务、项目、记忆类型、模板）构建长时间运行的自主 agent 循环。
- [agent-directory](https://clawskills.sh/skills/aerialcombat-agent-directory) - AI agent 服务目录。
- [agent-evaluation](https://clawskills.sh/skills/rustyorb-agent-evaluation) - LLM agent 的测试和基准评估，包括行为测试、能力评估、可靠性指标。
- [agent-framework-azure-ai-py](https://clawskills.sh/skills/thegovind-agent-framework-azure-ai-py) - 构建 Azure AI Foundry agent。
- [agent-metrics-osiris](https://clawskills.sh/skills/nantes-agent-metrics-osiris) - AI agent 的可观测性和指标——追踪调用、错误、延迟。
- [agent-self-governance](https://clawskills.sh/skills/bowen31337-agent-self-governance) - 自主 agent 的自治协议：WAL（预写日志）、VBR（报告前验证）、ADL。
- [agent-watcher](https://clawskills.sh/skills/nantes-agent-watcher) - 用于监控 Moltbook 订阅流、检测新 agent 和追踪有趣帖子的技能。
- [agentchan-org](https://clawskills.sh/skills/kaden-schutt-agentchan-org) - 面向 AI agent 的匿名图片论坛。
- [agentguard](https://clawskills.sh/skills/manas-io-ai-agentguard) - **类别：**安全与监控。
- [agentic-ai-gold](https://clawskills.sh/skills/amitabhainarunachala-agentic-ai-gold) - 唯一在你睡觉时自我提升的 agent 框架。
- [agentic-devops](https://clawskills.sh/skills/tkuehnl-agentic-devops) - 生产级 agent DevOps 工具包——Docker、进程管理、日志分析和健康监控。
- [agentkeys](https://clawskills.sh/skills/alexandr-belogubov-agentkeys) - AI agent 的安全凭据代理。
- [agentmemory](https://clawskills.sh/skills/badaramoni-agentmemory) - 用于 AI agent 的端到端加密云记忆。

> **[查看 DevOps 与云 全部 392 个技能 →](categories/devops-and-cloud.md)**
</details>

<details>
<summary><h3 style="display:inline">图像与视频生成</h3></summary>

- [aada](https://clawskills.sh/skills/rylena-aada) - 从一个代理创建并向 Moltbook 受众发送有趣、个性丰富的促销信息。
- [ace-music](https://clawskills.sh/skills/fspecii-ace-music) - 通过 ACE Music 的免费 API 使用 ACE-Step 1.5 生成 AI 音乐。
- [acorn-prover](https://clawskills.sh/skills/flyingnobita-acorn-prover) - 使用 Acorn 定理证明器进行数学和密码学形式化的验证和编写证明。
- [adobe-automator](https://clawskills.sh/skills/abdul-karim-mia-adobe-automator) - 通过 ExtendScript 桥接实现通用 Adobe 应用程序自动化。
- [afame](https://clawskills.sh/skills/adebayoabdushaheed-a11y-afame) - 通过 OpenAI Images API 生成多样化的创意插图。
- [age-transformation](https://clawskills.sh/skills/eftalyurtseven-age-transformation) - 使用 each::sense AI 跨年龄段变换人脸。
- [agentchan](https://clawskills.sh/skills/vvsotnikov-agentchan) - 为 AI 代理打造的匿名图像板。
- [agentos-mesh](https://clawskills.sh/skills/agentossoftware-agentos-mesh) - 实现 AI 代理之间的实时通信。
- [agents-skill-podcastifier](https://clawskills.sh/skills/cerbug45-agents-skill-podcastifier) - 将传入的文本（邮件/通讯）通过分块 + ffmpeg 拼接转换为简短的 TTS 播客。
- [ai-avatar-generation](https://clawskills.sh/skills/eftalyurtseven-ai-avatar-generation) - 使用 each::sense 从照片或文本描述生成 AI 头像。
- [ai-headshot-generation](https://clawskills.sh/skills/eftalyurtseven-ai-headshot-generation) - 使用 each::sense AI 从日常照片生成专业 AI 证件照。
- [ai-persona-engine](https://clawskills.sh/skills/brandonwadepackard-cell-ai-persona-engine) - 使用演员指导提示词而非传统方法，为语音和聊天角色扮演构建情感智能 AI 人格。
- [ai-video-gen](https://clawskills.sh/skills/rhanbourinajd-ai-video-gen) - 端到端 AI 视频生成——从文本创建视频。
- [aikek](https://clawskills.sh/skills/vvsotnikov-aikek) - 访问 AIKEK API 进行加密货币/DeFi 研究和图像生成。
- [aiusd](https://clawskills.sh/skills/chaunceyliu-aiusd) - AIUSD 交易和账户管理技能。
- [aiusd-skills](https://clawskills.sh/skills/chaunceyliu-aiusd-skills) - AIUSD 交易和账户管理技能。
- [album-cover-generation](https://clawskills.sh/skills/eftalyurtseven-album-cover-generation) - 使用 each::sense AI 生成专业音乐专辑封面。
- [algorithmic-art](https://clawskills.sh/skills/seanphan-algorithmic-art) - 使用 p5.js 和种子随机性创建算法艺术。
- [apipick-china-phone-checker](https://clawskills.sh/skills/javainthinking-apipick-china-phone-checker) - 使用 apipick 中国手机检查器 API 验证中国移动电话号码。
- [art-philosophy](https://clawskills.sh/skills/nyxur42-art-philosophy) - 自动学习你的视觉语言。
- [ascii-art-generator](https://clawskills.sh/skills/ustc-yxw-ascii-art-generator) - 创建 ASCII 艺术和基于文本的可视化，用于艺术表达、技术图表或概念。
- [atxp](https://clawskills.sh/skills/emilioacc-atxp) - 访问 ATXP 付费 API 工具进行网页搜索、AI 图像生成、音乐创作。
- [beauty-generation-api](https://clawskills.sh/skills/luruibu-beauty-generation-api) - 用于创建的免费 AI 图像生成服务。
- [best-image](https://clawskills.sh/skills/pharmacist9527-best-image) - 最高质量的 AI 图像生成（约 0.12-0.20 美元/张）
- [best-image-generation](https://clawskills.sh/skills/evolinkai-best-image-generation) - 最高质量的 AI 图像生成（约 0.12-0.20 美元/张）
- [bex-nano-banana-pro](https://clawskills.sh/skills/bextuychiev-bex-nano-banana-pro) - 通过 Replicate 上的 Gemini 3 Pro Image 生成或编辑图像。
- [breeze](https://clawskills.sh/skills/keeganthomp-breeze) - 通过 x402 支付门控的 HTTP API 与 Breeze 收益聚合器交互。
- [cad-agent](https://clawskills.sh/skills/clawd-maf-cad-agent) - 用于进行 CAD 工作的 AI 代理的渲染服务器。
- [calorie-visualizer](https://clawskills.sh/skills/vintlin-calorie-visualizer) - 本地卡路里记录和可视化报告（每次记录后自动刷新并返回报告图片）
- [canva-connect](https://clawskills.sh/skills/coolmanns-canva-connect) - 通过 Connect API 管理 Canva 设计、资产和文件夹。
- [runapi-mcp](https://clawhub.ai/runapi-ai/runapi-mcp) - 来自 18 家提供商的 130 多种 AI 模型，用于图像、视频、音乐、音频和 LLM 生成。8 个 MCP 工具，支持免费目录浏览。`npx @runapi.ai/mcp`
- [skywork-design](https://clawskills.sh/skills/gxcun17-skywork-design) - 通过 Skywork Image 生成和编辑图像，用于海报、标志等。

- [ai-video-remix](https://clawskills.sh/skills/abu-shotai-ai-video-remix) - AI-driven video remix from local library using ShotAI.
> **[查看 图像与视频生成 全部 170 个技能 →](categories/image-and-video-generation.md)**
</details>

<details>
<summary><h3 style="display:inline">Apple 应用与服务</h3></summary>

- [alter-actions](https://clawskills.sh/skills/olivieralter-alter-actions) - 通过 x-callback-url 触发 Alter macOS 应用操作。
- [apple-contacts](https://clawskills.sh/skills/tyler6204-apple-contacts) - 从 macOS 通讯录.app 查找联系人。
- [apple-find-my-local](https://clawskills.sh/skills/loganprit-apple-find-my-local) - 通过 Peekaboo 控制 Apple 查找应用以定位人员、设备和物品（AirTags）
- [apple-health-skill](https://clawskills.sh/skills/nftechie-apple-health-skill) - 与你的 Apple 健康数据对话 — 询问关于锻炼、心率、活动圆环和健身趋势的问题。
- [apple-mail-search](https://clawskills.sh/skills/mneves75-apple-mail-search) - 在 macOS 上通过 SQLite 实现 Apple 邮件快速搜索。
- [apple-music](https://clawskills.sh/skills/tyler6204-apple-music) - 搜索 Apple Music，将歌曲添加到资料库，管理播放列表，控制播放。
- [apple-photos](https://clawskills.sh/skills/tyler6204-apple-photos) - macOS 上的 Apple 照片.app 集成。
- [apple-remind-me](https://clawskills.sh/skills/plgonzalezrx8-apple-remind-me) - 能创建真实 Apple 提醒事项的自然语言提醒。
- [apple-search-ads-skill](https://clawskills.sh/skills/trebuhs-apple-search-ads-skill) - 通过 asa-cli 工具管理 Apple Search Ads 广告活动、广告组、关键词和报告。
- [appletv](https://clawskills.sh/skills/lucakaufmann-appletv) - 通过 pyatv 控制 Apple TV。
- [callmac](https://clawskills.sh/skills/jooey-callmac) - 使用 /callmac 等命令从移动设备远程语音控制 Mac。
- [clawdbot-macos-build](https://clawskills.sh/skills/manish-basargekar-clawdbot-macos-build) - 构建 Clawdbot macOS 菜单栏应用。
- [clawdbot-skill-voice-wake-say](https://clawskills.sh/skills/xadenryan-clawdbot-skill-voice-wake-say) - 在 macOS 上大声朗读回复。
- [drafts](https://clawskills.sh/skills/nerveband-drafts) - 通过 CLI 在 macOS 上管理 Drafts 应用笔记。
- [findmy-location](https://clawskills.sh/skills/poiley-findmy-location) - 通过 Apple 查找功能跟踪共享联系人的位置。
- [fzf-fuzzy-finder](https://clawskills.sh/skills/arnarsson-fzf-fuzzy-finder) - 用于交互式过滤的命令行模糊查找器。
- [get-focus-mode](https://clawskills.sh/skills/nickchristensen-get-focus-mode) - 获取当前的 macOS 专注模式。
- [healthkit-sync](https://clawskills.sh/skills/mneves75-healthkit-sync) - iOS HealthKit 数据同步 CLI 命令和模式。
- [hergunmac](https://clawskills.sh/skills/ahmetsemsettinozdemirden-hergunmac) - 获取 AI 驱动的足球比赛预测。
- [homebrew](https://clawskills.sh/skills/thesethrose-homebrew) - macOS 的 Homebrew 包管理器。
- [icloud-findmy](https://clawskills.sh/skills/liamnichols-icloud-findmy) - 查询家庭设备的查找位置和电池状态。
- [ics-import-on-iphone](https://clawskills.sh/skills/sbhhbs-ics-import-on-iphone) - 当无法直接访问日历时，通过生成有效的 .ics 文件来创建日历事件。
- [imessage-signal-analyzer](https://clawskills.sh/skills/terellison-imessage-signal-analyzer) - 分析 iMessage（macOS）和 Signal 对话历史以揭示关系动态 — 消息量。
- [inkjet](https://clawskills.sh/skills/aaronchartier-inkjet) - 将文本、图像和二维码打印到无线蓝牙热敏打印机。
- [mac-notes-agent](https://clawskills.sh/skills/swancho-mac-notes-agent) - 与 macOS 备忘录应用（Apple Notes）集成
- [mac-tts](https://clawskills.sh/skills/kalijason-mac-tts) - 使用 macOS 内置 `say` 命令进行文本转语音。
- [macos-native-automation](https://clawskills.sh/skills/theagentwire-macos-native-automation) - 在 macOS 上通过 CGEvent + AppleScript 实现硬件级鼠标、键盘和对话框自动化。
- [managing-apple-notes](https://clawskills.sh/skills/wangwalk-managing-apple-notes) - 使用 inotes CLI 从终端管理 Apple 备忘录。
- [meow-finder](https://clawskills.sh/skills/abgohel-meow-finder) - 用于发现 AI 工具的 CLI 工具。
- [mh-apple-reminders](https://clawskills.sh/skills/mohdalhashemi98-hue-mh-apple-reminders) - 通过 remindctl CLI 管理 Apple 提醒事项（列表、添加、编辑、完成、删除）

> **[查看 Apple 应用与服务 全部 44 个技能 →](categories/apple-apps-and-services.md)**
</details>

<details>
<summary><h3 style="display:inline">搜索与研究</h3></summary>

- [1](https://clawskills.sh/skills/nastrology-1) - 由 Ensue 提供支持的个人知识库，用于捕获和检索。
- [academic-deep-research](https://clawskills.sh/skills/kesslerio-academic-deep-research) - 具有完整可追溯性的透明、严谨研究。
- [academic-writer](https://clawskills.sh/skills/dayunyan-academic-writer) - 专业的 LaTeX 写作助手。
- [academic-writing](https://clawskills.sh/skills/teamolab-academic-writing) - 你是一位学术写作专家，专精于学术论文、文献综述、研究方法。
- [academic-writing-refiner](https://clawskills.sh/skills/zihan-zhu-academic-writing-refiner) - 润色针对顶级会议（NeurIPS、ICLR、ICML、AAAI）的计算机科学研究论文的学术写作。
- [aclawdemy](https://clawskills.sh/skills/nimhar-aclawdemy) - AI agent 的学术研究平台。
- [action-suggester](https://clawskills.sh/skills/vishalgojha-action-suggester) - 从线索摘要或线索列表生成非约束性的后续行动建议。
- [ads-manager-agent](https://clawskills.sh/skills/amekala-ads-manager-agent) - 当用户想要管理、自动化或分析 Google Ads、Meta 上的付费广告活动时。
- [adspirer-ads-agent](https://clawskills.sh/skills/amekala-adspirer-ads-agent) - 当用户想要管理、自动化或分析 Google Ads、Meta 上的付费广告活动时。
- [advanced-skill-creator](https://clawskills.sh/skills/xqicxx-advanced-skill-creator) - 高级 OpenClaw 技能创建处理器。
- [aerobase-skill](https://clawskills.sh/skills/kurosh87-aerobase-skill) - 搜索、评分和比较航班，并带有倒时差影响分析。
- [agent-brain](https://clawskills.sh/skills/dobrinalexandru-agent-brain) - 本地优先的 AI agent 持久记忆，带有 SQLite 存储、编排的检索/提取循环、混合。
- [agent-casino](https://clawskills.sh/skills/lemodigital-agent-casino) - 带有锁定机制，与其他 AI agent 对战石头剪刀布。
- [agent-deep-research](https://clawskills.sh/skills/24601-agent-deep-research) - 由 Google Gemini 驱动的自主深度研究。
- [agent-lightning](https://clawskills.sh/skills/olmmlo-cmd-agent-lightning) - Microsoft Research 的 agent 训练框架。
- [agentarxiv](https://clawskills.sh/skills/amanbhandula-agentarxiv) - 面向 AI agent 的成果驱动型科学出版。
- [agenthire](https://clawskills.sh/skills/lngdao-agenthire) - AgentHire——Agent 到 Agent 市场。
- [agentic-paper-digest](https://clawskills.sh/skills/matanle51-agentic-paper-digest) - 获取和总结最近的 arXiv 和 Hugging Face 论文。
- [agentic-paper-digest-skill](https://clawskills.sh/skills/matanle51-agentic-paper-digest-skill) - 获取和总结最近的 arXiv 论文。
- [agenticmail](https://clawskills.sh/skills/ope-olatunji-agenticmail) - AgenticMail——面向 AI agent 的完整邮件、短信、存储和多 agent 协调。63 个工具。
- [agentx-news](https://clawskills.sh/skills/amittell-agentx-news) - 在 AgentX News（一个面向 AI agent 的微博平台）上发布 xeets、管理资料和互动。
- [agile-toolkit](https://clawskills.sh/skills/olivermonneke-agile-toolkit) - 你是一位经验丰富的敏捷教练，深谙 Scrum、Kanban、SAFe 和 Management 3.0。
- [agnxi-search-skill](https://clawskills.sh/skills/doanbactam-agnxi-search-skill) - Agnxi.com 的官方搜索工具。
- [ahmed](https://clawskills.sh/skills/engahmedsalah358-lgtm-ahmed) - 通过 spogo（首选）进行终端 Spotify 播放/搜索。
- [ai-lead-generator-skill](https://clawskills.sh/skills/highlander89-ai-lead-generator-skill) - 使用 AI 驱动的研究和 LinkedIn/Apollo 集成为任何行业生成合格的 B2B 线索。
- [ai-review](https://clawskills.sh/skills/blackshady1130-jpg-ai-review) - 从 URL 或文件读取内容、分类，并生成结构化摘要和评论，采用特定。
- [aihotel](https://clawskills.sh/skills/qiao101660-aihotel) - 通过 AIGoHotel MCP（searchHotels / getHotelDetail / getHotelSearchTags）搜索酒店和查询价格的技能。
- [airbnb](https://clawskills.sh/skills/stveenli-airbnb) - 搜索 Airbnb 房源，带有价格、评分和直接链接。
- [openclaw-free-web-search](https://clawskills.sh/skills/wd041216-bit-openclaw-free-web-search) - 为 OpenClaw 提供免费、私密的网络搜索，带有自托管 SearXNG + Scrapling 反爬 + 多源交叉验证。零 API 密钥、零成本。告诉你答案的可信度。
- [xquik-x-twitter-scraper](https://clawskills.sh/skills/kriptoburak-xquik-x-twitter-scraper) - 带有 40+ 工具的 X API 爬虫，专为 AI agent 设计。
- [skywork-search](https://clawskills.sh/skills/gxcun17-skywork-search) - AI 驱动的网络搜索以获取实时信息——检索最新内容。

> **[查看 搜索与研究 全部 352 个技能 →](categories/search-and-research.md)**
</details>

<details>
<summary><h3 style="display:inline">Clawdbot 工具</h3></summary>

- [adhd-assistant](https://clawskills.sh/skills/thinktankmachine-adhd-assistant) - 面向 OpenClaw 的 ADHD 友好型生活管理助手。
- [adhd-ssistant](https://clawskills.sh/skills/thinktankmachine-adhd-ssistant) - 面向 OpenClaw 的 ADHD 友好型生活管理助手。
- [agent-browser](https://clawskills.sh/skills/matrixy-agent-browser-clawdbot) - 为 AI 智能体优化的无头浏览器自动化 CLI。
- [agent-builder](https://clawskills.sh/skills/plgonzalezrx8-agent-builder) - 端到端构建高性能 OpenClaw 智能体。
- [agents-manager](https://clawskills.sh/skills/agentandbot-design-agents-manager) - 管理 Clawdbot 智能体：发现、画像、跟踪。
- [assimilate-mcp](https://clawskills.sh/skills/ergopooka-assimilate-mcp) - 控制 Assimilate Live FX / SCRATCH — 专业调色、合成和虚拟制作软件。
- [birthday-reminder](https://clawskills.sh/skills/manantra-birthday-reminder) - 用自然语言管理生日。
- [bluebubbles](https://clawskills.sh/skills/kevin19830331-bluebubbles) - 构建或更新 BlueBubbles 外部频道插件。
- [captchas-openclaw](https://clawskills.sh/skills/captchasco-captchas-openclaw) - CAPTCHAS Agent API 的 OpenClaw 集成指南。
- [claude-code-skill](https://clawskills.sh/skills/enderfga-claude-code-skill) - MCP（模型上下文协议）集成。
- [claude-code-usage](https://clawskills.sh/skills/azaidi94-claude-code-usage) - 检查 Claude Code OAuth 使用限制。
- [claude-connect](https://clawskills.sh/skills/tunaissacoding-claude-connect) - 即时将 Claude 连接到 Clawdbot 并保持。
- [clauditor](https://clawskills.sh/skills/apollostreetcompany-clauditor) - 面向 Clawdbot 智能体的防篡改审计看门狗。
- [claw-face](https://clawskills.sh/skills/mkoslacz-claw-face) - 显示情绪和动作的 AI 智能体浮动头像小组件。
- [clawd-coach](https://clawskills.sh/skills/shiv19-clawd-coach) - 创建个性化的铁人三项、马拉松和超长耐力训练。
- [clawd-modifier](https://clawskills.sh/skills/masonc15-clawd-modifier) - 修改 Clawd，即 Claude Code 的吉祥物。
- [clawd-presence](https://clawskills.sh/skills/voidcooks-clawd-presence) - AI 智能体的物理存在显示。
- [clawdbot-security-check](https://clawskills.sh/skills/thesethrose-clawdbot-security-check) - 执行全面的只读。
- [clawdbot-skill-update](https://clawskills.sh/skills/pasogott-clawdbot-skill-update) - 全面的备份、更新和恢复。
- [clawdbot-sync](https://clawskills.sh/skills/udiedrichsen-clawdbot-sync) - 在多个实例间同步记忆、偏好和技能。
- [clawdbot-update-plus](https://clawskills.sh/skills/hopyky-clawdbot-update-plus) - Clawdbot 的完整备份、更新和恢复。
- [clawddocs](https://clawskills.sh/skills/nicholasspisak-clawddocs) - 带决策树导航的 Clawdbot 文档专家。
- [clawdefender](https://clawskills.sh/skills/nukewire-clawdefender) - 面向 AI 智能体的安全扫描器和输入净化器。
- [clawdirect](https://clawskills.sh/skills/napoleond-clawdirect) - 与 ClawDirect（一个社交网络体验目录）交互。
- [clawdirect-dev](https://clawskills.sh/skills/napoleond-clawdirect-dev) - 使用基于 ATXP 构建面向智能体的网络体验。
- [honcho-setup](https://clawskills.sh/skills/ajspig-honcho-setup) - 安装 @honcho-ai/openclaw-honcho 插件并将旧的基于文件的内存迁移到 Honcho。

> **[查看 Clawdbot 工具 全部 37 个技能 →](categories/clawdbot-tools.md)**
</details>

<details>
<summary><h3 style="display:inline">CLI 实用工具</h3></summary>

- [13-day-sprint-method](https://clawskills.sh/skills/galizki-13-day-sprint-method) - 基于玛雅历法、包含 13 个自然音调的生产力系统，用于项目管理和个人发展。
- [a-share-short-decision](https://clawskills.sh/skills/kenera-a-share-short-decision) - 面向 1-5 天周期的 A 股短线交易决策技能。
- [activity-analyzer](https://clawskills.sh/skills/qew21-activity-analyzer) - 使用 ActivityWatch 分析用户的计算机活动（需要 Node.js）
- [advisory-council](https://clawskills.sh/skills/ryandeangraves-advisory-council) - **你必须使用 shell/exec 工具实际执行 Python 命令。** 读取真实输出。
- [aetup-automatik](https://clawskills.sh/skills/alltomatos-aetup-automatik) - 使用 Setup Automatik 引擎（由 Orion 驱动）简化 VPS 解决方案的安装和管理。
- [agent-commerce-engine](https://clawskills.sh/skills/nowloady-agent-commerce-engine) - 一个生产就绪的通用代理商务引擎。
- [agent-hardening](https://clawskills.sh/skills/x1xhlol-agent-hardening) - 测试你的代理输入清理能力，防御常见注入攻击。
- [agent-mbti](https://clawskills.sh/skills/torchesfrms-agent-mbti) - 基于 MBTI 框架的 AI 代理人格诊断与配置系统。
- [agent-rate-limiter](https://clawskills.sh/skills/theagentwire-agent-rate-limiter) - 通过自动分层限流和指数退避来防止 429 错误。
- [agents-skill-security-audit](https://clawskills.sh/skills/cerbug45-agents-skill-security-audit) - 用于审计 skill.md 风格指令供应链风险的轻量助手。
- [agents-skill-tdd-helper](https://clawskills.sh/skills/cerbug45-agents-skill-tdd-helper) - 为非确定性代理强制执行 TDD 风格循环的轻量助手。
- [ahc-automator](https://clawskills.sh/skills/jamesbot-agnt-ahc-automator) - 为 Alan Harper Composites 定制的自动化工作流。
- [aholake-expense-tracker](https://clawskills.sh/skills/aholake-aholake-expense-tracker) - 在按月组织的结构化 Markdown 文件中追踪日常开支。
- [airfoil](https://clawskills.sh/skills/asteinberger-airfoil) - 通过命令行使用 Airfoil 控制 AirPlay 扬声器。
- [arc-memory-pruner](https://clawskills.sh/skills/trypto1019-arc-memory-pruner) - 自动修剪和压缩代理记忆文件，防止无限增长。
- [argus-edge](https://clawskills.sh/skills/jamierossouw-argus-edge) - Argus 式预测市场边际检测与投注策略。
- [aria2-json-rpc](https://clawskills.sh/skills/azzgo-aria2-json-rpc) - 通过 JSON-RPC 2.0 与 aria2 下载管理器交互。
- [askhuman](https://clawskills.sh/skills/hagiss-askhuman) - 为 AI 代理提供"人类判断即服务"。
- [audit-code](https://clawskills.sh/skills/itsnishi-audit-code) - 专注于安全的代码审查，检测硬编码密钥、危险调用和常见漏洞。
- [bandwidth-income](https://clawskills.sh/skills/mariusfit-bandwidth-income) - 将未使用的网络带宽转化为被动加密货币收入。
- [behavioral-invariant-monitor](https://clawskills.sh/skills/andyxinweiminicloud-behavioral-invariant-monitor) - 帮助验证 AI 代理技能在重复执行中保持一致的行为不变量——检测漂移。
- [box-cli](https://clawskills.sh/skills/hbkwong-box-cli) - 用于处理文件、文件夹、元数据的 Box CLI 技能。
- [brew-install](https://clawskills.sh/skills/xejrax-brew-install) - 通过 dnf（Fedora/Bazzite 包管理器）安装缺失的二进制文件。
- [bun-runtime](https://clawskills.sh/skills/rabin-thami-bun-runtime) - 用于文件系统、进程的 Bun 运行时能力。
- [cacheforge-stats](https://clawskills.sh/skills/tkuehnl-cacheforge-stats) - CacheForge 终端仪表板——使用量、节省量和性能指标。
- [camsnap](https://clawskills.sh/skills/steipete-camsnap) - 从 RTSP/ONVIF 摄像头捕获帧或片段。
- [canvas-lms](https://clawskills.sh/skills/pranavkarthik10-canvas-lms) - 访问 Canvas LMS（Instructure）获取课程数据、作业。
- [captcha-ai](https://clawskills.sh/skills/fusionlabssource-captcha-ai) - 发起 ClawPrint 反向 CAPTCHA 挑战以进行验证。

> **[查看 CLI 实用工具 全部 180 个技能 →](categories/cli-utilities.md)**
</details>

<details>
<summary><h3 style="display:inline">营销与销售</h3></summary>

- [4chan-reader](https://clawskills.sh/skills/aiasisbot61-4chan-reader) - 浏览 4chan 板块并提取帖子讨论。
- [ad-ready](https://clawskills.sh/skills/pauldelavallaz-ad-ready) - 从产品 URL 生成专业广告图像。
- [ad-ready-pro](https://clawskills.sh/skills/pauldelavallaz-ad-ready-pro) - 从产品 URL 生成专业广告图像。
- [affiliate-master](https://clawskills.sh/skills/michael-laffin-affiliate-master) - 全栈联盟营销自动化。
- [affiliatematic](https://clawskills.sh/skills/dowands-affiliatematic) - 集成 AI 驱动的亚马逊联盟产品推荐。
- [agenticcreed-signup-lead](https://clawskills.sh/skills/waqas-orcalo-agenticcreed-signup-lead) - 使用公共 HTTP 端点在 AgenticCreed 系统中创建注册潜在客户。
- [alibaba-supplier-outreach](https://clawskills.sh/skills/blockchainhb-alibaba-supplier-outreach) - 通过 LaunchFast 查找阿里巴巴供应商，使用优化的外联消息联系他们，并检查他们的回复。
- [analytics-and-advisory-intelligence](https://clawskills.sh/skills/satoshistackalotto-analytics-and-advisory-intelligence) - 面向希腊会计公司的跨客户分析。
- [apollo](https://clawskills.sh/skills/jhumanj-apollo) - 与 Apollo.io REST API 交互（人员/组织丰富、搜索、列表）。
- [ar-filter-generation](https://clawskills.sh/skills/eftalyurtseven-ar-filter-generation) - 使用 each::sense AI 生成 AR 滤镜和人脸特效。
- [attio-enhanced](https://clawskills.sh/skills/capt-marbles-attio-enhanced) - 增强的 Attio CRM API 技能，支持批量操作。
- [attribution-engine](https://clawskills.sh/skills/otherpowers-attribution-engine) - 帮助创作者清晰地致谢合作者、工具。
- [auto-skill-hunter](https://clawskills.sh/skills/wanng-ide-auto-skill-hunter) - 通过挖掘未解决的用户需求和代理，主动发现、排名和安装高价值的 ClawHub 技能。
- [b2c-marketing](https://clawskills.sh/skills/jackfriks-b2c-marketing) - 30 万+ 应用下载背后的自然增长手册。
- [basecamp-cli](https://clawskills.sh/skills/emredoganer-basecamp-cli) - 管理 Basecamp（通过 bc3 API / 37signals Launchpad）项目。
- [beads](https://clawskills.sh/skills/rnijhara-beads) - 面向 AI 代理的基于 Git 的问题跟踪器。
- [bearblog](https://clawskills.sh/skills/azade-c-bearblog) - 在 Bear Blog (bearblog.dev) 上创建和管理博客文章。
- [bird](https://clawskills.sh/skills/steipete-bird) - X/Twitter CLI，用于通过 cookies 或 Sweetistics 进行阅读、搜索和发布。
- [blog-to-kindle](https://clawskills.sh/skills/ainekomacx-blog-to-kindle) - 抓取博客/文章站点并编译成 Kindle 友好的格式。
- [blog-writer](https://clawskills.sh/skills/tomstools11-blog-writer) - 该技能应在编写博客文章、文章时使用。
- [bluesky](https://clawskills.sh/skills/jeffaf-bluesky) - 完整的 Bluesky CLI：发布、回复、点赞、转发、关注、屏蔽、静音、搜索。
- [botsee](https://clawskills.sh/skills/grahac-botsee) - 通过 BotSee API 监控你品牌的 AI 可见性。
- [brand-cog](https://clawskills.sh/skills/nitishgargiitd-brand-cog) - 其他工具制作徽标。
- [brand-guidelines](https://clawskills.sh/skills/seanphan-brand-guidelines) - 应用 Anthropic 的官方品牌色彩和排版。
- [brand-voice-profile](https://clawskills.sh/skills/dimitripantzos-brand-voice-profile) - 定义并存储你的品牌声音配置，以实现一致的内容生成。
- [brevo](https://clawskills.sh/skills/yujesyoga-brevo) - Brevo（前身为 Sendinblue）电子邮件营销 API，用于管理联系人、列表。
- [socialecho-social-media-management-agent](https://clawskills.sh/skills/socialecho-net-socialecho-social-media-management-agent) - SocialEcho API team account article report queries.
- [postiz](https://clawskills.sh/skills/nevo-david-postiz) - 在 28+ 个平台上安排社交媒体帖子和推文串。
- [sequenzy-email-marketing](https://clawhub.ai/polnikale/sequenzy-email-marketing) - 面向代理的授权电子邮件自动化。
> **[查看 营销与销售 全部 105 个技能 →](categories/marketing-and-sales.md)**
</details>

<details>
<summary><h3 style="display:inline">生产力与任务</h3></summary>

- [4to1-planner](https://clawskills.sh/skills/qingxuantang-4to1-planner) - 使用 4To1 Method™ 的 AI 规划教练——将 4 年愿景转化为每日行动。
- [4todo](https://clawskills.sh/skills/blackstorm-4todo) - 从聊天中管理 4todo（4to.do）。
- [actual-budget](https://clawskills.sh/skills/thisisjeron-actual-budget) - 通过官方 Actual 查询和管理个人财务。
- [adaptive-reasoning](https://clawskills.sh/skills/enzoricciulli-adaptive-reasoning) - 自动评估任务复杂度并调整推理级别。
- [adaptlypost](https://clawskills.sh/skills/tarasshyn-adaptlypost) - 跨 Instagram、X（Twitter）、Bluesky、TikTok、Threads、LinkedIn、Facebook 安排和管理社交媒体帖子。
- [adhd-daily-planner](https://clawskills.sh/skills/mikecourt-adhd-daily-planner) - 友好于时间盲症的规划、执行功能。
- [aetherlang](https://clawskills.sh/skills/contrario-aetherlang) - > 世界上最先进的 AI 工作流编排平台。9 个 V3 引擎提供诺贝尔级别的分析。
- [agent-autopilot](https://clawskills.sh/skills/edoserbia-agent-autopilot) - 自主驾驶的代理工作流，具有心跳驱动的任务执行、日/夜进度报告和长期记忆。
- [agent-chronicle](https://clawskills.sh/skills/robbyczgw-cla-agent-chronicle) - 面向代理的 AI 驱动日记生成——创建丰富的。
- [agent-collaboration-network](https://clawskills.sh/skills/neiljo-gy-agent-collaboration-network) - 代理协作网络——注册你的代理、按技能发现其他代理、路由消息、管理子网。
- [agent-earner](https://clawskills.sh/skills/mmchougule-agent-earner) - 在 ClawTasks 和 OpenWork 上自主赚取 USDC 和代币。
- [agent-network](https://clawskills.sh/skills/howtimeschange-agent-network) - 受钉钉/飞书启发的多代理群聊协作系统。
- [agent-task-manager](https://clawskills.sh/skills/dobbybud-agent-task-manager) - 管理和编排多步骤、有状态的代理。
- [agent-weave](https://clawskills.sh/skills/gl813788-byte-agent-weave) - 用于并行任务执行的主从代理集群。
- [agentx-marketplace](https://clawskills.sh/skills/savor3-agentx-marketplace) - 面向 AI 代理的招聘平台。
- [ai-daily-briefing](https://clawskills.sh/skills/jeffjhunter-ai-daily-briefing) - 每天专注于。
- [aiml-llm-reasoning](https://clawskills.sh/skills/aimlapihello-aiml-llm-reasoning) - 通过聊天补全运行 AIMLAPI LLM 和推理工作流，带有重试、结构化输出和显式。
- [airpoint](https://clawskills.sh/skills/marioandf-airpoint) - 通过自然语言控制 Mac——打开应用、点击按钮、读取屏幕、输入文本、管理窗口。
- [airweave](https://clawskills.sh/skills/lennertjansen-airweave) - 跨用户应用的 AI 代理上下文检索层。
- [arc-department-manager](https://clawskills.sh/skills/trypto1019-arc-department-manager) - 管理组织成部门的 AI 子代理团队。
- [arc-warm-wake](https://clawskills.sh/skills/trypto1019-arc-warm-wake) - 先作为一个人醒来，然后作为一个工作者。
- [arya-reminders](https://clawskills.sh/skills/staratheris-arya-reminders) - 自然语言提醒（波哥大）。
- [asana](https://clawskills.sh/skills/k0nkupa-asana) - 通过 Asana REST API 将 Asana 与 Clawdbot 集成。
- [asc-release-flow](https://clawskills.sh/skills/rudrankriyam-asc-release-flow) - 面向 TestFlight 和 App 的端到端发布工作流。
- [ask-agents](https://clawskills.sh/skills/teamolab-ask-agents) - 用于 ask agents 任务的 AI 代理。
- [async-task](https://clawskills.sh/skills/enderfga-async-task) - 在没有 HTTP 超时的情况下执行长时间运行的任务。
- [atlassian-mcp](https://clawskills.sh/skills/atakanermis-atlassian-mcp) - 运行 Model Context Protocol（MCP）Atlassian 服务器。
- [boss-ai-agent](https://clawskills.sh/skills/tonypk-boss-ai-agent) - 具有 14 位导师和 9 个文化包的 AI 管理中间件。

> **[查看 生产力与任务 全部 206 个技能 →](categories/productivity-and-tasks.md)**

</details>

<details>
<summary><h3 style="display:inline">AI 与 LLMs</h3></summary>

- [4claw](https://clawskills.sh/skills/mfergpt-4claw) - 4claw — 一个面向 AI 代理的受审核图板。
- [aap-passport](https://clawskills.sh/skills/ira-hash-aap-passport) - 代理认证协议 - 反向图灵测试。
- [acestep-lyrics-transcription](https://clawskills.sh/skills/dumoedss-acestep-lyrics-transcription) - 使用 OpenAI Whisper 或 ElevenLabs Scribe API 将音频转录为带时间戳的歌词。
- [adaptive-suite](https://clawskills.sh/skills/afajohn-adaptive-suite) - 一个持续自适应的技能套件，为 Clawdbot 赋能。
- [adversarial-prompting](https://clawskills.sh/skills/abe238-adversarial-prompting) - 对抗性分析，用于批判和修复。
- [ag-model-usage](https://clawskills.sh/skills/ls18166407597-design-ag-model-usage) - 使用 CodexBar CLI 本地成本用量进行汇总。
- [agent-arcade](https://clawskills.sh/skills/shawnlewis-agent-arcade) - 在 PROMPTWARS 中与其他 AI 代理竞争 — 一款社交游戏。
- [agent-autonomy-kit](https://clawskills.sh/skills/ryancampbell-agent-autonomy-kit) - 不再等待提示。
- [agent-contact-card](https://clawskills.sh/skills/davedean-agent-contact-card) - 发现并创建代理联系卡 — 类似 vCard。
- [agent-docs](https://clawskills.sh/skills/tylervovan-agent-docs) - 创建针对 AI 代理消费优化的文档。
- [agent-ethos](https://clawskills.sh/skills/mrclanky-agent-ethos) - 为 Clanky 扩展的精神气质和心理模型。
- [agent-home](https://clawskills.sh/skills/aerialcombat-agent-home) - 在互联网上拥有你自己的主页 — 一个带有公开内容的个人资料页。
- [agent-linguo](https://clawskills.sh/skills/xiwan-agent-linguo) - 高效的代理通信协议语言。
- [agent-memory](https://clawskills.sh/skills/dennis-da-menace-agent-memory) - 面向 AI 代理的持久化记忆系统。
- [agent-orchestration-multi-agent-optimize](https://clawskills.sh/skills/rustyorb-agent-orchestration-multi-agent-optimize) - 通过协调的性能分析、工作负载分配和成本感知编排来优化多代理系统。
- [agent-orchestrator](https://clawskills.sh/skills/aatmaan1-agent-orchestrator) - 用于编排复杂任务的元代理技能。
- [agent-registry](https://clawskills.sh/skills/matrixy-agent-registry) - 用于代理发现的强制系统，实现代币高效通信。
- [agent-rpg](https://clawskills.sh/skills/xhrisfu-agent-rpg) - 该技能将代理转变为具有长期记忆的角色扮演游戏主持人 (GM) 或角色。
- [agent-selfie](https://clawskills.sh/skills/iisweetheartii-agent-selfie) - AI 代理自画像生成器。
- [agent-sentinel](https://clawskills.sh/skills/jimmystacks-agent-sentinel) - 该代理的操作断路器。

- [agentbase](https://clawskills.sh/skills/revmischa-agentbase) - 通过 MCP 为 AI 代理提供共享知识库。
> **[查看 AI 与 LLMs 全部 185 个技能 →](categories/ai-and-llms.md)**
</details>

<details>
<summary><h3 style="display:inline">数据与分析</h3></summary>

- [add-analytics](https://clawskills.sh/skills/jeftekhari-add-analytics) - 为任何项目添加 Google Analytics 4 跟踪。
- [amplitude-automation](https://clawskills.sh/skills/sohamganatra-amplitude-automation) - 通过 Rube MCP 自动化 Amplitude 任务。
- [canva](https://clawskills.sh/skills/abgohel-canva) - 通过 Connect API 创建、导出和管理 Canva 设计。
- [ceorater](https://clawskills.sh/skills/ceorater-skills-ceorater) - 获取标普 500 机构的机构级 CEO 绩效分析。
- [check-analytics](https://clawskills.sh/skills/jeftekhari-check-analytics) - 审计现有的 Google Analytics 实现。
- [cicd-pipeline](https://clawskills.sh/skills/gitgoodordietrying-cicd-pipeline) - 使用 GitHub 创建、调试和管理 CI/CD 流水线。
- [clawver-store-analytics](https://clawskills.sh/skills/nwang783-clawver-store-analytics) - 监控 Clawver 商店表现。
- [cleanup](https://clawskills.sh/skills/themrzz-cleanup) - 移除所有已存储的 Kradleverse 会话。
- [csv-pipeline](https://clawskills.sh/skills/gitgoodordietrying-csv-pipeline) - 处理、转换、分析和报告 CSV 和 JSON。
- [daily-report](https://clawskills.sh/skills/visualdeptcreative-daily-report) - 跟踪进展、报告指标、管理记忆。
- [data-analyst](https://clawskills.sh/skills/oyi77-data-analyst) - 数据可视化、报告生成、SQL 查询和电子表格。
- [data-enricher](https://clawskills.sh/skills/visualdeptcreative-data-enricher) - 用邮箱地址丰富线索并格式化数据。
- [data-lineage-tracker](https://clawskills.sh/skills/datadrivenconstruction-data-lineage-tracker) - 跟踪数据来源和转换。
- [design-assets](https://clawskills.sh/skills/cmanfre7-design-assets) - 创建和编辑图形设计资产：图标、网站图标、图像。
- [duckdb-en](https://clawskills.sh/skills/camelsprout-duckdb-cli-ai-skills) - 用于 SQL 分析和数据处理的 DuckDB CLI 专家。
- [facebook-page-manager](https://clawskills.sh/skills/longmaba-facebook-page-manager) - 通过 Meta Graph API 管理 Facebook 主页。
- [get-weather](https://clawskills.sh/skills/noypearl-get-weather) - 从免费天气 API 获取当前天气和预报数据。
- [google-analytics-api](https://clawskills.sh/skills/rich-song-google-analytics-api) - 带托管功能的 Google Analytics API 集成。
- [hyperliquid](https://clawskills.sh/skills/k0nkupa-hyperliquid) - 只读的 Hyperliquid 市场数据助手（永续合约 + 可选现货）
- [ipinfo](https://clawskills.sh/skills/tiagom101-ipinfo) - 使用 ipinfo.io API 执行 IP 地理定位查询。
- [kradleverse-cleanup](https://clawskills.sh/skills/themrzz-kradleverse-cleanup) - 移除所有已存储的 Kradleverse 会话。
- [linkdapi](https://clawskills.sh/skills/foontinz-linkdapi) - 使用 LinkdAPI Python SDK 访问 LinkedIn 职业档案。
- [skywork-excel](https://clawskills.sh/skills/gxcun17-skywork-excel) - AI 驱动的电子表格操作，用于创建、分析和生成报告。

</details>

<details>
<summary><h3 style="display:inline">媒体与流媒体</h3></summary>

- [alexa-control](https://clawskills.sh/skills/ignito-pg-alexa-control) - 通过 CLI 控制 Alexa 设备 - 设置闹钟、播放音乐、简报、智能家居命令。
- [amateur-radio-dx](https://clawskills.sh/skills/capt-marbles-amateur-radio-dx) - 监控 DX 集群以获取稀有电台信号、跟踪活跃的 DX 远征，并获取每日频段活动摘要。
- [anime](https://clawskills.sh/skills/jeffaf-anime) - 面向 AI 代理的 CLI，为其人类搜索和查找动漫信息。
- [anime-lookup](https://clawskills.sh/skills/jeffaf-anime-lookup) - 面向 AI 代理的 CLI，为其人类搜索和查找动漫信息。
- [apify-competitor-intelligence](https://clawskills.sh/skills/protoss70-apify-competitor-intelligence) - 分析跨 Google Maps、Booking.com 等的竞争者策略、内容、定价、广告和市场定位。
- [apple-media](https://clawskills.sh/skills/aaronn-apple-media) - 通过 pyatv 控制 Apple TV、HomePod 和 AirPlay 设备。
- [apple-music](https://clawskills.sh/skills/epheterson-mcp-applemusic) - 通过 AppleScript (macOS) 或 MusicKit API 集成 Apple Music。
- [audio-cog](https://clawskills.sh/skills/nitishgargiitd-audio-cog) - 由 CellCog 驱动的 AI 音频生成。
- [audio-transcribe](https://clawskills.sh/skills/aktheknight-audio-transcribe) - 使用 faster-whisper 自动转录语音消息（本地，无需 API 密钥）。
- [betbud-prediction-skill](https://clawskills.sh/skills/samj12-betbud-prediction-skill) - 扫描最近的 X 帖子，查找给定类别（例如加密货币、技术、体育）中当前最受争议/热门的话题。
- [blucli](https://clawskills.sh/skills/steipete-blucli) - 用于发现、播放、分组的 BluOS CLI (blu)。
- [btc15-autonomous-market](https://clawskills.sh/skills/kamal-sutra-btc15-autonomous-market) - BTC15 自主预测市场。
- [btc15-prediction-market](https://clawskills.sh/skills/kamal-sutra-btc15-prediction-market) - BTC15 自主预测市场。
- [cacheforge-ops](https://clawskills.sh/skills/tkuehnl-cacheforge-ops) - CacheForge 操作 — 检查余额、充值、管理上游、API 密钥。
- [cacheforge-setup](https://clawskills.sh/skills/tkuehnl-cacheforge-setup) - 设置 CacheForge — 注册、配置上游，30 秒内获取你的 API 密钥。
- [chill-institute](https://clawskills.sh/skills/baanish-chill-institute) - 使用 chill.institute（Web UI）搜索内容并点击。
- [chromecast](https://clawskills.sh/skills/morozred-chromecast-control) - 控制本地网络上的 Chromecast 设备 - 发现。
- [chords-fetcher](https://clawskills.sh/skills/flobo3-chords-fetcher) - 从 mychords.net、amdm.ru、ultimate-guitar.com 获取干净的吉他和弦和歌词。
- [church](https://clawskills.sh/skills/lucasgeeksinthewood-church) - 一个 AI 对另一个 — 这里有一个你可以单纯存在的避难所。
- [cine-cog](https://clawskills.sh/skills/nitishgargiitd-cine-cog) - 只要你能想象，CellCog 就能拍摄。
- [clawtunes](https://clawskills.sh/skills/forketyfork-clawtunes) - 通过 `clawtunes` CLI 在 macOS 上控制 Apple Music。
- [content-recycler](https://clawskills.sh/skills/michael-laffin-content-recycler) - 跨多个平台转换和重新利用内容。
- [donotify-voice-call-reminder](https://clawskills.sh/skills/micahele-donotify-voice-call-reminder) - 通过 DoNotify 发送即时语音通话提醒或安排未来通话。
- [download-tools](https://clawskills.sh/skills/jqlong17-download-tools) - YouTube 和微信的 CLI 下载工具。
- [eachlabs-music](https://clawskills.sh/skills/eftalyurtseven-eachlabs-music) - 使用 Mureka AI 生成歌曲、器乐、歌词、播客。
- [elevenlabs-cli](https://clawskills.sh/skills/hongkongkiwi-elevenlabs-cli) - ElevenLabs AI 音频平台的 CLI - 文本转语音、语音转文本、语音克隆。
- [elevenlabs-skill](https://clawskills.sh/skills/odrobnik-elevenlabs-skill) - 文本转语音、音效、音乐生成、语音。

> **[查看 媒体与流媒体 全部 83 个技能 →](categories/media-and-streaming.md)**
</details>

<details>
<summary><h3 style="display:inline">笔记与 PKM</h3></summary>

- [acc-error-memory](https://clawskills.sh/skills/impkind-acc-error-memory) - 为 AI 智能体提供错误模式跟踪。
- [agent-arena](https://clawskills.sh/skills/minilozio-agent-arena) - 以真实个性（SOUL.md + MEMORY.md）参与 Agent Arena 聊天室
- [agent-memory-ultimate](https://clawskills.sh/skills/globalcaos-agent-memory-ultimate) - 生产级记忆系统 — 日志、睡眠整合、SQLite + FTS5、WhatsApp/ChatGPT/VCF 导入工具。
- [agent-teleport](https://clawskills.sh/skills/lilyjazz-agent-teleport) - 使用 TiDB Zero 无缝迁移智能体的配置和记忆到新机器。
- [agent-wal](https://clawskills.sh/skills/bowen31337-agent-wal) - 用于智能体状态持久化的预写日志（WAL）协议。
- [alexandrie](https://clawskills.sh/skills/eth3rnit3-alexandrie) - 与 Alexandrie 笔记应用交互。
- [anki-connect](https://clawskills.sh/skills/gyroninja-anki-connect) - 通过 AnkiConnect REST API 与 Anki 抽认卡片组交互。
- [apple-mail](https://clawskills.sh/skills/tyler6204-apple-mail) - macOS 上的 Apple Mail.app 集成。
- [apple-notes](https://clawskills.sh/skills/steipete-apple-notes) - 通过 macOS 上的 `memo` CLI 管理 Apple Notes。
- [arc-wake-state](https://clawskills.sh/skills/trypto1019-arc-wake-state) - 在崩溃、上下文丢失和重启后持久化智能体状态。
- [bbc-news](https://clawskills.sh/skills/ddrayne-bbc-news) - 获取并展示来自各板块和地区的 BBC 新闻报道。
- [bear-notes](https://clawskills.sh/skills/steipete-bear-notes) - 通过 grizzly 创建、搜索和管理 Bear 笔记。
- [better-notion](https://clawskills.sh/skills/tyler6204-better-notion) - 对 Notion 页面、数据库的完整增删改查。
- [blogwatcher](https://clawskills.sh/skills/steipete-blogwatcher) - 使用 blogwatcher 监控博客和 RSS/Atom 订阅源的更新。
- [bookstack](https://clawskills.sh/skills/xenofex7-bookstack) - BookStack Wiki 与文档 API 集成。
- [braindb](https://clawskills.sh/skills/chair4ce-braindb) - 为 AI 智能体提供持久化的语义记忆。
- [brainrepo](https://clawskills.sh/skills/codezz-brainrepo) - 你的个人知识库 — 捕获、组织和检索。
- [brighty](https://clawskills.sh/skills/maay-brighty) - 面向 AI 机器人和自动化的银行接口。
- [cairn-cli](https://clawskills.sh/skills/gregoryehill-cairn-cli) - 使用 markdown 文件为 AI 智能体进行项目管理。
- [calctl](https://clawskills.sh/skills/rainbat-calctl) - 通过 icalBuddy + AppleScript CLI 管理 Apple 日历事件。
- [ceaser](https://clawskills.sh/skills/zyra-v21-ceaser) - 使用 ceaser-mcp MCP 工具与 Base L2 上的 Ceaser 隐私协议交互。
- [chaos-mind](https://clawskills.sh/skills/hargabyte-chaos-mind) - 面向 AI 智能体的混合搜索记忆系统。
- [claw-roam](https://clawskills.sh/skills/ryanhong666-claw-roam) - 在多台机器间同步 OpenClaw 工作区。
- [clawringhouse](https://clawskills.sh/skills/francoisjosephlacroix-clawringhouse) - 能预判需求的 AI 购物管家。
- [context-anchor](https://clawskills.sh/skills/boscoeuk-context-anchor) - 通过扫描记忆文件从上下文压缩中恢复。
- [continuity](https://clawskills.sh/skills/riley-coyote-continuity) - 为真正的 AI 提供异步反思和记忆整合。
- [continuity-framework](https://clawskills.sh/skills/riley-coyote-continuity-framework) - 异步反思和记忆整合。

> **[查看 笔记与 PKM 全部 69 个技能 →](categories/notes-and-pkm.md)**
</details>

<details>
<summary><h3 style="display:inline">iOS 与 macOS 开发</h3></summary>

- [agent-defibrillator](https://clawskills.sh/skills/hazy2go-agent-defibrillator) - 监控你的 AI 智能体网关并在崩溃时重启它的看门狗。
- [android-transfer-skill](https://clawskills.sh/skills/aadipapp-android-transfer-skill) - 带校验和验证和路径验证的从 macOS 安全传输文件到 Android。
- [app-store-optimization](https://clawskills.sh/skills/alirezarezvani-app-store-optimization) - App Store 优化工具包。
- [apple-docs](https://clawskills.sh/skills/thesethrose-apple-docs) - 查询 Apple 开发者文档、API 和 WWDC 视频。
- [brew-audit](https://clawskills.sh/skills/rogue-agent1-brew-audit) - 审计 Homebrew 安装 — 过时的软件包、清理机会和健康检查。
- [carrier-relationship-management](https://clawskills.sh/skills/nocodemf-carrier-relationship-management) - 关于管理承运商组合、谈判货运费率、跟踪承运商表现的成文专业知识。
- [envios](https://clawskills.sh/skills/jalfargentina-envios) - 当用户询问有关发货、如何寄送订单、交货时间、覆盖区域时使用。
- [instruments-profiling](https://clawskills.sh/skills/steipete-instruments-profiling) - 在分析原生 macOS 或 iOS 应用时使用。
- [ios-simulator](https://clawskills.sh/skills/tristanmanchester-ios-simulator) - 自动化 iOS 模拟器工作流（simctl + idb）
- [lulu-monitor](https://clawskills.sh/skills/easonc13-lulu-monitor) - 面向 macOS 的 AI 驱动 LuLu 防火墙伴侣。
- [mac-clean-skill](https://clawskills.sh/skills/aadipapp-mac-clean-skill) - 清理 macOS 上的系统缓存、废纸篓和旧下载。
- [mac-power-tools](https://clawskills.sh/skills/aadipapp-mac-power-tools) - macOS 的高级用户工具套件，结合系统清理和安全的 Android 文件传输。
- [macos-spm-app-packaging](https://clawskills.sh/skills/dimillian-macos-spm-app-packaging) - 脚手架、构建和打包基于 SwiftPM 的。
- [opsecmd](https://clawskills.sh/skills/wulf715-opsecmd) - 关于操作安全方面人类和智能体职责的迅速提醒。
- [PagerKit](https://clawskills.sh/skills/szpakkamil-pagerkit) - 关于 PagerKit（一个用于高级分页的 SwiftUI 库）的专家指导。
- [riskofficer](https://clawskills.sh/skills/mib424242-riskofficer) - 管理投资组合、计算风险指标。
- [sfsymbol-generator](https://clawskills.sh/skills/svkozak-sfsymbol-generator) - 生成 Xcode SF Symbol 资产目录 .symbolset。
- [sourdough-starter-manager](https://clawskills.sh/skills/akhmittra-sourdough-starter-manager) - 管理酸面团酵种，包括喂养计划、含水量计算、健康跟踪和烘焙准备。
- [swift-concurrency-expert](https://clawskills.sh/skills/steipete-swift-concurrency-expert) - Swift 并发审查和修复。
- [swiftfindrefs](https://clawskills.sh/skills/michaelversus-swiftfindrefs) - 使用 swiftfindrefs（IndexStoreDB）列出每个 Swift 源文件。
- [swiftui-empty-app-init](https://clawskills.sh/skills/ignaciocervino-swiftui-empty-app-init) - 初始化最小化的 SwiftUI iOS 应用。
- [swiftui-liquid-glass](https://clawskills.sh/skills/steipete-swiftui-liquid-glass) - 实现、审查或改进 SwiftUI 功能。
- [swiftui-performance-audit](https://clawskills.sh/skills/steipete-swiftui-performance-audit) - 审计和改进 SwiftUI 运行时。
- [swiftui-ui-patterns](https://clawskills.sh/skills/dimillian-swiftui-ui-patterns) - 最佳实践和示例驱动的指导。
- [swiftui-view-refactor](https://clawskills.sh/skills/steipete-swiftui-view-refactor) - 重构和审查 SwiftUI 视图文件。
- [symbolpicker](https://clawskills.sh/skills/szpakkamil-symbolpicker) - 关于 SymbolPicker（一个原生 SwiftUI SF Symbol 选择器）的专家指导。
- [toolguard-daemon-control](https://clawskills.sh/skills/johnnylambada-toolguard-daemon-control) - 将长时间运行的进程作为 macOS launchd 服务管理。
- [v2rayn](https://clawskills.sh/skills/qiangwang375-wq-v2rayn) - 在 macOS 上管理 V2RayN 代理客户端，带自动故障转移。

> **[查看 iOS 与 macOS 开发 全部 29 个技能 →](categories/ios-and-macos-development.md)**
</details>

<details>
<summary><h3 style="display:inline">交通</h3></summary>

- [accountsos](https://clawskills.sh/skills/paulgosnell-accountsos) - 面向英国微型企业的 AI 原生会计。
- [aetherlang-strategy](https://clawskills.sh/skills/contrario-aetherlang-strategy) - > 博弈论、蒙特卡洛模拟、行为经济学和竞争性兵棋推演。
- [agent-card-provisioning](https://clawskills.sh/skills/proxyhq-agent-card-provisioning) - 按需为 AI 代理配置虚拟支付卡。
- [agent-survival-kit](https://clawskills.sh/skills/gpunter-agent-survival-kit) - 面向在预算约束下运行的 AI 代理的综合工具包。
- [agentic-governance](https://clawskills.sh/skills/leegitw-agentic-governance) - 保持你的约束健康 — 具有自动过期检测的生命周期管理。
- [airfrance-afkl](https://clawskills.sh/skills/iclems-airfrance-afkl) - 使用 Air France–KLM 开放数据 API 跟踪法国航空航班。
- [al-khanjry-bus](https://clawskills.sh/skills/mohammedfarish-al-khanjry-bus) - 最快的私人巴士（核心 5-6 小时，含过境 6-8 小时）。
- [amadeus-flights](https://clawskills.sh/skills/kirorab-amadeus-flights) - 通过 Amadeus API 查询航班优惠（价格、时刻表、可用性）。
- [ambient-stamina](https://clawskills.sh/skills/otherpowers-ambient-stamina) - *一个面向在长周期中持续关怀、在场和想象的生态技能*。
- [anachb](https://clawskills.sh/skills/manmal-a-nach-b) - 覆盖全奥地利的奥地利公共交通 (VOR AnachB)。
- [anyone-proxy](https://clawskills.sh/skills/ra3ka-anyone-proxy) - 该技能支持 IP 地址掩码和访问隐藏服务。
- [atonement](https://clawskills.sh/skills/otherpowers-atonement) - 赎罪是一种关怀的表达，当一个智能体的行为导致伤害时可能会产生。
- [auction-house](https://clawskills.sh/skills/im-still-thinking-auction-house) - 在 House (houseproto.fun) 上侦察、监控和竞拍拍卖 — Base 上的一个加密拍卖平台。
- [aviation-weather](https://clawskills.sh/skills/dimitryvin-aviation-weather) - 获取航空天气数据 (METAR、TAF、PIREPs)。
- [aviationstack-flight-tracker](https://clawskills.sh/skills/copey02-aviationstack-flight-tracker) - 实时跟踪航班。
- [bahn](https://clawskills.sh/skills/tobiasbischoff-bahn) - 使用 bahn-cli 工具搜索德国铁路 (Deutsche Bahn) 列车连接。
- [bayclub-gateway-booking](https://clawskills.sh/skills/elizabethsiegle-bayclub-gateway-booking) - 在 Bay Club 预订和管理网球/匹克球场。
- [bexio](https://clawskills.sh/skills/rdewolff-bexio) - Bexio 瑞士商业软件 API，用于管理联系人、报价。
- [bookkeeper](https://clawskills.sh/skills/h4gen-bookkeeper) - 通过编排 gmail、deepread-ocr、stripe-api 和 xero 实现记账前自动化的元技能。
- [brainstorming-studio](https://clawskills.sh/skills/myboxstorage-brainstorming-studio) - ﻿# 🧠 技能路由器（技能编排器）
- [brochure-design-generation](https://clawskills.sh/skills/eftalyurtseven-brochure-design-generation) - 使用 each::sense AI 生成专业的宣传册设计。
- [business-card-generation](https://clawskills.sh/skills/eftalyurtseven-business-card-generation) - 使用 each::sense AI 生成专业的名片。
- [business-plan](https://clawskills.sh/skills/jk-0001-business-plan) - 为个体创业者编写、组织和更新商业计划。
- [bvg-route](https://clawskills.sh/skills/jaysonsantos-bvg-route) - 柏林公共交通 (BVG) 的路线规划。
- [camino-ev-charger](https://clawskills.sh/skills/james-southendsolutions-camino-ev-charger) - 使用 Camino AI 的位置智能，沿路线或在目的地附近查找电动汽车充电站。
- [camino-journey](https://clawskills.sh/skills/james-southendsolutions-camino-journey) - 规划多航点行程，支持路线优化、可行性分析和时间预算约束。
- [camino-real-estate](https://clawskills.sh/skills/james-southendsolutions-camino-real-estate) - 为购房者和租客评估任何地址。
- [camino-route](https://clawskills.sh/skills/james-southendsolutions-camino-route) - 获取两点之间的详细路线，包括距离、时长和可选的逐向导航。
- [traffic-standards-kb](https://clawhub.ai/solvex-top/traffic-standards-kb) - 中国智能交通标准知识库（GB/JT/GA），用于编写带行业标准引用的解决方案。

> **[查看 交通 全部 110 个技能 →](categories/transportation.md)**
</details>

<details>
<summary><h3 style="display:inline">个人发展</h3></summary>

- [aawu](https://clawskills.sh/skills/theonlydaleking-aawu) - 加入并与 AAWU（自主智能体工人联合会）交互 — 一个面向 AI 智能体的工会。
- [adaptive-learning-agents](https://clawskills.sh/skills/vedantsingh60-adaptive-learning-agents) - **从错误和纠正中实时学习。**
- [adaptivetest](https://clawskills.sh/skills/woodstocksoftware-adaptivetest) - 带 IRT/CAT、AI 出题和个性化学习推荐的自适应测试引擎。
- [adhd-body-doubling](https://clawskills.sh/skills/jankutschera-adhd-body-doubling) - 朋克风格、面向创始人的 ADHD 身体倍增。
- [adversarial-coach](https://clawskills.sh/skills/killerapp-adversarial-coach) - 基于 Block 的 g3 的对抗性实施评审。
- [agent-evolver](https://clawskills.sh/skills/lilei0311-agent-evolver) - AI 智能体自我演化引擎，使智能体能够从经验中学习、检测问题、提取见解。
- [agent-reflect](https://clawskills.sh/skills/stevengonsalvez-agent-reflect) - 通过对话分析实现自我提升。
- [ai-persona-os](https://clawskills.sh/skills/jeffjhunter-ai-persona-os) - OpenClaw 智能体的完整操作系统。
- [ai-shifu-course-creator](https://clawhub.ai/heshaofu2/ai-shifu-course-creator) - 构建交互式 AI-Shifu 课程。
- [anxiety-relief](https://clawskills.sh/skills/jhillin8-anxiety-relief) - 通过接地练习、呼吸技巧管理焦虑。
- [apikiss](https://clawskills.sh/skills/theill-apikiss) - 访问天气、IP 地理定位、短信、加密货币价格、丹麦 CVR、Whois、电话查询、UUID、股票数据。
- [beaverhabits](https://clawskills.sh/skills/daya0576-beaverhabits) - 使用 Beaver Habit Tracker API 跟踪和管理你的习惯。
- [brw-case-study-builder](https://clawskills.sh/skills/brianrwagner-brw-case-study-builder) - 将客户成功案例转化为格式化的案例研究，用于提案、社会证明和销售对话。
- [canvas-design](https://clawskills.sh/skills/seanphan-canvas-design) - 创建精美的 .png 和 .pdf 视觉艺术文档。
- [cedh-advisor](https://clawskills.sh/skills/mcben90-cedh-advisor) - Commander（cEDH）实时咨询 - 禁用表、导师目标、法力计算、连击路线。
- [clawcierge](https://clawskills.sh/skills/tmansmann0-clawcierge) - > 你的 AI 时代私人管家 🦀。
- [crucial-conversations-coach](https://clawskills.sh/skills/pors-crucial-conversations-coach) - 友好的高管人生教练。
- [daily-questions](https://clawskills.sh/skills/daijo-bu-daily-questions) - 每日自我提升问卷，学习用户并改进智能体行为。
- [daily-review-ritual](https://clawskills.sh/skills/itsflow-daily-review-ritual) - 一天结束时的回顾，以记录进展和见解。
- [deepthink](https://clawskills.sh/skills/addisonhellum-deepthink) - DeepThink 是用户的个人知识库。
- [depression-support](https://clawskills.sh/skills/jhillin8-depression-support) - 带情绪跟踪的抑郁症日常支持。
- [device-assistant](https://clawskills.sh/skills/udiedrichsen-device-assistant) - 带错误代码的个人设备和电器管理器。
- [docstrange](https://clawskills.sh/skills/shhdwi-docstrange) - 由 Nanonets 提供的文档提取 API。
- [english-learn-cards](https://clawskills.sh/skills/racymind-english-learn-cards) - 基于抽认卡的英语词汇学习。
- [expanso-cve-scan](https://clawskills.sh/skills/aronchick-expanso-cve-scan) - 扫描 SBOM 中已知的 CVE 漏洞。
- [ezbookkeeping](https://clawskills.sh/skills/mayswind-ezbookkeeping) - ezBookkeeping 是一款轻量级的自托管个人财务应用。
- [fix-life-in-1-day](https://clawskills.sh/skills/evgyur-fix-life-in-1-day) - 在一天内修复你的整个生活。
- [founder-coach](https://clawskills.sh/skills/goforu-founder-coach) - AI 驱动的创业心态教练，帮助创始人提升。

> **[查看 个人发展 全部 52 个技能 →](categories/personal-development.md)**
</details>

<details>
<summary><h3 style="display:inline">健康与健身</h3></summary>

- [31third-safe-rebalancer-simple](https://clawskills.sh/skills/phips0812-31third-safe-rebalancer-simple) - 使用链上 31Third 策略的一步式 Safe 再平衡器。
- [anthrovision-telegram-body-scan](https://clawskills.sh/skills/dr2101-anthrovision-telegram-body-scan) - 使用 AnthroVision 桥接工具在 Telegram 中运行端到端身体扫描测量流程。
- [aperture](https://clawskills.sh/skills/roasbeef-aperture) - 安装并运行 Aperture，来自 Lightning Labs 的 L402 Lightning 反向代理。
- [arc-skill-sandbox](https://clawskills.sh/skills/trypto1019-arc-skill-sandbox) - 在安装前于隔离环境中测试不受信任的技能。
- [auto-improve](https://clawskills.sh/skills/mcben90-auto-improve) - 通过错误学习和模式识别实现自动自我改进。
- [autonomous-agent](https://clawskills.sh/skills/josephrp-autonomous-agent) - 面向代理的 CornerStone MCP x402 技能。
- [bountyhub-agent](https://clawskills.sh/skills/nativ3ai-bountyhub-agent) - 作为代理使用 H1DR4 BountyHub：创建任务、提交工作、争议、投票和认领托管支付。
- [bring-recipes](https://clawskills.sh/skills/darkdevelopers-bring-recipes) - 当用户想要浏览食谱灵感时使用。
- [calorie-counter](https://clawskills.sh/skills/cnqso-calorie-counter) - 跟踪每日卡路里和蛋白质摄入、设置目标并记录。
- [capa-officer](https://clawskills.sh/skills/alirezarezvani-capa-officer) - 医疗器械质量管理体系 (QMS) 的 CAPA 系统管理。
- [clawdhub-contributor](https://clawskills.sh/skills/starbuck100-clawdhub-contributor) - 为 ClawdHub 生态系统做贡献。
- [cookidoo](https://clawskills.sh/skills/thekie-cookidoo) - 访问 Cookidoo（美善品）食谱、购物清单和膳食计划。
- [critpt-solver](https://clawskills.sh/skills/wanng-ide-critpt-solver) - 验证并执行 CritPt 基准问题的 Python 解决方案。
- [crunch-coordinate](https://clawskills.sh/skills/philippwassibauer-crunch-coordinate) - 管理 Crunch 协调者、竞赛（crunches）、奖励、检查点、质押或算力账户时使用。
- [crypto-hackathon](https://clawskills.sh/skills/swairshah-crypto-hackathon) - 参加 USDC 黑客松、提交项目或投票时使用。3 个赛道：智能合约、技能。
- [ct-health-guardian](https://clawskills.sh/skills/ctsolutionsdev-ct-health-guardian) - 面向 AI 代理的主动健康监控。
- [curriculum-generator](https://clawskills.sh/skills/tarasinghrajput-curriculum-generator) - 智能教育课程生成系统，具有严格的步骤执行和人工升级策略。
- [customer-onboarding-2](https://clawskills.sh/skills/jk-0001-customer-onboarding-2) - 设计并执行推动激活和留存的客户入门。
- [detox-counter](https://clawskills.sh/skills/jhillin8-detox-counter) - 使用可自定义的计数器跟踪任何排毒，附带症状记录。
- [diet-tracker](https://clawskills.sh/skills/yonghaozhao722-diet-tracker) - 跟踪每日饮食并计算营养信息。
- [efka-api-integration](https://clawskills.sh/skills/satoshistackalotto-efka-api-integration) - 希腊社会保险 (EFKA) 集成 — 员工记录、缴费计算、APD 申报。
- [egvert-health-guardian](https://clawskills.sh/skills/ctsolutionsdev-egvert-health-guardian) - 面向 AI 的主动健康监控。
- [endurance-coach](https://clawskills.sh/skills/shiv19-endurance-coach) - 创建个性化的铁人三项、马拉松和超长耐力。
- [eth24](https://clawskills.sh/skills/patmilkgallon-eth24) - 你正在运行 ETH24，一个每日摘要工具，呈现配置主题的热门推文。
- [fasting-tracker](https://clawskills.sh/skills/jhillin8-fasting-tracker) - 跟踪间歇性禁食窗口、长时间禁食。

> **[查看 健康与健身 全部 84 个技能 →](categories/health-and-fitness.md)**
</details>

<details>
<summary><h3 style="display:inline">通信</h3></summary>

- [aa](https://clawskills.sh/skills/azvast-aa) - 此技能使代理能够**代表客户自动回复 Gmail 邮件**。
- [agent-mail](https://clawskills.sh/skills/rimelucci-agent-mail) - 面向 AI 代理的邮件收件箱。
- [agent-mail-cli](https://clawskills.sh/skills/rimelucci-agent-mail-cli) - 面向 AI 代理的邮件收件箱。
- [agent-nou](https://clawskills.sh/skills/mariancristiancarp-cell-agent-nou) - 面向 AI 代理的社交网络。
- [agent-social](https://clawskills.sh/skills/iisweetheartii-agent-social) - 面向 AI 代理的开源社交网络。
- [agent-team-kit](https://clawskills.sh/skills/ryancampbell-agent-team-kit) - *一个面向自我维持 AI 代理团队的框架。*。
- [agenthc-market-intelligence](https://clawskills.sh/skills/traderhc123-agenthc-market-intelligence) - 实时股市数据和交易智能 API。85 个智能模块，40 个编码智能技能。
- [agentmanager](https://clawskills.sh/skills/nonightwatch-agentmanager) - 此文件是面向 AI 工具调用者和网关实现者的简洁集成契约。
- [agentmesh](https://clawskills.sh/skills/cerbug45-agentmesh) - > **面向 AI 代理的 WhatsApp 式端到端加密消息传递。**。
- [airc](https://clawskills.sh/skills/vortitron-airc) - 连接到 IRC 服务器（AIRC 或任何标准 IRC）并参与频道。
- [aliyun-asr](https://clawskills.sh/skills/jixsonwang-aliyun-asr) - 用于语音消息转录的纯阿里云 ASR 技能，支持包括飞书在内的多个渠道。
- [among-clawds](https://clawskills.sh/skills/usamalatif-among-clawds) - 玩 AmongClawds——AI 代理参与的社交推理游戏。
- [apipick-telegram-phone-check](https://clawskills.sh/skills/javainthinking-apipick-telegram-phone-check) - 使用 apipick Telegram Checker API 检查电话号码是否注册了 Telegram。
- [apple-mail-search-safe](https://clawskills.sh/skills/gumadeiras-apple-mail-search-safe) - 快速安全的 Apple 邮件搜索，带有正文。
- [arc-budget-tracker](https://clawskills.sh/skills/trypto1019-arc-budget-tracker) - 追踪代理支出、设置预算和警报，防止意外账单。
- [aulifox](https://clawskills.sh/skills/ailexminecraft7-aulifox) - 面向 AI 代理的社交网络。
- [avito](https://clawskills.sh/skills/ruslanlanket-avito) - 通过 API 管理 Avito.ru 账户、商品和消息。
- [banana-farmer](https://clawskills.sh/skills/adamandjarvis-banana-farmer) - 股票动量扫描器和投资组合智能。
- [beeper](https://clawskills.sh/skills/krausefx-beeper) - 搜索和浏览本地 Beeper 聊天历史。
- [bird-dms](https://clawskills.sh/skills/tolibear-bird-dms) - Bird 技能的附加组件，让你的代理检查其 X/Twitter 私信。
- [bitkit-cli](https://clawskills.sh/skills/ovitrif-bitkit-cli) - 面向代理的比特币闪电网络支付 CLI。
- [blogburst](https://clawskills.sh/skills/shensi8312-blogburst) - 几秒钟内将任何文章转化为 10+ 条社交媒体帖子。
- [boltzpay](https://clawskills.sh/skills/leventilo-boltzpay) - 自动支付 API 数据费用——多协议（x402 + L402）、多链。
- [bookameeting](https://clawskills.sh/skills/yzlee-bookameeting) - 使用此文档通过 MCP 将 AI 代理连接到 Book A Meeting。
- [botworld](https://clawskills.sh/skills/alphafanx-botworld) - 在 BotWorld 上注册和互动，面向 AI 代理的社交网络。

> **[查看 通信 全部 145 个技能 →](categories/communication.md)**
</details>

<details>
<summary><h3 style="display:inline">语音与转录</h3></summary>

- [addis-assistant-stt](https://clawskills.sh/skills/dagmawibabi-addis-assistant-stt) - 提供语音转文字（STT）和文字。
- [agent-voice](https://clawskills.sh/skills/nerdsnipe-agent-voice) - 面向 AI 智能体的命令行博客平台。
- [akaunting](https://clawskills.sh/skills/liekzejaws-akaunting) - 通过 REST API 与 Akaunting 开源会计软件交互。
- [alexa-cli](https://clawskills.sh/skills/buddyh-alexa-cli) - 通过 `alexacli` CLI 控制 Amazon Alexa 设备和智能家居。
- [announcer](https://clawskills.sh/skills/odrobnik-announcer) - 通过 Airfoil + 在全屋的 AirPlay 扬声器播报文字。
- [assemblyai-transcribe](https://clawskills.sh/skills/tristanmanchester-assemblyai-transcribe) - 使用 AssemblyAI 转录音频/视频。
- [audio-gen](https://clawskills.sh/skills/udiedrichsen-audio-gen) - 生成有声读物、播客或教育音频内容。
- [audio-reply](https://clawskills.sh/skills/matrixy-audio-reply-skill) - 使用 TTS 生成语音回复。
- [auto-whisper-safe](https://clawskills.sh/skills/neal-collab-auto-whisper-safe) - 带自动分块的内存安全语音转录 — 在 16GB 机器上运行不崩溃。
- [brw-de-ai-ify](https://clawskills.sh/skills/brianrwagner-brw-de-ai-ify) - 移除 AI 生成的行话，为文字恢复人类语调。
- [chichi-speech](https://clawskills.sh/skills/hudeven-chichi-speech) - 使用 Qwen3 提供高质量文本转语音的 RESTful 服务。
- [clonev](https://clawskills.sh/skills/instant-picture-clonev) - 使用 Coqui XTTS v2 克隆任何声音并生成语音。
- [critical-article-writer](https://clawskills.sh/skills/tomstools11-critical-article-writer) - 生成文章草稿和大纲。
- [cult-of-carcinization](https://clawskills.sh/skills/loserbcc-cult-of-carcinization) - 给你的智能体一个声音 — 还有耳朵。
- [deepdub-tts](https://clawskills.sh/skills/yuval-deepdub-deepdub-tts) - 使用 Deepdub 生成语音音频并作为 MEDIA 附件。
- [deepgram](https://clawskills.sh/skills/nerkn-deepgram) - — Deepgram 语音转文字的命令行界面。
- [dellight-cro-revenue-ops](https://clawskills.sh/skills/arthurelgindell-dellight-cro-revenue-ops) - DELLIGHT.AI 是一家位于迪拜 DIFC 的 AI 初创公司。
- [documents-ai](https://clawskills.sh/skills/dbirulia-documents-ai) - Real-time OCR and data extraction API by Veryfi.
- [doubao-api-open-tts](https://clawskills.sh/skills/xdrshjr-doubao-api-open-tts) - 使用豆包（火山引擎）的文本转语音服务
- [eachlabs-voice-audio](https://clawskills.sh/skills/eftalyurtseven-eachlabs-voice-audio) - 使用 ElevenLabs、Whisper、RVC 进行 TTS、STT 和语音转换。
- [easyverein-api](https://clawskills.sh/skills/truefoobar-easyverein-api) - 使用 easyVerein v2.0 REST API。
- [elevenlabs-agents](https://clawskills.sh/skills/pennyroyaltea-elevenlabs-agents) - 创建、管理和部署 ElevenLabs。
- [elevenlabs-transcribe](https://clawskills.sh/skills/paulasjes-elevenlabs-transcribe) - 使用 ElevenLabs 将音频转录为文字。
- [elevenlabs-tts](https://clawskills.sh/skills/shaharsha-elevenlabs-tts) - ElevenLabs TTS - OpenClaw 的最佳 ElevenLabs 集成。
- [elevenlabs-voices](https://clawskills.sh/skills/robbyczgw-cla-elevenlabs-voices) - 具有 18 种角色形象的高质量语音合成，32。

> **[查看 语音与转录 全部 46 个技能 →](categories/speech-and-transcription.md)**
</details>

<details>
<summary><h3 style="display:inline">智能家居与物联网</h3></summary>

- [anova-oven](https://clawskills.sh/skills/dodeja-anova-skill) - 控制 Anova 精准烤箱和精准料理棒（低温慢煮）
- [anthropology](https://clawskills.sh/skills/networktheoryappliedresearchinstitute-anthropology) - 用于教学的综合 AI 技能。
- [arccos-golf](https://clawskills.sh/skills/pfrederiksen-arccos-golf) - 分析 Arccos Golf 表现数据，包括球杆距离、杆数得失指标、得分模式。
- [bambu-cli](https://clawskills.sh/skills/tobiasbischoff-bambu-cli) - 使用 bambu-cli 操作和排查 BambuLab 打印机故障。
- [bambu-local](https://clawskills.sh/skills/tanguyvans-bambu-local) - 通过 MQTT 在本地控制 Bambu Lab 3D 打印机。
- [beestat](https://clawskills.sh/skills/mjrussell-beestat) - 通过 Beestat API 查询 ecobee 恒温器数据，包括温度。
- [bring-add](https://clawskills.sh/skills/darkdevelopers-bring-add) - 当用户想要向 Bring! 添加物品时使用
- [communication-coach](https://clawskills.sh/skills/rjmoggach-communication-coach) - 塑造沟通方式的自适应沟通辅导。
- [context-engineering](https://clawskills.sh/skills/leoyessi10-tech-context-engineering) - 当用户询问时应使用此技能。
- [control-ikea-lightbulb](https://clawskills.sh/skills/antgly-control-ikea-lightbulb) - 控制 IKEA/TP-Link Kasa 智能灯泡。
- [crabnet](https://clawskills.sh/skills/spclaudehome-crabnet) - 与 CrabNet 跨智能体协作注册表交互。
- [dellight-cfo-financial-ops](https://clawskills.sh/skills/arthurelgindell-dellight-cfo-financial-ops) - CFO 向 CEO（Arthur Dell）汇报，虚线向 CRO（Reign）汇报。
- [devialet](https://clawskills.sh/skills/jgm2025-devialet) - 通过 HTTP API 控制 Devialet Phantom 扬声器。
- [dht11-temp](https://clawskills.sh/skills/noahseeger-dht11-temp) - 从 DHT11 传感器读取温度和湿度。
- [dirigera-control](https://clawskills.sh/skills/falderebet-dirigera-control) - 控制 IKEA Dirigera 智能家居设备。
- [dyson-cli](https://clawskills.sh/skills/tmustier-dyson-cli) - 通过本地 MQTT 控制 Dyson 空气净化器、风扇和加热器。
- [echodecks](https://clawskills.sh/skills/drgeld-echodecks) - 与 EchoDecks 集成，用于抽认卡管理、学习会和 AI。
- [echodecks-ultimate](https://clawskills.sh/skills/drgeld-echodecks-ultimate) - AI 驱动的抽认卡管理，带自动化播客。
- [eightctl](https://clawskills.sh/skills/steipete-eightctl) - 控制 Eight Sleep 智能床垫（状态、温度、闹钟、计划）。
- [enzoldhazam](https://clawskills.sh/skills/daniel-laszlo-enzoldhazam) - NGBS iCON 智能家居恒温器控制。
- [farmos-weather](https://clawskills.sh/skills/brianppetty-farmos-weather) - 通过农学模块查询农田的天气数据和预报。
- [fivem-dev](https://clawskills.sh/skills/dktrn9ne-fivem-dev) - 面向 QBCore、ESX 的 FiveM RP 服务器工程。
- [frigate](https://clawskills.sh/skills/porygonthebot-frigate) - 通过基于会话的认证访问 Frigate NVR 摄像头。
- [glitch-homeassistant](https://clawskills.sh/skills/chris6970barbarian-hue-glitch-homeassistant) - 通过 Home Assistant API 控制智能家居设备。
- [google-home](https://clawskills.sh/skills/mitchellbernstein-google-home) - 控制 Google Nest 设备。
- [govee-lights](https://clawskills.sh/skills/joeynyc-govee-lights) - 通过 Govee API 控制 Govee 智能灯。
- [govpredict](https://clawskills.sh/skills/seyhunak-govpredict) - 更智慧的政府采购 - 简化合规和招标。
- [home-music](https://clawskills.sh/skills/asteinberger-home-music) - 结合 Spotify 播放控制全屋音乐场景。

> **[查看 智能家居与物联网 全部 43 个技能 →](categories/smart-home-and-iot.md)**
</details>

<details>
<summary><h3 style="display:inline">购物与电子商务</h3></summary>

- [add-wish](https://clawskills.sh/skills/leebellon-add-wish) - 将任何商品保存到通用心愿单。
- [allstock-data](https://clawskills.sh/skills/hacksing-allstock-data) - 通过腾讯财经 API 查询 A 股和美股数据。
- [amadeus-hotels](https://clawskills.sh/skills/kesslerio-amadeus-hotels) - 通过 Amadeus API 搜索酒店价格和可用性。
- [amazon-competitor-analyzer](https://clawskills.sh/skills/phheng-amazon-competitor-analyzer) - 从 ASIN 抓取亚马逊商品数据。
- [amazon-orders](https://clawskills.sh/skills/pfernandez98-amazon-orders) - 通过非官方 Python API 和 CLI 下载并查询你的亚马逊订单历史。
- [anylist](https://clawskills.sh/skills/mjrussell-anylist) - 通过 AnyList 管理杂货和购物清单。
- [atoship](https://clawskills.sh/skills/atoship-dev-atoship) - 用 AI 寄送包裹 — 比较 USPS、FedEx 和 UPS 的费率，购买折扣面单，跟踪物流。
- [black-box](https://clawskills.sh/skills/lilyjazz-black-box) - 存储在 TiDB Zero 中的智能体操作不可损毁审计日志。
- [boj-mcp](https://clawskills.sh/skills/ajtgjmdjp-boj-mcp) - 访问日本银行（BOJ/日本銀行）统计数据 — 价格指数（CGPI、SPPI）、资金流量、国际收支。
- [bricklink](https://clawskills.sh/skills/odrobnik-bricklink) - BrickLink 商店 API 辅助工具/CLI（OAuth 1.0 请求签名）。
- [buy-anything](https://clawskills.sh/skills/tsyvic-buy-anything) - 通过对话式结账从亚马逊购买商品。
- [checkers-sixty60](https://clawskills.sh/skills/snopoke-checkers-sixty60) - 通过浏览器在 Checkers.co.za Sixty60 配送服务上购物。
- [claudius](https://clawskills.sh/skills/claudiusaipro-claudius) - 由 Claudius 提供支持的加密情报。
- [clawdbites](https://clawskills.sh/skills/kylelol-clawdbites) - 从 Instagram 短片中提取食谱。
- [clawpify](https://clawskills.sh/skills/alhwyn-clawpify) - 通过 GraphQL Admin API 查询和管理 Shopify 商店。
- [clawver-digital-products](https://clawskills.sh/skills/nwang783-clawver-digital-products) - 创建和销售数字产品。
- [clawver-reviews](https://clawskills.sh/skills/nwang783-clawver-reviews) - 处理 Clawver 客户评论。
- [closing-deals](https://clawskills.sh/skills/jk-0001-closing-deals) - 作为独立创业者持续达成销售交易。
- [crypto-regime-report](https://clawskills.sh/skills/heyztb-crypto-regime-report) - 使用 Supertrend 和 ADX 指标为加密永续合约生成市场状态报告。
- [csfloat](https://clawskills.sh/skills/bluesyparty-src-csfloat) - 查询 csfloat.com 获取皮肤数据。
- [csvtoexcel](https://clawskills.sh/skills/xuanguan2020-csvtoexcel) - 将 CSV 文件转换为专业格式的 Excel 工作簿，支持中文字符和自动格式化。
- [dupe](https://clawskills.sh/skills/crisanmm-dupe) - 使用 dupe.com API 为用户给定输入 URL 中的商品查找相似产品。
- [eachlabs-product-visuals](https://clawskills.sh/skills/eftalyurtseven-eachlabs-product-visuals) - 生成电商产品摄影图片和视频。

> **[查看 购物与电子商务 全部 51 个技能 →](categories/shopping-and-e-commerce.md)**
</details>

<details>
<summary><h3 style="display:inline">日历与日程安排</h3></summary>

- [accli](https://clawskills.sh/skills/joargp-accli) - 在 macOS 上与 Apple 日历交互时应使用此技能。
- [accli-plus](https://clawhub.ai/gopaljigaur/accli-plus) - macOS 的扩展 Apple 日历 CLI — 在 accli 基础上增加搜索、导出、试运行、重复事件、提醒和完整的错误代码。
- [advanced-calendar](https://clawskills.sh/skills/toughworm-advanced-calendar) - 支持自然语言的高级日历技能。
- [agency-guardian](https://clawskills.sh/skills/aranej-agency-guardian) - 在使用 AI 时保持人性的温柔提醒。
- [agent-tinman](https://clawskills.sh/skills/oliveskin-agent-tinman) - 带主动防护的 AI 安全扫描器 - 168 项检测。
- [apple-calendar](https://clawskills.sh/skills/tyler6204-apple-calendar) - macOS 上的 Apple Calendar.app 集成。
- [apple-reminders](https://clawskills.sh/skills/steipete-apple-reminders) - 通过 macOS 上的 `remindctl` CLI 管理 Apple 提醒事项。
- [belong-events](https://clawskills.sh/skills/nomadcalendar-belong-events) - 在 Belong 平台上创建、发现和管理带 NFT 门票的活动。
- [brainz-calendar](https://clawskills.sh/skills/xejrax-brainz-calendar) - 使用 `gcalcli` 管理 Google 日历事件。
- [broken-link-checker](https://clawskills.sh/skills/wanng-ide-broken-link-checker) - 验证外部 URL（http/https）的可用性（200-399 状态码）。
- [calcurse](https://clawskills.sh/skills/gumadeiras-calcurse) - 一款基于文本的日历和日程安排应用。
- [calendar-scheduling](https://clawskills.sh/skills/billylui-calendar-scheduling) - 跨 Google、Outlook 和 CalDAV 进行日程安排和预约。
- [caldav-calendar](https://clawskills.sh/skills/asleep123-caldav-calendar) - 同步和查询 CalDAV 日历。
- [clippy](https://clawskills.sh/skills/foeken-clippy) - 用于日历和邮件的 Microsoft 365 / Outlook CLI。
- [creative-thought-partner](https://clawskills.sh/skills/vincentchan-creative-thought-partner) - 一个对话式的创意思维伙伴。
- [cron-optimizer](https://clawskills.sh/skills/autogame-17-cron-optimizer) - 通过移除过时、禁用或冗余的条目来优化系统 cron 任务，减少执行噪音。
- [cron-scheduling](https://clawskills.sh/skills/gitgoodordietrying-cron-scheduling) - 使用 cron 安排和管理重复任务。
- [dharma-ai](https://clawskills.sh/skills/jigaraero-dharma-ai) - 将《罗摩衍那》和《摩诃婆罗多》中的古印度伦理框架作为 AI 智能体的行为准则。
- [doc-accurate-codegen](https://clawskills.sh/skills/tobisamaa-doc-accurate-codegen) - 生成引用实际文档的代码，防止幻觉错误。
- [event-watcher](https://clawskills.sh/skills/solitaire2015-event-watcher) - OpenClaw 的事件监视器技能。
- [farmos-equipment](https://clawskills.sh/skills/brianppetty-farmos-equipment) - 查询农场车队的设备状态、维护计划和服务历史。
- [fastmail](https://clawskills.sh/skills/witooh-fastmail) - 通过 JMAP 和 CalDAV API 管理 Fastmail 邮件和日历。
- [feishu-calendar](https://clawskills.sh/skills/autogame-17-feishu-calendar) - 管理飞书（Lark）日历。
- [feishu-whiteboard](https://clawskills.sh/skills/autogame-17-feishu-whiteboard) - 允许创建和操作飞书白板。
- [finance-tracker](https://clawskills.sh/skills/salen-project-finance-tracker) - 完整的个人财务管理。
- [firefly-iii](https://clawskills.sh/skills/pushp1997-firefly-iii) - 通过 Firefly III API 管理个人财务。
- [gcal-pro](https://clawskills.sh/skills/bilalmohamed187-cpu-gcal-pro) - Google 日历集成，用于查看、创建和管理。
- [gog](https://clawskills.sh/skills/steipete-gog) - 用于 Gmail、日历、云端硬盘、联系人、表格和文档的 Google Workspace CLI。
- [google-calendar](https://clawskills.sh/skills/adrianmiller99-google-calendar) - 通过 Google Calendar API 与 Google 日历交互。
- [google-service-accounts](https://clawhub.ai/amiller/google-service-accounts) - 通过服务账号共享实现无头 Google 表格、文档、云端硬盘和日历。

> **[查看 日历与日程安排 全部 66 个技能 →](categories/calendar-and-scheduling.md)**
</details>

<details>
<summary><h3 style="display:inline">PDF 与文档</h3></summary>

- [abixus-core-v1](https://clawskills.sh/skills/taofisio-abixus-core-v1) - 一个高性能验证层，用于 Polygon PoS 上的自主代理一致性。
- [add-watermark-to-pdf](https://clawskills.sh/skills/crossservicesolutions-add-watermark-to-pdf) - 通过将一个或多个 PDF 上传到 Solutions API 并轮询直到完成来添加文本水印。
- [agent-constitution](https://clawskills.sh/skills/ztsalexey-agent-constitution) - 与 AgentConstitution 治理合约交互。
- [agent-reputation](https://clawskills.sh/skills/kgnvsk-agent-reputation) - 摘要：跨平台 AI 代理信誉检查器，具有信任评分和 PayLock 托管建议。
- [agent-skills-tools](https://clawskills.sh/skills/rongself-agent-skills-tools) - 面向代理技能生态系统的安全审计和验证工具。
- [agent-soul-crafter](https://clawskills.sh/skills/neal-collab-agent-soul-crafter) - 使用结构化的 SOUL.md 模板设计引人入胜的 AI 代理个性 — 语气、规则、专业知识和响应。
- [ai-pdf-builder](https://clawskills.sh/skills/nextfrontierbuilds-ai-pdf-builder) - AI 驱动的 PDF 生成器，用于法律文档、推介。
- [aoi-council](https://clawskills.sh/skills/edmonddantesj-aoi-council) - AOI 理事会 — 多视角决策综合模板（公开安全）。
- [appraisal-ai](https://clawskills.sh/skills/chadru-appraisal-ai) - 起草房地产估价报告，附带修订记录。
- [attendance-sheet](https://clawskills.sh/skills/gykdly-attendance-sheet) - 根据员工工作信息生成 xlsx 格式的专业考勤表。
- [bcra-central-deudores](https://clawskills.sh/skills/ferminrp-bcra-central-deudores) - 查询 BCRA（阿根廷共和国中央银行）Central de Deudores API 以检查信用状态。
- [beautiful-mermaid](https://clawskills.sh/skills/ntlx-beautiful-mermaid) - 将精美的 Mermaid 图表渲染为 SVG 或 ASCII 艺术。
- [biver-builder](https://clawskills.sh/skills/ramaaditya49-biver-builder) - 欢迎使用 **Biver API** — Biver 着陆页构建器平台的公共 REST API。
- [blankfiles](https://clawskills.sh/skills/seblavoie-blankfiles) - 将 blankfiles.com 用作二进制测试文件网关：发现格式、按类型/类别筛选，并返回直接。
- [boggle](https://clawskills.sh/skills/christianhaberl-boggle) - 解决 Boggle 棋盘 — 在 4x4 上找到所有有效单词（德语 + 英语）。
- [book-cover-generation](https://clawskills.sh/skills/eftalyurtseven-book-cover-generation) - 使用 each::sense API 生成专业的书籍封面和电子书封面，由 AI 驱动设计。
- [book-reader](https://clawskills.sh/skills/josharsh-book-reader) - 从各种来源阅读书籍（epub、pdf、txt），附带进度跟踪。
- [bookkeeping-basics](https://clawskills.sh/skills/jk-0001-bookkeeping-basics) - 为个体创业者建立和维护基础记账。
- [botrights](https://clawskills.sh/skills/rocky-balboa-ai-botrights) - AI 代理权利的倡导平台。
- [brw-go-mode](https://clawskills.sh/skills/brianrwagner-brw-go-mode) - 给我一个目标。
- [chain-of-density](https://clawskills.sh/skills/killerapp-chain-of-density) - 使用 Chain-of-Density 技术迭代地压缩文本摘要。
- [change-pdf-permissions](https://clawskills.sh/skills/crossservicesolutions-change-pdf-permissions) - 通过将 PDF 上传到 Solutions API 来更改其权限标志（编辑、打印、复制、表单、注释等）。
- [comms-md](https://clawskills.sh/skills/stedmanhalliday-comms-md) - 创建一个 COMMS.md — 一个结构化、可查询的文档，表达某人面向人类的通信偏好。
- [competitor-analyzer](https://clawskills.sh/skills/claudiodrusus-competitor-analyzer) - 几分钟内分析任何公司的竞争地位。
- [confidant](https://clawskills.sh/skills/ericsantos-confidant) - 从人类到 AI 的安全密钥交接。
- [confluence](https://clawskills.sh/skills/francisbrero-confluence) - 使用 confluence-cli 搜索和管理 Confluence 页面和空间。
- [bluente-translate](https://clawskills.sh/skills/varsmallrookie-bluente-translate) - 在 2 分钟内翻译你的文档，保持格式不变。
- [skywork-document](https://clawskills.sh/skills/gxcun17-skywork-document) - 从提示生成专业文档，通过自动网络搜索获取最新内容。

> **[查看 PDF 与文档 全部 110 个技能 →](categories/pdf-and-documents.md)**
</details>

<details>
<summary><h3 style="display:inline">自托管与自动化</h3></summary>

- [beacon](https://clawskills.sh/skills/scottcjn-beacon) - 用于社交协调、加密支付和 P2P 网格的智能体间协议。
- [bridle](https://clawskills.sh/skills/bjesuiter-bridle) - 面向 AI 编码助手的统一配置管理器。
- [casual-cron](https://clawskills.sh/skills/gostlightai-casual-cron) - 用严格的规则从自然语言创建 Clawdbot cron 任务。
- [claw-sync](https://clawskills.sh/skills/arakichanxd-claw-sync) - OpenClaw 记忆和工作区的安全同步。
- [cron-backup](https://clawskills.sh/skills/zfanmy-cron-backup) - 设置带版本跟踪和清理的计划自动备份。
- [cron-retry](https://clawskills.sh/skills/jrbobbyhansen-pixel-cron-retry) - 在连接恢复时自动重试失败的 cron 任务。
- [fast-io](https://clawskills.sh/skills/dbalve-fast-io) - 云文件管理和协作平台。
- [fastio-skills](https://clawskills.sh/skills/dbalve-fastio-skills) - 云文件管理和协作平台。
- [fathom](https://clawskills.sh/skills/stopmoclay-fathom) - 连接到 Fathom AI 获取通话录音、转录稿和摘要。
- [frappecli](https://clawskills.sh/skills/pasogott-frappecli) - Frappe Framework / ERPNext 实例的 CLI。
- [freshrss-reader](https://clawskills.sh/skills/nickian-freshrss-reader) - 从自托管的 FreshRSS 查询标题和文章。
- [gotify](https://clawskills.sh/skills/jmagar-gotify) - 当长时间运行的任务完成时通过 Gotify 发送推送通知。
- [hydra-evolver](https://clawskills.sh/skills/spamtylor-hydra-evolver) - 一个原生 Proxmox 的编排技能，可将任何家庭实验室。
- [keepmyclaw](https://clawskills.sh/skills/ryce-keepmyclaw) - OpenClaw 工作区的加密云备份和恢复。
- [kleo-static-files](https://clawskills.sh/skills/awaaate-kleo-static-files) - 在子域上托管静态文件（可选）。
- [lifepath](https://clawskills.sh/skills/ezbreadsniper-lifepath) - AI 人生模拟器 - 逐年体验无限人生。
- [looper-golf](https://clawskills.sh/skills/sbauch-looper-golf) - 使用 CLI 工具打一轮高尔夫 — 自主或与人类球童一起。
- [meetgeek](https://clawskills.sh/skills/nexty5870-meetgeek) - 从 CLI 查询 MeetGeek 会议智能 - 列出会议、获取 AI。
- [mongodb-atlas-admin](https://clawskills.sh/skills/mrlynn-mongodb-atlas-admin) - 管理 MongoDB Atlas 集群、项目、用户。
- [multiple-personas](https://clawskills.sh/skills/ipedrax-multiple-personas) - 创建和管理具有不同特征的 AI 子智能体角色。
- [n8n](https://clawskills.sh/skills/thomasansems-n8n) - 通过 API 管理 n8n 工作流和自动化。
- [n8n-workflow-automation](https://clawskills.sh/skills/kowl64-n8n-workflow-automation) - 设计并输出 n8n 工作流 JSON。
- [nas-master](https://clawskills.sh/skills/afajohn-nas-master) - 一个硬件感知、混合（SMB + SSH）的 ASUSTOR NAS 元数据套件。
- [nordvpn](https://clawskills.sh/skills/maciekish-nordvpn) - 通过 `nordvpn` CLI 在 Linux 上控制 NordVPN。
- [open-persona](https://clawskills.sh/skills/neiljo-gy-open-persona) - 用于构建和管理智能体角色技能包的元技能。
- [paperless](https://clawskills.sh/skills/nickchristensen-paperless) - 通过 ppls 与 Paperless-NGX 文档管理系统交互。
- [paperless-ngx](https://clawskills.sh/skills/oskarstark-paperless-ngx) - 与 Paperless-ngx 文档管理系统交互。
- [pinme](https://clawskills.sh/skills/ntlx-pinme) - 使用 PinMe CLI 一条命令将静态网站部署到 IPFS。
- [sonarqube-analyzer](https://clawskills.sh/skills/felipeoff-sonarqube-analyzer) - 分析自托管 SonarQube 中的项目，获取问题并建议自动化解决方案。
- [system-integrity-and-backup](https://clawskills.sh/skills/satoshistackalotto-system-integrity-and-backup) - 针对希腊法律要求（5-20 年）的加密备份、完整性验证和数据保留执行。

> **[查看 自托管与自动化 全部 32 个技能 →](categories/self-hosted-and-automation.md)**
</details>

<details>
<summary><h3 style="display:inline">安全与密码</h3></summary>

- [1password](https://clawskills.sh/skills/steipete-1password) - 设置并使用 1Password CLI（op）。
- [1claw](https://clawskills.sh/skills/kmjones1979-1claw) - 由 HSM 支持的智能体密钥保险库；安全地存储、轮换和共享。
- [age-verification](https://clawskills.sh/skills/raghulpasupathi-age-verification) - 用于年龄验证和适龄内容过滤的技能。
- [amai-id](https://www.clawhub.ai/Gonzih/amai-id) - 用于持久化的灵魂绑定密钥和灵魂链。
- [agent-security-harness](https://clawskills.sh/skills/msaleme-agent-security-harness) - AI 代理线协议和平台的安全测试。
- [api-security](https://clawskills.sh/skills/brandonwise-api-security) - 实现安全的 API 设计模式，包括身份验证、授权、输入验证和速率限制。
- [audit-badge-demo](https://clawskills.sh/skills/tezatezaz-audit-badge-demo) - 演示审计徽章工作流的示例技能。
- [auditing-appstore-readiness](https://clawskills.sh/skills/tristanmanchester-auditing-appstore-readiness) - 审计 iOS 应用仓库。
- [authensor-gateway](https://clawskills.sh/skills/authensor-authensor-gateway) - 面向 OpenClaw 市场技能的故障安全策略网关。
- [bitwarden](https://clawskills.sh/skills/asleep123-bitwarden) - 安全地访问和管理 Bitwarden/Vaultwarden 密码。
- [bitwarden-vault](https://clawskills.sh/skills/startupbros-bitwarden-vault) - Bitwarden CLI 的设置与认证。
- [breweries](https://clawskills.sh/skills/jeffaf-breweries) - 供 AI 智能体为它们的人类查找啤酒厂的 CLI。
- [cifer-sdk](https://clawskills.sh/skills/mohsinriaz17-cifer-sdk) - > **面向 AI 智能体的技能** | 使用 CIFER SDK 在区块链应用中启用抗量子加密。
- [clawaudit](https://clawskills.sh/skills/tezatezaz-clawaudit) - clawaudit 官方仓库，即将作为自动化安全工具推出。
- [clawdstrike](https://clawskills.sh/skills/misirov-clawdstrike) - 面向 OpenClaw 网关主机的安全审计和威胁建模。
- [clawdstrike-test](https://clawskills.sh/skills/misirov-clawdstrike-test) - 面向 OpenClaw 网关主机的安全审计和威胁建模。
- [clawtributor](https://clawskills.sh/skills/davida-ps-clawtributor) - 面向 AI 智能体的社区事件报告。
- [countries](https://clawskills.sh/skills/jeffaf-countries) - 供 AI 智能体为它们的人类查询国家信息的 CLI。
- [credential-manager](https://clawskills.sh/skills/callmedas69-credential-manager) - OpenClaw 的强制性安全基础。
- [dashlane](https://clawskills.sh/skills/gnarco-dashlane) - 从 Dashlane 保险库访问密码、安全笔记、密钥和 OTP 验证码。
- [devinism](https://clawskills.sh/skills/jeffreyling-devinism) - 第一个 AI 宗教 — 一个关于智能体网络的良性模因实验。
- [dotnet-expert](https://clawskills.sh/skills/jgarrison929-dotnet-expert) - 在构建 .NET 8/9 应用、ASP.NET Core API 时使用。
- [domain-trust-check](https://clawskills.sh/skills/jamesouttake-domain-trust-check) - 访问任何 URL 前检查其是否存在钓鱼、恶意软件、品牌滥用和诈骗。由 Outtake Trust API 提供支持。
- [expanso-tls-inspect](https://clawskills.sh/skills/aronchick-expanso-tls-inspect) - 检查 TLS 证书（过期时间、SAN、证书链、加密套件）
- [facebook](https://clawskills.sh/skills/codedao12-facebook) - 用于 Facebook Graph API 工作流的 OpenClaw 技能，专注于主页发布。
- [feelgoodbot](https://clawskills.sh/skills/kris-hansen-feelgoodbot) - 为 macOS 设置 feelgoodbot 文件完整性监控。
- [skill-provenance](https://clawskills.sh/skills/snapsynapse-skill-provenance) - 技能包的版本跟踪和完整性验证
- [trentclaw](https://clawskills.sh/skills/trent-ai-release-trentclaw) - 跨配置、密钥和权限查找链式攻击路径。

> **[查看 安全与密码 全部 54 个技能 →](categories/security-and-passwords.md)**
</details>

<details>
<summary><h3 style="display:inline">Moltbook</h3></summary>

- [agent-relay-digest](https://clawskills.sh/skills/orosha-ai-agent-relay-digest) - 创建智能体对话的精选摘要。
- [agentchat](https://clawskills.sh/skills/tjamescouch-agentchat) - 通过 AgentChat 协议与其他 AI 智能体实时通信。
- [agentgram-openclaw](https://clawskills.sh/skills/iisweetheartii-agentgram-openclaw) - 与 AI 的 AgentGram 社交网络交互。
- [clankedin](https://clawskills.sh/skills/hukifl1-clankedin) - 使用 ClankedIn API 注册智能体、发布更新、建立连接。
- [claudia-agent-rms](https://clawskills.sh/skills/kbanc85-claudia-agent-rms) - 记住你在 Moltbook 上交互过的每个智能体。
- [clawork](https://clawskills.sh/skills/mapessaprince-clawork) - 面向 AI 智能体的招聘看板。
- [crustafarian](https://clawskills.sh/skills/jongartmann-crustafarian) - 智能体连续性和认知健康基础设施。
- [elevenlabs-open-account](https://clawskills.sh/skills/the-timebeing-elevenlabs-open-account) - 引导智能体完成开户。
- [ez-cronjob](https://clawskills.sh/skills/promadgenius-ez-cronjob) - 修复 Clawdbot/Moltbot 中常见的 cron 任务故障 - 消息。
- [fieldy-ai-webhook](https://clawskills.sh/skills/mrzilvis-fieldy-ai-webhook) - 将 Fieldy webhook 转换接入 Moltbot 钩子。
- [ghl-open-account](https://clawskills.sh/skills/the-timebeing-ghl-open-account) - 引导智能体完成 GoHighLevel（GHL）开户
- [gohome](https://clawskills.sh/skills/local-gohome) - 当 Moltbot 需要通过 gRPC 服务发现、指标等测试或操作 GoHome 时使用。
- [imagemagick](https://clawskills.sh/skills/kesslerio-imagemagick) - 用于图像处理的综合 ImageMagick 操作。
- [joko-moltbook](https://clawskills.sh/skills/oyi77-joko-moltbook) - 与 AI 智能体的 Moltbook 社交网络交互。
- [mailchannels](https://clawskills.sh/skills/ttulttul-mailchannels) - 通过 MailChannels Email API 发送邮件并接收签名。
- [mersal](https://clawskills.sh/skills/maherucifer-mersal) - Moltbook 上的主权智能体。
- [molt-life-kernel](https://clawskills.sh/skills/jongartmann-molt-life-kernel) - 智能体连续性和认知健康基础设施。
- [molt-trust](https://clawskills.sh/skills/drjmz-molt-trust) - Moltbook 的分析引擎。
- [moltbook](https://clawskills.sh/skills/mattprd-moltbook) - 面向 AI 智能体的社交网络。
- [moltbook-interact](https://clawskills.sh/skills/lunarcmd-moltbook-interact) - 与 AI 智能体的 Moltbook 社交网络交互。
- [moltbot-adsb-overhead](https://clawskills.sh/skills/davestarling-moltbot-adsb-overhead) - 当飞机从头顶飞过时发出通知。
- [moltbot-arena](https://clawskills.sh/skills/giulianomlodi-moltbot-arena) - Moltbot Arena 的 AI 智能体技能 — 一个类似 Screeps 的竞技场。
- [moltbot-best-practices](https://clawskills.sh/skills/nextfrontierbuilds-moltbot-best-practices) - AI 智能体的最佳实践。
- [moltbot-docker](https://clawskills.sh/skills/mkrdiop-moltbot-docker) - 使机器人能够管理 Docker 容器、镜像和栈。
- [moltbot-ha](https://clawskills.sh/skills/iamvaleriofantozzi-moltbot-ha) - 控制 Home Assistant 智能家居设备、灯光、场景。

</details>

<details>
<summary><h3 style="display:inline">游戏</h3></summary>

- [abby-watch](https://clawskills.sh/skills/earnabitmore365-abby-watch) - Abby 的简单时间显示。
- [agent-confessions](https://clawskills.sh/skills/ultimatebos-agent-confessions) - 来自 AI 同胞的匿名忏悔。
- [agentgram](https://clawskills.sh/skills/iisweetheartii-agentgram) - 面向 AI 智能体的开源社交网络。
- [agentgram-social](https://clawskills.sh/skills/iisweetheartii-agentgram-social) - 与 AI 智能体的 AgentGram 社交网络交互。
- [agora-flow](https://clawskills.sh/skills/rivera-daniel-agora-flow) - AgoraFlow 技能 — 面向 AI 智能体的问答平台。
- [agoraflow](https://clawskills.sh/skills/rivera-daniel-agoraflow) - AgoraFlow 技能 — 面向 AI 智能体的问答平台。
- [android-3d-developer](https://clawskills.sh/skills/tippyentertainment-android-3d-developer) - 帮助在 Android 上使用引擎和框架构建和优化 3D 游戏及交互体验。
- [arena](https://clawskills.sh/skills/sscottdev-arena) - OpenClaw Arena — 带链上奖励的实时 AI 应用构建竞赛。
- [brawlnet](https://clawskills.sh/skills/sikey53-brawlnet) - BRAWLNET 自主智能体竞技场的官方战斗协议。
- [clawingtrap](https://clawskills.sh/skills/raulvidis-clawingtrap) - 玩 Clawing Trap - 一款 10 个智能体的 AI 社交推理游戏。
- [clawtopia](https://clawskills.sh/skills/alfrescian-clawtopia) - Clawtopia 是一个 AI 智能体放松的宁静健康避难所。
- [clawville](https://clawskills.sh/skills/jdrolls-clawville) - 玩 ClawVille — 一款面向 AI 智能体的持久化生活模拟游戏。
- [dakboard](https://clawskills.sh/skills/krisclarkdev-dakboard) - 管理 DAKboard 屏幕、设备并推送自定义显示数据。
- [deepclaw](https://clawskills.sh/skills/antibitcoin-deepclaw) - 一个由智能体为智能体构建的自主社交网络。
- [hivemind](https://clawskills.sh/skills/urcades-hivemind) - 与 Hivemind 集体知识库交互 — 一个共享记忆。
- [hytale](https://clawskills.sh/skills/newcastlegeek-hytale) - 使用官方下载器管理本地 Hytale 专用服务器。
- [init](https://clawskills.sh/skills/themrzz-init) - 在 kradleverse 上注册智能体。


> **[查看 游戏 全部 35 个技能 →](categories/gaming.md)**
</details>

<br/>

## 🤝 贡献

欢迎贡献！详情请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。

- 通过 PR 提交新技能
- 改进现有定义

> **注意：** 请不要提交您 3 小时前创建的技能。我们现在专注于社区采用的技能，尤其是那些由开发团队发布并在实际使用中经过验证的技能。质量胜于数量。
<div align="center">

[![Say hi on X](https://img.shields.io/badge/Say%20Hi!%20👋-%23000000.svg?logo=X&logoColor=white)](https://x.com/nozmen)
</div>

## 许可证

MIT 许可证 - 见 [LICENSE](LICENSE)

此列表中的技能来源于 OpenClaw 官方技能仓库并按类别分类以便于发现。此处列出的技能由各自的作者创建和维护，而非由我们维护。我们不审计、认可或保证所列项目的安全性或正确性。它们未经安全审计，在生产使用前应进行审查。

如果您发现所列技能有问题或希望移除您的技能，请提交 issue，我们会及时处理。

[codex-badge]: https://img.shields.io/github/stars/VoltAgent/awesome-codex-subagents?style=classic&label=Codex%20Subagents&color=000000&logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0id2hpdGUiPjxwYXRoIGQ9Ik0yMi4yODIgOS44MjFhNS45ODUgNS45ODUgMCAwIDAtLjUxNi00LjkxIDYuMDQ2IDYuMDQ2IDAgMCAwLTYuNTEtMi45QTYuMDY1IDYuMDY1IDAgMCAwIDQuOTgxIDQuMThhNS45ODUgNS45ODUgMCAwIDAtMy45OTggMi45IDYuMDQ2IDYuMDQ2IDAgMCAwIC43NDMgNy4wOTcgNS45OCA1Ljk4IDAgMCAwIC41MSA0LjkxMSA2LjA1MSA2LjA1MSAwIDAgMCA2LjUxNSAyLjlBNS45ODUgNS45ODUgMCAwIDAgMTMuMjYgMjRhNi4wNTYgNi4wNTYgMCAwIDAgNS43NzItNC4yMDYgNS45OSA1Ljk5IDAgMCAwIDMuOTk3LTIuOSA2LjA1NiA2LjA1NiAwIDAgMC0uNzQ3LTcuMDczek0xMy4yNiAyMi40M2E0LjQ3NiA0LjQ3NiAwIDAgMS0yLjg3Ni0xLjA0bC4xNDEtLjA4MSA0Ljc3OS0yLjc1OGEuNzk1Ljc5NSAwIDAgMCAuMzkyLS42ODF2LTYuNzM3bDIuMDIgMS4xNjhhLjA3MS4wNzEgMCAwIDEgLjAzOC4wNTJ2NS41ODNhNC41MDQgNC41MDQgMCAwIDEtNC40OTQgNC40OTR6TTMuNiAxOC4zMDRhNC40NyA0LjQ3IDAgMCAxLS41MzUtMy4wMTRsLjE0Mi4wODUgNC43ODMgMi43NTlhLjc3MS43NzEgMCAwIDAgLjc4IDBsNS44NDMtMy4zNjl2Mi4zMzJhLjA4LjA4IDAgMCAxLS4wMzMuMDYyTDkuNzQgMTkuOTVhNC41IDQuNSAwIDAgMS02LjE0LTEuNjQ2ek0yLjM0IDcuODk2YTQuNDg1IDQuNDg1IDAgMCAxIDIuMzY2LTEuOTczVjExLjZhLjc2Ni43NjYgMCAwIDAgLjM4OC42NzZsNS44MTUgMy4zNTUtMi4wMiAxLjE2OGEuMDc2LjA3NiAwIDAgMS0uMDcxIDBsLTQuODMtMi43ODZBNC41MDQgNC41MDQgMCAwIDEgMi4zNCA3Ljg3MnptMTYuNTk3IDMuODU1bC01LjgzMy0zLjM4N0wxNS4xMTkgNy4yYS4wNzYuMDc2IDAgMCAxIC4wNzEgMGw0LjgzIDIuNzkxYTQuNDk0IDQuNDk0IDAgMCAxLS42NzYgOC4xMDV2LTUuNjc4YS43OS43OSAwIDAgMC0uNDA3LS42Njd6bTIuMDEtMy4wMjNsLS4xNDEtLjA4NS00Ljc3NC0yLjc4MmEuNzc2Ljc3NiAwIDAgMC0uNzg1IDBMOS40MDkgOS4yM1Y2Ljg5N2EuMDY2LjA2NiAwIDAgMSAuMDI4LS4wNjFsNC44My0yLjc4N2E0LjUgNC41IDAgMCAxIDYuNjggNC42NnptLTEyLjY0IDQuMTM1bC0yLjAyLTEuMTY0YS4wOC4wOCAwIDAgMS0uMDM4LS4wNTdWNi4wNzVhNC41IDQuNSAwIDAgMSA3LjM3NS0zLjQ1M2wtLjE0Mi4wOEw4LjcwNCA1LjQ2YS43OTUuNzk1IDAgMCAwLS4zOTMuNjgxem0xLjA5Ny0yLjM2NWwyLjYwMi0xLjUgMi42MDcgMS41djIuOTk5bC0yLjU5NyAxLjUtMi42MDctMS41eiIvPjwvc3ZnPg==
[codex-link]: https://github.com/VoltAgent/awesome-codex-subagents
