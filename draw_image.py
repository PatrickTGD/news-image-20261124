#!/usr/bin/env python3
"""Draw the 'Day in One Picture' front page for Tuesday, November 24, 2026.

Original vector-style artwork drawn with Pillow only -- no copied photos,
artwork or characters. Output: entry.png (1024x1024) next to this script.

Numbers (all from the Nov 24, 2026 market close, checked against Finnhub /
Motley Fool / the day's closing summary):
- NVDA: Mon +31.5% to $165.05 (Huang reinstated), Tue -5.86% to $155.38
  (open $159.10, high $159.92, low $150.50)
- S&P 500 7,201 (-0.49%), Dow 50,021 (+0.86%), Nasdaq 23,733 (-1.48%)
- Chip selloff: Micron -11% (downgrade), Analog Devices -17% (weak outlook),
  AMD -9%
- Consumer confidence 103.3, highest in ~2 years; Dick's +17%
- Sanofi buys Insmed for $41B cash; Insmed +14%
- Anthropic -10%, below its $83 IPO price; HPE -16% on margin warning
- Gold $3,561.90 (-2.5%), WTI oil $82.05 (+2.4%); markets closed Thu
  for Thanksgiving
"""
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path

W = H = 1024
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

INK = (20, 24, 31)
PAPER = (247, 243, 234)
NAVY = (18, 32, 54)
RED = (179, 35, 42)
GREEN = (22, 128, 57)
WHITE = (255, 255, 255)

img = Image.new("RGB", (W, H), PAPER)
d = ImageDraw.Draw(img)


def font(path, size):
    return ImageFont.truetype(path, size)


def fit(text, path, max_w, start, min_size=14):
    """Largest font size <= start that fits text in max_w."""
    s = start
    while s > min_size:
        f = font(path, s)
        if d.textlength(text, font=f) <= max_w:
            return f
        s -= 2
    return font(path, min_size)


def center(text, cx, y, f, fill=INK):
    w = d.textlength(text, font=f)
    d.text((cx - w / 2, y), text, font=f, fill=fill)
    return y + f.size


def left(text, x, y, f, fill=INK):
    d.text((x, y), text, font=f, fill=fill)
    return y + f.size


# ---------------------------------------------------------------- masthead
d.rectangle([0, 0, W, 10], fill=RED)
center("THE DAY IN ONE PICTURE", W // 2, 30, fit("THE DAY IN ONE PICTURE", SERIF, 940, 66))
d.rectangle([36, 118, W - 36, 124], fill=INK)
# date band
d.rectangle([36, 140, W - 36, 228], fill=NAVY)
center("TUESDAY, NOVEMBER 24, 2026", W // 2, 158,
       fit("TUESDAY, NOVEMBER 24, 2026", SANS, 900, 56), fill=WHITE)
center("THE WORLD'S NEWS · ONE FRONT PAGE", W // 2, 240,
       fit("THE WORLD'S NEWS · ONE FRONT PAGE", SANS, 900, 24), fill=(90, 96, 105))


# ---------------------------------------------------------------- helpers
def panel(x0, y0, x1, y1, bg):
    d.rectangle([x0, y0, x1, y1], fill=bg, outline=INK, width=3)


def headline_lines(lines, cx, y, max_w, start=44, fill=INK, gap=6):
    for ln in lines:
        f = fit(ln, SANS, max_w, start)
        center(ln, cx, y, f, fill=fill)
        y += f.size + gap
    return y


def subline(text, cx, y, max_w, start=26, fill=(52, 58, 66)):
    f = fit(text, SANS, max_w, start)
    center(text, cx, y, f, fill=fill)
    return y + f.size


# ---------------------------------------------------------------- lead: NVDA rollercoaster
panel(36, 284, W - 36, 512, (222, 232, 242))
# price line: Fri $125.53 -> Mon $165.05 -> Tue low $150.50 -> Tue close $155.38
# y = 490 - (price - 120) * 3.0
def py(p):
    return 490 - (p - 120) * 3.0

pts = [(70, py(125.53)), (190, py(165.05)), (310, py(150.50)), (450, py(155.38))]
d.line([(70, 490), (470, 490)], fill=(120, 126, 134), width=2)
d.line(pts, fill=RED, width=6, joint="curve")
for (x, y) in pts[1:]:
    d.ellipse([x - 7, y - 7, x + 7, y + 7], fill=RED, outline=WHITE, width=2)
center("+31.5% MON", 190, 300, font(SANS, 22), fill=GREEN)
center("FRI $125.53", 130, 478, font(SANS, 18), fill=(52, 58, 66))
center("TUE CLOSE $155.38", 380, 452, font(SANS, 18), fill=(52, 58, 66))

lx = 740  # text centre for lead panel
y = headline_lines(["NVIDIA'S", "ROLLERCOASTER"], lx, 300, 420, start=46)
y = subline("MON +31.5% · TUE -5.9%", lx, y + 6, 420, start=27, fill=RED)
y = subline("$165.05 → $155.38", lx, y + 4, 420, start=27)
subline("HUANG'S RETURN RALLY FADES", lx, y + 4, 420, start=24)

# ---------------------------------------------------------------- row 2
panel(36, 528, 504, 748, (244, 231, 199))     # chip selloff (left)
panel(520, 528, 988, 748, (222, 214, 240))    # rotation (right)

# Chip selloff: falling line
d.line([(66, 560), (150, 600), (240, 580), (330, 640), (420, 620)],
       fill=RED, width=6, joint="curve")
y = headline_lines(["CHIP SELLOFF"], 270, 646, 440, start=36)
y = subline("MICRON -11% · ADI -17%", 270, y + 2, 440, start=24, fill=RED)
subline("AMD -9% · DOWNGRADE + WEAK OUTLOOK", 270, y + 4, 440, start=20)

# Rotation to safer stocks
y = headline_lines(["DOW +0.86%", "S&P -0.5% · NASDAQ -1.5%"], 754, 548, 440, start=34)
y = subline("MONEY MOVES TO SAFER STOCKS", 754, y + 4, 440, start=23, fill=GREEN)
y = subline("CONFIDENCE 103.3 · BEST IN ~2 YRS", 754, y + 4, 440, start=22)
subline("DICK'S +17% · DOLLAR TREE +11%", 754, y + 4, 440, start=22)

# ---------------------------------------------------------------- row 3
panel(36, 764, 504, 956, (226, 236, 219))     # Sanofi-Insmed (left)
panel(520, 764, 988, 956, (214, 234, 234))    # Anthropic / HPE (right)

y = headline_lines(["SANOFI BUYS", "INSMED: $41B"], 270, 786, 440, start=36)
y = subline("ALL-CASH DEAL", 270, y + 4, 440, start=24, fill=RED)
subline("INSMED +14% · BIGGEST BIOTECH DEAL IN ~3 YRS", 270, y + 4, 440, start=19)

y = headline_lines(["ANTHROPIC -10%"], 754, 786, 440, start=36)
y = subline("BELOW ITS $83 IPO PRICE", 754, y + 4, 440, start=24, fill=RED)
subline("HPE -16% ON MARGIN WARNING", 754, y + 4, 440, start=22)

# ---------------------------------------------------------------- footer
d.rectangle([0, 972, W, H], fill=INK)
center("ALSO TODAY: GOLD $3,561.90 (-2.5%) · OIL $82.05 (+2.4%) · MARKETS CLOSED THU FOR THANKSGIVING",
       W // 2, 986, fit("ALSO TODAY: GOLD $3,561.90 (-2.5%) · OIL $82.05 (+2.4%) · MARKETS CLOSED THU FOR THANKSGIVING",
                        SANS, 980, 24), fill=WHITE)

out = Path(__file__).resolve().parent / "entry.png"
img.save(out, "PNG", optimize=True)
print("wrote", out, out.stat().st_size, "bytes")
