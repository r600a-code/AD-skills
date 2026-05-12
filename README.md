# AD-skills

> A Claude Code Skill that converts Markdown articles into single-file HTML for WeChat Official Account publishing — 5 curated themes, 11 components, Vogue editorial aesthetics, 135-editor compatible.

将 Markdown 文章转换为微信公众号 HTML，融合 **Vogue 高定感**和**电子杂志风**设计原则。全内联样式，直接复制到 135 编辑器即可发布。

## 效果

![example](articles/2026-05-10-shen-gun-gan/article.html)

- **衬线标题 + 非衬线正文 + 等宽元数据**：三层字体系统，视觉层次分明
- **版面有攻击性**：大号数字序号、左对齐分割线、直角边框、黑底引用框
- **克制优于炫技**：不用阴影、圆角、渐变装饰，靠字号对比和留白制造张力
- **135 编辑器兼容**：全选 HTML 复制粘贴即可使用，无需构建工具
- **双版本输出**：浏览器预览版（Google Fonts）+ 135 编辑器版（纯内联样式）

## 安装

### 方式一：一行命令（推荐）

```bash
git clone https://github.com/r600a-code/AD-skills.git ~/.claude/skills/AD-skills
```

### 方式二：手动安装

```bash
# 1. 确保目录存在
mkdir -p ~/.claude/skills/

# 2. 克隆仓库
git clone https://github.com/r600a-code/AD-skills.git ~/.claude/skills/AD-skills

# 3. 验证
ls ~/.claude/skills/AD-skills/
# 应该看到：SKILL.md  templates/  references/
```

安装后，Claude Code 会在对话中自动发现并调用这个 skill。

## 使用

### 触发关键词

在 Claude Code 对话中，提到以下关键词即可触发：

- "帮我写一篇公众号文章"
- "微信排版"
- "135 编辑器"
- "公众号文章"
- "微信公众号 HTML"

### 工作流

1. **输入**：将 Markdown 文章放入 `wechat-input/YYYY-MM-DD.md`
2. **选择主题**：从 5 套预设主题中选一套（或让 AI 根据内容推荐）
3. **生成**：AI 自动输出两个 HTML 文件
4. **预览**：浏览器打开 `article.html` 检查效果
5. **发布**：打开 `article-wechat.html`，全选复制到 135 编辑器

### 输出结构

```
articles/YYYY-MM-DD-slug/
├── article.html           ← 浏览器预览版（Google Fonts + CSS 变量）
└── article-wechat.html    ← 135 编辑器版（全内联样式）
```

## 设计原则

### 字体系统（严禁混用）

| 元素 | 字体 | 用途 |
|------|------|------|
| 标题 | Noto Serif SC / Songti SC | 主标题、副标题、金句 |
| 正文 | Noto Sans SC / PingFang SC | 正文描述、大段阅读 |
| 元数据 | SF Mono / Menlo | 标签、日期、分类 |

### 版面攻击性（Vogue 核心）

- 左对齐，绝对不居中（除结尾金句）
- 直角边框，不用圆角
- 强烈的字号对比（72px 数字序号 vs 17px 正文）
- 黑白对比 + 强调色点缀
- 留白制造张力

### 排版规则

- 大号数字序号：`01 / 02 / 03`，字号 48-72px
- 等宽标签：全大写、字母间距 0.25em、字号 11px
- 左对齐分割线：从左到右渐变消失
- 黑底引用框：深色背景 + 浅色文字
- 左边框高亮：酒红色/金色左边框 + 浅色背景

## 主题色

5 套预设主题，**不允许自定义 hex 值**，保护美学比给自由更重要。

| 主题 | 适合场景 | 特点 |
|------|---------|------|
| 墨水经典 | 通用默认、随笔 | 纯墨黑 + 暖米白 |
| 靛蓝瓷 | 科技 / AI / 技术 | 深靛蓝 + 瓷白 |
| 森林墨 | 文化 / 人文 / 非虚构 | 深森林绿 + 象牙 |
| 牛皮纸 | 个人随笔 / 文学 | 深棕 + 暖米 + 金色 |
| 沙丘 | 设计 / 艺术 / 品牌 | 炭灰 + 沙色 |

每套主题含 7-8 个 CSS 变量，一篇文章只用一套，不可中途换色。

## 组件

11 个可复用的 HTML 组件，全内联样式：

| 组件 | 用途 |
|------|------|
| Chrome | 顶部元信息条（等宽小字 + 日期） |
| Cover Section | 标题区域（Kicker + 衬线大标题 + 引言） |
| Subhead | 章节标题（衬线字体 + 顶部边框） |
| Body | 正文段落（非衬线 17px，行高 2） |
| Pull Quote | 左边框引用（酒红色左边框 + 浅色背景） |
| Vision Block | 洞察框（金色左边框） |
| Timeline | 时间线组件 |
| Quote | 居中金句（上下边框） |
| Ghost | 巨型装饰性背景字 |
| Closing | 结束语 |
| Footer | 底部元信息条 |

详见 [`references/components.md`](references/components.md)。

## 目录结构

```
AD-skills/
├── README.md                    ← 本文件
├── LICENSE                      ← MIT 协议
├── SKILL.md                     ← Claude Code skill 主入口
├── templates/
│   └── template.html            ← HTML 模板（全内联样式）
├── references/
│   ├── design-principles.md     ← 设计原则详解
│   ├── components.md            ← 11 个组件规范手册
│   ├── themes.md                ← 5 套预设主题色
│   └── checklist.md             ← P0/P1/P2 质量检查清单
└── articles/                    ← 示例输出
    └── 2026-05-10-shen-gun-gan/
```

## 致谢

本 skill 的设计原则和视觉系统深受 [guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill) 启发。

[歸藏](https://x.com/op7418) 的 guizang-ppt-skill 是一个用于生成横向翻页 PPT 的 Claude Code Skill，内置电子杂志风和瑞士国际主义两套视觉系统，5 套预设主题，10+ 种页面布局。它的核心设计哲学——**衬线标题 + 非衬线正文 + 等宽元数据**、**克制优于炫技**、**版面有攻击性**——直接塑造了 AD-skills 的审美方向。

感谢歸藏的开源贡献。

## 许可证

[MIT](LICENSE)
