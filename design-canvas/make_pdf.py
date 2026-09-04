#!/usr/bin/env python3
"""Render the SHUMI artboards to a single vector PDF, one page per artboard."""
import pathlib, subprocess, sys
from playwright.sync_api import sync_playwright

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "SHUMI_Editorial_House.pdf"
TMP = pathlib.Path("/tmp/pdfpages"); TMP.mkdir(exist_ok=True)

COVER = """<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bodoni+Moda:opsz,wght@6..96,400&family=Jost:wght@300;400;500&display=swap">
<style>
  html,body{margin:0;padding:0}
  body{width:1440px;height:1000px;background:#F2EDE6;color:#14100E;
       font-family:'Jost',system-ui,sans-serif;position:relative;overflow:hidden}
  .lbl{font:500 12px/1 'Jost',sans-serif;letter-spacing:.22em;text-transform:uppercase}
  .dsp{font-family:'Bodoni Moda',Didot,serif;font-weight:400}
</style></head><body>
  <div style="position:absolute;left:0;top:0;width:14px;height:1000px;background:#4A1228"></div>
  <div style="padding:120px 110px 0 150px">
    <div class="lbl" style="color:#A8265C;margin-bottom:60px">Website concept &middot; September 2026</div>
    <div class="dsp" style="font-size:118px;line-height:.94;letter-spacing:-.03em;margin-bottom:34px">
      SHUMI<br><span style="font-style:italic;color:#4A1228">The Editorial House</span>
    </div>
    <div style="width:150px;height:2px;background:#A8265C;margin-bottom:40px"></div>
    <div style="font-size:20px;line-height:1.7;color:#6B6259;max-width:640px;margin-bottom:64px">
      An elegant, editorial, event-first concept. Homepage on desktop and mobile,
      a named gathering page, and the design system.
    </div>
    <div style="display:flex;gap:70px">
      <div>
        <div class="lbl" style="color:#A8265C;margin-bottom:12px">In this document</div>
        <div style="font-size:16px;line-height:2;color:#14100E">
          I&nbsp;&nbsp;&nbsp;Homepage &mdash; desktop<br>
          II&nbsp;&nbsp;Homepage &mdash; mobile<br>
          III&nbsp;The Autumn Assembly<br>
          IV&nbsp;&nbsp;Design system
        </div>
      </div>
      <div style="max-width:420px">
        <div class="lbl" style="color:#A8265C;margin-bottom:12px">Please note</div>
        <div style="font-size:15px;line-height:1.75;color:#6B6259">
          Every photograph is an AI-generated placeholder and cannot go live.
          Every fact SHUMI has not supplied appears as a visible
          <span style="color:#A8265C">[PLACEHOLDER]</span>, including the figures,
          which sit as XX by design &mdash; nothing has been invented.
        </div>
      </div>
    </div>
  </div>
  <div style="position:absolute;left:150px;bottom:70px" class="lbl">TedcanLabs</div>
</body></html>"""

PAGES = [("Main.dc.html", "Homepage — desktop"), ("Mobile.dc.html", "Homepage — mobile"),
         ("Event.dc.html", "The Autumn Assembly"), ("System.dc.html", "Design system")]

def render(pg, url, out, width):
    pg.goto(url)
    pg.wait_for_timeout(1200)
    pg.evaluate("() => document.fonts.ready")
    pg.wait_for_timeout(900)
    loaded = pg.evaluate("() => [document.fonts.check('16px \"Bodoni Moda\"'),"
                         "document.fonts.check('16px \"Jost\"')]")
    h = pg.evaluate("() => Math.ceil(document.documentElement.scrollHeight)")
    pg.pdf(path=str(out), width=f"{width}px", height=f"{h}px",
           print_background=True, margin={"top":"0","bottom":"0","left":"0","right":"0"})
    return loaded, h

cov = TMP / "cover.html"; cov.write_text(COVER, encoding="utf-8")
with sync_playwright() as p:
    b = p.chromium.launch(executable_path=CHROME)
    pg = b.new_page(viewport={"width": 1440, "height": 1000})
    fonts, _ = render(pg, cov.as_uri(), TMP/"00.pdf", 1440)
    print(f"cover        fonts bodoni={fonts[0]} jost={fonts[1]}")
    for i, (f, label) in enumerate(PAGES, start=1):
        w = 390 if "Mobile" in f else (1390 if "System" in f else 1440)
        pg.set_viewport_size({"width": w, "height": 1000})
        fonts, h = render(pg, (ROOT/f).as_uri(), TMP/f"{i:02d}.pdf", w)
        print(f"{label:22} {w}x{h}  bodoni={fonts[0]} jost={fonts[1]}")
    b.close()

import pymupdf
doc = pymupdf.open()
for f in sorted(TMP.glob("*.pdf")):
    doc.insert_pdf(pymupdf.open(f))
doc.set_metadata({"title": "SHUMI — The Editorial House",
                  "author": "TedcanLabs", "subject": "Website design concept"})
doc.save(str(OUT), garbage=4, deflate=True)
print(f"\nwrote {OUT.name}: {doc.page_count} pages, {OUT.stat().st_size//1024}K")
