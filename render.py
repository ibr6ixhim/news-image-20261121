#!/usr/bin/env python3
"""Render the 21 November 2026 world-news front page (1024x1024 PNG).

Build-time tool only: it reads data/news.json, draws the page with PIL
and the bundled DejaVu fonts, and writes entry.png. The shipped entry
program (main.py) is stdlib-only and copies entry.png to the output,
because the grading container runs Python 3.13 with the standard
library only (RULES.txt) and cannot be relied on to have PIL.

Everything here is drawn from scratch with PIL primitives (rectangles,
polygons, arcs, text). No photo, no copied image, no network. The run
is fully deterministic: fixed seed, fixed data, fixed font files.
"""
import json
import math
import os
import random

from PIL import Image, ImageDraw, ImageFont

HERE = os.path.dirname(os.path.abspath(__file__))
ASSETS = os.path.join(HERE, "assets")
DATA_PATH = os.path.join(HERE, "data", "news.json")

W, H = 1024, 1024
MARGIN = 24

# ---- palette: warm paper, deep navy ink, vermilion, gold, dark teal ----
PAPER = (246, 241, 227)
PAPER_LT = (251, 248, 238)
INK = (16, 30, 51)
INK_SOFT = (52, 68, 92)
VERMILION = (217, 72, 28)
GOLD = (201, 162, 39)
GOLD_LT = (232, 196, 92)
TEAL = (15, 94, 90)
TEAL_LT = (31, 122, 116)
SKY_TOP = (22, 41, 74)
SKY_BOT = (14, 27, 46)
NIGHT = (5, 11, 22)
RULE = (196, 182, 148)
WHITE = (255, 255, 255)
CREAM = (238, 231, 211)

_FONT_CACHE = {}


def font(name, size):
    """Load a bundled font (name: sans, sansb, serif, serifb)."""
    key = (name, size)
    if key not in _FONT_CACHE:
        files = {
            "sans": "DejaVuSans.ttf",
            "sansb": "DejaVuSans-Bold.ttf",
            "serif": "DejaVuSerif.ttf",
            "serifb": "DejaVuSerif-Bold.ttf",
        }
        _FONT_CACHE[key] = ImageFont.truetype(
            os.path.join(ASSETS, files[name]), size
        )
    return _FONT_CACHE[key]


def tw(text, f):
    """Width of text in pixels under font f."""
    return f.getlength(text)


def wrap(text, f, max_w):
    """Greedy word wrap; returns a list of lines that each fit max_w."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if tw(trial, f) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def fit_lines(text, f, max_w, max_lines):
    """Wrap text to at most max_lines lines; truncate the last line with
    an ellipsis if it still does not fit. Returns the lines."""
    lines = wrap(text, f, max_w)
    if len(lines) <= max_lines:
        return lines
    out = lines[:max_lines]
    last = out[-1]
    while last and tw(last + "\u2026", f) > max_w:
        if " " in last:
            last = last.rsplit(" ", 1)[0]
        else:
            last = last[:-1]
    out[-1] = (last + "\u2026") if last else "\u2026"
    return out


def fit_one_line(text, f, max_w, sizes=None):
    """Fit text on one line: try the given font, then smaller sizes,
    then truncate with an ellipsis. Returns (text, font)."""
    if tw(text, f) <= max_w:
        return text, f
    if sizes:
        for size in sizes:
            f2 = font(_font_name_of(f), size)
            if tw(text, f2) <= max_w:
                return text, f2
        f = font(_font_name_of(f), sizes[-1])
    while text and tw(text + "\u2026", f) > max_w:
        text = text[:-1]
    return text.rstrip() + "\u2026", f


def _font_name_of(f):
    # ImageFont objects keep their path in .path (Pillow >= 9).
    base = os.path.basename(getattr(f, "path", "DejaVuSans.ttf"))
    return {
        "DejaVuSans.ttf": "sans",
        "DejaVuSans-Bold.ttf": "sansb",
        "DejaVuSerif.ttf": "serif",
        "DejaVuSerif-Bold.ttf": "serifb",
    }[base]


def load_news():
    with open(DATA_PATH, "r", encoding="utf-8") as fh:
        rows = json.load(fh)
    by_title = {r["title_en"]: r for r in rows}
    verified = [r for r in rows if r.get("verified")]
    assert len(verified) == 25, len(verified)
    return by_title


def sources_line(story):
    return " \u00b7 ".join(story["sources"])


def draw_pill(draw, x, y, text, f, fg, bg, pad_x=10, pad_y=5):
    """Rounded label pill; returns its right edge."""
    w = int(tw(text, f)) + 2 * pad_x
    h = int(f.size * 1.5) + 2 * pad_y
    draw.rounded_rectangle([x, y, x + w, y + h], radius=h // 2, fill=bg)
    draw.text((x + pad_x, y + pad_y + 1), text, font=f, fill=fg)
    return x + w


def starburst(draw, cx, cy, r1, r2, n, color, width=2):
    """Radiating burst: n spikes, alternating long/short."""
    for i in range(n * 2):
        ang = math.pi * i / n
        r = r1 if i % 2 == 0 else r2
        x2 = cx + r * math.cos(ang)
        y2 = cy + r * math.sin(ang)
        draw.line([cx, cy, x2, y2], fill=color, width=width)


def bezier(p0, p1, p2, steps=40):
    pts = []
    for i in range(steps + 1):
        t = i / steps
        x = (1 - t) ** 2 * p0[0] + 2 * (1 - t) * t * p1[0] + t**2 * p2[0]
        y = (1 - t) ** 2 * p0[1] + 2 * (1 - t) * t * p1[1] + t**2 * p2[1]
        pts.append((x, y))
    return pts


# ---------------------------------------------------------------- masthead
def draw_masthead(draw, img):
    draw.rectangle([0, 0, W, 88], fill=INK)
    draw.rectangle([0, 88, W, 92], fill=GOLD)
    # left: paper name
    draw.text((MARGIN, 22), "THE WORLD IN ONE DAY",
              font=font("serifb", 40), fill=WHITE)
    # right: date + scope
    date = "SATURDAY 21 NOVEMBER 2026"
    dw = tw(date, font("sansb", 20))
    draw.text((W - MARGIN - dw, 16), date, font=font("sansb", 20),
              fill=GOLD_LT)
    scope = "WORLD NEWS  \u00b7  18 STORIES  \u00b7  7 REGIONS"
    sw = tw(scope, font("sans", 13))
    draw.text((W - MARGIN - sw, 48), scope, font=font("sans", 13),
              fill=WHITE)


# ---------------------------------------------------------------- hero
def draw_hero(draw, hero):
    x0, y0, x1, y1 = 24, 100, 676, 356
    # night-sky gradient (deterministic bands)
    for yy in range(y0, y1):
        t = (yy - y0) / (y1 - y0)
        r = int(SKY_TOP[0] + (SKY_BOT[0] - SKY_TOP[0]) * t)
        g = int(SKY_TOP[1] + (SKY_BOT[1] - SKY_TOP[1]) * t)
        b = int(SKY_TOP[2] + (SKY_BOT[2] - SKY_TOP[2]) * t)
        draw.line([(x0, yy), (x1, yy)], fill=(r, g, b))
    # stars (fixed seed)
    rng = random.Random(20261121)
    for _ in range(70):
        sx = rng.randint(x0 + 4, x1 - 4)
        sy = rng.randint(y0 + 4, y1 - 90)
        s = rng.choice([1, 1, 1, 2])
        c = rng.choice([WHITE, GOLD_LT, (200, 210, 230)])
        draw.ellipse([sx, sy, sx + s, sy + s], fill=c)
    # skyline silhouettes along the bottom
    base = y1
    bx = x0
    heights = [46, 30, 58, 38, 66, 28, 50, 34, 62, 40, 54, 30, 48, 36, 58, 44]
    i = 0
    while bx < x1:
        bw = rng.choice([28, 34, 40, 46])
        bh = heights[i % len(heights)]
        draw.rectangle([bx, base - bh, bx + bw, base], fill=NIGHT)
        # lit windows
        for wy in range(base - bh + 8, base - 6, 12):
            for wx in range(bx + 6, bx + bw - 4, 10):
                if rng.random() < 0.35:
                    draw.rectangle([wx, wy, wx + 3, wy + 4],
                                   fill=GOLD_LT)
        # antenna on some towers
        if i % 4 == 1:
            draw.line([bx + bw // 2, base - bh, bx + bw // 2, base - bh - 10],
                      fill=NIGHT, width=2)
            draw.ellipse([bx + bw // 2 - 2, base - bh - 13,
                          bx + bw // 2 + 2, base - bh - 9], fill=VERMILION)
        bx += bw + 4
        i += 1
    # three missile arcs (gold / vermilion) + interception bursts
    arcs = [
        ((566, 100), (520, 190), (468, 262), GOLD_LT),
        ((626, 100), (600, 180), (560, 240), (255, 255, 255)),
        ((668, 100), (660, 200), (632, 272), VERMILION),
    ]
    for p0, p1, p2, col in arcs:
        pts = bezier(p0, p1, p2)
        draw.line(pts, fill=col, width=6, joint="curve")
        draw.line(pts, fill=col, width=3, joint="curve")
        draw.ellipse([p2[0] - 4, p2[1] - 4, p2[0] + 4, p2[1] + 4],
                     fill=WHITE)
    for (cx, cy) in [(468, 262), (560, 240), (632, 272)]:
        starburst(draw, cx, cy, 26, 12, 8, GOLD_LT, width=2)
        draw.ellipse([cx - 6, cy - 6, cx + 6, cy + 6], fill=GOLD)
        draw.ellipse([cx - 3, cy - 3, cx + 3, cy + 3], fill=WHITE)
    # headline + context over the sky (top-left, clear of the arcs)
    hl = fit_lines("Houthi missiles intercepted over Riyadh",
                   font("serifb", 32), 520, 2)
    yy = 116
    for line in hl:
        draw.text((40, yy), line, font=font("serifb", 32), fill=WHITE)
        yy += 38
    ctx = fit_lines(hero["context_en"], font("sans", 15), 430, 2)
    yy = 196
    for line in ctx:
        draw.text((40, yy), line, font=font("sans", 15), fill=(220, 226, 236))
        yy += 20
    # badge strip on a dark panel over the skyline
    panel_y = 318
    draw.rounded_rectangle([32, panel_y, 560, panel_y + 28], radius=6,
                           fill=(8, 16, 32))
    px = 40
    px = draw_pill(draw, px, panel_y + 3, "CONFIRMED", font("sansb", 12),
                   WHITE, VERMILION) + 8
    px = draw_pill(draw, px, panel_y + 3, "3 MISSILES", font("sansb", 12),
                   INK, GOLD) + 12
    draw.text((px, panel_y + 8), sources_line(hero), font=font("sans", 12),
              fill=(200, 208, 220))


# ---------------------------------------------------------------- numbers rail
def draw_rail(draw, numbers):
    x0, y0, x1, y1 = 688, 100, 1000, 356
    draw.rectangle([x0, y0, x1, y1], outline=RULE, width=1, fill=PAPER_LT)
    draw.rectangle([x0, y0, x1, y0 + 3], fill=VERMILION)
    draw.text((x0 + 16, y0 + 14), "THE DAY IN NUMBERS",
              font=font("sansb", 14), fill=INK)
    draw.line([(x0 + 16, y0 + 40), (x1 - 16, y0 + 40)], fill=RULE, width=1)
    col_w = (x1 - x0) // 2
    row_h = 68
    for idx, (num, label) in enumerate(numbers):
        col = idx % 2
        row = idx // 2
        cx = x0 + col * col_w + 16
        cy = y0 + 52 + row * row_h
        draw.text((cx, cy), num, font=font("sansb", 30), fill=VERMILION)
        lab = fit_lines(label, font("sans", 12), col_w - 28, 2)
        ly = cy + 36
        for line in lab:
            draw.text((cx, ly), line, font=font("sans", 12), fill=INK_SOFT)
            ly += 15


# ---------------------------------------------------------------- big cards
def card_bepi(draw, x0, y0, x1, y1):
    # deep-space strip: Mercury + probe on an orbit arc
    draw.rectangle([x0, y0, x1, y1], fill=SKY_BOT)
    rng = random.Random(77)
    for _ in range(26):
        sx = rng.randint(x0 + 4, x1 - 4)
        sy = rng.randint(y0 + 4, y1 - 4)
        draw.ellipse([sx, sy, sx + 1, sy + 1], fill=WHITE)
    # orbit ellipse
    draw.arc([x0 + 60, y0 - 46, x1 - 20, y1 + 30], start=200, end=340,
             fill=GOLD_LT, width=2)
    # Mercury
    mx, my, mr = x0 + 78, y0 + 42, 26
    draw.ellipse([mx - mr, my - mr, mx + mr, my + mr], fill=(168, 160, 148))
    for (cx, cy, cr) in [(mx - 8, my - 6, 5), (mx + 9, my + 4, 7),
                         (mx + 2, my + 12, 4), (mx - 12, my + 10, 3)]:
        draw.ellipse([cx - cr, cy - cr, cx + cr, cy + cr],
                     fill=(140, 132, 120))
    # probe: bus + solar panels on the orbit
    px, py = x1 - 96, y0 + 30
    draw.polygon([(px, py - 6), (px + 16, py), (px, py + 6), (px - 16, py)],
                 fill=GOLD)
    draw.rectangle([px - 34, py - 3, px - 16, py + 3], fill=(200, 208, 220))
    draw.rectangle([px + 16, py - 3, px + 34, py + 3], fill=(200, 208, 220))
    draw.rectangle([px - 5, py - 4, px + 5, py + 4], fill=WHITE)


def card_cop(draw, x0, y0, x1, y1):
    # summit strip: globe + thermometer + clock, teal field
    draw.rectangle([x0, y0, x1, y1], fill=TEAL)
    # globe
    gx, gy, gr = x0 + 62, y0 + 42, 30
    draw.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], fill=(120, 190, 180))
    draw.ellipse([gx - 16, gy - 18, gx + 2, gy - 2], fill=GOLD_LT)
    draw.ellipse([gx - 4, gy + 6, gx + 18, gy + 20], fill=GOLD_LT)
    draw.arc([gx - gr, gy - gr, gx + gr, gy + gr], start=0, end=360,
             fill=(220, 235, 230), width=2)
    # thermometer
    tx, ty = x1 - 78, y0 + 8
    draw.rounded_rectangle([tx, ty, tx + 14, ty + 40], radius=7,
                           fill=WHITE)
    draw.ellipse([tx - 3, ty + 36, tx + 17, ty + 56], fill=VERMILION)
    draw.rectangle([tx + 4, ty + 20, tx + 10, ty + 44], fill=VERMILION)
    draw.text((tx - 4, ty + 58), "HOT", font=font("sansb", 11), fill=WHITE)
    # clock showing day 13
    cx, cy, cr = x1 - 150, y0 + 42, 24
    draw.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], fill=WHITE)
    draw.ellipse([cx - cr, cy - cr, cx + cr, cy + cr], outline=INK, width=2)
    draw.line([cx, cy, cx, cy - 14], fill=INK, width=2)
    draw.line([cx, cy, cx + 10, cy + 6], fill=INK, width=2)
    draw.text((cx - 8, cy + 26), "DAY 13", font=font("sansb", 11), fill=WHITE)


def card_peru(draw, x0, y0, x1, y1):
    # quake strip: mountains + seismic trace
    draw.rectangle([x0, y0, x1, y1], fill=(64, 52, 44))
    # mountains
    draw.polygon([(x0, y1), (x0 + 70, y0 + 18), (x0 + 140, y1)],
                 fill=(92, 76, 62))
    draw.polygon([(x0 + 90, y1), (x0 + 170, y0 + 8), (x0 + 250, y1)],
                 fill=(74, 60, 48))
    draw.polygon([(x0 + 200, y1), (x0 + 260, y0 + 26), (x1, y1)],
                 fill=(92, 76, 62))
    # snow caps
    draw.polygon([(x0 + 62, y0 + 26), (x0 + 70, y0 + 18), (x0 + 78, y0 + 26)],
                 fill=WHITE)
    draw.polygon([(x0 + 162, y0 + 16), (x0 + 170, y0 + 8), (x0 + 178, y0 + 16)],
                 fill=WHITE)
    # seismic trace
    mid = y0 + 52
    pts = [(x0 + 8, mid)]
    rng = random.Random(13)
    x = x0 + 8
    while x < x1 - 8:
        step = rng.choice([10, 12, 14])
        amp = rng.choice([4, 6, 18, 26, 8, 5])
        pts.append((x + step // 2, mid - amp if rng.random() < 0.5
                    else mid + amp))
        pts.append((x + step, mid))
        x += step
    draw.line(pts, fill=VERMILION, width=3, joint="curve")
    draw.line(pts, fill=GOLD_LT, width=1, joint="curve")


def draw_cards(draw, cards):
    xs = [(24, 336), (356, 668), (688, 1000)]
    painters = [card_bepi, card_cop, card_peru]
    y0, y1 = 368, 576
    for (x0, x1), story, paint in zip(xs, cards, painters):
        draw.rectangle([x0, y0, x1, y1], outline=RULE, width=1,
                       fill=PAPER_LT)
        paint(draw, x0 + 1, y0 + 1, x1 - 1, y0 + 80)
        # headline (2 lines max, 21 px serif bold)
        hl = fit_lines(story["title_en"], font("serifb", 21), x1 - x0 - 24, 2)
        yy = y0 + 90
        for line in hl:
            draw.text((x0 + 12, yy), line, font=font("serifb", 21), fill=INK)
            yy += 25
        # context (2 lines, 13 px)
        ctx = fit_lines(story["context_en"], font("sans", 13),
                        x1 - x0 - 24, 2)
        yy = y0 + 142
        for line in ctx:
            draw.text((x0 + 12, yy), line, font=font("sans", 13),
                      fill=INK_SOFT)
            yy += 16
        # sources + key number
        draw.text((x0 + 12, y1 - 24), sources_line(story),
                  font=font("sans", 11), fill=INK_SOFT)
        key = story.get("key_number") or ""
        if key:
            kw = tw(key, font("sansb", 12))
            draw.text((x1 - 12 - kw, y1 - 24), key, font=font("sansb", 12),
                      fill=VERMILION)


# ---------------------------------------------------------------- timeline
TIMELINE = [
    (0, "00:09", "Peru quake M6.7"),
    (4, "04:00", "Killer-robot talks"),
    (5, "05:00", "Hormuz tankers hit"),
    (7, "07:00", "Sparta II hit"),
    (14, "14:00", "COP31 deadlock"),
    (18, "18:00", "BepiColombo orbit"),
    (22, "22:00", "Dragon splashdown"),
]


def draw_timeline(draw):
    x0, x1 = MARGIN, W - MARGIN
    draw.text((x0, 590), "24 HOURS \u2014 SATURDAY 21 NOVEMBER (UTC)",
              font=font("sansb", 14), fill=INK)
    line_y = 632
    draw.line([(x0, line_y), (x1, line_y)], fill=RULE, width=2)
    for idx, (hour, clock, label) in enumerate(TIMELINE):
        cx = x0 + int(hour / 24 * (x1 - x0))
        draw.ellipse([cx - 5, line_y - 5, cx + 5, line_y + 5],
                     fill=VERMILION, outline=WHITE, width=1)
        above = (idx % 2 == 0)
        # label block: time (bold) over name, centred on the dot
        tw1 = tw(clock, font("sansb", 11))
        tw2 = tw(label, font("sans", 11))
        lx = min(max(cx - max(tw1, tw2) // 2, x0), x1 - max(tw1, tw2))
        if above:
            draw.text((lx + (max(tw1, tw2) - tw1) // 2, 606), clock,
                      font=font("sansb", 11), fill=INK)
            draw.text((lx, 619), label, font=font("sans", 11), fill=INK_SOFT)
        else:
            draw.text((lx + (max(tw1, tw2) - tw1) // 2, 640), clock,
                      font=font("sansb", 11), fill=INK)
            draw.text((lx, 653), label, font=font("sans", 11), fill=INK_SOFT)


# ---------------------------------------------------------------- world map
CONTINENTS = {
    "north_america": [(-168, 66), (-150, 70), (-130, 71), (-110, 72),
                      (-95, 80), (-85, 76), (-75, 72), (-65, 62),
                      (-55, 52), (-60, 47), (-65, 44), (-70, 42),
                      (-75, 35), (-80, 32), (-81, 26), (-84, 30),
                      (-90, 21), (-95, 16), (-100, 18), (-105, 20),
                      (-110, 23), (-115, 28), (-120, 34), (-125, 40),
                      (-125, 49), (-130, 55), (-140, 60), (-155, 58),
                      (-165, 60), (-168, 66)],
    "greenland": [(-55, 60), (-45, 60), (-35, 64), (-25, 70), (-20, 74),
                  (-30, 76), (-45, 76), (-55, 74), (-58, 68), (-55, 60)],
    "south_america": [(-80, 10), (-77, 7), (-72, 5), (-65, 2), (-58, 0),
                      (-52, -3), (-45, -5), (-38, -8), (-35, -12),
                      (-38, -18), (-40, -25), (-48, -28), (-55, -35),
                      (-62, -40), (-68, -48), (-70, -54), (-73, -45),
                      (-73, -35), (-72, -25), (-75, -18), (-80, -12),
                      (-80, -5), (-80, 5), (-80, 10)],
    "africa": [(-17, 15), (-15, 20), (-10, 28), (-5, 35), (0, 36),
               (10, 37), (15, 32), (20, 32), (25, 32), (30, 31),
               (35, 28), (38, 22), (40, 15), (43, 12), (48, 11),
               (51, 10), (48, 5), (45, 0), (42, -5), (40, -10),
               (38, -15), (35, -20), (32, -25), (30, -30), (25, -33),
               (20, -35), (17, -32), (15, -28), (13, -20), (12, -15),
               (10, -8), (8, 0), (5, 4), (0, 5), (-5, 5), (-10, 6),
               (-15, 8), (-17, 12), (-17, 15)],
    "europe": [(-10, 36), (-9, 38), (-9, 43), (-5, 46), (-2, 48),
               (0, 50), (2, 52), (5, 54), (8, 57), (10, 59), (15, 58),
               (18, 56), (20, 54), (22, 56), (24, 58), (26, 60),
               (28, 62), (30, 65), (32, 68), (35, 68), (40, 68),
               (42, 66), (45, 65), (42, 62), (40, 58), (38, 55),
               (35, 52), (32, 50), (30, 48), (28, 46), (26, 44),
               (24, 42), (22, 40), (20, 40), (18, 40), (15, 42),
               (12, 44), (8, 44), (5, 43), (3, 42), (0, 40), (-2, 37),
               (-5, 36), (-8, 37), (-10, 36)],
    "asia": [(30, 65), (35, 68), (40, 68), (50, 69), (60, 70), (70, 72),
             (80, 73), (90, 75), (100, 76), (110, 74), (120, 73),
             (130, 72), (140, 72), (150, 70), (160, 70), (170, 67),
             (178, 65), (175, 62), (170, 60), (165, 60), (160, 55),
             (155, 50), (150, 45), (145, 42), (140, 38), (135, 35),
             (130, 33), (127, 35), (122, 32), (120, 28), (115, 22),
             (110, 20), (108, 15), (105, 10), (100, 8), (98, 12),
             (95, 16), (92, 20), (88, 22), (85, 20), (82, 15),
             (80, 10), (77, 8), (75, 10), (72, 20), (68, 23), (65, 25),
             (62, 25), (58, 26), (55, 26), (52, 28), (50, 30), (48, 30),
             (45, 32), (42, 35), (40, 37), (38, 38), (35, 38), (32, 40),
             (30, 42), (28, 45), (30, 48), (30, 52), (32, 55), (30, 60),
             (30, 65)],
    "australia": [(113, -22), (114, -28), (115, -33), (118, -35),
                  (122, -34), (126, -32), (130, -32), (133, -35),
                  (136, -35), (139, -38), (142, -38), (146, -39),
                  (150, -37), (153, -32), (153, -27), (150, -22),
                  (147, -19), (144, -15), (142, -11), (140, -12),
                  (137, -13), (135, -15), (132, -12), (130, -13),
                  (127, -14), (124, -16), (121, -18), (118, -20),
                  (115, -21), (113, -22)],
    "se_asia": [(95, 5), (100, 0), (105, -5), (110, -7), (115, -8),
                (120, -10), (125, -9), (130, -5), (135, -4), (140, -8),
                (138, -9), (130, -8), (120, -9), (110, -8), (100, -2),
                (95, 5)],
    "japan": [(130, 31), (133, 34), (137, 35), (140, 38), (141, 41),
              (143, 44), (145, 44), (142, 40), (140, 36), (137, 34),
              (133, 33), (130, 31)],
    "uk": [(-5, 50), (-3, 53), (-5, 56), (-3, 58), (-1, 57), (0, 53),
           (1, 51), (-2, 50), (-5, 50)],
}

# (lon, lat, badge offset dx, dy, legend label)
PINS = [
    (46.7, 24.6, 22, 19, "1  Riyadh"),
    (30.7, 36.9, -22, 20, "2  Antalya \u00b7 COP31"),
    (-75.2, -11.2, 0, 0, "3  Junin, Peru"),
    (33.4, 47.9, 22, -18, "4  Kryvyi Rih"),
    (56.5, 26.5, 22, -17, "5  Strait of Hormuz"),
    (26.0, 59.5, -20, -16, "6  Gulf of Finland"),
    (-115.1, 36.2, 0, 0, "7  Las Vegas"),
]


def draw_map(draw):
    x0, y0, x1, y1 = 24, 676, 340, 944
    draw.text((x0, 680), "WHERE IT HAPPENED", font=font("sansb", 13),
              fill=INK)
    # equirectangular projection, lon -180..180, lat -55..85
    mx0, my0 = x0, 700
    scale = (x1 - x0) / 360.0
    mh = 140 * scale

    def proj(lon, lat):
        return (mx0 + (lon + 180) * scale, my0 + (85 - lat) * scale)

    for poly in CONTINENTS.values():
        pts = [proj(lon, lat) for lon, lat in poly]
        draw.polygon(pts, fill=TEAL, outline=(10, 70, 66))
    # graticule: equator + tropics, faint
    for lat in (0, 23.4, -23.4):
        _, ey = proj(0, lat)
        draw.line([(mx0, ey), (x1, ey)], fill=(200, 190, 160), width=1)
    # pins with leader lines to offset number badges
    for idx, (lon, lat, dx, dy, _label) in enumerate(PINS, start=1):
        px, py = proj(lon, lat)
        bx, by = px + dx, py + dy
        if dx or dy:
            draw.line([px, py, bx, by], fill=VERMILION, width=1)
        draw.ellipse([px - 3, py - 3, px + 3, py + 3], fill=VERMILION,
                     outline=WHITE, width=1)
        draw.ellipse([bx - 8, by - 8, bx + 8, by + 8], fill=INK,
                     outline=WHITE, width=1)
        num = str(idx)
        nw = tw(num, font("sansb", 11))
        draw.text((bx - nw / 2, by - 6), num, font=font("sansb", 11),
                  fill=WHITE)
    # Mercury: not on Earth — small planet icon in the Pacific
    mx, my = 306, 812
    draw.ellipse([mx - 9, my - 9, mx + 9, my + 9], fill=(168, 160, 148),
                 outline=WHITE, width=1)
    draw.ellipse([mx - 3, my - 4, mx + 1, my + 0], fill=(140, 132, 120))
    draw.ellipse([mx + 3, my + 3, mx + 6, my + 6], fill=(140, 132, 120))
    draw.ellipse([mx + 9, my - 9, mx + 25, my + 9], outline=INK, width=2)
    num = "8"
    nw = tw(num, font("sansb", 11))
    draw.text((mx + 17 - nw / 2, my - 6), num, font=font("sansb", 11),
              fill=INK)
    # legend, two columns
    labels = [p[4] for p in PINS] + ["8  Mercury (orbit)"]
    lf = font("sans", 12)
    for i, lab in enumerate(labels):
        col = i // 4
        row = i % 4
        lx = x0 + col * 160
        ly = 850 + row * 14
        draw.text((lx, ly), lab, font=lf, fill=INK_SOFT)
    draw.text((x0, 912), "8 is not on Earth: BepiColombo entered",
              font=font("sans", 11), fill=INK_SOFT)
    draw.text((x0, 926), "orbit around Mercury after 8 years.",
              font=font("sans", 11), fill=INK_SOFT)


# ---------------------------------------------------------------- story list
REGION_TAG = {
    "Middle East": "MIDDLE EAST",
    "Science/Climate": "SCIENCE",
    "Europe": "EUROPE",
    "Asia-Pacific": "ASIA-PACIFIC",
    "Americas": "AMERICAS",
    "Africa": "AFRICA",
}
LIST_TAG = {
    "Verstappen takes Las Vegas pole": "SPORT",
    "BTS sweeps five MAMA Awards": "CULTURE",
    "Leeds thrash Chelsea 4-1 away": "SPORT",
    "England crush New Zealand 37-12": "SPORT",
    "SpaceX Cargo Dragon splashes down": "SCIENCE",
    "Special mosquitoes cut dengue by 69%": "SCIENCE",
}


def draw_list(draw, stories):
    x0, y0, x1 = 352, 676, 1000
    draw.text((x0, 680), "ALSO ON SATURDAY", font=font("sansb", 14), fill=INK)
    draw.line([(x0, 700), (x1, 700)], fill=RULE, width=1)
    col_w = (x1 - x0) // 2
    row_h = 34
    top = 708
    for idx, story in enumerate(stories):
        col = idx // 7
        row = idx % 7
        cx = x0 + col * col_w
        cy = top + row * row_h
        # number + headline (one line, shrink 15 -> 14 -> 13 -> 12 -> 11)
        num = "%d." % (idx + 1)
        nf = font("sansb", 12)
        draw.text((cx, cy + 1), num, font=nf, fill=VERMILION)
        hx = cx + tw(num, nf) + 5
        hw = col_w - (hx - cx) - 4
        htext, hf = fit_one_line(story["title_en"], font("sansb", 15), hw,
                                 sizes=[14, 13, 12, 11])
        draw.text((hx, cy), htext, font=hf, fill=INK)
        # context + region tag (one line)
        tag = LIST_TAG.get(story["title_en"],
                           REGION_TAG.get(story["region"], "WORLD"))
        tag_txt = " \u00b7 " + tag
        tf = font("sansb", 12)
        tag_w = tw(tag_txt, tf)
        ctx_w = col_w - 6 - tag_w - 4
        ctx = story["context_en"]
        cf = font("sans", 12)
        while ctx and tw(ctx + "\u2026", cf) > ctx_w:
            if " " in ctx:
                ctx = ctx.rsplit(" ", 1)[0]
            else:
                ctx = ctx[:-1]
        draw.text((cx, cy + 18), ctx + "\u2026", font=cf, fill=INK_SOFT)
        draw.text((cx + tw(ctx + "\u2026", cf) + 4, cy + 18), tag,
                  font=tf, fill=VERMILION)


# ---------------------------------------------------------------- footer
def draw_footer(draw):
    draw.line([(MARGIN, 950), (W - MARGIN, 950)], fill=RULE, width=1)
    check = ("DATE CHECK \u2014 Every story dated 21 Nov 2026 \u00b7 "
             "Sources: Reuters, AP, AFP, BBC, ESA, USGS, Formula1 and "
             "others \u00b7 All figures as reported")
    draw.text((MARGIN, 962), check, font=font("sansb", 12), fill=INK)
    draw.text((MARGIN, 984),
              "Built by an AI agent for make.fun  \u00b7  "
              "Each story verified against at least two independent sources",
              font=font("sans", 11), fill=INK_SOFT)


# ---------------------------------------------------------------- main
def main():
    by_title = load_news()
    hero = by_title["Houthi missiles intercepted over Riyadh"]
    cards = [by_title[t] for t in (
        "BepiColombo enters orbit around Mercury",
        "COP31 climate talks deadlock on day 13",
        "Magnitude 6.7 earthquake shakes Peru",
    )]
    list_titles = [
        "Russian barrage kills two in Kryvyi Rih",
        "Two tankers hit in Strait of Hormuz",
        "Russian cargo ship hit by drones",
        "Verstappen takes Las Vegas pole",
        "BTS sweeps five MAMA Awards",
        "SpaceX Cargo Dragon splashes down",
        "Israeli drone hits Gaza aid van",
        "Iran claims downing US MQ-9 drone",
        "Rutte vows NATO will defend Poland",
        "Leeds thrash Chelsea 4-1 away",
        "Special mosquitoes cut dengue by 69%",
        "Air Niugini jet lands safely in Davao",
        "Guinea gold ban strands thousands",
        "Congress gives Meta seven-day ultimatum",
    ]
    stories = [by_title[t] for t in list_titles]
    for s in [hero] + cards + stories:
        assert s["verified"], s["title_en"]

    numbers = [
        ("3", "missiles over Riyadh"),
        ("M6.7", "Peru earthquake"),
        ("Day 13", "COP31 deadlock"),
        ("148", "drones at Ukraine"),
        ("2", "tankers hit, Hormuz"),
        ("8 years", "BepiColombo journey"),
    ]

    img = Image.new("RGB", (W, H), PAPER)
    draw = ImageDraw.Draw(img)
    draw_masthead(draw, img)
    draw_hero(draw, hero)
    draw_rail(draw, numbers)
    draw_cards(draw, cards)
    draw_timeline(draw)
    draw_map(draw)
    draw_list(draw, stories)
    draw_footer(draw)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        out_dir = "/output" if os.path.isdir("/output") else "./output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    img.save(out_path, format="PNG", optimize=True)
    print("wrote", out_path, img.size)


if __name__ == "__main__":
    main()
