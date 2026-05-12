from pathlib import Path
import re
from PIL import Image, ImageDraw, ImageFont

BASE = Path('/Users/aiad/Desktop/claw/weixingzh/articles/2026-04-29-mimo-100t-orbit')
SRC = BASE / 'mimo-100t-wechat.mixed.md'
OUT = BASE / 'assets'
DEBUG = OUT / 'debug-markdown'
OUT.mkdir(parents=True, exist_ok=True)
DEBUG.mkdir(parents=True, exist_ok=True)

SERIF = '/System/Library/Fonts/Supplemental/Songti.ttc'
SANS = '/System/Library/Fonts/Hiragino Sans GB.ttc'
W, H = 1600, 900
MARGIN_X = 120
MARGIN_TOP = 96
MARGIN_BOTTOM = 88
CONTENT_W = W - MARGIN_X * 2
CONTENT_H = H - MARGIN_TOP - MARGIN_BOTTOM

TARGETS = [
    ('02-track.png', '![不是送福利，是在筛选谁能进入轨道]'),
    ('03-builders.png', '![不是围观者，是已经在干活的人]'),
    ('04-workflow.png', '![真正想抢的，是你的工作流入口]'),
    ('05-orbit.png', '![100T 只是表面，真正发出去的是轨道资格]'),
]


def load_body_lines():
    text = SRC.read_text(encoding='utf-8')
    parts = text.split('---', 2)
    body = parts[2] if len(parts) >= 3 else text
    return body.splitlines()


def find_marker(lines, marker):
    for i, line in enumerate(lines):
        if line.strip().startswith(marker):
            return i
    raise ValueError(marker)


def collect_chunk(lines, marker):
    start = find_marker(lines, marker)
    out = []
    for i in range(start, len(lines)):
        line = lines[i].rstrip()
        if i != start and line.startswith('!['):
            break
        if line.strip() == '---':
            break
        out.append(line)
    return out


def classify(line):
    s = line.strip()
    if not s:
        return ('space', '')
    if s.startswith('# '):
        return ('h1', s[2:].strip())
    if s.startswith('## '):
        return ('h2', s[3:].strip())
    if s.startswith('### '):
        return ('h3', s[4:].strip())
    if s.startswith('!['):
        m = re.match(r'!\[(.*?)\]', s)
        return ('caption', m.group(1).strip() if m else '')
    return ('p', s)


def font(path, size):
    return ImageFont.truetype(path, size, index=0)


def line_height(f):
    a, d = f.getmetrics()
    return a + d


def wrap_text(draw, text, f, max_width):
    if not text:
        return ['']
    result = []
    cur = ''
    for ch in text:
        test = cur + ch
        box = draw.textbbox((0, 0), test, font=f)
        if box[2] - box[0] <= max_width or not cur:
            cur = test
        else:
            result.append(cur)
            cur = ch
    if cur:
        result.append(cur)
    return result


def specs(kind, mode='normal'):
    if mode == 'tight':
        if kind == 'h1': return (font(SERIF, 50), (20,18,16), 12, 14)
        if kind == 'h2': return (font(SERIF, 38), (28,26,24), 8, 12)
        if kind == 'h3': return (font(SERIF, 32), (33,31,28), 6, 10)
        if kind == 'caption': return (font(SANS, 18), (92,86,80), 4, 10)
        return (font(SERIF, 26), (40,36,32), 4, 8)
    if mode == 'compact':
        if kind == 'h1': return (font(SERIF, 54), (20,18,16), 14, 18)
        if kind == 'h2': return (font(SERIF, 40), (28,26,24), 10, 18)
        if kind == 'h3': return (font(SERIF, 34), (33,31,28), 8, 14)
        if kind == 'caption': return (font(SANS, 20), (92,86,80), 6, 12)
        return (font(SERIF, 28), (40,36,32), 6, 12)
    if kind == 'h1': return (font(SERIF, 60), (20,18,16), 16, 24)
    if kind == 'h2': return (font(SERIF, 44), (28,26,24), 12, 22)
    if kind == 'h3': return (font(SERIF, 36), (33,31,28), 10, 18)
    if kind == 'caption': return (font(SANS, 22), (92,86,80), 8, 18)
    return (font(SERIF, 32), (40,36,32), 8, 16)


def build_blocks(raw_lines, mode='normal'):
    img = Image.new('RGB', (W, H), 'white')
    draw = ImageDraw.Draw(img)
    blocks = []
    for line in raw_lines:
        kind, text = classify(line)
        if kind == 'space':
            gap = 10 if mode == 'tight' else 14 if mode == 'compact' else 18
            blocks.append({'kind': 'space', 'gap_after': gap, 'height': 0})
            continue
        f, color, spacing, gap_after = specs(kind, mode=mode)
        lines = wrap_text(draw, text, f, CONTENT_W)
        lh = line_height(f)
        height = len(lines) * lh + max(0, len(lines) - 1) * spacing
        blocks.append({'kind': kind, 'font': f, 'color': color, 'spacing': spacing, 'gap_after': gap_after, 'lines': lines, 'height': height})
    return blocks


def total_height(blocks):
    return sum(b['height'] + b['gap_after'] for b in blocks)


def filter_raw_lines(raw_lines, level=0):
    out = []
    p_count = 0
    for line in raw_lines:
        kind, _ = classify(line)
        if kind == 'p':
            p_count += 1
            if level == 1 and p_count > 5:
                continue
            if level == 2 and p_count > 4:
                continue
            if level == 3 and p_count > 3:
                continue
        if kind == 'space' and level >= 2:
            continue
        out.append(line)
    return out


def squeeze_blocks(raw_lines):
    for level, mode in [(0, 'normal'), (0, 'compact'), (1, 'compact'), (2, 'tight'), (3, 'tight')]:
        candidate = filter_raw_lines(raw_lines, level)
        blocks = build_blocks(candidate, mode=mode)
        if total_height(blocks) <= CONTENT_H:
            return blocks
    raise RuntimeError(f'content too tall after squeeze: {total_height(build_blocks(filter_raw_lines(raw_lines, 3), mode="tight"))} > {CONTENT_H}')


def background(draw):
    for y in range(H):
        ratio = y / H
        r1, g1, b1 = (244, 239, 231)
        r2, g2, b2 = (233, 227, 217)
        r = int(r1 + (r2 - r1) * ratio)
        g = int(g1 + (g2 - g1) * ratio)
        b = int(b1 + (b2 - b1) * ratio)
        draw.line((0, y, W, y), fill=(r, g, b))
    for x in range(0, W, 9):
        for y in range((x * 5) % 13, H, 13):
            draw.point((x, y), fill=(229, 221, 210))
    for x in range(4, W, 17):
        for y in range((x * 7) % 19, H, 19):
            draw.point((x, y), fill=(249, 246, 240))
    draw.rounded_rectangle((62, 54, W - 62, H - 54), radius=28, outline=(212, 201, 186), width=1)
    draw.rounded_rectangle((82, 74, W - 82, H - 74), radius=24, outline=(226, 216, 202), width=1)
    draw.line((MARGIN_X, 132, W - MARGIN_X, 132), fill=(191, 181, 168), width=1)
    draw.line((MARGIN_X, H - 104, W - MARGIN_X, H - 104), fill=(191, 181, 168), width=1)


def render_one(name, raw_lines):
    blocks = squeeze_blocks(raw_lines)
    img = Image.new('RGB', (W, H), '#f3eee6')
    draw = ImageDraw.Draw(img)
    background(draw)

    label_font = font(SANS, 20)
    draw.text((MARGIN_X, 92), 'MIXED MARKDOWN / DIRECT RENDER', font=label_font, fill=(100, 94, 86))
    draw.text((W - MARGIN_X - 120, 92), name.replace('.png', '').upper(), font=label_font, fill=(100, 94, 86))

    y = MARGIN_TOP + 68
    debug_boxes = []
    for b in blocks:
        if b['kind'] == 'space':
            y += b['gap_after']
            continue
        for line in b['lines']:
            draw.text((MARGIN_X, y), line, font=b['font'], fill=b['color'])
            box = draw.textbbox((MARGIN_X, y), line, font=b['font'])
            debug_boxes.append(box)
            y = box[3] + b['spacing']
        y -= b['spacing']
        y += b['gap_after']

    sign_font = font(SANS, 18)
    draw.text((W - MARGIN_X - 46, H - 84), 'AIAD', font=sign_font, fill=(108, 102, 95))
    img.save(OUT / name)

    dbg = img.copy()
    dd = ImageDraw.Draw(dbg)
    dd.rectangle((MARGIN_X, MARGIN_TOP + 32, W - MARGIN_X, H - MARGIN_BOTTOM), outline=(255, 0, 0), width=2)
    for box in debug_boxes:
        dd.rectangle(box, outline=(0, 120, 255), width=1)
    dbg.save(DEBUG / name)


lines = load_body_lines()
for name, marker in TARGETS:
    chunk = collect_chunk(lines, marker)
    render_one(name, chunk)

print('rendered', ', '.join(name for name, _ in TARGETS))
print('debug', DEBUG)
