---
title: "AI 为什么把图画错？从六根手指说起"
date: 2026-10-23
posttype: "复盘"
summary: "AI 观察笔记第 1 期：模型不是在「画错」，它只是从来没有过一双手。"
draft: false
slug: "ai-six-fingers"
description: "一期 AI 科普的制作笔记：从六根手指讲起，聊扩散模型为什么总是画错手——以及这一期是怎么做出来的。"
tags: ["AI 观察笔记", "AI 科普", "扩散模型", "视频制作"]
categories: ["AI与工具"]
related: ['my-ai-workflow', 'ai-count-strawberry']
---

> **AI 观察笔记 · 科普系列 第 1 期** ｜ 约 4 分钟 ｜ 横屏 + 竖屏双版本
> 这期讲：模型不是在"画错"，它只是从来没有过一双手。

![六根手指](/images/works/six-fingers.jpg)
*图 1｜第 1 期：一只手，六根手指*

## 这期讲什么

生成模型画手，十张里有八张是错的：多一根、少一根、关节反折。

原因不在"手难画"，而在**模型没有身体**。它学的是海量图片里的像素统计，不是"人手有五根手指"这条常识；手又是一个自由度极高的部位，手指互相遮挡、姿态千变万化，训练数据里"标准的手"本来就少。

所以它画出来的不是"错误的手"，而是"看起来最像手的一团形状"。

## 看 4.5 秒片段

<video controls muted loop playsinline preload="metadata" poster="/images/works/six-fingers.jpg" src="/images/works/previews/six-fingers.mp4" style="width:100%;border-radius:10px"></video>

## 制作笔记

- **流程**：选题 → 研究（找论文与案例）→ 剧本（按 4.9 字/秒 排时长）→ 分镜（一镜一动作）→ 本地生成镜头 → edge-tts 配音 → Whisper 词级字幕 → ffmpeg 合成 → 抽帧质检
- **规格**：约 4 分钟，1920×1080 横屏 + 1080×1920 竖屏各一版，响度统一 -16 LUFS
- **成本**：全本地生成，￥0

## 本期一个坑

手部特写必须**裁剪放大**检查。缩略图上看不出问题的六根手指，放大后一眼就能看穿——这期的封面就是放大后才发现"第六根"特别明显，反而成了标题。

## 相关

- 完整流程见《[把博客、视频、海报都交给 AI](/posts/my-ai-workflow/)》
- 全部作品在 [作品页](/works/)
