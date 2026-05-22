from __future__ import annotations

from pathlib import Path
import sys

sys.path.insert(0, "/tmp/fontdeps")

from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "fonts" / "InterV.tripster.woff2"
WEIGHTS = {
    400: "Regular",
    500: "Medium",
    600: "SemiBold",
    800: "ExtraBold",
}


for weight, name in WEIGHTS.items():
    font = TTFont(SOURCE)
    instance = instantiateVariableFont(font, {"wght": weight}, inplace=False)
    instance.flavor = "woff2"
    instance.save(ROOT / "fonts" / f"InterOptimized-{name}.woff2")
