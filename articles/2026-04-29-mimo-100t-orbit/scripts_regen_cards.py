from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

OUT = Path('/Users/aiad/Desktop/claw/weixingzh/articles/2026-04-29-mimo-100t-orbit/assets')
DEBUG = OUT / 'debug'
OUT.mkdir(parents=True, exist_ok=True)
DEBUG.mkdir(parents=True, exist_ok=True)

W, H = 1600, 900
OUTER = 42
FRAME = 66
MARGIN = 110
TOP_LINE_Y = 132
BOTTOM_LINE_Y = 776
RIGHT_COL_W = 226
GUTTER = 78
RIGHT_X = W - MARGIN - RIGHT_COL_W
LEFT_X = MARGIN
LEFT_W = RIGHT_X - LEFT_X - GUTTER
SIDE_LEFT = RIGHT_X + 34
SIDE_RIGHT = W - MARGIN
SIDE_W = SIDE_RIGHT - SIDE_LEFT
TITLE_TOP = 214
TITLE_MAX_H = 286
FOOTER_Y = 818

SERIF = '/System/Library/Fonts/Supplemental/Songti.ttc'
SANS = '/System/Library/Fonts/Hiragino Sans GB.ttc'

cards = [
    {
        'file': '02-track.png',
        'index': '01',
        'label': 'MIMO ORBIT / FILTER',
        'title': ['不是送福利', '是在筛选谁能', '进入轨道'],
        'footer': 'What looks free is really a gate.',
        'side_label_a': 'EDITORIAL NOTE',
        'side_label_b': 'THIS PAGE',
        'side': ['30 天', '100T', '申请制', '人工评估'],
    },
    {
        'file': '03-builders.png',
        'index': '02',
        'label': 'BUILDER SCREEN',
        'title': ['它不是在找', '围观的人', '是在找干活的人'],
        'footer': 'The form is already a filter.',
        'side_label_a': 'EDITORIAL NOTE',
        'side_label_b': 'THIS PAGE',
        'side': ['项目截图', '账单证明', 'GitHub', 'Demo'],
    },
    {
        'file': '04-workflow.png',
        'index': '03',
        'label': 'WORKFLOW ENTRY',
        'title': ['它真正想抢的', '不是试用用户', '而是工作流入口'],
        'footer': 'Not pageviews. Default call chains.',
        'side_label_a': 'EDITORIAL NOTE',
        'side_label_b': 'THIS PAGE',
        'side': ['IDE', 'Agent', '默认调用', '工作流入口'],
    },
    {
        'file': '05-orbit.png',
        'index': '04',
        'label': 'VALUE SIGNAL',
        'title': ['100T 只是表面', '真正发出去的', '是轨道资格'],
        'footer': 'The real signal is who gets let in.',
        'side_label_a': 'EDITORIAL NOTE',
        'side_label_b': 'THIS PAGE',
        'side': ['开源', '开放平台', '生态接入'],
    },
]


def font(path, size, index=0):
    return ImageFont.truetype(path, size, index=index)


def text_box(draw, xy, text, f, anchor='lt'):
    return draw.textbbox(xy, text, font=f, anchor=anchor)


def line_height(f):
    a = f.getmetrics()
    return a[0] + a[1]


def fit_single_line(draw, text, path, start, end, max_width):
    for size in range(start, end - 1, -2):
        f = font(path, size, 0)
        box = text_box(draw, (0, 0), text, f)
        if box[2] - box[0] <= max_width:
            return f
    return font(path, end, 0)


def fit_title(draw, lines, max_width, max_height):
    for size in range(84, 50, -2):
        f = font(SERIF, size, 0)
        lh = line_height(f)
        gap = int(size * 0.26)
        widths = []
        for line in lines:
            b = text_box(draw, (0, 0), line, f)
            widths.append(b[2] - b[0])
        total_h = lh * len(lines) + gap * (len(lines) - 1)
        if max(widths) <= max_width and total_h <= max_height:
            return f, lh, gap
    f = font(SERIF, 50, 0)
    return f, line_height(f), 14


def draw_debug_rect(draw, box, color):
    draw.rectangle(box, outline=color, width=2)


for card in cards:
    img = Image.new('RGB', (W, H), '#f4eee4')
    draw = ImageDraw.Draw(img)

    for y in range(H):
        ratio = y / H
        r1, g1, b1 = (247, 241, 233)
        r2, g2, b2 = (236, 228, 217)
        r = int(r1 + (r2 - r1) * ratio)
        g = int(g1 + (g2 - g1) * ratio)
        b = int(b1 + (b2 - b1) * ratio)
        draw.line((0, y, W, y), fill=(r, g, b))

    for x in range(0, W, 11):
        for y in range((x * 5) % 17, H, 17):
            draw.point((x, y), fill=(232, 224, 212))
    for x in range(7, W, 19):
        for y in range((x * 9) % 23, H, 23):
            draw.point((x, y), fill=(251, 248, 241))

    draw.rectangle((OUTER, OUTER, W - OUTER, H - OUTER), outline=(207, 195, 180), width=1)
    draw.rectangle((FRAME, FRAME, W - FRAME, H - FRAME), outline=(223, 213, 199), width=1)
    draw.line((MARGIN, TOP_LINE_Y, W - MARGIN, TOP_LINE_Y), fill=(191, 180, 165), width=1)
    draw.line((MARGIN, BOTTOM_LINE_Y, W - MARGIN, BOTTOM_LINE_Y), fill=(191, 180, 165), width=1)
    draw.line((RIGHT_X, TOP_LINE_Y, RIGHT_X, BOTTOM_LINE_Y), fill=(191, 180, 165), width=1)

    draw.rounded_rectangle((SIDE_LEFT, 166, SIDE_RIGHT, 308), radius=16, fill=(241, 234, 224))
    draw.rounded_rectangle((SIDE_LEFT, 340, SIDE_RIGHT, 646), radius=16, fill=(244, 238, 230))

    label_font = fit_single_line(draw, card['label'], SANS, 20, 16, 420)
    idx_font = font(SANS, 20, 0)
    side_label_font = font(SANS, 20, 0)
    title_font, title_lh, title_gap = fit_title(draw, card['title'], LEFT_W, TITLE_MAX_H)
    footer_font = fit_single_line(draw, card['footer'], SANS, 20, 14, LEFT_W)
    aiad_font = font(SANS, 18, 0)

    draw.text((LEFT_X, 92), card['label'], font=label_font, fill=(99, 92, 84))
    idx_box = text_box(draw, (0, 0), card['index'], idx_font)
    idx_w = idx_box[2] - idx_box[0]
    draw.text((W - MARGIN - idx_w, 92), card['index'], font=idx_font, fill=(99, 92, 84))

    title_boxes = []
    y = TITLE_TOP
    for line in card['title']:
        draw.text((LEFT_X, y), line, font=title_font, fill=(23, 21, 19))
        b = text_box(draw, (LEFT_X, y), line, title_font)
        title_boxes.append(b)
        y += title_lh + title_gap

    footer_box = text_box(draw, (LEFT_X, FOOTER_Y), card['footer'], footer_font)
    draw.text((LEFT_X, FOOTER_Y), card['footer'], font=footer_font, fill=(109, 100, 91))
    aiad_box_0 = text_box(draw, (0, 0), 'AIAD', aiad_font)
    aiad_w = aiad_box_0[2] - aiad_box_0[0]
    aiad_x = W - MARGIN - aiad_w
    draw.text((aiad_x, FOOTER_Y + 1), 'AIAD', font=aiad_font, fill=(109, 100, 91))
    aiad_box = text_box(draw, (aiad_x, FOOTER_Y + 1), 'AIAD', aiad_font)

    draw.text((SIDE_LEFT + 18, 188), card['side_label_a'], font=side_label_font, fill=(77, 93, 118))
    draw.text((SIDE_LEFT + 18, 366), card['side_label_b'], font=side_label_font, fill=(132, 91, 76))

    side_boxes = []
    sy = 232
    for item in card['side']:
        side_font = fit_single_line(draw, item, SERIF if len(item) <= 4 else SANS, 28 if len(item) <= 4 else 22, 18, SIDE_W - 36)
        draw.text((SIDE_LEFT + 18, sy), item, font=side_font, fill=(30, 27, 23))
        b = text_box(draw, (SIDE_LEFT + 18, sy), item, side_font)
        side_boxes.append((item, b))
        sy = b[3] + 26

    accent = 'Calm. Controlled. Deliberate.'
    accent_font = fit_single_line(draw, accent, SANS, 18, 14, SIDE_W - 36)
    draw.line((SIDE_LEFT + 18, 548, SIDE_RIGHT - 18, 548), fill=(141, 116, 98), width=2)
    accent_box = text_box(draw, (SIDE_LEFT + 18, 574), accent, accent_font)
    draw.text((SIDE_LEFT + 18, 574), accent, font=accent_font, fill=(97, 90, 82))

    img.save(OUT / card['file'])

    debug = img.copy()
    dd = ImageDraw.Draw(debug)
    draw_debug_rect(dd, (LEFT_X, TITLE_TOP, LEFT_X + LEFT_W, TITLE_TOP + TITLE_MAX_H), (255, 0, 0))
    draw_debug_rect(dd, (LEFT_X, FOOTER_Y - 6, LEFT_X + LEFT_W, FOOTER_Y + 34), (0, 128, 255))
    draw_debug_rect(dd, (SIDE_LEFT, 166, SIDE_RIGHT, 308), (0, 180, 0))
    draw_debug_rect(dd, (SIDE_LEFT, 340, SIDE_RIGHT, 646), (0, 180, 0))
    for b in title_boxes:
        draw_debug_rect(dd, b, (255, 100, 100))
    draw_debug_rect(dd, footer_box, (80, 160, 255))
    draw_debug_rect(dd, aiad_box, (80, 160, 255))
    for _, b in side_boxes:
        draw_debug_rect(dd, b, (80, 220, 120))
    draw_debug_rect(dd, accent_box, (80, 220, 120))
    debug.save(DEBUG / card['file'])

print('generated', ', '.join(card['file'] for card in cards))
print('debug_dir', DEBUG)
