# 质量检查清单（Checklist）

生成微信公众号 HTML 后，必须对照此清单逐项检查。

---

## P0 级（必须通过）

### 字体系统

- [ ] **标题用衬线字体**：`font-family: 'Noto Serif SC', 'Songti SC', 'STSong', serif`
- [ ] **正文用非衬线字体**：`font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', 'PingFang SC', 'Noto Sans SC', sans-serif`
- [ ] **元数据用等宽字体**：`font-family: 'SF Mono', 'Menlo', 'Consolas', monospace`
- [ ] **无字体混用**：标题不出现非衬线，正文不出现衬线

### 颜色系统

- [ ] **主题一致**：整篇文章只用一套主题色（从 themes.md 5 套中选）
- [ ] **无混搭**：不从不同主题取色
- [ ] **无自定义 hex**：不使用预设外的颜色
- [ ] **用到强调色**：accent 和 accent-gold 至少各出现 1 次
- [ ] **不只是黑白灰**：至少有 2 个彩色层次（如 kicker 金色、pull-quote 棕色边框）

### 排版规则

- [ ] **无 emoji**：全文不含任何 emoji 字符
- [ ] **无居中排版**：除结尾金句外，所有元素左对齐
- [ ] **无圆角卡片**：所有容器不使用 border-radius
- [ ] **无渐变装饰**：除分割线外，不使用渐变背景
- [ ] **无阴影**：不使用 box-shadow

---

## P1 级（强烈建议）

### 章节结构

- [ ] **大号数字序号**：章节用 01/02/03 标记，字号 48px（手机适配）
- [ ] **等宽标签**：全大写、字母间距 0.25em、字号 11px
- [ ] **内容左缩进**：正文区与标题对齐（padding-left: 60px）
- [ ] **章节标题**：衬线字体，22px，字重 600
- [ ] **主标题**：衬线字体，28px，行高 1.3

### 引用框

- [ ] **黑底白字**：金句使用深色背景 + 浅色文字，padding: 20px
- [ ] **左边框高亮**：洞察使用左侧深红边框，padding: 20px
- [ ] **标签正确**：等宽字体、全大写、颜色与主题一致
- [ ] **金句字号**：15px（手机适配）

### 分割线

- [ ] **左对齐渐变**：从左到右渐变消失，非居中
- [ ] **颜色正确**：使用主题色（--ink）

---

## P2 级（可选优化）

### 细节

- [ ] **行高舒适**：正文行高 1.8-1.9
- [ ] **段落间距**：段落间 margin-bottom: 16px
- [ ] **章节间距**：章节间 margin-bottom: 40px
- [ ] **引用框间距**：引用框上下 margin: 24px 0

### 微信公众号适配

- [ ] **不设置容器宽度**：微信自动处理，不使用 max-width
- [ ] **不设置居中**：微信自动居中，不使用 margin: 0 auto
- [ ] **使用微信默认内边距**：不额外设置 padding
- [ ] **字号适配**：主标题 28px，章节标题 22px，正文 15px
- [ ] **大号数字适配**：48px（非 72px）
- [ ] **左缩进适配**：60px（非 88px）

---

## 135 编辑器兼容性

- [ ] **全选可复制**：HTML 可直接全选复制到 135 编辑器
- [ ] **样式内联**：所有 CSS 使用 style 属性，不依赖外部样式表
- [ ] **无 JavaScript**：不使用任何 JS
- [ ] **无外部资源**：不引用外部字体、图片、CSS

---

## 自检命令

生成 HTML 后，用以下命令快速检查：

```bash
# 检查是否有 emoji
grep -P '[\x{1F600}-\x{1F64F}\x{1F300}-\x{1F5FF}\x{1F680}-\x{1F6FF}\x{1F1E0}-\x{1F1FF}]' output.html

# 检查是否有 text-align: center（除结尾外）
grep -n "text-align.*center" output.html

# 检查是否有 border-radius
grep -n "border-radius" output.html

# 检查是否有 box-shadow
grep -n "box-shadow" output.html
```

---

## 常见问题

### Q: 标题显示成非衬线字体？

A: 检查 font-family 是否包含 `'Noto Serif SC', 'Songti SC', 'STSong', serif`

### Q: 粘贴到 135 编辑器后样式丢失？

A: 确保所有 CSS 使用内联 style 属性，不使用 class

### Q: 分割线不显示？

A: 检查 background 的渐变语法是否正确

### Q: 引用框背景色不显示？

A: 检查 background 属性是否正确设置
