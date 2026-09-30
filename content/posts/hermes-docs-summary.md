---
title: "Hermes Agent 官方文档中文摘要"
date: 2026-09-30
posttype: "教程"
summary: "1055 页官方文档全站抓取，12 个板块压缩成一篇中文摘要；命令、配置键与路径保留英文原文。"
draft: false
slug: "hermes-docs-summary"
description: "对 Hermes Agent 官方文档（1055 个页面）的全站抓取与中文浓缩：安装上手、核心用法、消息平台、技能体系、插件生态、开发者指南与集成。"
tags: ["Hermes", "AI Agent", "Nous Research", "官方文档"]
categories: ["AI与工具"]
related: ['agent-101', 'tech-tools']
---

> **来源**：[https://hermes-agent.nousresearch.com/docs](https://hermes-agent.nousresearch.com/docs)（Nous Research 官方文档站，1055 个页面）
> **抓取**：2026-09-30 用 crawl4ai 0.9.4（HTTP 模式）整站抓取 —— 1055 页 / 19 MB Markdown / 98 秒 / 0 失败
> **整理**：全站按 12 个板块 → 6 路并行压缩 → 合并为本文；命令、配置键、路径一律保留英文原文
> **原始抓取件**：`C:\Users\p\Documents\hermes-docs-crawl\`（1055 页 + digests + 脚本）

## 本文目录（板块 / 源页数）

| 板块 | 源页数 | 板块 | 源页数 |
|---|---|---|---|
| 一、Hermes 是什么 | 1 | 七、插件生态 | 604 |
| 二、快速上手（安装 / 平台支持 / 更新） | 7 | 八、开发者指南（架构 / 扩展点） | 56 |
| 三、核心用法（CLI、TUI、会话、配置、安全、Profiles） | 30 | 九、教程（guides） | 35 |
| 四、消息平台接入 | 35 | 十、参考（reference） | 14 |
| 五、功能全览（模型、记忆、技能、自动化、工具、界面、语音） | 56 | 十一、集成（integrations） | 4 |
| 六、技能体系 | 212 | 附、抓取统计 | — |

## 一、Hermes 是什么

Hermes Agent 是 Nous Research 打造的「自改进」agent：内置学习循环——从经验中生成技能、在使用中改进、跨会话积累对你的理解。三种形态同用一套 agent、配置、会话、技能与记忆：

- **桌面应用**（macOS Apple Silicon / Windows 10-11 / Linux）
- **CLI 与 TUI**（`hermes`、`hermes --tui`）
- **消息网关**（接进 35+ 平台当 bot 用：Telegram、Discord、Slack、微信、飞书…）

数据默认全部留存在本机（`~/.hermes`，Windows 为 `%LOCALAPPDATA%\hermes`），无遥测：只发给你自己配置的模型 provider。官网收录社区用户故事 **326 条**（15 类、11 个来源：Discord 116、X 61、Reddit 60、GitHub 38 等）。

## 二、快速上手（安装 / 平台支持 / 更新）

### 2.1 安装

**桌面安装包（推荐）**：官网下载。Windows 打开 `.appinstaller`（Windows App Installer 安装签名 MSIX 包并记录更新源，Microsoft Store 包走 Store 更新）；macOS 打开 DMG 把 Hermes.app 拷入 Applications，**仅支持 Apple Silicon**，Intel Mac 不在支持之列。捆绑包内置 agent、Python、依赖和预构建界面，首次启动不构建基础运行时。

**纯命令行安装**：

```bash
# Linux / macOS / WSL2
curl -fsSL https://hermes-agent.nousresearch.com/install.sh | bash

# Windows 原生（PowerShell）
iex (irm https://hermes-agent.nousresearch.com/install.ps1)
```

Android 走 Termux APT。只装 CLI 后随时可用 `hermes desktop` 补装桌面端。源码安装器会克隆源码、引导 uv、把依赖交给 PM（固定 Python/Node.js/npm/ripgrep/FFmpeg），选择 `all` extra，默认装 `agent-browser` + Chromium 与 `cua-driver`；某下载失败时安装仍会完成并打印重试命令。

**安装布局**：POSIX 源码 `~/.hermes/hermes-agent/`、CLI 包装器 `~/.local/bin/hermes`、数据 `~/.hermes/`；Windows 源码在 `%LOCALAPPDATA%\hermes\` 下；Docker 代码 `/opt/hermes/`、数据挂载 `/opt/data/`；Termux 在 `$PREFIX/lib/hermes-agent/`。`HERMES_HOME` 决定数据目录。

**装完后的常用命令**：`hermes model`（选模型）、`hermes tools`（选工具后端）、`hermes gateway setup`（接消息平台）、`hermes config set/get`（改配置）、`hermes setup`（总向导）。

### 2.2 快速开始（五步）

**目标对照**：想先跑通 → `hermes setup`；已知 provider → `hermes model`；要 bot/常驻 → `hermes gateway setup`；本地模型 → `hermes model` 的 custom endpoint；多 provider 回退 → 先跑通基础聊天再加。原则：**聊天都跑不通就别叠加功能**。

**五步**：① 安装；② 选 provider（新手推荐 `hermes setup --portal`——一次 OAuth 覆盖模型 + Tool Gateway 四项工具；`hermes setup` 有 Quick Setup (Nous Portal) / Full Setup / Blank Slate 三种模式）；③ `hermes --tui` 或 `hermes` 首聊，验证能回复、会用工具、可多轮；④ `hermes --continue` 验证会话恢复；⑤ 试 `/help`、`/tools`、`/model`、`/personality pirate`、`/save` 与多行输入快捷键。

### 2.3 平台支持

| 层级 | 平台 |
|---|---|
| Tier 1 | macOS（Apple Silicon，Hermes Desktop / `install.sh`）；Windows 10/11 `x86_64`+`aarch64`（`install.ps1` / MSIX，需 Win11 22H2 以上）；Linux/WSL2（`install.sh`）；Docker（不支持 `hermes update`，更新靠拉新镜像） |
| Tier 2 | Nix（flake 与模块，best-effort）、Android/Termux `aarch64`（签名 APT） |
| 不支持 | 非 `aarch64` Termux、AUR、32 位 macOS、pypi 安装等 |

**Nix / Termux**：Nix 提供 flake、NixOS module、Home Manager module；`nix run github:NousResearch/hermes-agent#desktop`、`nix profile install github:NousResearch/hermes-agent`、`nix run ... -- setup` 或 `-- --tui`；default 包约 +700MB，`#messaging` 仅 +33MB。Termux：仅 `aarch64`，`stable` / `canary` 两个 APT 频道（suite `hermes-stable` / `hermes-canary`），仓库指纹 `C572 B5FD D1A2 9CCF A9A9 12B6 840B 0848 E139 156D`，不一致即停止。

### 2.4 更新

按安装方式：源码 `hermes update`；Windows sideload MSIX 用桌面 Update 与 App Installer；Store 包用 Store；macOS 捆绑 App 用桌面 Update（electron-updater）；Docker 拉镜像重建容器；Nix 更新 flake/profile 重建；Termux `pkg update` 再 `pkg upgrade hermes-agent`。`hermes pm update` 是维护者 pin 更新命令，不是应用更新器。频道默认 main，可 `hermes update --set-channel stable|canary`；`--check` 只预览、`--plan` 批量预览、`--branch NAME` 临时换分支、`--keep-stash` 不重放本地改动（默认 stash 并自动恢复）。

### 2.5 学习路径

初次用户几乎都该先 `hermes setup --portal`；按经验分级（Beginner 约 1 小时：Installation → Quickstart → CLI Usage → Configuration），并按用例导航（CLI 编码助手 / Telegram·Discord bot / 任务自动化 / 专家 bot 团队 / 自定义工具技能 / 训练模型 / Python 库）。

## 三、核心用法（User Guide 主体）

### 模型与配置

模型分两类槽位：主模型（agent 思考用，所有用户消息、工具调用循环、流式响应都经它）与辅助模型（上下文压缩、视觉/图像分析、网页摘要、审批打分、MCP 工具路由、会话标题生成、技能搜索，可逐项独立覆盖）。dashboard 的 Models 页可配置两者；偏好文件/CLI 也有替代方法，本机跑模型见 Local Models。所有设置存于 `~/.hermes/`：`config.yaml`（model、terminal、TTS、compression 等）、`.env`（API key 与 secrets）、`auth.json`（OAuth 凭证如 Nous Portal）、`SOUL.md`（主代理身份）。最省事的路径是 `hermes setup --portal`——一次 OAuth 就拿到模型 provider 和全部四个 Tool Gateway 工具，无需手编 YAML；Portal 订阅者对按 token 计费的 provider 另有 10% 折扣。

数据库方面，`state.db` 的 journal mode 为 `wal`（默认）或 `delete`：WAL 不安全的文件系统（网络挂载）用 delete，Docker Desktop/Podman/OrbStack 的 virtiofs/9p 挂载会被自动识别；已存在的 WAL 库不会在线降级，须停掉所有进程后运行 `hermes sessions set-journal-mode delete`；durability 可选 OFF/NORMAL/FULL/EXTRA（0-3），macOS 上低于 FULL 会被拒绝。

### CLI 与 TUI

CLI 是完整终端界面：多行编辑、slash 命令补全、会话历史、打断并重定向、流式工具输出。常用命令：`hermes chat`（默认交互）、`hermes chat --query-file prompt.txt`、`hermes chat --query-file - < prompt.txt`（文件/stdin 原样传入、不经 shell 解释）、`hermes chat --model "anthropic/claude-sonnet-4"`、`hermes chat --provider nous`；还支持指定 toolsets、预载 skills、恢复历史会话、verbose 调试、隔离 git worktree、插件管理，以及 `!` shell 模式。

TUI 是现代前端（同一 runtime、同一会话与 slash 命令，官方推荐的交互方式），支持模态浮层、鼠标选择、非阻塞输入：`hermes --tui` 启动；`hermes --tui -r <session_id>`、`hermes --tui --resume "my t0p session"`、`hermes --tui --resume latest --in ./my-project` 恢复会话；可在 `~/.hermes/config.yaml` 设 `interface: tui`（或 `display.interface: tui`）为持久默认，显式 flag 优先。

### 本地模型（Local Models）

可完全在本机运行开源模型：Hermes 负责下载并管理推理引擎（llama.cpp）、按硬件挑选模型构建、自动处理内存（你无需配置 context size、GPU layers、quantization），选好模型其余交给它；下载完成后无账号、无 API key、无网络访问。桌面 Local Models 界面在 canary 构建启用，其他构建需 `--local` 启动 flag；引擎安装/更新、目录模型、Hugging Face 下载与 quickstart 均支持 Pause/Resume；也可接自己的 llama-server（默认仅探测 :8080）。

### Sessions 会话

每次对话自动存为 session（来自 CLI、Telegram、Discord、Slack、WhatsApp、Signal、Matrix、Teams 等任意平台），含完整消息历史，存放在 SQLite `~/.hermes/state.db`：会话 ID、来源平台、用户 ID、唯一人类可读标题、模型名与配置、完整历史，带 FTS5 全文检索（支撑跨会话搜索）。CLI 恢复：继续最近会话（`-c`）、按名称（自动取 lineage 中最新，如 my project #2）、按 ID 或标题、按目录（恢复 `./my-project` 最新会话，TUI 亦然）。存储恢复：`state.db` 旁有 `state.db-wal`（write-ahead log）和 `state.db-shm`；gateway、Desktop、dashboard、cron、CLI 多进程可安全共享，但在别的进程写入时重写存储不安全——此后旧进程会停止写入并每轮报 "another Hermes process still holds an old copy of the session database's write-ahead log"（该页另述三步修复、禁忌操作，并说明有写入时维护命令会被拒绝）。

### 安全（八层纵深防御）

可见的前几层：① 用户授权（allowlist、DM pairing）；② 危险命令审批（human-in-the-loop）；③ 文件写入安全（`write_file` / `patch` 的 denylist 与可选写沙箱）；④ 容器隔离（Docker/Singularity/Modal，硬化设置）；⑤ MCP 凭据过滤（MCP 子进程环境变量隔离）。

审批相关：Approval Modes、YOLO 模式、supervised-gateway 生命周期限制、Hardline blocklist（常开底线）、用户自定义拒绝规则 `approvals.deny`、审批超时、CLI 与 Gateway/消息端两套审批流程、永久 allowlist、用 `hermes approvals suggest` 从历史挖掘规则；文件写保护含「受保护路径（始终阻止）」、可选沙箱 `HERMES_WRITE_SAFE_ROOT` 及 cron/其他 Hermes 状态防护；gateway 侧有用户授权与检查顺序。出口安全：iron-proxy 为远程终端沙箱做凭据注入——沙箱只持不透明 proxy token、真 key 不出主机（`hermes egress` 管理，钉版本 SHA-256 校验）；Docker 默认 `network_mode: host` 出网不受限，可用 `docker-compose.override.yml` 做网络出口隔离。

### Profiles（多档与多实例）

Profile 即独立 Hermes home 目录（自己的 `config.yaml`、`.env`、`SOUL.md`、memory、sessions、skills、cron、state 库）；`~/.hermes/profiles/` 下只有带身份文件（`config.yaml`、`.env`、`SOUL.md`、`profile.yaml`、`auth.json`、`state.db` 之一）的目录才算 profile，裸目录被 `profile list`、gateway 和 `-p` 忽略。克隆选项：空白创建、`--clone`（只克隆配置）、`--sync-imports`、`--clone-all`（全部）、可从指定 profile 克隆；消息通道默认不克隆（`--clone-channels` 才选入）。使用：`-p` 指定、`hermes profile use` 设粘性默认。

多 gateway：把多个 profile 装成 launchd/systemd 托管服务批量运行（各自 bot token、sessions、memory），也可多路复用为单 gateway（HTTP 入站用 `/p/<profile>/` 前缀），临时可用 `gateway.standalone: true`；桌面端在 Settings → Gateway 登记本地运行时、LAN/VPS 远端 gateway、SSH 主机与 Hermes Cloud，连接持久并存。分发：Profile distribution 把整个 agent（人格、skills、cron、MCP、config）打成 git 仓库，`hermes profile install <repo>` 一键安装/更新；快速分享用导出文件（`.tar.gz`）；作者需写 `distribution.yaml`（声明所需环境变量）并在首提交前建 `.gitignore`（凭据与用户数据绝不提交）。Managed scope 则供管理员推送用户不可覆盖的基线（如 model provider、API base URL、`security.redact_secrets: true`），优先级高于用户 config/.env/shell 环境。

### Secrets（外部密钥）

启动时可从外部管理器拉 API key：Bitwarden Secrets Manager（`bws` CLI，免费档可用；`.env` 只放 `BWS_ACCESS_TOKEN`，启动时 `bws secret list <project_id>`）、1Password（官方 `op` CLI，`op://vault/item/field` 引用，service-account 或桌面会话认证）、命令 helper（任何 CLI vault：`keepassxc-cli`、`secret-tool`、`pass` 等；命令写 config.yaml，启动时经 `/bin/sh -c` 执行一次，stdout 解析为 KEY=VALUE）。多来源可同时启用；冲突时映射来源胜过批量来源，`.env`/shell 优先（除非 `override_existing: true`），先声明者赢。

### 导入、Worktrees 与检查点

`hermes import-agent` 一条命令导入 Claude Code（`~/.claude`）或 Codex CLI（`~/.codex`）：预览优先、`--dry-run` 不写盘，支持 `--source`、`--overwrite --yes`；例：`CLAUDE.md` → `~/.hermes/memories/MEMORY.md` 记忆条目，`settings.json` 的 `permissions.allow`（`Bash(...)` 规则）→ `config.yaml` 的 `command_allowlist`。

Git worktrees 适合同项目并行多 agent 或隔离实验重构：Hermes 以当前工作目录为项目根（CLI=启动目录，消息 gateway=`terminal.cwd`），会话内可用 `/worktree new`，或用 `hermes -w` 自动 worktree 模式。Checkpoints / `/rollback`：破坏性操作前自动快照、一条命令恢复；v2 起 opt-in（默认关），会话级 `--checkpoints` 或全局写 `~/.hermes/config.yaml`；shadow git 库在 `~/.hermes/checkpoints/store/`，不碰真实 `.git`；自动维护按 `retention_days` 清理、从不自动删 orphan，orphan 清理只走 `hermes checkpoints prune`（带确认）；`/rollback diff` 预览、用户手改默认保留。

### Docker、Desktop、Bot Mode、文件分工、Windows

**Docker** 两种用法：Hermes 跑在容器里（数据集中于宿主挂载的 `/opt/data`，镜像无状态可 pull 升级，支持 gateway 模式、dashboard、交互 CLI、s6 多 profile 管理）或 Docker 作为终端后端（宿主跑 agent、命令在持久沙箱执行）。

**Desktop** 与 CLI/gateway 是同一 agent（同 config、API key、sessions、skills、memory），跑在 macOS (Apple Silicon)/Windows/Linux，含 Chat、仓库发现、file browser、Artifacts、内置 terminal、live subagents、git review & worktrees、Memory Graph、Quick Entry、Voice、HUD mode 等。

**Bot Mode** 把 profile 变成命名 Bot 名册（各自 role/model/memory/skills/avatar，可跑 routines、群聊共同讨论、互发消息），内置于桌面应用、默认开启；Bot 就是 profile（`~/.hermes/profiles/<any-bot>/profile.yaml` 空块即可标记）；跨机消息走 Desktop relay，跨机 DM 可用 `hermes peer`。

**文件分工**：`SOUL.md` 是主身份（人格、语气、沟通风格），由你写、Hermes 只在缺失时生成起始版且从不覆盖，会话开始时占 system prompt 的 slot #1，位于 `~/.hermes/SOUL.md`（自定义 home 为 `$HERMES_HOME/SOUL.md`）、永不在工作目录；页内 master table 还列 USER.md 等（存什么/谁写/何时被看到/在哪）及常见混淆。

**Windows**：原生支持 Win10/11（无需 WSL/Cygwin/Docker），PowerShell `iex (irm ...)` 一行安装，另有 MSIX/Store；原生数据在 `%LOCALAPPDATA%\hermes`、WSL 在 `~/.hermes`，可共存；涉及依赖引导、feature matrix、shell 执行方式、UTF-8 控制台、编辑器 Ctrl-X Ctrl-E、Ctrl+Enter 换行、登录自启 gateway（非 Windows 服务）等；WSL2 适合要 dashboard 内嵌终端（`/chat` 需 POSIX PTY，仅 WSL2）与 POSIX 重型开发，原生足以跑聊天、gateway、cron、browser、MCP。

## 四、消息平台接入（Messaging）

### 总览

Hermes 可从 Telegram、Discord、Slack、WhatsApp、Signal、SMS、Email、Home Assistant、Mattermost、Matrix、DingTalk、Feishu/Lark、WeCom、Weixin、BlueBubbles (iMessage)、QQ、Yuanbao、Microsoft Teams、LINE、ntfy 或浏览器聊天；另有 Google Chat、IRC、SimpleX Chat、Raft、Buzz、A2A、Photon iMessage、Teams Meetings/Graph webhook、WeCom Callback、WhatsApp Business Cloud API、Webhooks 等专门页面。

gateway 是单个后台进程：连接所有已配置平台、处理 sessions、跑 cron、投递语音消息；bot 需要模型 provider 与工具 provider（TTS、web），Nous Portal 订阅把它们打包。消息状态属于「所选机器上的所选 profile」。通用流程：跑 `hermes gateway setup` 选平台走引导（多数平台页都提示这句），或手配 config.yaml / 环境变量；平台侧建 bot/app 拿 token 与自己 user ID，配 allowlist，启动 gateway 验证。通用概念：DM 每条都回、群聊默认要 @mention（各平台有开关）、按用户/会话隔离 session、home channel 承接 cron 与通知、`hermes send` 主动发消息。

### Telegram

全功能会话 bot（基于 python-telegram-bot），支持文本、语音（自动转写）、图片、文件附件；dashboard/desktop 的 Messaging → Telegram 页有 Create with QR：扫码即自动建 bot、识别你的 user ID，并把 `TELEGRAM_BOT_TOKEN`、`TELEGRAM_ALLOWED_USERS` 写进 profile 的 `.env` 后重启 gateway。群聊关键是关闭 Privacy Mode；可选 Online/Offline 状态、冷启动 pending 队列、命令菜单设置。

### Discord

bot DM 每条都回（无需 @mention）、服务器频道默认只在 @mention 时回（另有 free-response 频道）；每个 DM 独立 session；支持文本、语音消息、文件与 slash 命令；按第 1-6 步建 Application → 建 Bot → 开启 Privileged Gateway Intents → 取 Bot Token → 生成 Invite URL（推荐用 Installation tab）→ 邀请入服。

### Slack

用 Socket Mode（WebSocket、无需公网 URL，可在防火墙后/笔记本运行）；凭据为 Bot Token（`xoxb-`）+ App-Level Token（`xapp-`），用户以 Member ID（如 `U01ABC2DEF3`）识别；经典 RTM 应用 2025 年 3 月已彻底弃用，须用现代 Bolt SDK 重建；流程：创建 app（推荐用 Hermes 生成 manifest）→ 配 scopes → 开 Socket Mode → 订阅事件 → 开 Messages tab → 安装到 workspace → 查 user ID 配 allowlist → 邀请入频道。

### WhatsApp

两条路径：内置 Baileys 桥（模拟 WhatsApp Web，个人号、免 Meta 账号、免公网 URL、上手快——但有封号风险）与 WhatsApp Business Cloud API（Meta 官方生产路径：无 Node.js 桥、无 QR、无封号风险，但需 Meta Business 账号、专用商业号码和公网 HTTPS URL；用户最后消息 24 小时后再回复需预批准 template）。访问控制可用 `WHATSAPP_ALLOWED_USERS=*` 或 `WHATSAPP_ALLOW_ALL_USERS=true`；支持语音消息与 `reply_prefix` 自定义前缀。

### 微信系与国内平台

Weixin（个人微信）用腾讯 iLink Bot API、long-polling 无需公网端点，QR 登录绑的是 iLink bot 身份（如 `a5ace6fd482e@im.bot`），普通微信群可能不适用（变量如 `WEIXIN_TOKEN`、`WEIXIN_SPLIT_MULTILINE_MESSAGES=true`）；WeCom（企业微信）走 AI Bot WebSocket 网关、实时双向、同样无需公网端点（Bot ID + Secret，可扫码创建）；WeCom Callback 是自建应用回调模式（加密 XML 回调、显示在用户侧边栏、支持多企业路由，`WECOM_CALLBACK_HOST` 可选固定）；Feishu/Lark 是 full-featured bot，连接模式 `websocket`（推荐，免公网 webhook）或 `webhook`，支持文本/图片/音频/文件，cron 结果可投 home chat；DingTalk 走 Stream Mode 长连接（免公网 URL），markdown 回复，配置项如 `DINGTALK_ALLOWED_USERS=user-id-1,user-id-2`、`DINGTALK_REQUIRE_MENTION=true`、`DINGTALK_FREE_RESPONSE_CHATS=cidABC==,cidDEF==`。

### 其他平台速览

- **Signal**：signal-cli daemon HTTP 模式，SSE 收/JSON-RPC 发，需 Java 17+，E2EE 隐私最强。
- **Matrix**：mautrix SDK，任意 homeserver 含 Synapse/Conduit/Dendrite/matrix.org，支持可选 E2EE 与音视频，mention/threading 及 room 隔离配置。
- **Microsoft Teams**：消息靠公网 HTTPS webhook 投递，devtunnel/ngrok/cloudflared 均可；`teams status --verbose` 取 AAD object ID 限用户；另有 Teams Meetings 管道：Graph webhook → 优先 transcript → 录音+STT 兜底 → 摘要，投递模式 `incoming_webhook` / `graph`，及 `msgraph_webhook` 通知监听，clientState 为主认证、源 IP allowlist。
- **Email**：标准 IMAP/SMTP，Python 内建模块、无外部依赖，Gmail/Outlook/Yahoo/Fastmail 等皆可，来件在 thread 回信；与需外部 `himalaya` CLI 的邮件 skill 不同。
- **SMS**：Twilio，复用 telephony skill 的 `TWILIO_ACCOUNT_SID`、`TWILIO_AUTH_TOKEN`、`TWILIO_PHONE_NUMBER`，需公网 webhook + 建议签名校验。
- **IRC**：纯文本、stdlib 无依赖，公共网络或自建 ircd，不支持富媒体/线程/流式，昵称默认 `hermes-bot`。
- **Mattermost**：自托管 Slack 替代，REST v4 + WebSocket，`MATTERMOST_ALLOWED_USERS`、`MATTERMOST_REPLY_MODE=thread|off`、`MATTERMOST_REQUIRE_MENTION`。
- **Google Chat**：Cloud Pub/Sub pull 收 + Chat REST 发，免公网 URL，需 Workspace 账号，经 GCP 项目/API/service account/Pub-Sub+IAM/配置 app 等九步。
- **LINE**：官方 Messaging API、bundled plugin，1:1 全回、群/房间按 allowlist，出站先用免费 reply token，需公网 webhook，发媒体需公开 HTTPS base URL。
- **iMessage** 两条路——BlueBubbles（免费开源 macOS server，需常开 Mac + Apple ID + Server v1.0.0+）或 Photon（托管服务，免费共享线路池/Business 专用号，持久连接免 webhook）。
- **QQ**：官方 Bot API v2，私聊/群 @/guild/DM、WebSocket+REST、语音转写。
- **Yuanbao**：腾讯企业消息平台，WebSocket 网关、HMAC 认证，`APP_ID` / `APP_SECRET` 来自平台管理员、`YUANBAO_BOT_ID`、`YUANBAO_ROUTE_ENV=production`，home channel 形如 `direct:<account>`、`group:<group_code>`。
- **ntfy**：HTTP pub-sub 推送，免 SDK/daemon，可只出站通知。
- **Home Assistant**：gateway 平台订阅实时事件 + 四个工具 `ha_list_entities` / `ha_get_state` / `ha_list_services` / `ha_call_service`，`HASS_TOKEN` 与可选 `HASS_URL`，设 token 后 `homeassistant` toolset 自动启用。
- **Webhooks**：收 GitHub/GitLab/JIRA/Stripe 事件触发 agent，校验 HMAC、payload 转 prompt，路由可 config.yaml 或 `hermes webhook subscribe`，端点 `http://your-server:8644/webhooks/<route-name>`，有 payload filter/事件合并/脚本 transform/prompt 模板。
- **A2A**：开放 Agent2Agent 协议 v1.0，双向互通任何兼容实现。
- **Hermes Relay**：实验性连接器——gateway 不持平台凭据、外连 connector 的认证 WebSocket、免入站端口。
- **Buzz**：Block 的 Nostr 协作平台，`buzz` CLI + 原生 WebSocket，支持 markdown/图片/线程。
- **Raft**：本地 wake-channel bridge，agent 用 `raft message check` / `raft message send` 经 CLI 读写。
- **Open WebUI**：把内置 API server 当 OpenAI 兼容端点，API server 是 agent runtime、工具在服务端执行，Chat Completions 推荐。
- **SimpleX**：去中心化、无持久 ID，需 simplex-chat daemon，可 `hermes send`。

### Gateway 通用能力

消息内 chat commands、session 管理与持久化、`/sessions` 找历史会话、`/model` 持久覆盖、投递可靠性（delivery reliability）与会话连续性、intentional silence tokens、`SIGUSR2` 按需 stack dump、内建事件循环存活看门狗（另有可选 Linux 看门狗）。

## 五、功能全览（user-guide/features，56 页）

基于官方文档 user-guide/features 板块 56 个页面整理；命令、配置键与路径保留原文。

### 5.1 模型与可靠性

- **Fallback Providers**：三层韧性——① Credential Pools 同提供商多密钥轮换（最先尝试）；② 主模型回退：主 provider 出错（限流、过载、鉴权失败、断连）时自动切到备份 provider:model，会话不中断；③ 辅助任务回退：vision、上下文压缩等侧任务独立解析提供商。三者可选、互相独立。
- **Credential Pools**：为同一 provider 注册多个 API key / OAuth token（如第二个 OpenRouter、Anthropic key），某个 key 触发限流或额度耗尽时自动轮换到下一个健康凭证；「全部密钥耗尽后才启用跨提供商 fallback」。注意轮换会重置 prompt cache（缓存按 key 作用域）。
- **Provider Routing**：使用 OpenRouter 时可在 `~/.hermes/config.yaml` 加 `provider_routing` 段，用 `sort: "price"`、only（白名单）、ignore（黑名单）、order、require_parameters、data_collection 控制底层提供商与优先级；Nous Portal 集中路由并忽略该配置。
- **Mixture of Agents**：虚拟模型提供商，每个 preset 在 `moa` provider 下是可选项；aggregator 为实际执行模型（写回复、发工具调用），reference 模型先跑供其参考，费用几乎全记在 aggregator 的提供商上。用 `hermes moa configure` / `hermes moa list` 管理 preset。
- **Nous Tool Gateway**：付费 Nous Portal 订阅附带，统一路由 web search、图像生成（九个模型：FLUX 2 Klein 9B、FLUX 2 Pro、Z-Image Turbo、Nano Banana Pro、GPT Image 1.5、GPT Image 2、Ideogram V3、Recraft V4 Pro、Qwen Image）、TTS 与云浏览器，无需自备各厂商 key；`hermes setup --portal` 一次配好模型 + 四个网关工具。

### 5.2 记忆、上下文与个性化

- **Persistent Memory**：跨会话的有界记忆，两个文件：`MEMORY.md`（agent 笔记，约 2,200 字符 / ~800 tokens）与 `USER.md`（用户画像，约 1,375 字符 / ~500 tokens），存于 `~/.hermes/memories/`，会话开始时作为冻结快照注入系统提示；agent 通过 `memory` 工具自行增删改。不要让两个 agent 进程共用同一 Hermes home。
- **Memory Providers**：内置 7 个外部记忆插件（provider: openviking / honcho / mem0 / holographic / retaindb / byterover / supermemory，hindsight 需先 `hermes plugins install hindsight`），同一时间只能启用一个，内置记忆始终并存。命令：`hermes memory setup`、`hermes memory status`、`hermes memory off`，也可在 `hermes plugins` → Provider Plugins 选择。
- **Honcho Memory**：AI 原生记忆后端，在会话结束后做 dialectic 推理，持续为用户建模（偏好、沟通风格、目标、模式）；属 Memory Provider 插件，支持服务端持久化、per-peer 画像隔离与会话级上下文注入。
- **Personality & SOUL.md**：`SOUL.md` 是 agent 首要身份（系统提示 slot #1），位于 `HERMES_HOME`，Hermes 会自动播种默认文件；内置/自定义 `/personality` preset 作为会话级系统提示叠加层。
- **Context Files**：自动发现并加载。`.hermes.md` / `HERMES.md` 项目指令优先级最高（走到 git root）；`AGENTS.md`、`CLAUDE.md` 在启动 CWD 及子目录逐步发现；`AGENTS.override.md` 为个人目录级覆盖；`SOUL.md` 仅从 `HERMES_HOME/SOUL.md` 读取；`.cursorrules` 亦被识别。
- **Context References（@ 引用）**：输入 `@` 把内容注入消息，附于 `--- Attached Context ---` 段。支持 `@file:path/to/file.py`、`@file:path/to/file.py:10-25`（行区间，1 起始）、`@folder:path/to/dir`、`@diff`、`@staged`、`@git:5`（最近 N 提交，最多 10）、`@url:https://example.com`；一条消息可含多个引用。
- **Pets**：CLI、TUI、桌面端的动画吉祥物（来自 petdex 图库），按 agent 状态（idle、跑工具、思考等六种动画）反应；纯装饰、默认关闭，选择后写入 `display.pet.slug` 与 `display.pet.enabled`，用 `hermes pets` 命令、`/pet` 管理，`/hatch` 可生成宠物。
- **Skins & Themes**：控制 CLI 外观（横幅颜色、spinner、品牌文字等），与改变语气的人格分离。`/skin` 查看/列出，`/skin ares` 切内置皮肤，`/skin mytheme` 加载 `~/.hermes/skins/mytheme.yaml`；默认皮肤 default。
- **Language Packs**：内置 17 种 UI 语言（`display.language`）；语言包即插件（声明 `provides_locales`）或 `<HERMES_HOME>/locales/<lang>.yaml`，翻译 CLI 提示、`hermes --tui` 与桌面端静态 UI 文本，不翻译 agent 回复、工具输出与命令名。

### 5.3 技能与扩展机制

- **Skills System**：按需加载的知识文档，遵循渐进式披露省 token，兼容 agentskills.io 标准；技能统一存放 `~/.hermes/skills/`，可指外部技能目录；Desktop 的 Capabilities → Skills 可浏览安装；`/learn` 可从文档、网页、对话等来源学习生成技能（大块来源生成 knowledge-base 技能）；格式为 `SKILL.md`。
- **Curator**：针对 agent 自建技能的后台维护，按浏览/使用/打补丁频率把长期未用技能迁移 active → stale → archived；`curator.prune_builtins: true` 可选归档未用的内置技能（经 `archive_after_days` 判定）；支持备份回滚、审计账本与 pin。
- **Plugins**：不改核心代码即可添加自定义工具、hooks 与集成；把含 `plugin.yaml` 的目录放进 `~/.hermes/plugins/`（`__init__.py` 注册、`schemas.py` 定义 schema、`tools.py` 实现），启动 Hermes 后工具与内置工具一起可用。
- **Built-in Plugins**：随仓库分发于 `<repo>/plugins/<name>/`；`PluginManager` 按序扫描四类来源：Bundled → User（`~/.hermes/plugins/`）→ Project（`./.hermes/plugins/`，需 `HERMES_ENABLE_PROJECT_PLUGINS=1`）→ Pip entry points，同名时后者覆盖前者。内置含 disk-cleanup、security-guidance、observability/langfuse、google_meet、hermes-achievements 等。
- **Plugin Catalog**：人工审核的插件目录，在 `/docs/plugins` 按分类浏览（Memory、Desktop、Platforms、Web & Browser、Tools、Voice、Automation、Models），按名称单条命令安装并锁定 pinned commit。
- **Event Hooks**：四套钩子系统——Gateway hooks（`~/.hermes/hooks/` 下 `HOOK.yaml` + `handler.py`，仅网关）；Plugin hooks（插件内 `ctx.register_hook()`，CLI+Gateway）；Shell hooks（profile config.yaml 的 `hooks:` 段指向脚本，覆盖 CLI+Gateway+Desktop/TUI/dashboard）；Outbound webhooks（`hooks.outbound:`，向外部 HTTP 端点推送签名事件）。回调错误隔离记录、不会使 agent 崩溃。
- **LSP**：内置 pyright、gopls、rust-analyzer、typescript-language-server、clangd 等约 20+ 语言服务器后台运行，语义诊断（类型错误、未定义名、缺 import 等）注入 `write_file` / `patch` 的写后 lint；仅在 git 工作区内生效。

### 5.4 自动化与多代理

- **Scheduled Tasks (Cron)**：用自然语言或 cron 表达式排程，统一由 `cronjob_manage` 工具管理；支持一次性/周期任务与暂停、恢复、编辑、触发、删除，可挂 0..n 个技能，结果投递回原会话、本地文件或平台目标；有无 agent 模式（脚本按计划运行、stdout 原样投递、零 LLM 参与）；webhook 路由设 `cron_job` 可被外部事件触发。创建入口：聊天中的 `/cron` 或独立 CLI（schedule 与 prompt 为位置参数）。
- **Session Heartbeats（`/heartbeat`）**：给当前会话一条循环指令，如 `/heartbeat every 10m Check the deployment and report meaningful changes`；仅在空闲且间隔到时、以普通用户消息在轮次间注入（绝不打断运行中的任务）；状态存 SessionDB、网关重启后自动恢复。
- **Recurring Loops（`/loop`）**：在当前会话内按周期重跑 prompt 或 slash 命令（别名 `/proactive`），每次唤醒都是真实 agent 轮次并读取最新状态；定时器驱动，典型用途是轮询部署/CI/队列与「迭代到测试全绿」。
- **Persistent Goals（`/goal`）**：跨轮次的持续目标，每轮结束后由轻量 judge 模型判定是否达成，未达成则自动续跑，直至达成、暂停/清除或轮次预算耗尽（Ralph loop 思路）；可用 `/subgoal` 中途追加判据，支持完成契约与质量门。
- **Subagent Delegation**：`delegate_task` 生成上下文隔离的子 AIAgent（全新对话、独立终端会话、继承工具），只有最终摘要进入父会话；顶层调用自动后台运行并立即返回 handle，完成后作为新消息回传；支持并行批量与 `output_schema` 结构化输出。
- **Kanban**：跨全部 profile 共享的持久任务板，任务行存于 `~/.hermes/kanban.db`，每个 worker 是独立 OS 进程。`hermes kanban init` 初始化（首次 `hermes kanban <anything>` 自动初始化），`hermes dashboard` 打开 http://127.0.0.1:9119 观战；worker 用 `kanban_*` 工具集（`kanban_show`、`kanban_complete`、`kanban_request_review`、`kanban_block`、`kanban_attach` 等）驱动看板。支持多 board、附件、PR 完成契约；迭代预算近 90% 时发 checkpoint（可用 `agent.budget_warning_ratio` 提前）；多网关时仅一个网关持有 dispatcher，订阅支持 notify / wake / notify+wake；worker lane 由 assignee 字符串、spawn 机制、生命周期终止契约定义。
- **Batch Processing**：`batch_runner.py` 对 JSONL prompt 数据集并行跑完整 agent 会话，输出 ShareGPT 格式轨迹（含工具调用统计与推理覆盖指标），主要用于训练数据生成；支持断点续跑，`python batch_runner.py --list_distributions` 列出工具集分布。

### 5.5 工具与执行

- **Tools & Toolsets**：工具按可按平台启停的 toolset 组织，内置注册表覆盖 web search、浏览器自动化、终端执行、文件编辑、记忆、委派、定时任务、Home Assistant 等；终端后端可选 Docker、SSH、Singularity/Apptainer、Modal、Vercel Sandbox（`~/.hermes/config.yaml` 配置）。
- **Tool Search**：挂载大量 MCP/非核心插件工具时启用的渐进披露层——把它们的 schema 换成三个 bridge 工具、按需加载；核心工具（`terminal`、`read_file`、`write_file`、`patch`、`web_search`、`execute_code`、`delegate_task` 等 `_HERMES_CORE_TOOLS`）始终直接加载。
- **MCP (Model Context Protocol)**：连接外部工具服务器（GitHub、数据库、文件系统、内部 API 等）；`~/.claude.json` 的 `mcpServers` 对应 config.yaml 的 `mcp_servers`，`hermes import-agent claude-code` 可自动迁移（连同技能与指令）；官方目录支持一键安装经 Nous 审核的 MCP。
- **Code Execution**：`execute_code` 让 agent 写 Python 脚本（`from hermes_tools import ...`），经 Unix domain socket RPC 调用 Hermes 工具，把多步工作流压缩为一个 LLM 轮次；只有脚本 `print()` 输出返回模型，中间工具结果不进上下文窗口。
- **Document Extraction**：`read_file` 自动把常见文档转为可读文本——`.ipynb`、`.docx`、`.xlsx`、`.db/.sqlite/.sqlite3` 内置（stdlib）；`.pdf`、旧版 Office、`.odt/.ods/.odp`、`.rtf/.epub` 由可选 anydoc 转换器在首次使用时自动安装。
- **Deliverable Mode**：在 Slack、Discord、Telegram、WhatsApp、Signal 等网关中，agent 只需在回复里提一下生成文件的绝对路径，网关就会把文件作为原生附件上传（图表内联图片、PDF 文件下载、`.xlsx` 直接上传），无需 `MEDIA:` 标记。
- **Web Search & Extract**：`web_search` 检索、`web_extract` 抓取多 URL 正文；后端经 `hermes tools` 或 config.yaml 统一选择：Firecrawl（默认，`FIRECRAWL_API_KEY`，选定后可选无 key 云端，500 credits/月）、SearXNG（`SEARXNG_URL`，自托管免费）、Brave Search（`BRAVE_SEARCH_API_KEY`，2000 次/月）、DDGS（无需 key）。
- **X (Twitter) Search**：`x_search` 经 xAI Responses API（https://api.x.ai/v1/responses）搜索 X 帖子/主页/线程，返回带引用综合结果，推荐 `grok-4.5`；只用于只读发现，发帖、点赞、DM 等请用 xurl 技能。
- **Computer Use**：可在 macOS、Windows、Linux 后台驱动桌面（点击、输入、滚动、拖拽），不移动光标、不切换虚拟桌面；内置 `computer_use` toolset 经 MCP over stdio 连接开源 cua-driver，兼容任意工具型模型；支持权限模式与登录态浏览器 profile，首诊命令 `hermes computer-use doctor`。
- **Browser Automation**：多后端——Browser Use cloud（托管 Chromium、stealth、住宅代理、验证码求解）、Browserbase、Firecrawl、Camofox 本地反检测（Firefox 指纹伪装）、Lightpanda（内存为 Chrome 的 1/16、速度为其 9 倍、即时启动），默认 Browser Use mode（Browser Use CLI 3.0，驱动本地 Chrome 与云端浏览器）；配置位于 `~/.hermes/.env` 与 `~/.hermes/config.yaml`，支持混合路由（公网走云、LAN/localhost 走本地）与使用本机登录态的真实 profile 浏览。
- **Bot Screen**：无头 Linux 网关主机上每个 bot 有独立 Xfce 桌面，`computer_use` 与有头浏览器在其上操作并实时串流进 Hermes Desktop；遇到登录、2FA、验证码、付款可随时接管、处理完交还；若 terminal 在 docker/ssh/singularity 沙箱中运行，屏幕也在沙箱内，边界一致。
- **Spotify**：用官方 Web API + PKCE OAuth 控制播放、队列、搜索、歌单、收藏与收听历史；token 存 `~/.hermes/auth.json`、401 自动刷新；需注册自己的轻量开发者应用（Spotify 不允许第三方公共 OAuth 应用），`hermes auth spotify` 约两分钟引导完成；Free 账号可用搜索/歌单/库，播放控制需 Premium。

### 5.6 接入与界面

- **API Server**：把 hermes-agent 暴露为 OpenAI 兼容 HTTP 端点，Open WebUI、LobeChat、LibreChat、NextChat、ChatBox 等可直接接入，agent 以完整工具集作答、流式时内联显示工具进度。先 `hermes setup --portal` 配好 provider 与工具后端（300+ 模型 + Tool Gateway）；浏览器直连需设 `API_SERVER_CORS_ORIGINS`（如 `http://localhost:3000`）。主要端点：`POST /v1/chat/completions`、`POST /v1/responses`（`previous_response_id` 多轮、命名会话）、`GET / DELETE /v1/responses/{id}`、`GET /v1/models`。
- **Subscription Proxy**：本地 HTTP 服务器，让外部应用（OpenViking、Karakeep、Open WebUI 等 OpenAI 兼容客户端）以你的 Hermes 托管订阅为 LLM 端点，代理自动附带并刷新凭证；仅透传模型推理（无工具调用），与 API Server（整个 agent 作后端）互补。
- **ACP Host Integration**：Hermes 可作 ACP server 经 stdio 供 VS Code、Zed、JetBrains、Buzz Desktop 等宿主使用，支持流式思考/回复；运行策划好的 `hermes-acp` 工具集（文件与终端工具、memory/todo/session search、`execute_code`、`delegate_task`）。
- **Codex App-Server Runtime**：可选把 `openai/*`、`openai-codex/*` 等轮次交给 Codex CLI app-server 执行（终端、文件编辑、沙箱、MCP 都在 Codex 运行时内），Hermes 退为外壳（会话库、slash 命令、网关、记忆与技能审查）；纯 opt-in，默认行为不变；该运行时下 `/goal`、kanban、cron 等工作流功能不可用。
- **Hermes Web Dashboard**：浏览器管理界面，`hermes dashboard` 启动并打开 http://127.0.0.1:9119，数据不出本机；选项 `--port`（默认 9119）、`--host`（默认 127.0.0.1）、`--no-open`；`--insecure` 已废弃为 no-op（公网绑定始终要求认证）；可在多 profile 间管理。
- **Extending the Dashboard**：三层免 fork 扩展、运行时 drop-in（无需 clone 或 npm run build）——主题 YAML 放进 `~/.hermes/dashboard-themes/` 即出现在切换器；UI 插件为含 `manifest.json` 与 JS bundle 的目录（注册标签、替换/增强页面、注入槽位）；后端插件在同目录提供 FastAPI router，挂载于 `/api/plugins/<name>/`。

### 5.7 语音与多模态

- **Voice Mode**：CLI 与消息平台全语音交互（麦克风输入、语音回复），并可在 Discord 语音频道实时对话；前置条件：安装 Hermes、配置 LLM provider（`hermes model` 或 `~/.hermes/.env`）、先验证文本可用。本地 STT 用 Faster-Whisper 无需 key，Edge TTS / NeuTTS 也无需 key。
- **Wake Word（"Hey Hermes"）**：开启后 CLI、TUI、桌面端后台监听唤醒词，说出后自动新建会话、打开麦克风并按正常语音管线响应；检测完全在本地。设置 `wake_word.enabled: true` 或 `/wake on`；`wake_word.input_device` 指定输入设备、`surface` 选监听端；引擎可选 sherpa（任意短语、零训练）、openWakeWord（免费）、Porcupine（秒级自定义关键词）。
- **Voice & TTS**：共 11 个 TTS 提供商——默认 Edge TTS（免费、无需 key）、ElevenLabs（`ELEVENLABS_API_KEY`）、OpenAI TTS（`VOICE_TOOLS_OPENAI_KEY`，付费 Portal 订阅可经 Tool Gateway 免 key）、MiniMax（优秀）等；同时支持各消息平台语音消息转写；Telegram 语音气泡需 ffmpeg。
- **Vision & Image Paste**：把剪贴板图片直接粘进 CLI 让 agent 分析，图片以 base64 content block 发给任何支持视觉的模型；输入框上方显示 `[📎 Image #1]` 徽章，可附加多张、`Ctrl+C` 清空；粘贴方式：`/paste` 命令或 `Ctrl+V` / `Cmd+V`（VS Code/Cursor/Windsurf 需 `/terminal-setup`）；图片存于 `~/.hermes/images/`。
- **Image Generation**：经 FAL.ai 文生图，内置 11 个模型——默认 `fal-ai/flux-2/klein/9b`（<1s、$0.006/MP），另有 `fal-ai/flux-2-pro`（写实）、`fal-ai/z-image/turbo`（中英双语）、`fal-ai/nano-banana-pro`、`fal-ai/gpt-image-1.5` / `fal-ai/gpt-image-2`、`fal-ai/ideogram/v3`、`fal-ai/recraft/v4/pro/text-to-image` 等；模型经 `hermes tools` 选择并存于 config.yaml；支持图生图/编辑、宽高比等控制。

## 六、技能体系（212 条目录条目）

素材：`skills.list.txt`（212 条）与 `skills.md`（约 382 KB 摘要）。技能名保留英文原文，数量统计以清单为准。

### 6.1 Hermes 的技能体系是什么

技能（Skill）可以理解为 Hermes 的「按需加载的指令包」。每个技能页都写着同一段说明："The following is the complete skill definition that Hermes loads when this skill is triggered. This is what the agent sees as instructions when this skill is active." —— 意思是：某个技能被触发时，Hermes 会把这个技能的完整定义加载进上下文，作为 agent 执行该类任务时的行为指令；不触发就不会占用上下文。技能以 `SKILL.md` 文件为载体，前面带一段元数据（frontmatter）。

技能目录的入口是 **Skills Hub**（https://hermes-agent.nousresearch.com/docs/skills/），官方定位是「发现、搜索、安装（Discover, search, and install）」技能：可以在 Hermes Desktop 中打开审阅并安装，也可以复制 CLI 命令直接安装；页面提供按 Source（来源）、Category（分类）过滤的筛选器。Hub 页面还写着 "Fetching 88k+ skills across every registry" —— 说明整个技能生态（含各 registry）的规模远大于 Hermes 官方目录收录的这两百来个。

每个技能文档页的信息结构是固定的：一句话简介 → Source（来源）→ Path（安装路径）→ Author（作者／移植者）→ Platforms（支持平台）→ Tags（标签）→ Related skills（相关技能），之后是完整的 SKILL.md 正文和 Skill metadata 小节。从 Author 字段能看到部分技能来自社区并被 Hermes 移植：humanizer 来自 Siqi Chen（@blader），spike 改编自 gsd-build/get-shit-done，test-driven-development 改编自 obra/superpowers。

本次素材共 212 条：1 条 Skills Hub 首页、1 条 Google Workspace 技能专页、210 条技能条目。210 个技能同时挂载平台、标签与相关技能信息，说明官方是按「元数据 + 完整定义」的方式来组织这个目录的，便于按平台、场景或关键词筛选。

### 6.2 Bundled 与 Optional 的区别

官方把技能分成自带与可选两套：

- **Bundled（自带技能）58 个**：Source 字段标注 "Bundled (installed by default)"，安装路径形如 `skills/<分类>/<技能名>`。这 58 个随 Hermes 默认安装，开箱即用，不需要任何额外命令。
- **Optional（可选技能）152 个**：Source 字段标注 "Optional — install with `hermes skills install official/<分类>/<技能名>`"，路径形如 `optional-skills/<分类>/<技能名>`。它们不在默认安装包里，需要用户按页面给出的命令手动安装。

一句话概括区别：**Bundled 是「默认就在」，Optional 是「要自己装」**；可选技能数量约为自带技能的 2.6 倍，覆盖的场景也明显更「重」（训练、金融、安全等，详见下节）。

平台维度：绝大多数技能标注 linux / macos / windows 三平台通用；Apple 系列（apple-notes、apple-reminders、findmy、imessage）是 macOS 专属，因为它依赖 macOS 上的原生工具。

### 6.3 分类统计（共 210 个技能条目）

**Bundled：58 个，分 12 个分类**——productivity 14、software-development 12、creative 10、autonomous-ai-agents 5、apple 4、research 4、media 3、email 2、devops 1、note-taking 1、social-media 1、web 1。可见自带包的重心是办公与文档生产力、软件开发流程和创意生成，再辅以少量研究、媒体与平台集成能力。

**Optional：152 个，分 23 个分类**——mlops 36、creative 30、research 15、productivity 10、finance 9、autonomous-ai-agents 7、devops 7、security 6、software-development 6、web-development 5、blockchain 3、mcp 3、payments 3、gaming 2、health 2，以及 communication / data-science / email / dogfood / migration / smart-home / social-media / yuanbao 各 1。

几点观察：

1. 单项体量最大的是 mlops（36 个，全部在 optional，覆盖训练、推理、向量库、评测等）与 creative（optional 30 + bundled 10，合计 40 个，是全部技能里最大的领域）。
2. 只出现在 optional 的分类包括：mlops、finance、security、web-development、blockchain、mcp、payments、gaming、health、communication、data-science、dogfood、migration、smart-home、yuanbao。也就是说，模型训练与推理、金融建模、安全攻防、链上数据、支付、游戏、健康这类专业或高风险场景，官方一律放在可选包里，由用户自行安装。
3. bundled 与 optional 同时存在的分类有：creative、research、productivity、software-development、devops、email、autonomous-ai-agents、social-media。这类领域通常「基础版自带、进阶版可选」。

### 6.4 安装与管理方式

- **安装可选技能**：固定格式为 `hermes skills install official/<分类>/<技能名>`，例如 `hermes skills install official/mlops/unsloth`、`hermes skills install official/finance/dcf-model`。清单里每条 optional 技能的 Source 字段都直接写好了对应的完整命令，照抄即可。
- **浏览与挑选**：Skills Hub 页面支持按 Source 与 Category 过滤，可以在 Hermes Desktop 里打开技能页审阅后安装，也可以只复制 CLI 命令自己执行；每个技能页都能看到简介、标签、平台与完整 SKILL.md 内容，先看清楚再装。
- 需要说明的是：本批素材中出现的技能管理命令只有 `hermes skills install …` 这一种写法，其他子命令（列举、搜索、卸载等）没有被素材覆盖，此处不做推断。
- 另有一个独立专页 **Google Workspace**：整合 Gmail、Calendar、Drive、Contacts、Sheets、Docs，使用 OAuth2 并自动刷新令牌；优先调用 Google Workspace CLI（`gws`），不可用时回退到 Google 的 Python 客户端库；整个配置过程由 agent 驱动，技能路径为 `skills/productivity/google-workspace/`。

### 6.5 代表技能举例（15 个）

**Bundled 侧**

1. **hermes-agent** —— 使用、配置、换主题、扩展与编排 Hermes Agent 自身（安装、多 agent 派生、CLI/gateway 等）。
2. **claude-code** —— 把编码任务委派给 Claude Code CLI（功能开发、PR）；同族还有 codex（OpenAI Codex CLI）与 opencode。
3. **computer-use** —— 桌面 GUI 自动化：后台驱动优先，遇到信号再升级策略，跨平台。
4. **github** —— 通过 gh CLI 处理 PR、Issue、代码评审、仓库与认证。
5. **test-driven-development** —— 强制执行 RED-GREEN-REFACTOR：先写测试，再写代码。
6. **dogfood** —— 对 Web 应用做探索式 QA，产出可复现的 bug、证据与报告。
7. **docx** —— Word 文档的创建、读取、编辑、模板化与审阅；文档四件套还包括 xlsx、pdf、powerpoint。
8. **obsidian** —— 读取、搜索、创建、编辑 Obsidian 笔记库。
9. **arxiv** —— 按关键词、作者、分类或 ID 检索 arXiv 论文。
10. **grounded-citations** —— 让答案与文档建立在可核验、可引用的来源之上。
11. **baoyu-infographic** —— 生成信息图：21 种版式 × 21 种风格（信息图、可视化）。

**Optional 侧**

12. **unsloth** —— LoRA/QLoRA 微调提速 2–5 倍、占用显存更少。
13. **serving-llms-vllm** —— 用 vLLM 做高吞吐 LLM 服务（OpenAI API、量化）。
14. **sherlock** —— 跨 400+ 平台按用户名查找账号；security 分类还有 web-pentest（授权渗透测试）、1password（密钥注入）等。
15. **dcf-model** —— 在 Excel 中构建 DCF 估值工作簿；finance 分类成体系地覆盖 3-statement-model、lbo-model、merger-model、comps-analysis 等投行模型。

补充：creative 是可选包的第二个大类，代表还有 excalidraw（手绘风架构/流程/时序图）、comfyui（扩散工作流生成图像、视频、音频）、baoyu-comic（知识漫画）；research 侧有 scrapling（隐身抓取、绕 Cloudflare）、rss-feeds、duckduckgo-search 等检索与监测技能。

## 七、插件生态（348 个插件）

### 7.1 插件是什么（生态定位）

官方插件目录页（Plugin Catalog，`/docs/plugins/`）的定位语是：**"Give Hermes new powers. Memory, voice, messaging, browsing, Desktop panes and more, built by the community."**（给 Hermes 增加新能力：记忆、语音、消息、浏览、桌面面板等，由社区构建），并提供了 "Built a plugin? Submit it to the catalog →" 的投稿入口。

从 348 个插件页的「贡献内容」（What it adds）看，插件是给 Hermes 增加能力的外部扩展包，常见形态包括：工具（Tools）、生命周期钩子（Hooks）、中间件（Middleware）、模型提供商（Models）、记忆后端（Memory）、消息平台/网关适配器（Platforms）、桌面端页面与状态栏部件（Desktop）、语音 TTS/STT 提供商（Voice），以及把 MCP 服务器（stdio / Streamable HTTP / npx）桥接进 Hermes（素材中 MCP 出现 60 次）。部分插件还打包工作流技能（workflow skill / bundled skill）。分发上出现了 "Portable Agent Plugins v1" 可移植插件包格式（9 处）。

### 7.2 如何发现与安装

- **发现**：Plugin Catalog 页面提供筛选器——Source：All sources / Official / Community；Category：All categories；Sort：Most starred / Newest / Recently updated（目录内容为前端动态加载）。
- **安装**：插件页给出 `hermes plugins install <插件名>` 命令（如 `hermes plugins install afterforge`），带复制按钮；素材中 133 个插件页给出该命令。
- **管理**：另有 `hermes plugins enable <插件名>`（如 apify 页的排障小节 "hermes plugins enable apify fails"），也可在 `~/.hermes/config.yaml` 的 `plugins.enabled` 列表里启用并重启桌面端。
- **备选路径**：部分插件支持 pip 安装 + Hermes 自动发现、git clone、直接 npx、或「手动（disk door）」。

### 7.3 插件页面的结构

- **插件页**：面包屑 Plugin Catalog/<类别>/<插件名> → 元信息行「<类别> · by <作者> · added <日期>[ · updated <日期>]」→ 一句话简介 → 安装命令块 → 徽标行（Repository ↗ / Reviewed source @ \<commit\> ↗ / Documentation ↗）→ "What it adds" 摘要（如 Tools 8 | Hooks 3，或 Environment variables it needs 1、Middleware 1）与数据披露（Disclosure，71 个页面出现）→ README（含 Install、Requirements、Configuration、Usage、Screenshots、Security、License、Development 等小节）→ 页尾 "More by <作者>"。
- **作者页**：面包屑 Plugin Catalog/Authors/<作者>，统计行「N plugins in the catalog · ★ N GitHub stars across them · first listed <日期> · <类别列表>」，下方是该作者的全部插件卡片（图标 + 名称 + Community/Official 徽标 + 星数 + 简介 + 类别）。

### 7.4 功能类别与代表插件（9 类，合计 348）

| 类别 | 数量 | 代表插件（英文原名） |
|---|---|---|
| Desktop（桌面端页面/状态栏部件） | 92 | boardstate、agent-log、ai-usage-tracker、kanban-gantt、hermes-rich-ui、hermes-terminal、hermes-memory-wiki、session-dashboard、blinkenbar |
| Tools（给 agent 加工具） | 91 | afterforge、blender、snyk、android-emulator、nvidia-app、twenty-crm、financial-datasets、markifact、plan-mode |
| Memory（记忆/长期记忆后端） | 34 | chronicle、cashew、cognee、compartment、cortexlayer、entropicmem、supermemory、lancedb-suite、memory-zvec |
| Models（模型提供商/路由） | 30 | aihubmix、anyrouter、antigravity-oauth、claude-subscription-directsdk、kiro-provider、oc-free-provider、openrouter-picker、jev-model-router |
| Automation（自动化/定时/看护） | 25 | bot-forge、custodian、kanban-task-threads、morning-briefing、telegram-notify、self-wake、jev-cron-gate |
| Platforms（消息平台/网关适配） | 23 | agentchat、hermes-telegram-business、microsoft365、openmail、rocketchat-platform、whatsapp-agent-platform、vk-platform、hermes-rustpush-imessage |
| Web & Browser（web 搜索/抓取/浏览器） | 22 | brave-search、apify、anysearch、browserpaw、crawl4ai、parallel-search、hermes-plugin-chrome-profiles |
| General（通用/本地化/可观测） | 22 | hermes-zh、hermes-telemetry、hermes-evolve、cjk_sanitizer、hermes-discord-rpc、vaultwarden、little-canary |
| Voice（语音 TTS/STT/实时通话） | 9 | deepgram-voice、hermes-talk、hermes-live-voice、volcengine-voice、omnivoice、gemini-live-bridge |

### 7.5 生态规模统计

- 清单 `plugins.list.txt` 共 **604 条** = 348 个插件页 + 255 个作者页 + 1 个目录总览页。
- 348 个插件分布在 9 个类别；作者共 255 位；250 个作者页给出星标合计，共 **5,686 stars**；单个作者最多 13 个插件（3L0935、apoapostolov）。
- 能力声明：106 个插件共声明 **774 个 Tool**（单插件最多 41）；88 个插件共 249 个 Hook（最多 12）；71 个插件声明必需环境变量；9 个声明 Middleware。
- 收录时间：added 日期集中在 **2026-09-09 至 2026-09-28**，updated 最晚 2026-09-29——目录非常新、增长密集（9 月 15 日单日收录 83 个）。
- 署名构成：8 个插件署名 by NousResearch（blender、snyk、nvidia-app、nvidia-broadcast、touchdesigner、hermes-memory-wiki、hermes-telegram-business、claude-subscription-directsdk）；卡片徽标以 "❖ Community" 为主，另有 Official 徽标与 "independent of Nous Research"（Hermes Labs / Hermes Monitor contributors）等说明。
- 质量标记：94 个插件页带 "Reviewed source @ \<commit\>" 审核快照；103 个带 Repository 链接、59 个带 Documentation 链接。

## 八、开发者指南（developer-guide）

覆盖官方文档 developer-guide 板块 56 个页面（架构、Agent Loop、工具运行时、插件体系、Provider、Gateway、会话存储、上下文压缩与缓存、Skills、Contributing 等）。

### 8.1 整体架构

**顶层入口**：CLI（`cli.py`）、Gateway（`gateway/run.py`）、ACP（`acp_adapter/`）、Batch Runner、API Server，以及作为 Python 库直接调用。其下是三大核心组件：Prompt Builder（`prompt_builder.py`）、Provider Resolution（`runtime_provider.py`）、Tool Dispatch（`model_tools.py`）。

核心编排引擎是 **`AIAgent` 类**。`run_agent.py` 现在只是薄门面（thin facade）：主循环在 `agent/conversation_loop.py`，每个 turn 阶段拆到 `agent/turn_*.py`（iteration prep、API call、API error、overflow、truncation、recovery），构造函数装配在 `agent/agent_init.py`，从 prompt 组装、工具分发到 provider failover 的其余逻辑分散在专注的 `agent/*.py` 模块中，以 mixin 方式混入 `AIAgent`。

**主要子系统**：Agent Loop、Prompt System、Provider Resolution、Tool System、Session Persistence、Messaging Gateway、Plugin System、Cron、ACP Integration、Trajectories，另有 Design Principles 与 File Dependency Chain。数据流三条典型路径：CLI Session、Gateway Message、Cron Job。

**代码归属与测试**：`codebase-ownership` 把每个子系统映射到源码目录、改前应先读的文档入口与测试目录。测试镜像源码（tests mirror source）：`tools/` 的代码在 `tests/tools/` 测试，插件在 `tests/plugins/<type>/`。

**Prompt 组装的关键设计**：Hermes 刻意区分「缓存的 system prompt 状态」与「API 调用时的临时追加」，因为直接影响 prompt caching 效果。缓存的 system prompt 由 `agent/system_prompt.py` 按三个有序 tier 组装：

- **stable**：身份 SOUL.md（或回退）、tool/model 指引、coding operating brief；
- **context**：调用方传入的 `system_message`、项目上下文文件 `.hermes.md` / `AGENTS.md` / `CLAUDE.md` / `.cursorrules`、git workspace 快照、operator 指令与 platform hints；
- **volatile**：skills 索引、`MEMORY.md` 记忆快照、`USER.md` 用户画像快照、外部 memory provider 等。

### 8.2 Agent Loop 与工具运行时

`AIAgent` 的核心职责：用 `prompt_builder.py` 组装有效 system prompt 与工具 schema；选择正确的 provider/API mode（chat_completions、codex_responses、anthropic_messages）；发起可中断、支持取消的模型调用；执行工具调用（顺序或经线程池并发）；维护对话。两个入口：简单接口返回最终响应字符串，完整接口返回含 messages、metadata、usage stats 的 dict。其余机制包括 turn 生命周期、消息格式与交替规则、agent-level tools、callback surfaces、iteration budget、fallback model、压缩与持久化。

**工具运行时（Tools Runtime）**：工具是自注册函数，按 toolset 分组，经中央 registry/dispatch 执行。`tools/` 下每个工具文件在模块层调用 `registry.register(...)` 自我声明，签名为 `name=`（工具名）、`toolset=`、`schema=`（模型可见参数）、`handler=`、`check_fn=`（可用性）、`requires_env=`；`model_tools.py` 负责导入/发现工具模块并构建模型的 schema 列表；`discover_builtin_tools()` 负责发现，`get_tool_definitions()` 负责按 toolset 过滤。此外有 agent-loop 拦截工具、async bridging、`DANGEROUS_PATTERNS` 审批流、terminal/runtime environments、并发等。

### 8.3 扩展点（先选路径）

Hermes 有多个不同的可插拔接口——有的用 Python `register_*` API，有的是配置驱动或 drop-in 目录。

1. **通用插件（Build a Hermes Plugin）**：用于自定义工具、hooks、slash commands、skills 或 CLI 子命令。含 `plugin.yaml`（manifest v2）、能力声明、Python 依赖与依赖安全策略、工具 schema、工具 handler，可用 Plugin Doctor 校验；另有 Portable Agent Plugins v1 包、原生插件兼容性契约与弃用策略。
2. **Provider/Backend 插件（drop-in 目录 + ABC）**：Model Providers、Memory Providers、Context Engine、Secret Sources，以及 Web Search/Image Gen/Video Gen/Browser/Terminal Environment 等后端。统一模式是「放一个目录、声明 profile」，多为单选、配置驱动、经 `hermes plugins` 管理。浏览器后端放 `plugins/browser/<name>/`（内置 Browserbase、Browser Use、Firecrawl）；图像生成 `plugins/image_gen/<name>/`；视频生成 `plugins/video_gen/<name>/`；Web 搜索 `plugins/web/<name>/`；模型 provider 放 `$HERMES_HOME/plugins/model-providers/`，可覆盖内置；上下文引擎实现 `ContextEngine` ABC（`agent/context_engine.py`，内置默认 ContextCompressor），同时只能激活一个且从不自动激活；记忆 provider 从 Bundled / User（`$HERMES_HOME/plugins/<name>/`）/ Project（`./.hermes/plugins/<name>/`）等来源按优先级发现；Secret Source 实现 `SecretSource` ABC（内置 Bitwarden/1Password/通用命令助手，其余做成插件）；终端后端内置 local、Docker、Singularity、Modal、Daytona、Vercel Sandbox、SSH（`tools/environments/`），第三方以插件接入并由 `terminal.backend` 选择。
3. **Skill（首选扩展方式）**：比工具好创建、无需改 agent 代码、可社区分享。判定标准：能力可表达为「instructions + shell 命令 + 现有工具」（arXiv 搜索、git 工作流、Docker 管理、PDF 处理）→ 写 Skill；需要 API key 端到端集成、自定义处理逻辑、二进制/流式/实时事件（浏览器自动化、TTS、视觉分析）→ 写 Tool。SKILL.md 支持平台限定（macos/linux/windows）、条件激活、环境变量需求、加载时安全配置、config.yaml 配置项、凭据文件需求；guidelines 要求无外部依赖与渐进式披露。
4. **内置工具**：默认应走插件；只有确实要往仓库加 `tools/` 与 `toolsets.py` 的内置工具时才按 Adding Tools 走。添加工具只动 2 个文件（新建工具文件、加入 toolset），discovery import 步骤已不再需要。
5. **内置 Provider**：任意 OpenAI 兼容端点已可经 custom provider 路径接入；内置 provider 需贯通多层：`hermes_cli/auth.py`（凭据发现）→ `hermes_cli/runtime_provider.py`（运行时数据）→ `run_agent.py`（用 `api_mode` 决定请求形态）→ `hermes_cli/models.py` / `hermes_cli/main.py`（CLI 菜单与别名）。实现路径分 Path A（OpenAI 兼容）与 Path B（原生适配）。
6. **其他扩展面**：Desktop Plugin SDK（单个 ESM 文件 default-export `HermesPlugin`，只 import `@hermes/plugin-sdk`，可贡献 panes、页面与侧边栏、状态栏、命令面板与快捷键、主题等）；CLI 五个扩展缝；平台适配器（推荐插件路径，扩展 `gateway/platforms/base.py` 的 `BasePlatformAdapter`，实现 `connect()` / `disconnect()`）；Hermes Middleware（调用 provider 前改写 LLM 请求 kwargs、在护栏/审批/钩子前改写工具参数）；Observer hooks（只读遥测契约，面向 Langfuse、OpenTelemetry 类采集器）；插件 LLM 访问 `ctx.llm`（`complete()` / `complete_structured()`）；Subagent Lifecycle API（`ctx.subagent_lifecycle`，须在 agent turn 内调用）。

### 8.4 Provider 与运行时解析

共享的 provider 运行时解析器贯穿：`hermes_cli/runtime_provider.py`、`hermes_cli/auth.py`（provider registry 与 `resolve_provider()`）、`hermes_cli/model_switch.py`（CLI + gateway 共用的 `/model` 切换管线）、`agent/auxiliary_client.py`、`providers/`（ABC + registry：ProviderProfile、register_provider、get_provider_profile、list_providers）与 `plugins/model-providers/<name>/`（bundled，声明 `api_mode`、`base_url`、`env_vars`、`fallback_models`）。用户插件放 `$HERMES_HOME/plugins/model-providers/<name>/` 可覆盖内置。API mode 覆盖 chat completions、原生 Anthropic、OpenAI Codex（Responses）、Bedrock 原生接口等；支持 auxiliary model routing 与 fallback models。Model provider 插件还可声明模型能力并提供可覆盖 hook（例如 Qwen 把纯文本 content 规范化为 list-of-parts 数组并注入 cache_control，Kimi 重写工具调用 JSON），并支持外部进程（ACP）provider。

### 8.5 上下文压缩、缓存与会话存储

**双压缩系统 + Anthropic prompt caching**：核心文件 `agent/context_engine.py`（ABC）、`agent/context_compressor.py`（默认引擎）、`agent/prompt_caching.py`、`gateway/run_turn.py`（session hygiene）、`agent/compression_facade.py`。两级触发：Gateway Session Hygiene（85% 阈值）与 Agent ContextCompressor（50% 阈值、可配置）。支持 per-model 阈值覆盖（`model_thresholds`，子串匹配、最长 key 优先，如 `"glm-5.2": 0.40`）、in-place compaction（单一稳定 session id）、失败冷却与 provider 实证的 overflow 处理；Bedrock context 解析优先级为：显式覆盖 > provider 确认的限制 > 缓存/探测/静态表。Micro-compaction 把压缩成本分期偿还：每个完成的 turn 把最旧的一段未吸收 exchange 折入滚动摘要，用户消息永不被压缩。

**会话存储**：SQLite 数据库 `~/.hermes/state.db`，持久化 session 元数据、完整消息历史与模型配置（取代早期 per-session JSONL 文件）。源码为 `hermes_state.py`（facade）+ `hermes_state_*.py` 兄弟模块（schema、fts、search、compression、portability、gateway）。`get_hermes_home()` 是状态与配置的权威解析器：context-local override → `HERMES_HOME` 环境变量 → 平台默认（macOS/Linux 为 `~/.hermes`，Windows 为 `%LOCALAPPDATA%/hermes`）。`sessions` / `messages` 是正典记录，`messages_fts*` 是派生搜索索引；FTS 损坏时记录 `fts_stale`、移除同步触发器、不带派生索引重试写入并降级搜索。Trajectory 以 ShareGPT 兼容 JSONL 落盘（`trajectory_samples.jsonl` / `failed_trajectories.jsonl`）。

### 8.6 Gateway 与会话生命周期

消息网关是长驻进程，经统一架构连接 20+ 外部消息平台。关键文件：`gateway/run.py`（GatewayRunner 门面）、`gateway/session.py`（SessionStore）、`gateway/delivery.py`、`gateway/pairing.py`（DM 配对授权）、`gateway/channel_directory.py`、`gateway/hooks.py`。会话数据模型为 SessionSource / SessionEntry / SessionContext，会话键由 `build_session_key` 生成，另有二级消息守卫、running-agent 守卫、多用户隔离等机制。Multiplexing 默认开启（`gateway.multiplex_profiles` 默认 true）：一个 gateway 进程服务该安装的所有 profile，按 profile 隔离持久化、会话通道与 secret scope（`agent/secret_scope.py`）。平台适配器链路为：User ↔ Messaging Platform ↔ Platform Adapter ↔ Gateway Runner ↔ AIAgent，推荐以插件方式添加（零核心改动），内置方式需改 20+ 文件。网关还提供 OTLP/HTTP 监控平面（content-free，`/v1/metrics` 的 `hermes.gateway.*` 指标）。对外集成提供三种协议驱动同一 AIAgent：ACP（JSON-RPC over stdio，入口 `hermes acp`）、TUI gateway（JSON-RPC over stdio/WebSocket）、API server（HTTP + SSE，`gateway/platforms/api_server.py`，兼容 Open WebUI、LobeChat、LibreChat 等）。

### 8.7 关键约定与贡献

- 贡献优先级：1）bug 修复（崩溃、错误行为、数据丢失）；2）跨平台兼容（macOS、各 Linux 发行版、WSL2）；3）安全加固（shell 注入、prompt 注入、路径穿越）；4）性能与健壮性；5）新 skills；6）新 tools（很少需要，多数能力应是 skill）；7）文档。
- 默认走插件/skill 路线扩展，避免为个人或项目级需求改动核心；skill 优先于 tool。
- 内置改动遵循各子系统既有分层与文档入口（如 provider 改动要保持 auth → runtime → api_mode → CLI 全链路一致）。
- 测试目录镜像源码结构；插件与后端遵守兼容性契约与弃用策略；文档记录跨平台注意点（文件编码、进程管理、路径分隔符）。
- CLI 内部机制有自身约定：更新管线按 plan → snapshot → apply → restart-per-kind → verify → report 阶段推进；进程身份绝不能靠 argv 子串推断。
- Cron 子系统约定：`cron/jobs.py`（作业模型与 jobs.json 原子读写）、`cron/scheduler.py`（调度循环）、`tools/cronjob_tools.py`（cronjob_manage 工具）、`gateway/run.py`（网关内 tick）、`hermes_cli/cron.py`（hermes cron 子命令）；支持相对延迟、间隔、cron 表达式等四种调度格式，并有 fresh session 隔离、skill/script-backed jobs 等设计。

## 九、教程（guides，35 篇）要点

- **Cron 自动化**：5 个实战模式（如网站变更监控）；`script` 参数在每次执行前运行脚本，其 stdout 成为 agent 上下文；不需要 LLM 时用 script-only cron 或 `hermes send`。
- **Script-Only Cron（无 LLM）**：no-agent 模式，脚本决定是否报警（有输出即发）；`hermes cron create "every 5m" ...`、`hermes cron run <job_id>` 测试、`hermes cron edit <job_id> --interpreter "..."` 指定 Python。
- **Cron 排障**：按序查 job 状态（须 `[active]`，`[completed]` 可能是次数耗尽）、schedule 格式、投递配置、权限（`~/.hermes/cron/jobs.json` 需可读写）、技能是否安装；命令 `hermes cron list/run/edit`。
- **Daily Briefing Bot**：每天早晨自动搜索 → 汇总 → 发 Telegram/Discord，无代码；前置 gateway（`hermes gateway install`、`sudo hermes gateway install --system` 或前台 `hermes gateway`）与 `FIRECRAWL_API_KEY`；用自然语言或 `/cron add "0 8 * * *" "…"` 建任务；提示词必须完全自包含（cron 是全新会话）；`deliver: "local"` 存到 `~/.hermes/cron/output/`。
- **GitHub PR Review Agent**：cron 每 2 小时轮询（`hermes cron create "0 */2 * * *" "…"`），配合已登录的 gh（`gh pr list`、`gh pr diff`）；无需公网端点；也可用 `gh pr review NUMBER --repo REPO --approve/--request-changes` 把结论发回 PR。
- **团队 Telegram 助手**：向 @BotFather 发 `/newbot` 拿 token；`hermes gateway setup` 向导或手写 `TELEGRAM_BOT_TOKEN`、`TELEGRAM_ALLOWED_USERS`（多人逗号分隔）、`TELEGRAM_HOME_CHANNEL`；每成员独立会话、按用户授权。
- **技能用法**：`hermes skills list` 查看；以 `/技能名` 调用；`hermes skills install official/research/arxiv`、支持从 URL 安装；`hermes skills config <skill>` 配置，值存 config.yaml 的 `skills.config.*`。
- **Voice Mode**：三种体验（CLI 麦克风、Telegram/Discord 语音回复、Discord 语音频道实时对话）；顺序：先跑通普通聊天 → 装 extras → 系统依赖（portaudio、ffmpeg、opus、espeak-ng）→ 选 STT/TTS（本地 STT+Edge TTS 最省）→ 配置（`hermes setup tts`）；`/voice on`、`/voice tts`；Discord 需 Connect/Speak 权限。
- **SOUL.md**：实例的「首要身份」，位于 system prompt 最前，规定语气、风格与回避项（不用于仓库规范/项目流程）；会话内可 `/personality teacher` 临时换风格。
- **排障「我的 agent 变笨了」**：7 步顺序——① 当前模型（`/model`、`/status`；`/model` 默认仅本会话，`--global` 才持久化；dashboard 改模型只对新会话生效）② 上下文用量（`/usage`、`/context`、`/compress`）③ 检测到的上下文长度 ④ 记忆是冻结快照 ⑤ 记忆有界且经整理 ⑥ 技能/工具是否加载 ⑦ 压缩副作用。
- **各家模型接法**：Gemini 原生 provider（`GOOGLE_API_KEY` / `GEMINI_API_KEY`）；Vertex AI（OpenAI 兼容端点+OAuth2 服务账号/ADC，Gemini 3.x 预览须 `region: global`，`VERTEX_PROJECT_ID` / `VERTEX_REGION`）；AWS Bedrock 原生 provider（IAM、Guardrails、跨区域推理）；xAI Grok OAuth（浏览器 device-code，SuperGrok 或 X Premium+，无需 `XAI_API_KEY`）；MiniMax OAuth（PKCE 浏览器登录，Anthropic Messages 兼容传输，端点 https://api.minimax.io/anthropic 或中国 https://api.minimaxi.com/anthropic）；Microsoft Foundry/Azure（`AZURE_FOUNDRY_API_KEY` + `AZURE_FOUNDRY_BASE_URL`，或 Entra ID 免密钥 `model.auth_mode: entra_id`）；本地模型（桌面 Settings → Providers → Local Models 一键装 llama.cpp，或手动 Ollama/MLX）。
- **其他教程一句话**：专属邮箱（Himalaya 技能走 IMAP）；Delegation（子代理各自会话/终端/工具集，只回最终摘要）；`hermes send` 推脚本输出（如 `make | hermes send --to slack:#builds`）；作为 Python 库（`import AIAgent`）；从 OpenClaw 迁移（`hermes claw migrate`，Claude Code/Codex 用 `hermes import-agent`）；Teams 会议管道（`hermes teams-pipeline validate`、`token-health`）；MCP 日常使用与用 MCP 管理 Hermes Cloud；Webhook 触发 PR 评论（更实时）；OAuth over SSH（Spotify/远程 MCP 的 loopback 回调走 `ssh -L`）；Mac 本地 LLM 与 Ollama 零成本；Nemotron 3 Ultra 限免；Nous Portal 端到端指南；工作机安全（默认 `approvals.mode: smart`）；Desktop 原生登录（RFC 8252）。
- **Tips**：重复要求写进 `AGENTS.md` 自动读取；提示要具体（文件、行号、报错原文）。

## 十、参考（reference，14 页）要点

- **CLI 命令**：入口 `hermes [global-options] <command> [subcommand/options]`；全局选项 `--version/-V`、`--profile/-p`、`--resume/-r <session>`（`latest` 恢复最近会话）、`--continue/-c`、`--in <dir>`。顶层含 `hermes chat`（脚本化一次性 `hermes -z <prompt>`、`--format stream-json`、`--usage-file`）、model、moa、fallback、gateway、auth、send、cron、skills、bundles、curator、plugins、mcp、tools、webhook、hooks、kanban、profile、dashboard、desktop、doctor、status、usage、update、backup / import、logs、config、skin 等。
- **一次性运行退出码**：0 完成、1 失败/部分/预算耗尽/未运行、130 被中断，provider 限流等临时故障退出 75（EX_TEMPFAIL）供调度器重排。
- **斜杠命令**：CLI 与消息平台两个入口，同由 `hermes_cli/commands.py` 的 `COMMAND_REGISTRY` 驱动；技能会暴露为动态斜杠命令，与内置同名时内置优先、技能用 `/skill <name>`；平台可配 admin/user 两级权限（`allow_admin_from`、`user_allowed_commands`）。
- **其余参考页**：环境变量（密钥放 `~/.hermes/.env`，非机密行为放 config.yaml）；MCP 配置（stdio/HTTP、`ssl_verify`、`client_cert`、工具过滤）；工具集（core/composite/platform，`hermes chat --toolsets web,file,terminal`、debugging）；内置工具约 100 个（10 浏览器+2 CDP、4 文件、2 终端、11 桌面 GUI、2 web、14 kanban 等）；捆绑技能装在 `~/.hermes/skills/`，误删用 `hermes skills reset <name> --restore`；可选技能 `hermes skills install official/<category>/<skill>`；模型目录（在线 JSON manifest，离线回退内置快照）；profile 命令（use/create/describe/show/alias/export/import/install/update）；包管理（`hermes pm` 只管工具二进制与 Python 依赖）；CLI 符号表；FAQ（支持任何 OpenAI 兼容 API；数据只发所配 provider、无遥测，本地存 `~/.hermes/`；可离线本地模型，base_url 如 http://localhost:11434/v1 、context 至少 64000；Hermes 本身 MIT 免费，只为模型用量付费）；自动化蓝图目录。

## 十一、集成（integrations）

- **Nous Portal（官方推荐）**：一次 OAuth 取代各家账号、API key 与账单；一个订阅 300+ 模型；Tool Gateway 五项：web 搜索与抓取、图像生成（FAL，9 模型）、TTS（OpenAI）、云浏览器（Browser Use）、云终端沙箱（Modal，可选）。最快路径 `hermes setup --portal`（等价 `hermes portal`）：Portal OAuth → 选模型 → 写 config.yaml → 开 Tool Gateway；`hermes portal info/status/tools/open` 查看；refresh token 存 `~/.hermes/auth.json`，每次推理换短命 JWT；可逐工具混用自家后端（`hermes tools`）。
- **LLM 与模型 Provider**：覆盖云 API（OpenRouter、Anthropic 等）到自托管端点（Ollama、vLLM）及路由/回退；`hermes model` 交互配置，也支持 OpenAI Codex 订阅、GitHub Copilot 等登录。
- **Buzz**（Block 开源、基于 Nostr）三种接法：桌面托管运行时、`buzz-acp` 中继桥、接进 gateway 作为原生消息平台。
- **集成总览**还包括：AI providers 与路由、MCP 工具服务器、搜索后端、浏览器自动化、语音/TTS、IDE 集成、编程访问、记忆与个性化、消息平台、协作工作区、家庭自动化、插件、训练与评估。

## 附录：本次抓取的统计与方法

| 板块 | 页数 | 板块 | 页数 |
|---|---|---|---|
| plugins（插件目录） | 604 | reference（参考） | 14 |
| user-guide/skills（技能） | 212 | getting-started（上手） | 7 |
| user-guide/features（功能） | 56 | integrations（集成） | 4 |
| developer-guide（开发） | 56 | 首页 / 用户故事 | 2 |
| guides（教程） | 35 | 合计 | 1055 |
| user-guide/messaging（消息） | 35 | 抓取用时 | 98 秒 |
| user-guide 主体 | 30 | 产出体积 | 19 MB Markdown |

- **抓取方式**：crawl4ai 0.9.4 的 AsyncHTTPCrawlerStrategy（HTTP 模式，不启浏览器；站点是服务端渲染，足够）+ `arun_many` 分批并发（semaphore_count=8），每页存一个 Markdown 文件（带 URL 与标题），逐页校验成功率 100%。
- **整理方式**：先把每页压成「标题 + 正文要点 + 小标题」的摘要素材（去导航噪声），再把 12 个板块分成 6 组交给 6 个子代理并行写成中文摘要，最后由主代理合并成本文。
- **局限**：① 目录类页面（604 个插件页、212 个技能页）在摘要里按统计口径处理（数量/分类/代表项），逐条细节请查抓取原件；② 文档站内容会随版本更新，本文反映 2026-09-30 的快照。
