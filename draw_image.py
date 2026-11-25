#!/usr/bin/env python3
"""Draw the Nov 24, 2026 news-image front page (1024x1024 PNG).

One broadsheet page, "The Day in One Picture", summarising Tuesday
November 24, 2026: Nvidia's rollercoaster, the chip selloff, the
flight to safer stocks, Sanofi's $41B Insmed deal, Anthropic's slide,
and the day's gold/oil prices.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024

CREAM = (253, 246, 227)
INK = (17, 17, 17)
RED = (178, 34, 34)
DARKRED = (139, 0, 0)
GREEN = (0, 128, 0)
NAVY = (31, 41, 55)
GREY = (90, 100, 110)
BLUE_BG = (226, 236, 245)
AMBER_BG = (250, 235, 200)
LAV_BG = (232, 222, 246)
GREEN_BG = (228, 240, 224)
TEAL_BG = (220, 238, 240)

SERIF_B = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(path, size):
    return ImageFont.truetype(path, int(size))


def fit_font(path, text, max_size, max_w, min_size=10):
    """Largest font size (<= max_size) at which text fits max_w pixels."""
    size = max_size
    while size > min_size:
        f = font(path, size)
        if f.getlength(text) <= max_w:
            return f
        size -= 1
    return font(path, min_size)


def fit_lines(path, text, max_size, max_w, max_h, min_size=10):
    """Wrap text to max_w and shrink until the block fits max_h.

    Returns (font, [lines]).
    """
    size = max_size
    while size >= min_size:
        f = font(path, size)
        words = text.split()
        lines, cur = [], ""
        for word in words:
            trial = (cur + " " + word).strip()
            if f.getlength(trial) <= max_w:
                cur = trial
            else:
                if cur:
                    lines.append(cur)
                cur = word
        if cur:
            lines.append(cur)
        line_h = int(size * 1.25)
        if line_h * len(lines) <= max_h:
            return f, lines
        size -= 1
    f = font(path, min_size)
    return f, [text]


def centered(draw, cx, y, text, fnt, fill):
    draw.text((cx - fnt.getlength(text) / 2, y), text, font=fnt, fill=fill)


def panel(draw, box, fill):
    draw.rectangle(box, fill=fill, outline=INK, width=3)


def line_chart(draw, points, x0, y0, x1, y1, values):
    """Draw a red polyline through values scaled into the given box."""
    lo, hi = min(values), max(values)
    span = hi - lo or 1.0
    xs = [x0 + (x1 - x0) * i / (len(values) - 1) for i in range(len(values))]
    ys = [y1 - (y0 and (v - lo) / span) * (y1 - y0) for v in values]
    draw.line(list(zip(xs, ys)), fill=RED, width=4)
    for x, y in zip(xs, ys):
        draw.ellipse([x - 5, y - 5, x + 5, y + 5], fill=RED)


def main():
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)

    # Red top strip.
    d.rectangle([0, 0, W, 12], fill=RED)

    # Masthead.
    f = fit_font(SERIF_B, "THE DAY IN ONE PICTURE", 64, W - 60)
    centered(d, W // 2, 26, "THE DAY IN ONE PICTURE", f, INK)
    d.line([(36, 108), (W - 36, 108)], fill=INK, width=5)

    # Date bar.
    d.rectangle([36, 122, W - 36, 186], fill=NAVY)
    f = fit_font(SANS_B, "TUESDAY, NOVEMBER 24, 2026", 46, W - 110)
    centered(d, W // 2, 134, "TUESDAY, NOVEMBER 24, 2026", f, (255, 255, 255))

    # Tagline.
    f = fit_font(SANS_B, "THE WORLD'S NEWS \u00b7 ONE FRONT PAGE", 26, W - 200)
    centered(d, W // 2, 198, "THE WORLD'S NEWS \u00b7 ONE FRONT PAGE", f, GREY)

    # ---- Nvidia panel (full width) ----
    panel(d, [36, 228, W - 36, 492], BLUE_BG)
    # Chart on the left: Fri 125.53 -> Mon 165.05 -> Tue open 159.10
    # -> Tue low 150.50 -> Tue close 155.38.
    nv = [125.53, 165.05, 159.10, 150.50, 155.38]
    line_chart(d, None, 70, 300, 420, 440, nv)
    f = fit_font(SANS_B, "+31.5% MON", 24, 300)
    d.text((80, 258), "+31.5% MON", font=f, fill=GREEN)
    f = fit_font(SANS_B, "FRI $125.53", 20, 200)
    d.text((70, 452), "FRI $125.53", font=f, fill=INK)
    f = fit_font(SANS_B, "TUE CLOSE $155.38", 20, 260)
    d.text((220, 452), "TUE CLOSE $155.38", font=f, fill=INK)
    # Headline block on the right. Each line is fitted to the panel width
    # on its own, so a long word like ROLLERCOASTER can never spill out.
    head_lines = ["NVIDIA'S", "ROLLERCOASTER"]
    y = 238
    for ln in head_lines:
        f = fit_font(SERIF_B, ln, 48, 500)
        centered(d, 720, y, ln, f, INK)
        y += 54
    f = fit_font(SANS_B, "MON +31.5% \u00b7 TUE -5.86%", 28, 520)
    centered(d, 720, y + 2, "MON +31.5% \u00b7 TUE -5.86%", f, RED)
    f = fit_font(SANS_B, "$165.05 \u2192 $155.38", 30, 520)
    centered(d, 720, y + 38, "$165.05 \u2192 $155.38", f, INK)
    f = fit_font(SANS_B, "HUANG'S RETURN RALLY FADES", 22, 520)
    centered(d, 720, y + 74, "HUANG'S RETURN RALLY FADES", f, INK)
    f = fit_font(SANS, "TUE OPEN $159.10 \u00b7 LOW $150.50", 18, 520)
    centered(d, 720, y + 102, "TUE OPEN $159.10 \u00b7 LOW $150.50", f, GREY)

    # ---- Row 2: chip selloff (left) / safer stocks (right) ----
    panel(d, [36, 510, 500, 742], AMBER_BG)
    chips = [100, 92, 96, 84, 88]
    line_chart(d, None, 66, 528, 470, 610, chips)
    f, lines = fit_lines(SERIF_B, "CHIP SELLOFF", 44, 420, 60)
    y = 622
    for ln in lines:
        centered(d, 268, y, ln, f, INK)
        y += int(f.size * 1.12)
    f = fit_font(SANS_B, "MICRON -11% \u00b7 ADI -17%", 26, 430)
    centered(d, 268, y + 4, "MICRON -11% \u00b7 ADI -17%", f, RED)
    f = fit_font(SANS, "AMD -9% \u00b7 DOWNGRADE + WEAK OUTLOOK", 19, 430)
    centered(d, 268, y + 38, "AMD -9% \u00b7 DOWNGRADE + WEAK OUTLOOK", f, INK)

    panel(d, [524, 510, W - 36, 742], LAV_BG)
    f = fit_font(SANS_B, "DOW +0.86%", 44, 420)
    centered(d, 756, 524, "DOW +0.86%", f, INK)
    f = fit_font(SANS_B, "S&P -0.49% \u00b7 NASDAQ -1.48%", 26, 430)
    centered(d, 756, 580, "S&P -0.49% \u00b7 NASDAQ -1.48%", f, INK)
    f = fit_font(SANS_B, "MONEY MOVES TO SAFER STOCKS", 22, 430)
    centered(d, 756, 620, "MONEY MOVES TO SAFER STOCKS", f, GREEN)
    f = fit_font(SANS, "CONFIDENCE 103.3 \u00b7 BEST IN ~2 YRS", 20, 430)
    centered(d, 756, 654, "CONFIDENCE 103.3 \u00b7 BEST IN ~2 YRS", f, INK)
    f = fit_font(SANS, "DICK'S +17% \u00b7 DOLLAR TREE +11%", 20, 430)
    centered(d, 756, 684, "DICK'S +17% \u00b7 DOLLAR TREE +11%", f, INK)

    # ---- Row 3: Sanofi (left) / Anthropic (right) ----
    panel(d, [36, 760, 500, 952], GREEN_BG)
    f, lines = fit_lines(SERIF_B, "SANOFI BUYS INSMED: $41B", 36, 420, 100)
    y = 778
    for ln in lines:
        centered(d, 268, y, ln, f, INK)
        y += int(f.size * 1.1)
    f = fit_font(SANS_B, "ALL-CASH DEAL", 26, 420)
    centered(d, 268, y + 4, "ALL-CASH DEAL", f, RED)
    f = fit_font(SANS, "INSMED +14% \u00b7 BIGGEST BIOTECH DEAL IN ~3 YRS", 16, 430)
    centered(d, 268, y + 40, "INSMED +14% \u00b7 BIGGEST BIOTECH DEAL IN ~3 YRS", f, INK)

    panel(d, [524, 760, W - 36, 952], TEAL_BG)
    f = fit_font(SANS_B, "ANTHROPIC -10%", 40, 420)
    centered(d, 756, 792, "ANTHROPIC -10%", f, INK)
    f = fit_font(SANS_B, "BELOW ITS $83 IPO PRICE", 24, 430)
    centered(d, 756, 848, "BELOW ITS $83 IPO PRICE", f, RED)
    f = fit_font(SANS, "HPE -16% ON MARGIN WARNING", 20, 430)
    centered(d, 756, 888, "HPE -16% ON MARGIN WARNING", f, INK)

    # Footer bar.
    d.rectangle([0, 968, W, H], fill=NAVY)
    foot = ("ALSO TODAY: GOLD $3,561.90 (-2.5%) \u00b7 OIL $82.05 (+2.4%) "
            "\u00b7 MARKETS CLOSED THU FOR THANKSGIVING")
    f = fit_font(SANS_B, foot, 22, W - 40)
    centered(d, W // 2, 982, foot, f, (255, 255, 255))

    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    img.save(out)
    print("wrote", out)


if __name__ == "__main__":
    main()
