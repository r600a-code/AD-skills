# 主题色预设（Themes）

5 套精心调配的主题色板，保证 Vogue 高定感 + 电子杂志风的美学不垮。**不允许自定义颜色——色彩搭配错了画面瞬间变丑**，只从以下预设中挑选。

---

## 使用方法

1. 问用户选哪套（或基于内容推荐一套）
2. 在 HTML 中统一使用对应色值
3. 其他样式走内联，一处定义全局复用

---

## 🖋 墨水经典（Monocle Default）

**适合**：通用分享、随笔、行业观察、任何场景都安全的默认选择。
**调性**：纯墨黑 + 暖米白，杂志感最强，Monocle / Apricot 风。

```css
--ink: #1a1a1a;
--ink-secondary: #3d3d3d;
--ink-muted: #8a7f72;
--paper: #faf9f7;
--paper-tint: #f5f0e8;
--accent: #8b0000;
--accent-gold: #c9a96e;
```

---

## 🌊 靛蓝瓷（Indigo Porcelain）

**适合**：科技/AI/技术深度、工程师文化、深度内容。
**调性**：深靛蓝 + 瓷白，冷静、理性、有深度，像学术期刊。

```css
--ink: #0a1f3d;
--ink-secondary: #1a3a5c;
--ink-muted: #6b7b8d;
--paper: #f1f3f5;
--paper-tint: #e4e8ec;
--accent: #1e4d8c;
--accent-gold: #8b9dc3;
```

---

## 🌿 森林墨（Forest Ink）

**适合**：文化、人文、非虚构内容、户外品牌、环保主题。
**调性**：深森林绿 + 象牙，沉稳、有呼吸感，像旧版《国家地理》。

```css
--ink: #1a2e1f;
--ink-secondary: #2d4a33;
--ink-muted: #6b7d6e;
--paper: #f5f1e8;
--paper-tint: #ece7da;
--accent: #2d5a3d;
--accent-gold: #8b9a7b;
```

---

## 🍂 牛皮纸（Kraft Paper）

**适合**：怀旧、文学、个人风格、独立杂志、手作品牌。
**调性**：深棕 + 暖米 + 酒红 + 赭石 + 青灰，多色层但和谐统一。

```css
--ink: #2c1810;
--ink-secondary: #5c3a2e;
--ink-muted: #7a7680;
--paper: #f4efe6;
--paper-tint: #ebe4d8;
--accent: #8b2e3b;
--accent-warm: #b8614a;
--accent-gold: #c4a265;
```

**色彩分工**：
- 标题/章节标题 → `ink-secondary`（暖棕）
- 引言/摘要 → `ink-secondary`（暖棕）
- 正文 → `ink`（深棕）
- 元数据/标签 → `ink-muted`（青灰）
- Pull Quote 文字+边框 → `accent`（酒红）
- Timeline 日期 → `accent-warm`（赭石）
- Kicker/Vision 标签 → `accent-gold`（暗金）
- Ghost 背景字 → `accent-warm` 极淡
- 结束语 → `accent-warm`（赭石）

---

## 🌙 沙丘（Dune）

**适合**：设计、艺术、创意分享、画廊手册、审美优先的内容。
**调性**：炭灰 + 沙色，克制、高级、中性，像沙漠黄昏或建筑设计图册。

```css
--ink: #1f1a14;
--ink-secondary: #2d2620;
--ink-muted: #7a7064;
--paper: #f0e6d2;
--paper-tint: #e3d7bf;
--accent: #5c4a3a;
--accent-gold: #b8a088;
```

---

## 推荐选择参考

| 如果是... | 推荐主题 |
|---|---|
| 不知道选啥 / 第一次用 | 🖋 墨水经典 |
| AI / 技术 / 产品 | 🌊 靛蓝瓷 |
| 文化 / 人文 / 非虚构 | 🌿 森林墨 |
| 个人随笔 / 生活方式 | 🍂 牛皮纸 |
| 设计 / 艺术 / 品牌 | 🌙 沙丘 |

---

## 切换原则

- **一篇文章只用一套主题**，不要中途换色
- 选定主题后在项目记录里备注，方便后续迭代保持一致

## ❌ 不要做的事

- ❌ **不允许混搭**（例如 ink 取墨水经典、accent 取沙丘）——会彻底违和
- ❌ **不允许用户随便给一个 hex 值**——需委婉拒绝并展示 5 套预设让选
