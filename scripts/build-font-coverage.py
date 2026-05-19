from __future__ import annotations

import json
from pathlib import Path
import sys

sys.path.insert(0, "/tmp/fontdeps")

from fontTools.ttLib import TTFont


ROOT = Path(__file__).resolve().parents[1]
FONTS = [
    (
        "original",
        [
            "fonts/Inter-Regular.woff2",
            "fonts/Inter-Medium.woff2",
            "fonts/Inter-SemiBold.woff2",
            "fonts/Inter-ExtraBold.woff2",
        ],
    ),
    (
        "optimized",
        [
            "fonts/InterOptimized-Regular.woff2",
            "fonts/InterOptimized-Medium.woff2",
            "fonts/InterOptimized-SemiBold.woff2",
            "fonts/InterOptimized-ExtraBold.woff2",
        ],
    ),
]


def codepoints(path: Path) -> list[int]:
    font = TTFont(path)
    points: set[int] = set()
    for table in font["cmap"].tables:
        if table.isUnicode():
            points.update(table.cmap.keys())
    return sorted(points)


def compact_ranges(points: list[int]) -> list[list[int]]:
    if not points:
        return []
    ranges: list[list[int]] = []
    start = prev = points[0]
    for point in points[1:]:
        if point == prev + 1:
            prev = point
            continue
        ranges.append([start, prev])
        start = prev = point
    ranges.append([start, prev])
    return ranges


coverage = {}
for font_id, rel_paths in FONTS:
    point_set: set[int] = set()
    for rel_path in rel_paths:
        point_set.update(codepoints(ROOT / rel_path))
    points = sorted(point_set)
    coverage[font_id] = {
        "count": len(points),
        "ranges": compact_ranges(points),
    }

(ROOT / "fonts" / "coverage.json").write_text(
    json.dumps(coverage, ensure_ascii=False, separators=(",", ":")),
    encoding="utf-8",
)
