#!/usr/bin/env python3
"""Entry for make.fun news-image-20261120: sum up 20 November 2026 in one image.

The image (entry.png, beside this file) is a front-page style summary of the
day's world news, composed programmatically with build_image.py from an
original generated illustration and hand-set headlines. This program's only
job at grading time is to copy it to /output/entry.png, using nothing but
the Python standard library.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    print(f"wrote {dst} ({os.path.getsize(dst)} bytes)")


if __name__ == "__main__":
    main()
