#!/usr/bin/env python3
"""Regenerate the article index block inside README.md.

Reads Hugo posts from content/posts/*.md and replaces the content between
<!-- POSTS:START --> and <!-- POSTS:END --> in README.md.
No third-party dependencies (runs on plain python3 in CI).
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
POSTS = os.path.join(ROOT, "content", "posts")
README = os.path.join(ROOT, "README.md")
SITE = "https://yutterx.com"

START = "<!-- POSTS:START -->"
END = "<!-- POSTS:END -->"


def parse_front_matter(text):
    m = re.match(r"^\ufeff?---\r?\n(.*?)\r?\n---", text, re.S)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"^([A-Za-z_]+):\s*(.*)$", line)
        if mm:
            fm[mm.group(1)] = mm.group(2).strip()
    return fm


def clean(value):
    v = (value or "").strip()
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        v = v[1:-1]
    return v.strip()


def parse_list(value):
    v = (value or "").strip()
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1]
        try:
            return [str(x) for x in json.loads(v.replace("'", '"'))]
        except Exception:
            v = inner
    if not v:
        return []
    return [clean(x) for x in v.split(",") if clean(x)]


def main():
    rows = []
    for path in sorted(glob.glob(os.path.join(POSTS, "*.md"))):
        name = os.path.basename(path)
        if name.startswith("_"):
            continue
        with open(path, encoding="utf-8") as f:
            fm = parse_front_matter(f.read())
        if not fm:
            continue
        if clean(fm.get("draft", "")).lower() == "true":
            continue
        title = clean(fm.get("title", "")) or name[:-3]
        date = clean(fm.get("date", ""))[:10]
        cats = parse_list(fm.get("categories", ""))
        cat = cats[0] if cats else "—"
        ptype = clean(fm.get("posttype", "")) or "—"
        slug = clean(fm.get("slug", "")) or name[:-3]
        rows.append((date, title, cat, ptype, f"{SITE}/posts/{slug}/"))

    rows.sort(key=lambda r: (r[0], r[1]), reverse=True)
    lines = [
        f"> 共 **{len(rows)}** 篇 · 按发布时间倒序 · 本表由 `scripts/update_readme.py` 自动生成",
        "",
        "| 日期 | 文章 | 分类 | 类型 |",
        "|---|---|---|---|",
    ]
    for date, title, cat, ptype, url in rows:
        lines.append(f"| {date} | [{title.replace('|', chr(92) + '|')}]({url}) | {cat} | {ptype} |")
    block = "\n".join(lines)

    with open(README, encoding="utf-8") as f:
        readme = f.read()
    if START not in readme or END not in readme:
        print("README 缺少 POSTS 标记，未修改", file=sys.stderr)
        return 1
    pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.S)
    new_readme = pattern.sub(lambda _m: START + "\n" + block + "\n" + END, readme)
    if new_readme == readme:
        print("索引无变化")
    else:
        with open(README, "w", encoding="utf-8", newline="\n") as f:
            f.write(new_readme)
        print(f"README 索引已更新：{len(rows)} 篇文章")
    return 0


if __name__ == "__main__":
    sys.exit(main())
