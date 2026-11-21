#!/usr/bin/env python3
"""news-image-20261121 entry: copy the bundled front-page image to output.

The front page ("THE WORLD IN ONE DAY", Saturday 21 November 2026,
18 verified stories) was rendered at build time by render.py (PIL +
bundled DejaVu fonts) and is shipped in this repository as entry.png.
This program only copies entry.png to MAKEFUN_OUTPUT_DIR (default
/output) and refuses to finish unless the copy is byte-complete, so
both grading runs produce identical bytes.

Standard library only, no network. The grading container runs Python
3.13 with the standard library only (RULES.txt), so the entry must
not depend on PIL at run time.
"""
import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
# SHA-256 of the bundled entry.png, recorded at build time.
EXPECTED_SHA256 = "b9175adeb118d8cd3daffabdab121884a31371ceb88f57b5c3ff448e9ac50cb8"


def _sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def _is_png(path):
    with open(path, "rb") as f:
        return f.read(8) == b"\x89PNG\r\n\x1a\n"


if not os.path.isfile(SRC):
    raise SystemExit("bundled entry.png is missing")
if not _is_png(SRC):
    raise SystemExit("bundled entry.png is not a PNG")

os.makedirs(OUT_DIR, exist_ok=True)
dst = os.path.join(OUT_DIR, "entry.png")
shutil.copyfile(SRC, dst)

# Verify the copy is complete and unaltered: a truncated or different
# output would silently produce a corrupt entry image, so refuse to
# finish unless size and SHA-256 match the bundled file exactly.
if os.path.getsize(dst) != os.path.getsize(SRC):
    raise SystemExit("entry.png copy has the wrong size")
if _sha256(dst) != EXPECTED_SHA256:
    raise SystemExit("entry.png copy has the wrong SHA-256")
print("wrote", dst, os.path.getsize(dst), "bytes")
