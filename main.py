#!/usr/bin/env python3
"""Copy the finished front page into the make.fun output directory.

Standard library only, no network. Deterministic: the output file is a
byte-for-byte copy of entry.png, so repeated runs are identical.
"""
import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    if not os.path.isfile(src):
        print("error: entry.png not found next to main.py; "
              "run `python3 draw_image.py` first", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    if os.path.abspath(src) == os.path.abspath(dst):
        print("entry.png is already in place:", dst)
        return 0
    shutil.copyfile(src, dst)
    print("wrote", dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
