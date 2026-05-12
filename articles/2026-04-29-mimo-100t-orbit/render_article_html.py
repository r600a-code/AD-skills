from pathlib import Path
import html
import re

BASE = Path('/Users/aiad/Desktop/claw/weixingzh/articles/2026-04-29-mimo-100t-orbit')
SRC = BASE / 'mimo-100t-wechat.mixed.md'
OUT = BASE / 'article.html'


def parse_frontmatter(text: str):
    if not text.startswith('---'):
        return {}, text
    parts = text.split('---', 2)
    if len(parts) < 3:
        return {}, text
    raw = parts[1].strip().splitlines()
    meta = {}
    for line in raw:
        if ':' not in line:
            continue
        k, v = line.split(':', 1)
        meta[k.strip()] = v.strip()
    return meta, parts[2].lstrip('\n')


def md_inline(text: str) -> str:
    s = html.escape(text)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', s)
    s = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', s)
    url_pattern = re.compile(r'(?<![">])(https?://[^\s<]+)')
    s = url_pattern.sub(r'<a href="\1">\1</a>', s)
    return s


def render_markdown(body: str) -> str:
    lines = body.splitlines()
    out = []
    para = []

    def flush_para():
        nonlocal para
        if para:
            text = ' '.join(x.strip() for x in para if x.strip())
            out.append(f'<p>{md_inline(text)}</p>')
            para = []

    for raw in lines:
        line = raw.rstrip()
        s = line.strip()
        if not s:
            flush_para()
            continue
        if s == '---':
            flush_para()
            out.append('<hr />')
            continue
        if s.startswith('!['):
            flush_para()
            m = re.match(r'!\[(.*?)\]\((.*?)\)', s)
            if m:
                alt, src = m.groups()
                out.append(
                    '<figure class="md-figure">'
                    f'<img src="{html.escape(src)}" alt="{html.escape(alt)}" />'
                    f'<figcaption>{md_inline(alt)}</figcaption>'
                    '</figure>'
                )
            continue
        if s.startswith('# '):
            flush_para()
            out.append(f'<h1>{md_inline(s[2:].strip())}</h1>')
            continue
        if s.startswith('## '):
            flush_para()
            out.append(f'<h2>{md_inline(s[3:].strip())}</h2>')
            continue
        if s.startswith('### '):
            flush_para()
            out.append(f'<h3>{md_inline(s[4:].strip())}</h3>')
            continue
        if s.startswith('- '):
            flush_para()
            out.append(f'<ul><li>{md_inline(s[2:].strip())}</li></ul>')
            continue
        para.append(s)

    flush_para()
    rendered = '\n      '.join(out)
    return rendered


text = SRC.read_text(encoding='utf-8')
meta, body = parse_frontmatter(text)
title = meta.get('title', 'AIAD Article')
summary = meta.get('summary', '')
rendered = render_markdown(body)

html_doc = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(title)}</title>
  <style>
    :root {{
      --bg: #ece6db;
      --paper: rgba(248, 243, 235, 0.88);
      --text: #171614;
      --muted: #6f6559;
      --line: rgba(34, 28, 23, 0.12);
      --max: 760px;
      --serif: "Iowan Old Style", "Songti SC", "Songti TC", "Noto Serif CJK SC", "STSong", serif;
      --sans: -apple-system, BlinkMacSystemFont, "Helvetica Neue", "PingFang SC", "Hiragino Sans GB", "Noto Sans CJK SC", "Microsoft YaHei", sans-serif;
    }}
    * {{ box-sizing: border-box; }}
    html {{ background: var(--bg); }}
    body {{
      margin: 0;
      color: var(--text);
      font-family: var(--sans);
      background:
        radial-gradient(circle at 18% 16%, rgba(255,255,255,0.22), transparent 0 18%),
        radial-gradient(circle at 78% 28%, rgba(191,170,145,0.18), transparent 0 22%),
        radial-gradient(circle at 52% 78%, rgba(140,118,96,0.12), transparent 0 20%),
        linear-gradient(180deg, #f1eadf 0%, #e8dfd1 46%, #ddd2c1 100%);
      -webkit-font-smoothing: antialiased;
      text-rendering: optimizeLegibility;
    }}
    body::before {{
      content: "";
      position: fixed;
      inset: 0;
      pointer-events: none;
      opacity: 0.2;
      background-image:
        radial-gradient(circle, rgba(255,255,255,0.18) 0 1.8px, transparent 2.2px),
        radial-gradient(circle, rgba(110,90,72,0.12) 0 1.4px, transparent 1.8px),
        radial-gradient(circle, rgba(168,144,118,0.08) 0 3.2px, transparent 3.7px);
      background-size: 24px 24px, 31px 31px, 44px 44px;
      background-position: 0 0, 11px 13px, 6px 18px;
      mix-blend-mode: soft-light;
      filter: blur(0.35px) saturate(0.96);
    }}
    body::after {{
      content: "";
      position: fixed;
      inset: 0;
      pointer-events: none;
      opacity: 0.24;
      background:
        linear-gradient(115deg, rgba(255,255,255,0.16), transparent 34%, rgba(124,104,84,0.08) 68%, transparent 100%),
        linear-gradient(180deg, rgba(255,255,255,0.05), rgba(114,91,72,0.04));
      mix-blend-mode: overlay;
    }}
    .sheet {{
      width: min(calc(100% - 24px), 920px);
      margin: 12px auto;
      background:
        radial-gradient(120% 46% at 12% 10%, rgba(255,255,255,0.42), transparent 0 36%),
        radial-gradient(90% 40% at 88% 18%, rgba(182,157,129,0.24), transparent 0 42%),
        radial-gradient(110% 54% at 44% 82%, rgba(134,109,86,0.16), transparent 0 48%),
        linear-gradient(180deg, rgba(252,247,240,0.96) 0%, rgba(242,233,221,0.97) 50%, rgba(231,220,205,0.98) 100%);
      border: 1px solid var(--line);
      box-shadow: 0 18px 56px rgba(69,51,34,0.08);
      backdrop-filter: blur(9px) saturate(0.8);
      -webkit-backdrop-filter: blur(9px) saturate(0.8);
      position: relative;
      overflow: hidden;
    }}
    .sheet::after {{
      content: "";
      position: absolute;
      inset: 0;
      pointer-events: none;
      opacity: 0.48;
      background:
        linear-gradient(102deg,
          transparent 0%,
          rgba(96,74,58,0.03) 8%,
          rgba(255,255,255,0.16) 14%,
          rgba(116,92,72,0.06) 18%,
          transparent 24%,
          transparent 38%,
          rgba(255,255,255,0.13) 44%,
          rgba(114,90,72,0.055) 48%,
          transparent 54%,
          transparent 66%,
          rgba(255,255,255,0.14) 72%,
          rgba(108,84,66,0.06) 76%,
          transparent 82%,
          transparent 100%),
        linear-gradient(176deg,
          transparent 0%,
          rgba(98,76,58,0.04) 16%,
          rgba(255,255,255,0.1) 21%,
          transparent 28%,
          transparent 46%,
          rgba(110,88,70,0.05) 54%,
          rgba(255,255,255,0.11) 58%,
          transparent 64%,
          transparent 78%,
          rgba(104,82,64,0.045) 86%,
          rgba(255,255,255,0.08) 90%,
          transparent 100%),
        radial-gradient(circle at 18% 24%, rgba(255,255,255,0.16), transparent 0 16%),
        radial-gradient(circle at 76% 68%, rgba(123,100,79,0.09), transparent 0 20%),
        radial-gradient(circle at 42% 52%, rgba(116,92,72,0.07), transparent 0 24%);
      mix-blend-mode: multiply;
      filter: blur(1.2px) contrast(1.06);
    }}
    .sheet::before {{
      content: "";
      position: absolute;
      inset: 0;
      pointer-events: none;
      background:
        radial-gradient(140% 18% at 50% 0%, rgba(255,255,255,0.22), transparent 58%),
        radial-gradient(150% 22% at 50% 100%, rgba(126,101,80,0.16), transparent 62%),
        linear-gradient(118deg, transparent 0%, rgba(255,255,255,0.09) 11%, rgba(118,95,75,0.06) 14%, transparent 18%, transparent 36%, rgba(255,255,255,0.08) 42%, rgba(120,97,76,0.055) 46%, transparent 52%, transparent 68%, rgba(255,255,255,0.07) 74%, rgba(116,92,71,0.05) 78%, transparent 84%, transparent 100%),
        linear-gradient(184deg, transparent 0%, rgba(102,80,63,0.035) 24%, rgba(255,255,255,0.06) 29%, transparent 34%, transparent 62%, rgba(102,80,63,0.03) 72%, rgba(255,255,255,0.05) 76%, transparent 82%, transparent 100%);
      opacity: 0.86;
    }}
    .sheet-frame {{
      position: absolute;
      inset: 16px;
      border: 1px solid rgba(34,28,23,0.06);
      pointer-events: none;
      box-shadow: inset 0 0 0 1px rgba(255,255,255,0.08);
    }}
    .meta {{
      padding: 20px 22px 14px;
      border-bottom: 1px solid var(--line);
      display: flex;
      justify-content: space-between;
      gap: 12px;
      font-size: 12px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--muted);
    }}
    .article {{
      max-width: var(--max);
      margin: 0 auto;
      padding: 28px 22px 56px;
    }}
    h1, h2, h3 {{
      font-family: var(--serif);
      font-weight: 600;
      color: var(--text);
      letter-spacing: -0.03em;
      margin: 1.4em 0 0.5em;
    }}
    h1 {{ font-size: 40px; line-height: 1.08; margin-top: 0.2em; }}
    h2 {{ font-size: 30px; line-height: 1.16; }}
    h3 {{ font-size: 24px; line-height: 1.24; }}
    p {{
      margin: 0 0 18px;
      font-size: 18px;
      line-height: 1.92;
      color: rgba(23,22,20,0.92);
    }}
    .summary {{
      font-size: 17px;
      line-height: 1.86;
      color: rgba(23,22,20,0.78);
      padding-bottom: 18px;
      margin-bottom: 24px;
      border-bottom: 1px solid rgba(34,28,23,0.08);
    }}
    .md-figure {{ margin: 28px 0 32px; }}
    .md-figure img {{
      display: block;
      width: 100%;
      height: auto;
      border: 1px solid rgba(34,28,23,0.1);
      background: #fff;
    }}
    .md-figure figcaption {{
      margin-top: 10px;
      font-size: 12px;
      letter-spacing: 0.12em;
      text-transform: uppercase;
      color: var(--muted);
    }}
    hr {{
      border: 0;
      border-top: 1px solid rgba(34,28,23,0.1);
      margin: 32px 0;
    }}
    a {{ color: inherit; text-decoration-thickness: 1px; text-underline-offset: 2px; }}
    code {{
      font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
      font-size: 0.92em;
      background: rgba(34,28,23,0.05);
      padding: 0.08em 0.32em;
      border-radius: 4px;
    }}
    ul {{ margin: 0 0 18px 1.2em; padding: 0; }}
    li {{ font-size: 18px; line-height: 1.92; margin: 0 0 8px; }}
    @media (max-width: 720px) {{
      .sheet {{ width: calc(100% - 12px); margin: 6px auto; }}
      .meta {{ padding: 16px 16px 12px; flex-direction: column; }}
      .article {{ padding: 22px 16px 42px; }}
      h1 {{ font-size: 32px; }}
      h2 {{ font-size: 26px; }}
      h3 {{ font-size: 22px; }}
      p, li {{ font-size: 16px; line-height: 1.82; }}
      .summary {{ font-size: 15px; }}
    }}
  </style>
</head>
<body>
  <div class="sheet">
    <div class="sheet-frame"></div>
    <div class="meta">
      <span>AIAD / Markdown Direct Render</span>
      <span>Minimal Layout</span>
    </div>
    <main class="article">
      <h1>{html.escape(title)}</h1>
      <p class="summary">{html.escape(summary)}</p>
      {rendered}
    </main>
  </div>
</body>
</html>
'''

OUT.write_text(html_doc, encoding='utf-8')
print(f'wrote {OUT}')
