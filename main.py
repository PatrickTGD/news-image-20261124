#!/usr/bin/env python3
"""make.fun entry for news-image-20261124.

Copies the finished front-page image (entry.png, drawn by draw_image.py and
shipped in this repository) to $MAKEFUN_OUTPUT_DIR/entry.png.
Standard library only, no network, deterministic: the output bytes are
exactly the asset's bytes on every run.
"""
import os
import shutil
from pathlib import Path


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    src = Path(__file__).resolve().parent / "entry.png"
    shutil.copyfile(src, out_dir / "entry.png")


if __name__ == "__main__":
    main()
