# 每日斯多葛 · Daily Stoic

> 每天一条斯多葛原文 + 白话翻译 + 现代解读 + 今日行动。
> 不搬运成功学，只搬运两千年前的冷静。

「不要让你的思想或精神自主，被集体思维的催眠力量所左右。」
—— 塞涅卡，如果他会用现代术语

---

## 📜 今日斯多葛

<!-- DAILY-STOIC:BEGIN -->

### 📜 2026 年 8 月 13 日

> "If you want to improve, be content to be thought foolish and stupid."
>
> — Epictetus, Enchiridion, XIII

**Interpretation**：Learning anything new has a price: looking like an idiot for a while. Adults learning English, changing careers, starting a channel, everyone goes through the 'getting laughed at' phase. Epictetus puts it plainly: that's the ticket, and no ticket means no entry. Pride is the biggest tax on progress.

**Today's Action**：Do one thing today that might make you look slow or dumb but helps you, like asking a basic question.

---

**白话**：如果你想进步，就要甘愿被人当成傻瓜。

**解读**：学新东西的代价，是当一段时间傻子。学英语、转行、做账号，都躲不过「被人笑话」那一关。爱比克泰德说得直白：这是门票，不买票进不了门。面子是进步最贵的一项税。

**今日行动**：今天做一件「可能显得很笨」但有益的事，比如问一个基础问题。

<!-- DAILY-STOIC:END -->

---

## 这是什么

一个全自动更新的斯多葛哲学项目：

- 每天北京时间早 8 点，自动发布一条斯多葛语录
- 每条包含：**原文（英文）→ 白话翻译 → 现代解读 → 今日行动**
- 解读侧重「精神自主」和「现代生活应用」，不是成功学
- 已发布的内容永久归档在 [`archive/`](archive/)

### 池子状态

语录池：`data/quotes.json`，轮换规则：已批阅（reviewed）优先发布，草稿（draft）兜底，永不卡更。

## 📚 精选资源

精选斯多葛资源库，见 [`data/resources.json`](data/resources.json)：

| 资源 | 作者 | 类型 | 说明 |
|------|------|------|------|
| 《沉思录》 | 马可·奥勒留 | 书 | 罗马皇帝写给自己的日记，最真实的斯多葛文本，建议入门首选 |
| 《道德书简》 | 塞涅卡 | 书 | 124 封信，谈愤怒、时间、死亡、人群，「每日一段」形态的祖师爷 |
| 《手册》 | 爱比克泰德 | 书 | 原为奴隶的哲学家，语录集，句句可直接拿来用 |
| 《论生命之短暂》 | 塞涅卡 | 书 | 生命不是短，是浪费得太多 |
| 《像哲学家一样生活》 | 威廉·欧文 | 书 | 最好的现代入门书，中文译本优秀 |
| 《每日斯多葛》 | 莱恩·霍利迪 | 书 | 365 天日历书，本项目的参照系 |
| 《障碍即道路》 | 莱恩·霍利迪 | 书 | 「障碍即道路」展开成实操书 |
| 《如何成为斯多葛主义者》 | 马西莫·皮柳奇 | 书 | 哲学教授写的实践手册 |
| Daily Stoic | 莱恩·霍利迪 | 网站 | 全球最大斯多葛内容站 |
| Modern Stoicism | 学术团体 | 网站 | 斯多葛学术复兴组织，每年斯多葛周 |
| Stoic Fellowship | 社区 | 网站 | 全球线下聚会索引 |
| 斯多葛主义 | 维基百科 | 网站 | 免费概览，不懂的概念先查这里 |
| Daily Stoic 播客 | 莱恩·霍利迪 | 播客 | 每天十分钟一集 |
| Stoic Meditations | 马西莫·皮柳奇 | 播客 | 朗读经典 + 学术点评 |
| 斯多葛周 | Modern Stoicism | 课程 | 免费七日实践课 |
| 《道德书简》有声书 | LibriVox | 有声书 | 免费公版全本朗读 |
| 《沉思录》梁实秋译本 | 马可·奥勒留 | 书 | 中文读者经典选择 |
| 斯多葛简介 | B 站 UP 主 | 视频 | 中文入门视频合集 |

完整条目（含链接、星级、标签）见 [`data/resources.json`](data/resources.json)。欢迎提交 PR 补充。

## ✍️ 每周批阅（5 分钟）

每日发布是自动的，但内容质量靠人工把关。每周抽 5 分钟：

1. 打开 [`data/quotes.json`](data/quotes.json)
2. 找 `"status": "draft"` 的条目，读解读和行动建议
3. 认可的改成 `"status": "reviewed"`；不满意的直接改文字
4. commit + push

批阅过的条目会优先发布，草稿是兜底。详细流程见 [`docs/批阅指南.md`](docs/批阅指南.md)。

## 🧠 如何贡献

- **补充语录**：按 `data/quotes.json` 的字段格式添加新条目（原文必须是真实出处）
- **补充资源**：按 `data/resources.json` 的字段格式添加，附链接和一句中文注解
- **改解读**：欢迎 PR 重写任何 draft 条目的解读，风格要求：口语化、直接、结合现代生活

### 语录字段规范

```json
{
  "id": "唯一英文 id",
  "author": "中文作者名",
  "author_en": "作者英文名",
  "source": "中文出处",
  "source_en": "英文出处",
  "original": "英文原文（必须真实，注明出处）",
  "translation": "白话翻译",
  "interpretation": "现代解读（口语化，80-150 字）",
  "action": "今日行动（一句话，可执行）",
  "status": "draft 或 reviewed",
  "date_published": "发布后自动填写，勿手动改"
}
```

## 🚀 技术细节

- 轮换引擎：`scripts/daily_pick.py`（本地可跑 `--dry-run` 预览）
- 自动化：`.github/workflows/daily.yml`，每天 UTC 0:00 和 6:00（北京时间 8:00 和 14:00）各触发一次
- 发布规则：已批阅优先 → 草稿兜底 → 全发完从头轮换，永不停更
- 所有发布永久归档在 `archive/YYYY-MM-DD.md`

### 已知限制：schedule 可能延迟或丢失

GitHub Actions 的定时触发是「尽力而为」，不保证准点，偶发延迟数小时甚至跳过（2026-08-05 实测丢失一次，8/4 延迟 2.5 小时）。已做双触发兜底，但若某天发现没更新，手动补发：

```bash
gh workflow run daily.yml --repo gengyueworks/daily-stoic
```

脚本幂等，同一天不会重复发布，手动补发安全。

---

*「人能征服世界，靠的是先征服自己。」—— 芝诺*
