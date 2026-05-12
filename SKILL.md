---
name: wechat-article
description: 将 Markdown 文章转换为微信公众号 HTML，融合 Vogue 审美（高端、冷峻、版面攻击性）和 guizang-ppt 杂志风设计原则（衬线标题 + 非衬线正文 + 等宽元数据）。当用户需要发布微信公众号文章、制作公众号排版、或提到"公众号文章"、"微信排版"、"135编辑器"时使用。
---

# 微信公众号文章 Skill

## 这个 Skill 做什么

将 Markdown 文章转换为**单文件 HTML**，视觉基调是：

- **Vogue 高定感** + **电子杂志风**混血风格
- **衬线标题（Noto Serif SC）+ 非衬线正文（Noto Sans SC）+ 等宽元数据（SF Mono）**
- **版面有攻击性**：大号数字序号、左对齐分割线、黑底引用框
- **克制优于炫技**：不用阴影、浮动卡片、渐变装饰
- **适配 135 编辑器**：全选复制粘贴即可使用

## 何时使用

**合适的场景**：
- 微信公众号文章发布
- 需要高端杂志感排版
- 个人随笔、行业观察、深度思考
- 135 编辑器排版

**不合适的场景**：
- 纯技术文档（用 GitHub）
- 需要代码高亮的教程
- 大段表格数据

## 工作流

### Step 1 · 输入规范

**输入目录**：`项目目录/wechat-input/`

```
项目目录/
└── wechat-input/
    └── article.md          ← 原始文章（Markdown 格式）
```

**输入文件要求**：
- 文件名：`YYYY-MM-DD.md`（如 `2026-05-10.md`）
- 格式：标准 Markdown
- 标题：一级标题为文章主标题
- 结构：用二级标题分节

**如果用户直接给文本**：
- 保存到 `wechat-input/YYYY-MM-DD.md`
- 再进入 Step 2

### Step 2 · 输出规范

**输出目录**：`项目目录/articles/YYYY-MM-DD-slug/`

```
项目目录/
└── articles/
    └── YYYY-MM-DD-slug/
        ├── article.html           ← 预览版（Google Fonts + CSS 变量）
        └── article-wechat.html    ← 135 编辑器版（全内联样式）
```

**输出文件要求**：
- `article.html`：带 Google Fonts 引入，可在浏览器直接预览
- `article-wechat.html`：全内联样式，可直接全选复制到 135 编辑器
- 两个文件内容一致，仅样式写法不同
- slug 为文章关键词的英文短横线写法（如 `shen-gun-gan`）

### Step 3 · 设计原则

**字体系统**（严禁混用）：

| 元素 | 字体 | 用途 |
|------|------|------|
| 标题 | Noto Serif SC / Songti SC | 主标题、副标题、金句 |
| 正文 | Noto Sans SC / PingFang SC | 正文描述、大段阅读 |
| 元数据 | SF Mono / Menlo | 标签、日期、分类 |

**颜色系统**（从 `references/themes.md` 选一套，每套含 7 个色值）：

| 主题 | 适合 | 特点 |
|------|------|------|
| 墨水经典 | 通用默认、随笔 | 纯墨黑 + 暖米白 |
| 靛蓝瓷 | 科技、AI、技术 | 深靛蓝 + 瓷白 |
| 森林墨 | 文化、人文 | 深森林绿 + 象牙 |
| 牛皮纸 | 个人随笔、文学 | 深棕 + 暖米 + 金色 |
| 沙丘 | 设计、艺术 | 炭灰 + 沙色 |

**色彩丰富度要求**：
- 每套主题必须用到 `accent` 和 `accent-gold` 两个强调色
- kicker / timeline 日期 / vision 标签用 `accent-gold`
- pull-quote 左边框用 `accent`
- vision block 左边框用 `accent-gold`
- 不要只用黑白灰——至少有 2 个彩色层次

**排版规则**：

1. **大号数字序号**：章节用 `01 / 02 / 03` 标记，字号 72px
2. **等宽标签**：全大写、字母间距 0.25em、小字号 11px
3. **左对齐分割线**：从左到右渐变消失，非居中
4. **黑底引用框**：深色背景 + 浅色文字，用于金句
5. **边框高亮框**：左侧深红边框，用于关键洞察

**版面攻击性**（Vogue 核心）：
- 不要居中排版（除结尾金句）
- 不要圆角卡片
- 不要渐变装饰
- 不要 emoji
- 用字号对比制造视觉张力

### Step 4 · 组件规范

详见 `references/components.md`

核心组件：
- **顶部标签**：等宽小字 + 分割线
- **标题区域**：衬线大标题 + 等宽日期
- **章节块**：大号数字 + 标签 + 标题 + 正文
- **引用框**：黑底白字 / 左边框高亮
- **总结区**：网格布局 + 边框
- **底部**：等宽标签

### Step 5 · 生成 HTML

1. 读取 `wechat-input/YYYY-MM-DD.md`
2. 从 `templates/template.html` 拷贝基础结构
3. 按文章结构填充内容
4. 应用选定的主题色（必须用到 accent + accent-gold）
5. 输出两个文件到 `articles/YYYY-MM-DD-slug/`：
   - `article.html`（Google Fonts 版，浏览器预览用）
   - `article-wechat.html`（全内联样式版，135 编辑器用）

### Step 6 · 自检

生成后对照 `references/checklist.md` 自检：
- [ ] 字体系统正确（衬线/非衬线/等宽）
- [ ] 颜色一致（不混搭主题）
- [ ] 分割线方向正确（左对齐渐变）
- [ ] 引用框样式正确（黑底或左边框）
- [ ] 无 emoji
- [ ] 无居中排版（除结尾）
- [ ] 可直接复制到 135 编辑器

## 目录结构

```
wechat-article/
├── SKILL.md                    ← 你正在读
├── assets/
│   └── fonts.css               ← 字体引入（可选）
├── templates/
│   └── template.html           ← HTML 模板
└── references/
    ├── design-principles.md    ← 设计原则详解
    ├── components.md           ← 组件规范
    ├── themes.md               ← 主题色预设
    └── checklist.md            ← 质量检查清单
```

## 参考审美

本 skill 的视觉基调融合了：

- **Vogue**：高端、冷峻、版面攻击性、绝对控制感
- **Guizang-ppt**：电子杂志风、衬线标题 + 非衬线正文、克制优于炫技
- **Monocle**：杂志版式、留白、结构感

把它们当做风格锚点。
