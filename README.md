# 每日斯多葛 · Daily Stoic

> 每天一条斯多葛原文 + 白话翻译 + 现代解读 + 今日行动。
> 不搬运成功学，只搬运两千年前的冷静。

「不要让你的思想或精神自主，被集体思维的催眠力量所左右。」
—— 塞涅卡，如果他会用现代术语

---

## 📜 今日斯多葛

<!-- DAILY-STOIC:BEGIN -->

### 📜 2026 年 8 月 31 日

> "I never return home with the same moral character I departed; something or other is unsettled which I had before settled, something or other I have either relaxed or destroyed in the midst of the crowd."
>
> — Seneca, Letters to Lucilius, Letter VII

**Interpretation**：He's not telling us to become hermits. The point is awareness: notice what shapes you when you're around people. Crowds have a hypnotic pull, and collective emotion overrides individual judgment. You walk into a frenzy, a fight, a trending topic, and walk out no longer yourself. The Stoic fix is to guard your autonomy as a rational being: sync up when it makes sense, but keep your own anchor.

**Today's Action**：Today, watch one 'follow-the-crowd' moment: when others' emotions rise, pause three seconds and ask: is this the reaction I want?

---

**白话**：我每次从人群回来，都不再是出发时的那个我。那些原本已经安顿好的心念，总会在人群里被动摇、被消解、被摧毁。

**解读**：他说「避开人群」，是要我们警惕自己正在被什么影响，不是让我们从此当隐士、不见人。群体有催眠的力量，集体的情绪会接管个人的判断。你走进一场狂欢、一次争吵、一个热搜，出来时你已经不是自己。斯多葛的解药，是守住理性人的自主权：该同频时同频，心里始终有一个自己的锚点。

**今日行动**：今天留意一件「随大流」的小事：别人的情绪起来时，先停三秒，问自己「这是我想要的反应吗」。

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
