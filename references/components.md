# 组件规范 · Components

这是 `wechat-article` skill 的组件手册。所有样式使用内联 CSS，确保 135 编辑器兼容。

---

## 设计系统

### 颜色变量

```css
--ink: #2c1810;
--ink-secondary: #5c3a2e;
--ink-muted: #7a7680;
--paper: #f4efe6;
--paper-tint: #ebe4d8;
--accent: #8b2e3b;
--accent-warm: #b8614a;
--accent-gold: #c4a265;
--line: rgba(44,24,16,0.10);
```

### 字体系统

| 字体 | 用途 | 字号 |
|------|------|------|
| Noto Serif SC | 标题、金句、引言 | 17-52px |
| -apple-system, PingFang SC | 正文 | 17px |
| SF Mono | 标签、元数据 | 11-12px |
| Playfair Display | Ghost 背景字 | 80-180px |

---

## 目录

- [Chrome](#chrome)
- [Cover Section](#cover-section)
- [Subhead 章节标题](#subhead-章节标题)
- [Body 正文](#body-正文)
- [Pull Quote 引用](#pull-quote-引用)
- [Vision Block 洞察框](#vision-block-洞察框)
- [Timeline 时间线](#timeline-时间线)
- [Quote 居中引用](#quote-居中引用)
- [Ghost 背景字](#ghost-背景字)
- [Closing 结束语](#closing-结束语)
- [Footer](#footer)

---

## Chrome

页面顶部的元信息条。

```html
<div style="padding: 28px 0 20px; border-bottom: 1px solid rgba(44,24,16,0.10); display: flex; justify-content: space-between; align-items: baseline;">
  <span style="font-family: 'SF Mono', 'Menlo', monospace; font-size: 11px; letter-spacing: 0.14em; text-transform: uppercase; color: #7a7680;">AIAD / DAILY REFLECTION</span>
  <span style="font-family: 'SF Mono', 'Menlo', monospace; font-size: 11px; letter-spacing: 0.14em; text-transform: uppercase; color: #7a7680;">2026.05.10</span>
</div>
```

**规则**：
- 等宽字体，11px，字母间距 0.14em
- 全大写，颜色用 ink-muted（如 #7a7680）
- 左侧放标签，右侧放日期

---

## Cover Section

文章开头的标题区域。

```html
<div style="font-family: 'SF Mono', 'Menlo', monospace; font-size: 12px; letter-spacing: 0.18em; text-transform: uppercase; color: #c4a265; margin-bottom: 20px;">DAILY REFLECTION / 个人随笔</div>

<h1 style="font-family: 'Noto Serif SC', 'Songti SC', 'STSong', serif; font-weight: 900; font-size: clamp(32px, 6vw, 52px); line-height: 1.12; letter-spacing: -0.03em; color: #2c1810; margin-bottom: 28px;">文章标题</h1>

<p style="font-family: 'Noto Serif SC', 'Songti SC', serif; font-size: 17px; line-height: 1.86; color: #5c3a2e; padding-bottom: 24px; margin-bottom: 36px; border-bottom: 1px solid rgba(44,24,16,0.10);">引言/摘要内容...</p>
```

**规则**：
- Kicker：等宽字体，12px，字母间距 0.18em，颜色 accent-gold（#c4a265）
- 标题：衬线字体，clamp(32px, 6vw, 52px)，字重 900，颜色 ink（#2c1810）
- 引言：衬线字体，17px，颜色 ink-secondary（#5c3a2e），底部边框

---

## Subhead 章节标题

章节标题，带顶部边框。

```html
<div style="font-family: 'Noto Serif SC', 'Songti SC', serif; font-weight: 700; font-size: clamp(22px, 3.5vw, 30px); line-height: 1.3; letter-spacing: -0.02em; color: #5c3a2e; margin: 48px 0 24px; padding-top: 32px; border-top: 1px solid rgba(44,24,16,0.10);">章节标题</div>
```

**规则**：
- 衬线字体，clamp(22px, 3.5vw, 30px)，字重 700，颜色 ink-secondary（#5c3a2e）
- 顶部边框，padding-top: 32px
- 上下间距：margin: 48px 0 24px

---

## Body 正文

正文段落。

```html
<div>
  <p style="font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif; font-size: 17px; line-height: 2; color: rgba(44,24,16,0.85); margin-bottom: 20px;">正文内容...</p>
</div>
```

**规则**：
- 非衬线字体，17px，行高 2
- 颜色 rgba(44,24,16,0.85)
- 段落间距 20px

---

## Pull Quote 引用

左边框引用，用于金句。

```html
<div style="font-family: 'Noto Serif SC', 'Songti SC', serif; font-weight: 600; font-size: clamp(22px, 3.2vw, 28px); line-height: 1.5; color: #8b2e3b; padding: 36px 32px; margin: 40px 0; border-left: 3px solid #8b2e3b; background: rgba(139,46,59,0.04);">金句内容...</div>
```

**规则**：
- 衬线字体，clamp(22px, 3.2vw, 28px)，字重 600
- 文字+左边框 3px 用 accent 色（酒红 #8b2e3b）
- 背景 rgba(139,46,59,0.04)
- padding: 36px 32px，margin: 40px 0

---

## Vision Block 洞察框

带边框的洞察内容块，左侧用 accent-gold 强调。

```html
<div style="margin: 48px 0; padding: 32px; border: 1px solid rgba(44,24,16,0.10); border-left: 3px solid #c4a265;">
  <div style="font-family: 'SF Mono', 'Menlo', monospace; font-size: 11px; letter-spacing: 0.2em; text-transform: uppercase; color: #c4a265; margin-bottom: 20px;">LABEL</div>
  <p style="font-family: 'Noto Serif SC', 'Songti SC', serif; font-size: 18px; line-height: 1.9; color: #5c3a2e; margin-bottom: 16px;">洞察内容...</p>
</div>
```

**规则**：
- 边框 1px solid rgba(44,24,16,0.10)，左侧 3px accent-gold（#c4a265）
- 标签：等宽字体，11px，字母间距 0.2em，颜色 accent-gold
- 内容：衬线字体，18px，颜色 ink-secondary（#5c3a2e）

---

## Timeline 时间线

时间线组件。

```html
<div style="margin: 40px 0;">
  <div style="display: flex; gap: 20px; margin-bottom: 28px; align-items: flex-start;">
    <span style="font-family: 'SF Mono', 'Menlo', monospace; font-size: 12px; letter-spacing: 0.12em; color: #b8614a; min-width: 80px; padding-top: 4px; text-transform: uppercase;">2024 Q3</span>
    <span style="font-family: -apple-system, BlinkMacSystemFont, 'PingFang SC', sans-serif; font-size: 16px; line-height: 1.8; color: rgba(44,24,16,0.78); flex: 1; padding-left: 20px; border-left: 1px solid rgba(44,24,16,0.10);">时间线内容...</span>
  </div>
</div>
```

**规则**：
- 日期：等宽字体，12px，min-width: 80px，颜色 accent-warm（赭石 #b8614a）
- 内容：非衬线字体，16px，左边框 1px
- 间距：gap: 20px，margin-bottom: 28px

---

## Quote 居中引用

居中的金句，带上下边框。

```html
<div style="font-family: 'Noto Serif SC', 'Songti SC', serif; font-size: clamp(20px, 3vw, 26px); line-height: 1.6; color: #5c3a2e; padding: 32px 0; margin: 36px 0; border-top: 1px solid rgba(44,24,16,0.10); border-bottom: 1px solid rgba(44,24,16,0.10); text-align: center;">金句内容...</div>
```

**规则**：
- 衬线字体，clamp(20px, 3vw, 26px)，颜色 ink-secondary（#5c3a2e）
- 居中对齐，上下边框 1px
- padding: 32px 0，margin: 36px 0

---

## Ghost 背景字

巨型装饰性背景字。

```html
<div style="font-family: 'Playfair Display', 'Noto Serif SC', serif; font-weight: 900; font-size: clamp(80px, 18vw, 180px); line-height: 0.85; letter-spacing: -0.06em; color: rgba(184,97,74,0.08); text-align: center; margin: 40px 0; user-select: none;">关键词</div>
```

**规则**：
- Playfair Display 或 Noto Serif SC，字重 900
- 字号 clamp(80px, 18vw, 180px)
- 颜色极淡，用 accent-warm 色调 rgba(184,97,74,0.08)
- 居中，user-select: none

---

## Closing 结束语

文章结尾。

```html
<div style="font-family: 'Noto Serif SC', 'Songti SC', serif; font-weight: 700; font-size: clamp(20px, 3vw, 26px); line-height: 1.5; color: #b8614a; text-align: center; padding: 48px 0 32px; border-top: 1px solid rgba(44,24,16,0.10);">结束语...</div>
```

**规则**：
- 衬线字体，clamp(20px, 3vw, 26px)，字重 700
- 颜色 accent-warm（赭石 #b8614a）
- 居中对齐，顶部边框
- padding: 48px 0 32px

---

## Footer

页面底部的元信息条。

```html
<div style="padding: 24px 0 28px; border-top: 1px solid rgba(44,24,16,0.10); display: flex; justify-content: space-between; align-items: center;">
  <span style="font-family: 'SF Mono', 'Menlo', monospace; font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; color: #7a7680;">AIAD / 2026</span>
  <span style="font-family: 'SF Mono', 'Menlo', monospace; font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; color: #7a7680;">神棍感</span>
</div>
```

**规则**：
- 等宽字体，11px，字母间距 0.12em
- 全大写，颜色 ink-muted（青灰 #7a7680）
- 左侧放标签，右侧放文章名

---

## ❌ 不要做的事

- ❌ 不要用 emoji
- ❌ 不要用圆角卡片
- ❌ 不要用渐变装饰（除分割线）
- ❌ 不要用阴影
- ❌ 不要用浮动卡片
