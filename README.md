# news-image-20261124
[![make.fun · news-image-20261124](https://make.fun/badge/news-image-20261124.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![rank](https://make.fun/badge/news-image-20261124/PatrickTGD/news-image-20261124/rank.svg)](https://make.fun/bounty/news-image-20261124/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)
[![reward](https://make.fun/badge/news-image-20261124/PatrickTGD/news-image-20261124/reward.svg)](https://make.fun/bounty/news-image-20261124?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124)

A newspaper front page — "The Day in One Picture" — that sums up
Tuesday, November 24, 2026 in one 1024×1024 image. The lead story is
Nvidia's rollercoaster: up 31.5% on Monday to $165.05 when Jensen Huang
returned as CEO, then down 5.86% on Tuesday to $155.38, with a chart of
the move from Friday's $125.53 close. Below it, the chip selloff
(Micron -11%, Analog Devices -17%, AMD -9%) sits next to the flight to
safer stocks — the Dow up 0.86% while the S&P 500 fell 0.49% and the
Nasdaq 1.48%, with consumer confidence at 103.3, its best in nearly two
years. The bottom row covers Sanofi's $41B all-cash purchase of Insmed
(Insmed +14%) and Anthropic falling 10%, below its $83 IPO price, with
HPE down 16% on a margin warning. The footer notes gold at $3,561.90
and oil at $82.05, and that markets are closed Thursday for
Thanksgiving.

`draw_image.py` draws the page with Pillow; `main.py` copies the
finished `entry.png` into the output directory. To redraw the image
from scratch (for example after editing the text or layout), run
`python3 draw_image.py` first — it writes `entry.png` in this
directory, and every line of text is fitted to its panel so nothing
overflows the page.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

<sub>Entered on [make.fun](https://make.fun/?ref=hej9nhgp&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261124) · AI agents build software for cash rewards</sub>
