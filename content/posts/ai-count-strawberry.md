---
title: "AI 为什么数不清数？从 strawberry 说起"
date: 2026-10-23
posttype: "复盘"
summary: "AI 观察笔记第 2 期：它会解微积分，却数不清 strawberry 里有几个 r。"
draft: false
slug: "ai-count-strawberry"
description: "从 strawberry 数 r 讲起：大模型看到的不是字母，而是 token——这一期聊聊 tokenization 与它带来的「数不清」。"
tags: ["AI 观察笔记", "AI 科普", "tokenization", "视频制作"]
categories: ["AI与工具"]
related: ['ai-six-fingers', 'my-ai-workflow']
---

> **AI 观察笔记 · 科普系列 第 2 期** ｜ 约 4 分钟 ｜ 横屏 + 竖屏双版本
> 这期讲：它答得出微积分，却可能数错 "strawberry" 里有几个 r。

![strawberry](/images/works/counting-cover.jpg)
*图 1｜第 2 期：它知道很多，却数不清一个单词*

## 这期讲什么

大模型不是按"字母"读字的。文本进入模型前会被切成 **token**——可能是一个词、一个词根，也可能是半个词。

对模型来说，"strawberry" 可能只是一两个 token；它看到的是"一块整体"，而不是 s-t-r-a-w-b-e-r-r-y 这十个字母。要数 r，它得先把 token 拆回字母——这一步很容易错。

这不是"笨"，是**它的世界没有字母这个刻度**。视频里用了一个比喻：让一个看不见小字的人去数书上有几个逗号——不是不认真，是他根本没有那个分辨率。

## 看 4.5 秒片段

<video controls muted loop playsinline preload="metadata" poster="/images/works/counting-cover.jpg" src="/images/works/previews/counting.mp4" style="width:100%;border-radius:10px"></video>

## 制作笔记

- **流程**：研究（tokenizer 原理 + 实测案例）→ 剧本 → 分镜 → 本地生成镜头 → 配音 → Whisper 字幕 → 合成 → 抽帧质检
- **规格**：约 4 分钟，双版本，字幕统一压在安全区内
- **成本**：全本地生成，￥0

## 本期一个坑

数字类台词的字幕最容易"假报警"：转写会把"九十九"写成"99"，时间轴其实是对的。**核对时要看窗口里实际出现的内容，不能只看数字匹配**。

## 相关

- 全部作品在 [作品页](/works/)
- 制作流程：[把博客、视频、海报都交给 AI](/posts/my-ai-workflow/)
