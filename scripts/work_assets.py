#!/usr/bin/env python3
"""作品墙资产流水线：一条命令把源文件变成 /works/ 需要的全部素材 + YAML 条目。

用法：
  # 海报（源图 → 1600x900 封面 + ≤3840 宽原图）
  python scripts/work_assets.py poster --src "C:/.../poster_4k.png" --slug my-poster \
      --title "作品名" --type "海报" --date "2026.11" --note "一句话说明" --write

  # 视频（源片 → 14~20s 精彩片段 + hover 小样 + 封面帧）
  python scripts/work_assets.py video --src "C:/.../final.mp4" --slug my-video \
      --start 0 --dur 15 --title "作品名" --type "科普视频" --date "2026.11" \
      --series "科普" --note "一句话说明" --write

  # 体检：data/works.yaml 里每个素材文件是否真的存在
  python scripts/work_assets.py check
  python scripts/work_assets.py check --build     # 顺便跑 hugo 构建

规则（用户 2026-10-27 定）：
  - 视频作品不发文章，只做卡片；点封面播精彩片段（带声音），hover 播 4.5s 无声小样。
  - 海报点封面看原图：cover 只给列表用（1600x900），full 才是原图（≤3840 宽）。
  - 网格缩略图必须轻：cover ≤400KB，preview ≤250KB，highlight ≤2MB。
"""
import argparse
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORKS = os.path.join(ROOT, "static", "images", "works")
DATA = os.path.join(ROOT, "data", "works.yaml")
POSTER_MARK = "  # ---------- 海报作品 ----------"

COVER_SIZE = (1600, 900)      # 海报封面 16:9
POSTER_FULL_W = 3840          # 海报原图最大宽度
VIDEO_COVER = (900, 1200)     # 视频封面 3:4
PREVIEW_W, PREVIEW_SEC = 540, 4.5
HL_W, HL_CRF = 1280, 26


def run(cmd):
    p = subprocess.run(cmd, capture_output=True, text=True)
    if p.returncode != 0:
        sys.exit("命令失败: %s\n%s" % (" ".join(cmd[:6]), p.stderr[-800:]))
    return p


def ffprobe_duration(path):
    out = run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
               "-of", "csv=p=0", path]).stdout.strip()
    return float(out)


def human(n):
    return "%.2fMB" % (n / 1048576) if n >= 1048576 else "%dKB" % (n / 1024)


# ---------------- 海报 ----------------
def make_poster(src, slug):
    from PIL import Image
    os.makedirs(WORKS, exist_ok=True)
    cover_path = os.path.join(WORKS, slug + ".jpg")
    full_path = os.path.join(WORKS, slug + "-full.jpg")

    im = Image.open(src).convert("RGB")
    full = im.copy()
    if full.width > POSTER_FULL_W:
        full = full.resize((POSTER_FULL_W, round(full.height * POSTER_FULL_W / full.width)),
                           Image.LANCZOS)
    full.save(full_path, "JPEG", quality=88, optimize=True, progressive=True)

    tw, th = COVER_SIZE
    ratio = max(tw / im.width, th / im.height)
    rw, rh = round(im.width * ratio), round(im.height * ratio)
    cover = im.resize((rw, rh), Image.LANCZOS).crop(
        ((rw - tw) // 2, (rh - th) // 2, (rw - tw) // 2 + tw, (rh - th) // 2 + th))
    cover.save(cover_path, "JPEG", quality=84, optimize=True, progressive=True)

    print("封面 %s  %s" % (os.path.basename(cover_path), human(os.path.getsize(cover_path))))
    print("原图 %s  %s  %dx%d" % (os.path.basename(full_path),
                                 human(os.path.getsize(full_path)), full.width, full.height))
    return {
        "cover": "/images/works/%s.jpg" % slug,
        "full": "/images/works/%s-full.jpg" % slug,
    }


# ---------------- 视频 ----------------
def make_video(src, slug, start, dur, cover_at=None, cover_src=None):
    os.makedirs(WORKS, exist_ok=True)
    hl_dir = os.path.join(WORKS, "highlights")
    pv_dir = os.path.join(WORKS, "previews")
    os.makedirs(hl_dir, exist_ok=True)
    os.makedirs(pv_dir, exist_ok=True)

    hl_path = os.path.join(hl_dir, slug + ".mp4")
    pv_path = os.path.join(pv_dir, slug + ".mp4")
    cover_path = os.path.join(WORKS, slug + ".jpg")

    # 精彩片段：带声音，1280 宽
    run(["ffmpeg", "-y", "-v", "error", "-ss", str(start), "-t", str(dur), "-i", src,
         "-vf", "scale=%d:-2" % HL_W, "-c:v", "libx264", "-crf", str(HL_CRF),
         "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "96k",
         "-movflags", "+faststart", hl_path])

    # hover 小样：无声，3:4 竖裁，4.5s
    total = ffprobe_duration(src)
    pv_start = min(max(total * 0.35, 0), max(total - PREVIEW_SEC - 0.2, 0))
    run(["ffmpeg", "-y", "-v", "error", "-ss", "%.2f" % pv_start, "-t", str(PREVIEW_SEC), "-i", src,
         "-vf", "crop=ih*3/4:ih,scale=%d:-2" % PREVIEW_W, "-an",
         "-c:v", "libx264", "-crf", "30", "-preset", "medium",
         "-pix_fmt", "yuv420p", "-movflags", "+faststart", pv_path])

    # 封面：默认取片段内一帧，竖裁 3:4；可用 --cover-src 指定精修图
    if cover_src:
        src_img = cover_src
    else:
        t = start + (cover_at if cover_at is not None else min(1.0, dur / 2))
        src_img = os.path.join(WORKS, ".cover-tmp.jpg")
        run(["ffmpeg", "-y", "-v", "error", "-ss", "%.2f" % t, "-i", src,
             "-frames:v", "1", "-q:v", "2", src_img])
    from PIL import Image
    im = Image.open(src_img).convert("RGB")
    tw, th = VIDEO_COVER
    ratio = max(tw / im.width, th / im.height)
    rw, rh = round(im.width * ratio), round(im.height * ratio)
    im.resize((rw, rh), Image.LANCZOS).crop(
        ((rw - tw) // 2, (rh - th) // 2, (rw - tw) // 2 + tw, (rh - th) // 2 + th)
    ).save(cover_path, "JPEG", quality=84, optimize=True, progressive=True)
    if not cover_src:
        os.remove(src_img)

    for label, p in (("片段", hl_path), ("小样", pv_path), ("封面", cover_path)):
        print("%s %s  %s" % (label, os.path.basename(p), human(os.path.getsize(p))))
    return {
        "cover": "/images/works/%s.jpg" % slug,
        "preview": "/images/works/previews/%s.mp4" % slug,
        "highlight": "/images/works/highlights/%s.mp4" % slug,
    }


# ---------------- YAML ----------------
def yaml_entry(kind, title, type_, date, note, files, series=None, link=None):
    q = lambda s: '"%s"' % str(s).replace('"', '\\"')
    lines = ["  - title: %s" % q(title), '    kind: "%s"' % kind]
    if series:
        lines.append("    series: %s" % q(series))
    lines += ["    type: %s" % q(type_), "    date: %s" % q(date)]
    for k in ("cover", "preview", "highlight", "full"):
        if files.get(k):
            lines.append("    %s: %s" % (k, q(files[k])))
    if link:
        lines.append("    link: %s" % q(link))
    if note:
        lines.append("    note: %s" % q(note))
    return "\n".join(lines) + "\n"


def write_entry(block, kind):
    text = open(DATA, encoding="utf-8").read()
    if kind == "video":
        if POSTER_MARK not in text:
            sys.exit("找不到海报分区标记，拒绝写入：%s" % POSTER_MARK)
        text = text.replace(POSTER_MARK, block + POSTER_MARK, 1)
    else:
        text = text.rstrip("\n") + "\n" + block
    with open(DATA, "w", encoding="utf-8") as f:
        f.write(text)
    print("已写入 data/works.yaml（%s）" % kind)


# ---------------- 体检 ----------------
def check(build=False):
    text = open(DATA, encoding="utf-8").read()
    items, cur = [], None
    for line in text.splitlines():
        m = re.match(r"\s+- title:\s*\"?(.+?)\"?$", line)
        if m:
            cur = {"title": m.group(1), "kind": "video"}
            items.append(cur)
            continue
        m = re.match(r"\s+(kind|cover|preview|highlight|full|link):\s*\"?([^\"]+)\"?$", line)
        if m and cur:
            cur[m.group(1)] = m.group(2).strip()

    problems = 0
    for it in items:
        missing = []
        for key in ("cover", "preview", "highlight", "full"):
            p = it.get(key)
            if p and p.startswith("/"):
                if not os.path.exists(os.path.join(ROOT, "static", p.lstrip("/"))):
                    missing.append("%s %s" % (key, p))
        if it.get("link"):
            slug = it["link"].strip("/").split("/")[-1]
            if not os.path.exists(os.path.join(ROOT, "content", "posts", slug + ".md")):
                missing.append("link %s（文章不存在）" % it["link"])
        if it["kind"] == "video" and not it.get("highlight"):
            missing.append("缺少 highlight（点开没东西播）")
        if it["kind"] == "poster" and not it.get("full"):
            missing.append("缺少 full（点开只有缩略图）")
        flag = "OK " if not missing else "!! "
        print("%s%-28s %-6s %s" % (flag, it["title"][:26], it["kind"], ", ".join(missing)))
        problems += bool(missing)

    videos = sum(1 for i in items if i["kind"] == "video")
    posters = sum(1 for i in items if i["kind"] == "poster")
    print("\n共 %d 条：视频 %d / 海报 %d，问题 %d" % (len(items), videos, posters, problems))
    if build:
        print("\n构建中…")
        run(["hugo", "--minify", "--cleanDestinationDir"])
        print("构建通过")
    return problems


def main():
    ap = argparse.ArgumentParser(description="作品墙资产流水线")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("poster", help="生成海报封面 + 原图")
    p.add_argument("--src", required=True)
    p.add_argument("--slug", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--type", default="海报")
    p.add_argument("--date", required=True)
    p.add_argument("--note", default="")
    p.add_argument("--write", action="store_true")

    v = sub.add_parser("video", help="切精彩片段 + 小样 + 封面")
    v.add_argument("--src", required=True)
    v.add_argument("--slug", required=True)
    v.add_argument("--start", type=float, default=0.0, help="精彩片段起点（秒）")
    v.add_argument("--dur", type=float, default=15.0, help="精彩片段时长（秒，建议 14-20）")
    v.add_argument("--cover-at", type=float, default=None, help="取封面帧的时间点（相对 --start）")
    v.add_argument("--cover-src", default=None, help="用现成图片当封面")
    v.add_argument("--title", required=True)
    v.add_argument("--series", default="科普")
    v.add_argument("--type", default="科普视频")
    v.add_argument("--date", required=True)
    v.add_argument("--note", default="")
    v.add_argument("--link", default=None)
    v.add_argument("--write", action="store_true")

    c = sub.add_parser("check", help="检查作品资产完整性")
    c.add_argument("--build", action="store_true")

    a = ap.parse_args()
    if a.cmd == "check":
        sys.exit(1 if check(a.build) else 0)

    for k in ("src", "cover_src"):
        path = getattr(a, k, None)
        if path and not os.path.exists(path):
            sys.exit("源文件不存在：%s" % path)

    if a.cmd == "poster":
        files = make_poster(a.src, a.slug)
        block = yaml_entry("poster", a.title, a.type, a.date, a.note, files)
    else:
        files = make_video(a.src, a.slug, a.start, a.dur, a.cover_at, a.cover_src)
        block = yaml_entry("video", a.title, a.type, a.date, a.note, files,
                           series=a.series, link=a.link)

    print("\nYAML 条目：\n" + block)
    if a.write:
        write_entry(block, a.cmd)
        print("下一步：python scripts/work_assets.py check --build")


if __name__ == "__main__":
    main()
