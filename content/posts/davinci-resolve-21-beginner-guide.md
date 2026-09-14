---
title: "DaVinci Resolve 21 保姆级使用教程：从安装到导出完整流程"
date: "2026-09-14T12:00:00+08:00"
posttype: "教程"
summary: "第一次打开达芬奇的 Windows 用户指南：安装、项目设置、素材管理、剪辑、字幕、调色、音频、代理与导出全流程。"
draft: false
slug: "davinci-resolve-21-beginner-guide"
description: "保姆级 DaVinci Resolve 21 入门教程：安装与首次设置、五大核心页面、第一条视频从 0 到导出、代理与缓存、备份与版本升级、常见问题排查、7 天入门计划"
tags: ["DaVinci Resolve", "视频剪辑", "教程", "Blackmagic"]
categories: ["AI与工具"]
homeblock: tutorial
---

> **素材 › 剪辑 › 音频 › 调色 › 交付**
> 研究范围：官方 Blackmagic Design 资料 + YouTube + Bilibili + 公开网页实践资料。检索时间：2026-09-14。X 公共搜索在当前环境触发登录墙，已在来源与覆盖说明中明确标注。

## 先给结论：不要从「学会所有功能」开始

达芬奇不是一个单一页面，而是一套完整的后期制作工作室。新手最容易犯的错误，是一打开就钻进调色节点、Fusion 特效或 AI 工具，最后连一条视频都没有导出。正确顺序是：**先完成一条 30–60 秒短片，再按实际需要补齐调色、音频、代理、Fusion 和版本 21 新功能。**

### 本教程的最小目标

第一条练习片只要求完成 7 件事：导入 3 个视频片段 → 剪出顺序 → 加一段音乐 → 加一个标题 → 做一次基础音量调整 → 做一次克制的亮度/饱和度调整 → 导出 MP4 并在播放器里从头到尾检查。

### 推荐学习路径

| 阶段 | 你要学会什么 | 完成标准 |
|---|---|---|
| 1. 跑通主流程 | 新建项目、导入、时间线、剪切、导出 | 能独立导出第一条视频 |
| 2. 提升可看性 | 标题、转场、关键帧、基础音频 | 画面不乱、声音不爆、字幕可读 |
| 3. 画面统一 | 节点、色轮、示波器、简单匹配 | 镜头之间不忽冷忽暖 |
| 4. 提速与稳定 | 代理、缓存、备份、项目归档 | 素材多、电脑弱也能稳定工作 |
| 5. 按需进阶 | Fusion、AI、Photo、协作、HDR | 有具体需求再学，不为「全会」而全会 |

依据：官方训练体系明确覆盖 Edit、Color、Fairlight、Fusion、Deliver；Casey Faris 的 Resolve 21 入门课也按 Media → Interface → Edit → Color → Fusion → Fairlight → Delivery 组织。[O1][Y1]

## 1. 先认识 DaVinci Resolve 21

### 1.1 21 版新增什么？

Resolve 21 的大变化包括 Photo 页面、更多 AI 工具、Edit/Cut 关键帧改进、Lottie 与 OGraf 图形支持、Fusion 的 Krokodove 图形工具、Fairlight 文件夹轨道，以及面向竖屏/方形内容和社交平台的交付能力。[O2][O4]

| 功能 | 新手是否马上学 | 用途 |
|---|---|---|
| Photo 页面 | 暂时不用 | 管理/调整照片，使用节点式调色；适合照片与视频混合工作流。 |
| AI 工具 | 按需学习 | IntelliSearch、CineFocus、面部/清晰度等工具；部分属于 Studio。 |
| 关键帧/曲线 | 建议第二阶段学 | 做缩放、移动、透明度、变速和更顺滑的动画。 |
| Lottie / OGraf | 有素材时再学 | 导入动态图形、透明标题、贴纸和动画元素。 |
| Krokodove / Fusion | 最后学 | 复杂动态图形、合成和 2D/3D 特效。 |
| Fairlight 文件夹轨道 | 音频项目再学 | 把多条对白、音乐和音效轨道折叠整理。 |

> **Resolve 20 教程能不能看？** 版本兼容提醒：官方当前训练页列出的成体系入门书仍以 Resolve 20 为主，而软件和新功能资料已到 Resolve 21。基础导入、剪辑、调色、Fairlight、Fusion、Deliver 的核心思路大体相同；遇到按钮位置差异，以当前安装版本为准。[O1][O2][O6]

### 1.2 免费版还是 Studio？

| 版本 | 适合谁 | 新手判断 |
|---|---|---|
| DaVinci Resolve Free | 个人创作者、学习、常规剪辑、基础调色和音频 | 先用免费版；官方提供完整的基础工作流，学习不需要先付费。 |
| DaVinci Resolve Studio | 需要更多 AI、降噪、HDR、额外特效、10-bit/更高规格和专业交付的人 | 等遇到明确的 Studio-only 功能再买，不要因为界面复杂就先付费。 |

21 官方产品页列出 Free 与 Studio 两条路线；Studio 价格和功能可能因地区、税费与版本变化，购买前以 Blackmagic 官方页面显示为准。[O3]

## 2. 安装与首次设置：先把项目安全性做好

### 2.1 从哪里下载？

1. 只从 Blackmagic Design 官方产品页或官方支持页下载。不要使用「免激活、破解、网盘安装包、汉化补丁」页面。
2. Windows 用户选择 Windows 版本；安装程序里按需保留主程序和相关组件。
3. 第一次打开后，在 Preferences/偏好设置里确认语言、媒体存储位置和项目保存/备份选项。
4. 在 Project Manager/项目管理器里创建项目，不要把 .drp 文件当作普通 Word 文档双击编辑。项目通常位于 Project Library/项目库中。

#### Windows 硬件提醒

当前检索到的 Resolve 21 Windows 兼容条目以 Windows 10 64 位及以上、16 GB 内存（Fusion 建议 32 GB）和至少 4 GB 显存级别为基础；这只是能否运行的门槛，不等于 4K、Fusion 或重度降噪会流畅。安装前仍应打开官方当前 Tech Specs/安装页核对显卡驱动和编码器要求。[O3][O6]

### 2.2 建议的硬盘文件夹

| 文件夹 | 放什么 | 不要做什么 |
|---|---|---|
| 01_Project | .drp、项目说明、版本记录 | 不要只依赖默认项目库而没有备份 |
| 02_Footage | 相机/手机原始视频 | 不要在剪辑过程中随意改名或移动 |
| 03_Audio | 录音、音乐、音效 | 不要把下载目录当长期素材库 |
| 04_Graphics | Logo、PNG、字体、Lottie | 不要使用来源不明的插件或素材 |
| 05_Exports | 预览版、最终版、平台版 | 不要用「final_final_真的最终.mp4」命名 |
| 06_Proxy_Cache | 代理与缓存 | 不要把缓存误当成原始素材备份 |

### 2.3 第一次创建项目的设置

1. 新建项目后，点击右下角齿轮进入 Project Settings/项目设置。
2. 先决定 Timeline frame rate/时间线帧率：通常跟主要拍摄素材和最终播放目标一致。电影感项目常见 24/25 fps；普通手机或 YouTube 项目常见 25/30 fps；高帧率素材用于慢动作时，不要因为素材是 60 fps 就把整个项目都改成 60 fps。
3. 再决定 Timeline resolution/时间线分辨率：横屏 1920×1080、4K 3840×2160；短视频常用竖屏 1080×1920。分辨率可按最终交付和电脑性能取舍。
4. 打开 Live Save/实时保存和 Project Backups/项目备份。重要项目在升级版本前，再从 Project Manager 导出 .drp；需要连素材一起搬家时使用 Project Archive。

> **关键设置**：时间线帧率是最容易返工的设置。很多实践教程建议在导入素材前先确定帧率；如果空项目第一次导入素材时出现「是否匹配帧率」的提示，要看清楚再点击，而不是无脑确认。[P1][Y2]

## 3. 认识页面：新手只需先掌握两页

| 页面 | 主要任务 | 新手优先级 |
|---|---|---|
| Media 媒体 | 导入、整理、同步、元数据、代理 | 第二优先；小项目也可以从 Edit 导入 |
| Photo 照片 | 照片管理、RAW、节点式照片调色 | Resolve 21 新页面，按需学习 |
| Cut 快编 | 快速粗剪、Source Tape、快速交付 | 想快速出片时再用 |
| Edit 剪辑 | 多轨剪辑、修剪、标题、转场、时间线 | **第一核心页面** |
| Fusion | 节点式合成、特效、动态图形 | 最后学习 |
| Color 调色 | 校色、风格化、节点、示波器、跟踪 | **第二核心页面** |
| Fairlight | 音频剪辑、降噪、EQ、混音、录音 | 先学基础音量，后学专业混音 |
| Deliver 交付 | 渲染、格式、码率、批量输出 | **第二核心页面** |

> **Media › Edit › Fairlight › Color › Deliver** —— 把 Resolve 理解成「多个小工作室共用一个项目」：Edit 负责把故事剪出来，Fairlight 负责听感，Color 负责画面统一，Deliver 负责交付。官方产品页也按这些页面组织功能。[O3][Y1]

## 4. 保姆级第一条视频：从 0 到导出

### 第 1 步：建立项目和媒体池

1. 打开 Resolve → New Project/新建项目，命名为「练习_日期_主题」，例如「练习_20260914_校园Vlog」。
2. 进入 Edit 页面，打开 Media Pool/媒体池。右键空白处 → Import Media/导入媒体，或把文件从资源管理器拖入。
3. 在媒体池里建立 bins/媒体夹：Footage、Audio、Music、Graphics、Timelines。素材量大时按日期/场景/机位继续分层。
4. 双击视频在 Source Viewer/源检视器里预览；不要把「导入媒体池」误认为「已经出现在成片里」，素材必须放入时间线才会被输出。

### 第 2 步：创建时间线

1. 把主素材拖到时间线空白处，Resolve 可以自动创建时间线；或右键媒体池 → Create New Timeline。
2. 检查时间线分辨率、帧率、音频轨道；竖屏视频要在时间线设置中使用 1080×1920，而不是导出时才强行裁切。
3. 在时间线里把主讲/主画面放在 V1，补充画面放在 V2，标题/字幕放在更高的视频轨道；人声放 A1，音效 A2，音乐 A3。

### 第 3 步：粗剪和精剪

| 动作 | 鼠标做法 | 常用快捷键/提示 |
|---|---|---|
| 选择/移动 | Selection Mode，点击拖动片段 | A；先学会撤销 Ctrl/Cmd+Z |
| 切开片段 | Blade 工具点击要切的位置 | B；也可用菜单命令 |
| 修剪长度 | 拖动片段左右边缘 | 放大时间线再修更准 |
| 删除空白 | 选中多余片段和间隙后删除 | Ripple Delete 需确认当前键盘预设 |
| 预览 | 播放头移到位置，空格播放/暂停 | J/K/L 可反向、停止、正向播放 |
| 源素材取段 | 在源检视器标记 In/Out 后插入 | I / O；适合先挑好镜头 |

**剪辑判断标准**：剪辑的核心不是「加很多特效」，而是删掉无效停顿、重复动作和不必要的镜头。先做一版没有转场的干净剪辑，再决定哪里需要音乐、标题或节奏变化。

### 第 4 步：标题、转场和简单动画

1. 打开 Effects/效果库 → Titles/标题，把 Basic Text/基础文本拖到视频上方的轨道。
2. 选中标题，在 Inspector/检查器里改文字、字体、大小、颜色、位置和持续时间。
3. 把 Cross Dissolve/交叉溶解拖到两个相邻片段的接缝；只在有叙事或节奏意义时使用，不要每个切点都加花哨转场。
4. 需要慢慢放大时，选中片段，在 Inspector 的 Zoom/缩放旁边打关键帧，移动播放头后改数值。关键帧的本质是「同一个参数在不同时间点有不同值」。

Zach 的 Resolve 21 入门转录实际展示了 Inspector 的 Transform/Cropping/Dynamic Zoom、标题、转场、音频和 Deliver 页面；Casey Faris 的课程则把 Inspector 和 Effects 放在完整剪辑路径中。[Y1][Y2]

### 第 5 步：基础音频，让人声先听清

1. 先在 Edit 页面调整剪辑片段音量，再到 Fairlight 页面处理更复杂的轨道和总线。
2. 人声、音乐、音效分轨；音乐通常要比人声低，具体音量以耳朵和电平表为准。不要只看波形大小。
3. 看到电平持续顶到红色或明显失真时，先降低增益；不要用「把整体再放大」解决小声问题。
4. 需要时再学 EQ、压缩、降噪、ducking/自动压低音乐。免费版与 Studio 版的音频/AI 功能可能不同，遇到锁定图标时查当前版本说明。

### 第 6 步：基础调色，不要一上来套 LUT

1. 进入 Color 页面，先做技术校正：曝光、白平衡、对比度、饱和度。
2. 用串行节点分开任务：Node 1 基础曝光/白平衡，Node 2 对比度和饱和度，Node 3 创意风格，Node 4 局部调整。
3. 打开 Scopes/示波器观察亮度和颜色，避免亮部/暗部完全丢细节。
4. 不同相机或不同光线的素材先匹配，再做风格；先统一，再「电影感」。

> **调色原则**：LUT 不是万能滤镜。素材的色彩空间、曝光和白平衡没有先处理好时，LUT 可能让画面过饱和、偏色或失去细节。新手先用少量节点完成「正常、统一、可看」，比追求夸张风格更重要。

### 第 7 步：字幕和交付

1. 短视频可用 Titles/文本做少量标题；需要整段对白字幕时，建立字幕轨道并逐条核对时间。自动转录/AI 字幕属于版本与授权相关功能，输出前必须人工校对。
2. 快速试片：用 Quick Export/快捷导出；需要控制分辨率、编码、音频和多个版本：进入 Deliver 页面。
3. Deliver 页面填写文件名和保存位置 → 选择预设或 Custom Export → Add to Render Queue → Render All。
4. 导出完成不代表结束：一定要用系统播放器从头到尾看一遍，检查第一帧、最后一帧、字幕、音频、画幅、颜色和是否有黑帧。

## 5. 导出设置：先用「够用且稳定」的预设

| 用途 | 起步参数 | 验收重点 |
|---|---|---|
| 普通横屏/YouTube | MP4；H.264；时间线分辨率；时间线帧率；AAC 音频 | 画面是否清晰、音画是否同步、上传后是否变色 |
| 竖屏短视频 | 时间线/输出 1080×1920；H.264；匹配帧率 | 主体不要被裁掉；字幕安全区；手机播放比例正确 |
| 高质量存档 | 按项目需求选择高质量中间编码/更高码率 | 文件体积、可再次剪辑性、磁盘空间 |
| 快速审片 | 低码率或代理媒体输出，仅用于预览 | 明确标记「预览」，不要误交付 |

**导出判断**：没有一个参数适合所有平台。平台、客户或电视台给出的规格优先于通用教程。最稳妥的做法是先导出 10–20 秒困难片段，播放并上传测试，再渲染整条片。

### 5.1 导出前 10 项检查

1. 时间线 In/Out 范围是否覆盖整条片？
2. 视频和音频是否都勾选？
3. 文件名、路径和磁盘剩余空间是否正确？
4. 分辨率和帧率是否符合目标平台？
5. 是否误勾选 Use Proxy Media？最终母版通常应关闭。
6. 原始素材是否在线，是否还有 Offline Media？
7. 音频是否爆音、过小或左右声道异常？
8. 字幕是否出画、错字、提前或延后？
9. 颜色在 Resolve 与系统播放器中是否差异异常？
10. 导出文件是否在 Resolve 外完整播放过？

依据：官方中文媒体页介绍快捷导出和渲染队列；Zach 的 21 版教程演示自定义导出、预设、音视频设置、队列与渲染；第三方实践指南强调导出后必须在 Resolve 外播放验收。[O5][Y2][P1]

## 6. 电脑卡顿怎么办：先分清代理、缓存和原片

| 现象 | 优先处理 | 不要误解 |
|---|---|---|
| 普通片段就卡 | 检查源编码、硬盘速度、显卡驱动；先生成 Proxy Media | 不一定是「电脑太差」，手机/无人机 H.264/H.265 也可能难解码 |
| 加了 Fusion/降噪后卡 | 用 Render Cache 或 Render in Place；降低时间线预览分辨率 | 代理只减轻原片解码，不能自动解决所有特效计算 |
| 代理生成后仍卡 | Playback → Proxy Handling → Prefer Proxies；检查代理是否真的链接 | 生成代理 ≠ 已经使用代理 |
| 导出画质低 | Deliver 高级设置里确认 Use Proxy Media 关闭；回到原片检查 | 代理通常只用于编辑预览，不等于最终画质 |

### 6.1 代理的实际操作

1. 在 Project Settings → Master Settings → Optimized Media and Render Cache 中设置代理分辨率和格式；第一次可用 Choose Automatically。
2. 在 Media Pool 选中素材 → 右键 → Generate Proxy Media。
3. 在 Viewer/检视器的 Proxy Handling 中选择 Prefer Proxies。
4. 剪辑完成后选择 Prefer Camera Originals 或关闭代理，检查焦点、细节、噪点、遮罩边缘和颜色。
5. 最终母版在 Deliver 高级选项中不要勾选 Use Proxy Media；先渲染困难片段并在 Resolve 外播放。

> **代理工作流的底线**：代理文件要放在稳定、快速、空间足够的 SSD 路径；不要把代理、缓存和原始素材混在一个随时会被清理的下载目录中。[P2]

## 7. 项目备份与版本升级：避免「能剪但打不开」

| 备份方式 | 保存什么 | 适合场景 |
|---|---|---|
| Live Save | 持续写入当前项目 | 日常防止突然崩溃丢几分钟工作 |
| Project Backups | 项目的滚动历史版本 | 误删、改坏、需要回退 |
| Export Project (.drp) | 项目结构与时间线等，不含全部原始媒体 | 小文件备份、分享项目结构 |
| Export Project Archive | 项目 + 相关媒体的归档包 | 换电脑、交接、长期保存 |

1. 升级 Resolve 前，先备份项目库，并给关键项目导出 .drp；无法重拍的项目再建立完整 Archive。
2. 升级后先打开项目副本，不要直接拿唯一生产项目测试。
3. 检查插件、字幕、Fusion、音频路由、颜色和最终交付，再决定是否迁移正式项目。
4. 不要把 21 版打开并保存的项目想当然地当作可以无损回到旧版本；跨版本兼容必须以当前版本说明为准。

## 8. 常见问题排查表

| 问题 | 先检查 | 常见处理 |
|---|---|---|
| 媒体离线 | 原始文件是否被移动/改名；磁盘盘符是否变化 | Relink Media；恢复原路径；不要随意重命名素材 |
| 帧率不对/画面卡顿 | 时间线帧率、素材帧率、慢动作意图 | 新建正确时间线或按目标重新解释素材；先备份 |
| 导出黑屏/少片段 | In/Out 范围、视频轨道开关、离线媒体 | 清除错误范围，打开需要的轨道，先短片段测试 |
| 人声听不清 | 人声与音乐是否同轨；电平是否过低/失真 | 分轨、降低音乐、调整增益，再做 EQ/压缩 |
| 画面偏灰/偏色 | 素材是否 Log/RAW；输入色彩空间；显示器/播放器差异 | 先做色彩管理和基础校正；不要直接套 LUT |
| Fusion 复杂难学 | 是否真的需要 Fusion | 先用 Edit 的标题、关键帧和基础效果；需要时再学节点 |
| 插件/AI 找不到 | 当前版本、Free/Studio 授权、是否需要下载模型 | 查官方手册和功能页；不要从破解包补功能 |

## 9. 7 天入门计划：每天都要产出一个小结果

| 天数 | 学习主题 | 当天交付 |
|---|---|---|
| 第 1 天 | 项目、媒体池、页面、时间线 | 一条只有 3 个片段的粗剪 |
| 第 2 天 | Blade、Trim、Ripple、J/K/L、B-roll | 30 秒节奏剪辑 |
| 第 3 天 | 标题、转场、Inspector、关键帧 | 一个标题 + 一次慢推镜头 |
| 第 4 天 | 人声、音乐、音效、基本电平 | 一条听得清人声的短片 |
| 第 5 天 | Color 节点、色轮、示波器、镜头匹配 | 三段素材的统一色调 |
| 第 6 天 | Deliver、代理、缓存、备份 | 一个横屏版 + 一个竖屏预览版 |
| 第 7 天 | 完整小项目 | 60–90 秒成片，导出并在播放器验收 |

**学习方法**：每天学习不超过 60–90 分钟，其中至少一半时间要动手。只看视频、不按暂停跟做，会产生「看懂了但不会用」的错觉。每个教程看完必须留下一个项目文件或导出文件。

## 10. 教程选择与推荐顺序

### 10.1 最推荐的组合

| 用途 | 资源 | 怎么用 |
|---|---|---|
| 权威基础 | Blackmagic 官方 Training + 官方训练书 | 先按项目课程完成一遍，不追求一次看完所有高级章节。[O1] |
| Resolve 21 快速入门 | Casey Faris 1 小时 24 分课程 | 按章节跟做，重点看 Media、Edit、Color、Fairlight、Delivery。[Y1] |
| 快速查按钮 | Zach 14 分钟 Resolve 21 教程 | 卡在导入、Inspector、标题、转场、导出时快速定位。[Y2] |
| 中文快速跟做 | 录录创作中 30 分钟中文教程 | 第一次做短片时跟做，理解下载、项目、剪辑、音频流程。[Y3] |
| 中文长线系统学习 | B站 2026 100 集系列 | 按「安装→设置→界面→调色→节点→导出」分阶段，不要从第 1 集一直刷到 100 集。[B1] |
| 深度提升 | Sam Kolder 中英字幕 95 集 | 等能完成一条片后，再学代理、Fusion、调色、Fairlight 和导出。[B3] |

### 10.2 关于 X 和搬运教程

本次对 X 的公共搜索进入登录/注册页，未能在不登录的情况下读取可核验的公开帖子，因此没有把 X 上不可验证的「快捷键清单」「版本爆料」写入教程结论。后续如果你提供具体 X 帖子链接，可以再逐条核实。B站的中文配音/搬运课程可以帮助理解，但教程版本、配音和授权情况与原作者页面可能不同；官方版本信息、功能边界和系统要求应回到 Blackmagic 页面确认。[X1][B2]

> ⚠️ **安全提醒**：不要从教程评论区、网盘或「安装包自取」链接安装破解 Studio、激活器或未知插件。它们可能带来恶意程序、项目损坏、账号/文件泄露和版权风险。本教程只提供官方软件下载路径，不提供破解包。

## 11. 一页式操作清单（打印版）

1. **创建项目**：命名清楚，设置帧率和分辨率。
2. **设置安全**：打开 Live Save、Project Backups，确认项目库位置。
3. **整理素材**：建立 bins，不在剪辑过程中移动或改名原始文件。
4. **先剪故事**：先删废片和空白，再加音乐、标题和转场。
5. **先做人声**：分轨、听清、避免红色削波。
6. **再做调色**：先统一曝光和白平衡，再做风格。
7. **卡顿就代理**：Generate Proxy Media → Prefer Proxies；重特效用 Render Cache。
8. **导出先测试**：10–20 秒困难片段先渲染并播放。
9. **最终验收**：关闭 Use Proxy Media、确认原片在线、完整播放成片。
10. **归档**：保存 .drp；重要项目保存 Project Archive 和原始素材。

## 12. 来源与证据说明

来源分级：**O** = Blackmagic Design 官方资料；**Y** = YouTube 视频/页面转录或章节；**B** = Bilibili 页面信息（部分为转载）；**P** = 第三方实践资料；**X** = 已检索但受登录墙限制的路径。视频内容用于总结「该教程实际讲了什么」，不等于官方规范；价格、系统要求、版本功能和授权边界以官方页面为准。

| 编号 / 类型 | 标题与能支持的内容 | 原始链接 |
|---|---|---|
| O1 官方 | Blackmagic Design：DaVinci Resolve Training（官方培训视频、项目文件、Resolve 20 训练书；适合搭建系统课程） | <https://www.blackmagicdesign.com/products/davinciresolve/training> |
| O2 官方 | DaVinci Resolve 21 New Features Guide（Resolve 21 新功能与 Photo、AI、Edit、Color、Fusion、Fairlight 变化） | <https://documents.blackmagicdesign.com/SupportNotes/DaVinci_Resolve_21_New_Features_Guide.pdf> |
| O3 官方 | DaVinci Resolve 产品页（页面划分、免费版/Studio 版定位、媒体/剪辑/调色/特效/音频/交付等功能边界） | <https://www.blackmagicdesign.com/products/davinciresolve> |
| O4 官方 | DaVinci Resolve – What's New（Photo、AI、关键帧、Lottie、Krokodove、Fairlight、社媒交付等） | <https://www.blackmagicdesign.com/products/davinciresolve/whatsnew> |
| O5 官方中文 | DaVinci Resolve – Media（中文媒体管理、素材同步、媒体夹、快捷导出和渲染队列说明） | <https://www.blackmagicdesign.com/cn/products/davinciresolve/media> |
| O6 官方 | DaVinci Resolve 21 Manual 入口（Resolve 21 参考手册入口；具体菜单以当前安装版本为准） | <https://www.blackmagicdesign.com/welcome/en/W-DRE-03> |
| Y1 YouTube | Casey Faris：Making Videos in Resolve 21 – Full Course for Beginners（2026-05-28；约 1 小时 24 分；覆盖 Media、Edit、Fusion、Color、Fairlight、Delivery，页面提供章节和字幕转录） | <https://www.youtube.com/watch?v=gjxiH2Tm4JE> |
| Y2 YouTube | Zach：DaVinci Resolve 21 – Tutorial for Beginners 2026（约 14 分钟；从新建项目、导入、剪切、Inspector、标题、音频到 Deliver） | <https://www.youtube.com/watch?v=iT4V4A7QSqY> |
| Y3 YouTube | 录录创作中：达芬奇完整剪辑入门教学（中文/繁中；约 30 分钟；从下载、项目、媒体池、时间线到剪辑与音频） | <https://www.youtube.com/watch?v=Nl5fh_sXy34> |
| B1 Bilibili | 100 集达芬奇软件基础（2026 新手版）（2026-02-27；分段讲安装、首次设置、界面、调色、节点、LUT、导出；适合作为中文索引） | <https://www.bilibili.com/video/BV1aFASz7EqE/> |
| B2 Bilibili | Casey Faris 中文配音全课程（转载）（约 5 小时 10 分；覆盖 Media、Edit、Cut、Fusion、Color、Fairlight、Deliver；非官方搬运，翻译/配音需自行核对） | <https://www.bilibili.com/video/BV1bsCSBaEAe/> |
| B3 Bilibili | Sam Kolder 达芬奇教程（中英字幕）（约 19 小时、95 集；文件管理、快捷键、代理、剪辑、Fusion、调色、Fairlight、导出） | <https://www.bilibili.com/video/BV1WBeGzyEgP/> |
| P1 实践资料 | DaVinci Resolve Club：Beginner Tutorial（第三方实践指南；强调先定帧率、项目备份、完整跑通导入—剪辑—导出并播放验收） | <https://davinciresolveclub.com/davinci-resolve-tutorial-beginners/> |
| P2 实践资料 | DaVinci Resolve Club：Proxy Workflow（第三方代理工作流；生成代理、Prefer Proxies、质量检查、最终交付关闭 Use Proxy Media） | <https://davinciresolveclub.com/davinci-resolve-proxy-workflow/> |
| X1 X 覆盖说明 | X 公共搜索入口（需登录）（本次公开浏览被 X 登录墙拦截，未把不可核验的帖子当作教程证据） | <https://x.com/search?q=%22DaVinci%20Resolve%2021%22&src=typed_query> |

> **使用边界**：本教程是「研究后整理的实践教程」，不是 Blackmagic Design 官方出版物。界面会随着 21.x 维护版本、语言、操作系统、Free/Studio 授权和硬件而变化；遇到差异时，先查当前软件的 Help/Manual，再按本教程的工作流原则判断。生成时间：2026-09-14。已完成：官方资料检索、YouTube/B站教程筛选、X 公共搜索覆盖检查、中文教程编排、文本与版式校验。
