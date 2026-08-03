#!/usr/bin/env python3
"""
每日斯多葛轮换引擎

从 data/quotes.json 中挑选一条"今天该发的"语录：
1. 优先选 reviewed 且未发布的（用户批阅过的）
2. 没有则选 draft 且未发布的（保证永不停更）
3. 全部发完则从头轮换（reviewed 优先）

用法：
  python3 scripts/daily_pick.py            # 正式运行（写 README + archive）
  python3 scripts/daily_pick.py --dry-run  # 只打印今天会选哪条，不改文件
  python3 scripts/daily_pick.py --date 2026-08-03  # 指定日期（用于补发/测试）
"""

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
QUOTES_PATH = ROOT / "data" / "quotes.json"
README_PATH = ROOT / "README.md"
ARCHIVE_DIR = ROOT / "archive"

BEGIN_MARK = "<!-- DAILY-STOIC:BEGIN -->"
END_MARK = "<!-- DAILY-STOIC:END -->"


def load_quotes():
    with open(QUOTES_PATH, encoding="utf-8") as f:
        return json.load(f)


def save_quotes(quotes):
    with open(QUOTES_PATH, "w", encoding="utf-8") as f:
        json.dump(quotes, f, ensure_ascii=False, indent=2)
        f.write("\n")


def pick_today(quotes, today):
    """挑选今天的语录，返回 (quote, is_new)。"""
    released = [q for q in quotes if q.get("date_published") == today]
    if released:
        return released[0], False

    pool = [q for q in quotes if not q.get("date_published")]
    if not pool:
        pool = quotes

    reviewed = [q for q in pool if q.get("status") == "reviewed"]
    draft = [q for q in pool if q.get("status") != "reviewed"]
    chosen = reviewed[0] if reviewed else draft[0]
    return chosen, True


def render_card(quote, today):
    date_cn = f"{today[:4]} 年 {int(today[5:7])} 月 {int(today[8:10])} 日"
    card = f"""### 📜 {date_cn}

> 「{quote['original']}」
>
> —— {quote['author']}，{quote['source']}

**白话**：{quote['translation']}

**解读**：{quote['interpretation']}

**今日行动**：{quote['action']}
"""
    return card


def update_readme(card):
    text = README_PATH.read_text(encoding="utf-8")
    pattern = re.compile(rf"{re.escape(BEGIN_MARK)}.*?{re.escape(END_MARK)}", re.S)
    block = f"{BEGIN_MARK}\n\n{card}\n{END_MARK}"
    if pattern.search(text):
        text = pattern.sub(block, text)
    elif "## 📜 今日斯多葛" in text:
        text = text.replace("## 📜 今日斯多葛\n\n", f"## 📜 今日斯多葛\n\n{block}\n", 1)
    else:
        text = text.rstrip() + f"\n\n{block}\n"
    README_PATH.write_text(text, encoding="utf-8")


def write_archive(quote, today):
    ARCHIVE_DIR.mkdir(exist_ok=True)
    path = ARCHIVE_DIR / f"{today}.md"
    if path.exists():
        return
    content = f"""# 每日斯多葛 {today}

{render_card(quote, today)}

> 自动发布，原文池：`data/quotes.json`
"""
    path.write_text(content, encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--date", default=None)
    args = parser.parse_args()

    today = args.date or datetime.date.today().isoformat()
    quotes = load_quotes()
    quote, is_new = pick_today(quotes, today)

    print(f"[{today}] 选中：{quote['id']}（{'新发布' if is_new else '已存在'}）")
    print(f"  作者：{quote['author']}  |  状态：{quote['status']}")

    if args.dry_run:
        return

    if is_new:
        quote["date_published"] = today
        save_quotes(quotes)

    card = render_card(quote, today)
    update_readme(card)
    write_archive(quote, today)
    print(f"README 已更新，归档写入 archive/{today}.md")


if __name__ == "__main__":
    main()
