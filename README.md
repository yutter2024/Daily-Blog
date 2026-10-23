<div align="center">

# Yutter的日常

**记录日常、AI、教程与折腾的个人博客**

<img src=".github/assets/preview.png" alt="网站预览" width="760">

[**🌐 在线访问 · yutterx.com**](https://yutterx.com)&nbsp;&nbsp;·&nbsp;&nbsp;[🪞 备用站](https://yutter2024.github.io/Daily-Blog/)

[![Deploy](https://github.com/yutter2024/Daily-Blog/actions/workflows/hugo.yml/badge.svg)](https://github.com/yutter2024/Daily-Blog/actions/workflows/hugo.yml)
![Hugo](https://img.shields.io/badge/Hugo-0.165.0-ff4088?logo=hugo&logoColor=white)
![Theme](https://img.shields.io/badge/Theme-PaperMod-0a84ff)
![Hosting](https://img.shields.io/badge/Hosting-Cloudflare%20Pages-f38020?logo=cloudflare&logoColor=white)

</div>

---

## 📌 地址

| 站点 | 地址 | 说明 |
|---|---|---|
| 主站 | [yutterx.com](https://yutterx.com) | Cloudflare Pages · 推送 `main` 自动部署 |
| 备用 | [yutter2024.github.io/Daily-Blog](https://yutter2024.github.io/Daily-Blog/) | GitHub Pages · 仅 fallback |

## 📚 内容索引

<!-- POSTS:START -->
> 共 **21** 篇 · 按发布时间倒序 · 本表由 `scripts/update_readme.py` 自动生成

| 日期 | 文章 | 分类 | 类型 |
|---|---|---|---|
| 2026-10-23 | [把博客、视频、海报都交给 AI：我的三条生产线](https://yutterx.com/posts/my-ai-workflow/) | AI与工具 | 复盘 |
| 2026-10-23 | [AI 分得清左右吗？](https://yutterx.com/posts/ai-left-right/) | AI与工具 | 复盘 |
| 2026-10-23 | [AI 分不清星期几？](https://yutterx.com/posts/ai-weekday/) | AI与工具 | 复盘 |
| 2026-10-23 | [AI 做海报的分工：画面交给模型，中文交给排版](https://yutterx.com/posts/ai-poster-workflow/) | AI与工具 | 教程 |
| 2026-10-23 | [AI 为什么数不清数？从 strawberry 说起](https://yutterx.com/posts/ai-count-strawberry/) | AI与工具 | 复盘 |
| 2026-10-23 | [AI 为什么把图画错？从六根手指说起](https://yutterx.com/posts/ai-six-fingers/) | AI与工具 | 复盘 |
| 2026-10-23 | [16 秒的 AI 短片：4 个镜头，从豆包到成片](https://yutterx.com/posts/ai-short-film-16s/) | AI与工具 | 教程 |
| 2026-09-30 | [Hermes Agent 官方文档中文摘要](https://yutterx.com/posts/hermes-docs-summary/) | AI与工具 | 教程 |
| 2026-09-18 | [英伟达发家史：从显卡到 AI 基础设施](https://yutterx.com/posts/nvidia-rising/) | 科技观察 | 复盘 |
| 2026-09-14 | [DaVinci Resolve 21 保姆级使用教程：从安装到导出完整流程](https://yutterx.com/posts/davinci-resolve-21-beginner-guide/) | AI与工具 | 教程 |
| 2026-09-10 | [从 0 开始学英语单词：听到、认出、想起、造句、开口使用](https://yutterx.com/posts/learn-english-words-from-zero/) | 学习笔记 | 教程 |
| 2026-09-10 | [VPS 自建 WireGuard VPN 节点：从购买到排障的详细教程](https://yutterx.com/posts/vps-wireguard-vpn/) | 建站教程 | 教程 |
| 2026-09-07 | [域名创建与品牌邮箱部署（详细图文教学版）](https://yutterx.com/posts/domain-email-setup/) | 建站教程 | 教程 |
| 2026-09-07 | [GitHub 从入门到精通：找项目、建仓库、协作与自动化](https://yutterx.com/posts/github-beginner-to-expert/) | 建站教程 | 教程 |
| 2026-09-07 | [Apple 横纵分析：一间公司的纵剖面与当前横切面](https://yutterx.com/posts/apple-hv-analysis/) | 科技观察 | 复盘 |
| 2026-09-06 | [荒野大镖客：救赎——两代亡命徒的完整史诗（1899–1914）](https://yutterx.com/posts/red-dead-redemption-saga/) | 游戏与创作 | 创作 |
| 2026-09-06 | [科技杂谈：我常用的网站和 App 清单](https://yutterx.com/posts/tech-tools/) | AI与工具 | 实测 |
| 2026-09-06 | [换域名记：从 GitHub Pages 迁到 Cloudflare Pages](https://yutterx.com/posts/domain-migration/) | 建站教程 | 复盘 |
| 2026-09-06 | [微剧本：《未命名的友谊》](https://yutterx.com/posts/unnamed-friendship/) | 游戏与创作 | 创作 |
| 2026-09-06 | [为什么我要搭这个博客](https://yutterx.com/posts/why-this-blog/) | 建站教程 | 复盘 |
| 2026-09-06 | [AI Agent 入门：从 LLM 到能办事的助手](https://yutterx.com/posts/agent-101/) | AI与工具 | 教程 |
<!-- POSTS:END -->

## 📝 写新文章

在 `content/posts/` 新建 `.md` 文件（front matter 参照已有文章），或使用命令行：

```bash
hugo new content posts/my-post.md
```

编辑完成后推送，主站约 1 分钟自动上线：

```bash
git add -A && git commit -m "new post" && git push
```

## 💻 本地预览

```bash
hugo server --port 1313
# 打开 http://127.0.0.1:1313/
```

## ✅ 发布前检查

- front matter 完整：`draft: false`、`slug`、`description`、`tags`、`posttype`
- 文章配图放到 `static/images/`，正文引用 `/images/xxx.png`
- 本地 `hugo --minify` 构建无报错后再推送

## 📂 目录结构

| 路径 | 用途 |
|---|---|
| `content/posts/` | 全部文章（Markdown） |
| `static/images/` | 文章配图（已压缩优化，新增建议 ≤1600px 宽） |
| `assets/css/extended/` | 自定义样式（排版标准） |
| `themes/PaperMod/` | 主题源码（已入库，含本地定制，勿整目录覆盖） |
| `.github/workflows/` | 部署与索引维护工作流 |
| `.github/assets/` | README 预览图 |
| `scripts/update_readme.py` | 生成上方内容索引（推送文章后由 Action 自动运行） |

## 🚀 部署与自动化

- **主站**：Cloudflare Pages，推送 `main` 后约 1 分钟自动上线
- **备用**：GitHub Pages，由 `hugo.yml` 工作流自动构建
- **README 索引**：推送 `content/posts/` 变更后，`update-index.yml` 自动重新生成并提交
- 完整说明见 [DEPLOY.md](DEPLOY.md)

---

<sub>© Yutter · yutter@yutterx.com · Made with Hugo + PaperMod</sub>
