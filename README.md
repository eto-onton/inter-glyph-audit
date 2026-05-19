# Inter Glyph Audit

Small self-hosted browser page for comparing the original Inter font against an optimized build.

## What it does

- Compares `Inter Original` and `Optimized` in four static weights: `400`, `500`, `600`, and `800`.
- Shows per-font glyph availability from real `cmap` coverage.
- Prevents system fallback from masking missing glyphs.
- Includes a full glyph/codepoint browser grouped by Unicode block.

## Run locally

```bash
python3 -m http.server 4173
```

Then open:

```text
http://127.0.0.1:4173/index.html
```

## Regenerate generated font data

```bash
python3 scripts/build-optimized-static.py
python3 scripts/build-font-coverage.py
```
