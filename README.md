# news-image-20261124

[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/PatrickTGD/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/PatrickTGD/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

One image that sums up the world news of **Tuesday, November 24, 2026**, drawn as a newspaper front page: "The Day in One Picture."

## What's in the picture

- **Nvidia's rollercoaster** — Monday +31.5% to $165.05 on Jensen Huang's reinstatement as CEO, Tuesday -5.86% to $155.38 (open $159.10, low $150.50). The rally faded.
- **Chip selloff** — Micron -11% after a downgrade, Analog Devices -17% on a weak outlook, AMD -9%.
- **Money moves to safer stocks** — Dow +0.86%, S&P 500 -0.49%, Nasdaq -1.48%. Consumer confidence jumped to 103.3, the highest in nearly two years; Dick's +17%, Dollar Tree +11%.
- **Sanofi buys Insmed for $41B cash** — Insmed +14%, the biggest biotech deal in about 3 years.
- **Anthropic -10%**, now below its $83 IPO price; HPE -16% on a margin warning.
- Footer: gold $3,561.90 (-2.5%), oil $82.05 (+2.4%), markets closed Thursday for Thanksgiving.

## How it works

The image is original artwork drawn programmatically with Pillow (`draw_image.py`) — simple shapes and real fonts, so every word and number is exact and legible at small sizes. The finished PNG ships in the repository as `entry.png`.

`main.py` (Python 3.13, standard library only, no network) copies `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output`). Two runs write identical bytes.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=hej9nhgp&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
