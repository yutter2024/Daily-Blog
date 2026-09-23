# Yutter的 AI 笔记

个人 AI 技术博客 —— 记录 AI 工具、教程与实测复盘。

**[🌐 线上访问：yutterx.com](https://yutterx.com)**

[![Deploy](https://github.com/yutter2024/AI-Blog/actions/workflows/hugo.yml/badge.svg)](https://github.com/yutter2024/AI-Blog/actions/workflows/hugo.yml)
![Hugo](https://img.shields.io/badge/Hugo-0.165.0-ff4088?logo=hugo&logoColor=white)
![Theme](https://img.shields.io/badge/Theme-PaperMod-0a84ff)
![Hosting](https://img.shields.io/badge/Hosting-Cloudflare%20Pages-f38020?logo=cloudflare&logoColor=white)

## 📌 地址

| 站点 | 地址 | 说明 |
|---|---|---|
| 主站 | [yutterx.com](https://yutterx.com) | Cloudflare Pages · 推送 `main` 自动部署 |
| 备用 | [yutter2024.github.io/AI-Blog](https://yutter2024.github.io/AI-Blog/) | GitHub Pages · 仅 fallback |

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
| `static/images/` | 文章配图 |
| `assets/css/extended/` | 自定义样式（排版标准） |
| `themes/PaperMod/` | 主题源码（已入库，含本地定制，勿整目录覆盖） |
| `.github/workflows/` | GitHub Pages 备用站工作流 |

## 🚀 部署

- **主站**：Cloudflare Pages，推送 `main` 后约 1 分钟自动上线
- **备用**：GitHub Pages，由 Actions 工作流自动构建
- 完整说明见 [DEPLOY.md](DEPLOY.md)

---

<sub>© Yutter · yutter@yutterx.com · Made with Hugo + PaperMod</sub>
