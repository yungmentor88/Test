# SHUMI — The Editorial House

Design canvas: homepage (desktop + mobile), the Autumn Assembly gathering page,
and the design system plate.

**Live canvas:** https://claude.ai/code/artifact/0483cdd8-9848-4e1e-952f-8e9581ef6b93

## Direction

SHUMI as a publication rather than a nonprofit. The hero splits asymmetrically with
type left and the portrait bleeding off the right edge; the homepage carries a numbered
contents index; programmes are a typeset list rather than cards; grounds alternate
bone → ink → bone → wine for rhythm. No cards, no rounded corners, no drop shadows.

Modern Day Wife informed the **experience** — named events as destinations with their
own identity, women-first positioning, editorial storytelling, the newsletter as part of
the brand. None of its layout, typography or palette is used.

## The colour rule

SHUMI's logo pink `#E85D9E` measures **2.78:1 on bone and fails AA for text**. It is
legal on ink (5.85:1) and wine (4.61:1). So the system runs two pinks: `#A8265C` rose
carries meaning on light grounds, brand pink carries the brand on dark. This is on the
system artboard because it is the rule most likely to get broken later.

## Files

| File | What |
|---|---|
| `Main.dc.html` | Homepage, desktop 1440 |
| `Mobile.dc.html` | Homepage, mobile 390 |
| `Event.dc.html` | The Autumn Assembly |
| `System.dc.html` | Palette, type, controls |
| `canvas.json` | Frame positions and sizes |
| `*.jpg` | Four AI placeholder photographs |

The seeded canvas HTML is generated and git-ignored. Rebuild it with:

```bash
BASE=<design skill base dir>
node "$BASE/seed-canvas.mjs" --template "$BASE/payload.template.html" \
  --out shumi-editorial-house.html --title "SHUMI — The Editorial House" \
  --artboard Main.dc.html --artboard Mobile.dc.html \
  --artboard Event.dc.html --artboard System.dc.html \
  --image hero.jpg --image portrait-a.jpg --image portrait-b.jpg --image gathering.jpg \
  --canvas canvas.json
```

## Placeholders

Every photograph is AI-generated and cannot go live. Every fact SHUMI has not supplied
is a visible `[PLACEHOLDER]`, including the impact figures, which sit as `XX` by design.
