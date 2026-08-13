#!/usr/bin/env python3
"""
Renders a carousel draft (content/drafts/*.md, following
content/templates/carousel-template.md) into one on-brand PNG per slide,
using the same dark/amber visual system as brand/assets/.

Usage:
    python3 scripts/generate_slides.py content/drafts/2026-08-13-am.md

Output:
    content/drafts/images/<draft-stem>/slide-1.png, slide-2.png, ...

Requires a Chromium binary (headless screenshot) — no other dependencies.
"""
import os
import re
import subprocess
import sys
import tempfile

WIDTH, HEIGHT = 1080, 1350

BG = "#0E0F11"
FG = "#F5F1EA"
ACCENT = "#F5A623"
MUTED = "#8a8a84"
CARD_BG = "#17181B"

HEADER_RE = re.compile(r"^(TOPIC|PILLAR|TOOLS USED|AFFILIATE):\s*(.*)$")
SLIDE_RE = re.compile(r"^SLIDE\s+(\d+)\s*(?:\(([^)]*)\))?\s*:\s*(.*)$")
SECTION_RE = re.compile(r"^(CAPTION|HASHTAGS|IMAGE BRIEF)\s*:\s*(.*)$")


def find_chrome():
    for candidate in (
        "/opt/pw-browsers/chromium",
        "/opt/pw-browsers/chromium_headless_shell-1194/chrome-headless-shell",
    ):
        if os.path.exists(candidate):
            return candidate
    raise RuntimeError("No Chromium binary found in /opt/pw-browsers/")


def parse_draft(text):
    result = {"topic": "", "pillar": "", "slides": []}
    slide_map = {}
    section_buffers = {"CAPTION": [], "HASHTAGS": [], "IMAGE BRIEF": []}
    current = None

    for raw in text.splitlines():
        line = raw.rstrip()

        m = HEADER_RE.match(line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if key == "TOPIC":
                result["topic"] = val
            elif key == "PILLAR":
                result["pillar"] = val
            current = None
            continue

        m = SLIDE_RE.match(line)
        if m:
            num = int(m.group(1))
            label = (m.group(2) or "").strip()
            inline = m.group(3).strip()
            slide_map[num] = {"label": label, "lines": [inline] if inline else []}
            current = ("slide", num)
            continue

        m = SECTION_RE.match(line)
        if m:
            key, inline = m.group(1), m.group(2).strip()
            if inline:
                section_buffers[key].append(inline)
            current = ("section", key)
            continue

        if line.strip() == "":
            continue
        if current is None:
            continue
        if current[0] == "slide":
            slide_map[current[1]]["lines"].append(line.strip())
        elif current[0] == "section":
            section_buffers[current[1]].append(line.strip())

    for num in sorted(slide_map):
        result["slides"].append(
            {"num": num, "label": slide_map[num]["label"], "lines": slide_map[num]["lines"]}
        )
    return result


def esc(s):
    return (
        s.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace('"', "&quot;")
    )


def headline_font_size(text):
    n = len(text)
    if n < 30:
        return 76
    if n < 55:
        return 60
    if n < 90:
        return 48
    return 38


def body_font_size(text):
    n = len(text)
    if n < 80:
        return 36
    if n < 160:
        return 30
    return 26


CHECK_ICON = f"""
<svg width="64" height="64" viewBox="0 0 90 90" xmlns="http://www.w3.org/2000/svg">
  <rect width="90" height="90" rx="20" fill="{ACCENT}"/>
  <path d="M18 48 L40 70 L74 22" fill="none" stroke="{BG}" stroke-width="10"
        stroke-linecap="round" stroke-linejoin="round"/>
</svg>
"""


def render_slide_html(slide, total, pillar, handle):
    is_hook = slide["num"] == 1
    is_cta = "cta" in slide["label"].lower() or slide["num"] == total

    lines = [l for l in slide["lines"] if l.strip()]
    headline = lines[0] if lines else ""
    body_lines = lines[1:] if len(lines) > 1 else []
    body = " ".join(body_lines)

    pillar_tag = ""
    if not is_hook:
        pillar_tag = f"""
        <div style="display:flex;align-items:center;gap:14px;">
          <div style="width:14px;height:14px;border-radius:4px;background:{ACCENT};"></div>
          <div style="font-family:Arial,Helvetica,sans-serif;font-size:26px;font-weight:700;
                      letter-spacing:3px;color:{ACCENT};text-transform:uppercase;">
            {esc(pillar)}
          </div>
        </div>
        """

    if is_hook:
        content = f"""
        <div style="display:flex;flex-direction:column;align-items:flex-start;gap:28px;">
          <div style="width:90px;height:8px;background:{ACCENT};border-radius:4px;"></div>
          <div style="font-family:Arial,Helvetica,sans-serif;font-weight:800;
                      font-size:{headline_font_size(headline)}px;line-height:1.15;
                      color:{FG};">
            {esc(headline)}
          </div>
        </div>
        """
    elif is_cta:
        content = f"""
        <div style="display:flex;flex-direction:column;align-items:center;text-align:center;gap:40px;">
          {CHECK_ICON}
          <div style="font-family:Arial,Helvetica,sans-serif;font-weight:800;
                      font-size:{headline_font_size(headline)}px;line-height:1.2;color:{FG};">
            {esc(headline)}
          </div>
          <div style="font-family:Arial,Helvetica,sans-serif;font-weight:700;
                      font-size:34px;letter-spacing:1px;color:{ACCENT};">
            {esc(handle)}
          </div>
        </div>
        """
    else:
        body_html = (
            f"""<div style="font-family:Arial,Helvetica,sans-serif;font-weight:400;
                     font-size:{body_font_size(body)}px;line-height:1.5;color:{MUTED};
                     max-width:840px;">{esc(body)}</div>"""
            if body
            else ""
        )
        content = f"""
        <div style="display:flex;flex-direction:column;gap:26px;
                    background:{CARD_BG};border-radius:28px;padding:64px;">
          <div style="font-family:Arial,Helvetica,sans-serif;font-weight:800;
                      font-size:{headline_font_size(headline)}px;line-height:1.2;color:{FG};">
            {esc(headline)}
          </div>
          {body_html}
        </div>
        """

    footer = "" if is_cta else f"""
    <div style="display:flex;justify-content:space-between;align-items:center;">
      <div style="font-family:Arial,Helvetica,sans-serif;font-size:24px;color:{MUTED};">
        {slide['num']}/{total}
      </div>
      <div style="font-family:Arial,Helvetica,sans-serif;font-size:24px;color:{MUTED};">
        {esc(handle)}
      </div>
    </div>
    """

    return f"""<!doctype html>
<html><head><meta charset="utf-8"><style>
  html,body{{margin:0;padding:0;background:{BG};width:{WIDTH}px;height:{HEIGHT}px;overflow:hidden;}}
</style></head>
<body>
  <div style="width:{WIDTH}px;height:{HEIGHT}px;background:{BG};box-sizing:border-box;
              padding:90px;display:flex;flex-direction:column;justify-content:space-between;">
    <div>{pillar_tag}</div>
    <div style="display:flex;flex-direction:column;justify-content:center;flex:1;">
      {content}
    </div>
    {footer}
  </div>
</body></html>
"""


def html_to_png(chrome, html_path, png_path):
    subprocess.run(
        [
            chrome,
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--hide-scrollbars",
            f"--window-size={WIDTH},{HEIGHT}",
            f"--screenshot={png_path}",
            f"file://{html_path}",
        ],
        check=True,
        capture_output=True,
    )


def main():
    if len(sys.argv) != 2:
        print("Usage: generate_slides.py <path-to-draft.md>", file=sys.stderr)
        sys.exit(1)

    draft_path = sys.argv[1]
    with open(draft_path) as f:
        text = f.read()

    parsed = parse_draft(text)
    if not parsed["slides"]:
        print("No SLIDE blocks found — is this a valid carousel draft?", file=sys.stderr)
        sys.exit(1)

    stem = os.path.splitext(os.path.basename(draft_path))[0]
    out_dir = os.path.join(os.path.dirname(draft_path), "images", stem)
    os.makedirs(out_dir, exist_ok=True)

    chrome = find_chrome()
    total = len(parsed["slides"])

    with tempfile.TemporaryDirectory() as tmp:
        for slide in parsed["slides"]:
            html = render_slide_html(slide, total, parsed["pillar"], "@theaishortlist")
            html_path = os.path.join(tmp, f"slide-{slide['num']}.html")
            png_path = os.path.join(out_dir, f"slide-{slide['num']}.png")
            with open(html_path, "w") as f:
                f.write(html)
            html_to_png(chrome, html_path, png_path)
            print(f"  slide {slide['num']}/{total} -> {png_path}")

    print(f"Done: {total} slides written to {out_dir}/")


if __name__ == "__main__":
    main()
