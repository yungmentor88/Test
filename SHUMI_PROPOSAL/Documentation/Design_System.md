# SHUMI — Design system

TedcanLabs · September 2026
Direction: **EDITORIAL × GLOBAL IMPACT**

> ⚠️ **Colour values are provisional.** The SHUMI logo reached this project as a chat
> image, not a source file, so the brand pink is read visually rather than sampled. Send
> the artwork (`.ai`, `.svg` or `.eps`) and the whole palette is re-derived from it in
> an hour. Every ratio below is computed, not estimated.

---

## 01. Colour

The brief asks for warm neutrals, off-white, deep charcoal, earth-inspired tones and a
restrained accent. SHUMI's own brand is pink, black and white. The system reconciles the
two by treating **wine as the earth-tone anchor** and **pink as punctuation**.

| Token | Hex | Role | Share |
|---|---|---|---|
| `--bone` | `#F2EDE6` | Primary ground. Warm off-white — never pure white. | ~58% |
| `--ink` | `#14100E` | All body text; the dark ground. | ~22% |
| `--wine` | `#4A1228` | The earth anchor. Section grounds, the event band. | ~10% |
| `--rose` | `#A8265C` | **The working pink.** Links, buttons, focus rings. | ~6% |
| `--stone` | `#6B6259` | Secondary text, captions, metadata. | ~3% |
| `--pink` | `#E85D9E` | **Brand pink — decorative and large-display only.** | ~1% |

### Measured contrast

```
#14100E on #F2EDE6   16.24:1   body text                    AA + AAA
#4A1228 on #F2EDE6   12.80:1   wine headings on bone        AA + AAA
#A8265C on #F2EDE6    5.82:1   links and buttons            AA + AAA
#6B6259 on #F2EDE6    5.13:1   captions and metadata        AA + AAA
#F2EDE6 on #14100E   16.24:1   reversed on ink              AA + AAA
#F2EDE6 on #4A1228   12.80:1   reversed on wine             AA + AAA
#F2EDE6 on #A8265C    5.82:1   white on the primary button  AA + AAA
#E85D9E on #14100E    5.85:1   brand pink on ink            AA  ✓
#E85D9E on #4A1228    4.61:1   brand pink on wine           AA  ✓
#E85D9E on #F2EDE6    2.78:1   brand pink on bone           FAILS ✗
```

### The rule that will otherwise get broken

**SHUMI's brand pink `#E85D9E` measures 2.78:1 on the bone ground and fails AA for
text.** It is not a text colour on light backgrounds. It is legal — and genuinely
beautiful — on the ink and wine grounds, where it reaches 5.85:1 and 4.61:1.

So the system runs two pinks:
- **`#E85D9E`** — the logo, large display type, and anything on a dark ground.
- **`#A8265C`** — everything that carries meaning on light: links, buttons, focus.

This is not a compromise on the brand. It is what makes the brand usable.

---

## 02. Typography

| Role | Face | Fallback |
|---|---|---|
| **Display** | **Bodoni Moda** — a true Didone. High contrast, hairline serifs, unmistakably editorial. | `Didot, 'Times New Roman', serif` |
| **Text & UI** | **Jost** — geometric sans with a deco quality. Clean, modern, unfussy. | `-apple-system, 'Segoe UI', sans-serif` |

### Why a Didone, when earlier advice said the opposite

Earlier in this project the recommendation was to *avoid* echoing the logo's dramatic
high-contrast serif, on the grounds that two dramatic serifs would compete.

**That advice was right for a warm community site and wrong for this one.** Under an
editorial direction the logo's Didone is an asset, not a liability: leaning into it makes
the mark and the site read as one designed thing rather than a logo sitting on top of a
website. Bodoni Moda is the logo's relative, at magazine scale.

The tradeoff is real and stated: Didones are for display only. Bodoni never appears below
28px, and Jost does all the reading.

### Scale

| Role | Mobile | Desktop | Face / weight | Tracking |
|---|---|---|---|---|
| Display | 44px / 1.02 | **112px / 0.94** | Bodoni Moda 400 | −0.03em |
| H1 | 34px / 1.08 | 68px / 1.02 | Bodoni Moda 400 | −0.02em |
| H2 | 27px / 1.15 | 44px / 1.08 | Bodoni Moda 400 | −0.015em |
| H3 | 21px / 1.3 | 24px / 1.3 | Jost 600 | 0 |
| Statistic | 48px / 1 | 96px / 0.95 | Bodoni Moda 400 | −0.02em |
| Lead | 20px / 1.6 | 22px / 1.55 | Jost 400 | 0 |
| **Body** | **18px / 1.65** | **18px / 1.65** | Jost 400 | 0 |
| Caption | 16px / 1.5 | 16px / 1.5 | Jost 400 | 0 |
| Eyebrow | 16px / 1 | 16px / 1 | Jost 500 | **+0.18em** |
| Button | 17px / 1 | 17px / 1 | Jost 500 | +0.02em |

**The signature move is scale contrast:** 112px display against a 16px tracked eyebrow.
That ratio — roughly 7:1 — is what separates editorial from corporate, and it costs
nothing to execute.

**Floors that do not move:** body 18px, nothing below 16px anywhere, measure capped at
68 characters. SHUMI serves women across a wide age range; this is a requirement, not a
preference.

**One honest caveat.** Jost is geometric and has a moderate x-height — it is a little
less forgiving at small sizes than a humanist sans would be. It earns its place on
character. If usability testing with older users pushes back, swap Jost for a humanist
face and keep everything else; the system does not depend on it.

---

## 03. Spacing and grid

4px base: `4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128 · 192`

| Breakpoint | Columns | Max width | Gutter |
|---|---|---|---|
| Mobile ≤ 767 | 4 | fluid | 20px |
| Tablet 768–1023 | 8 | fluid | 24px |
| Desktop ≥ 1024 | 12 | 1320px | 32px |

Sections breathe at `128px` desktop / `64px` mobile. Full-bleed bands ignore the grid
entirely — that break *is* the editorial rhythm.

---

## 04. Components

### Built first
Button (3 variants × 5 states) · Navigation + full-screen mobile panel · Editorial
statement band · Story card (country-tagged) · Programme block · Event band (light and
dark) · Newsletter · Contact dialog · Footer · Image slot with placeholder badge

### Designed, switched off until SHUMI has content
Impact counters · Presence map · Programme filters · Speaker rail · Countdown · Region
switcher · Membership · Donations

**Why the second list exists.** Each of these looks *worse empty than absent*. A counter
reading zero actively damages credibility. They are specified so they can be turned on
in an afternoon, not built to sit hollow.

### Rules that hold across every component

1. **No card grids of identical rectangles.** Content types are visually distinct
   objects: an event band is not a story card is not a programme block.
2. **No soft grey drop shadow under every box.** Separation comes from hairlines, ground
   changes and space.
3. **No rounded corners** except where a control genuinely needs them.
4. **The logo's outline-and-drop-shadow treatment stays on the logo.** It never appears
   on buttons, cards or type.
5. **External links are visually distinguishable** from internal navigation, with real
   "opens in a new tab" text for screen readers.

---

## 05. Motion

Motion serves story, discovery, hierarchy and connection. Nothing moves for decoration.

| Moment | Behaviour |
|---|---|
| Image reveal | Mask wipe up, 600ms, cubic-bezier(0.2, 0.6, 0.2, 1). Once, on first view. |
| Editorial statement | Line-by-line rise, 80ms stagger. Once. |
| Impact figures | Count up over 1200ms, on first view only — **and present as static text in the DOM before any script runs.** |
| Story rail | Horizontal momentum scroll, keyboard operable. |
| Page transition | 300ms cross-fade. |
| Hover | 150ms colour only — never scale, never lift. |

**Forbidden:** bounce, spin, fly-in, auto-advancing carousels, scroll-jacking, parallax
on text, anything that repeats on every scroll past.

`prefers-reduced-motion: reduce` disables all of it. Nothing is discoverable only through
motion, and no information exists only in an animation.

---

## 06. Photography

The most important element in the system, and the one most able to sink it.

**Direction:** documentary and editorial. Real women in real environments — working,
leading, teaching, building, thinking. Natural available light, deep shadow permitted,
warm sophisticated grade, fine grain, real skin texture.

**Global range is carried by authentic specificity** — a Kenyan organiser mid-sentence, a
Vietnamese engineer on a rooftop — never by landmarks, flags or a montage of skylines.

**The governing rule: women as agents, never as recipients.** Nobody in any frame is
being helped. This single rule rules out most NGO stock photography automatically.

**Never:** staged corporate shots, handshakes, volunteer group photos, white-background
portrait grids, hands-in-a-circle, raised fists, forced laughter, glamour retouching.

**Every image currently in these mockups is AI-generated and marked as such.** They
demonstrate the photographic language. They are not evidence of SHUMI's work and cannot
go live.

---

## 07. Accessibility

Not a checklist item — a design constraint that shaped the palette above.

WCAG 2.1 AA on every text and interactive element (measured, not estimated) · visible
focus in the brand palette on everything · 44px minimum touch targets with real spacing ·
fully keyboard operable · nothing discoverable only on hover · semantic landmarks and
ordered headings · descriptive alt text · labelled fields with errors that say what to
fix · `prefers-reduced-motion` honoured · plain language throughout.

**Contrast is verified against rendered pixels, not assumed from tokens.** Where type sits
over photography, the scrim is measured with the text hidden and the worst-case bright
region sampled — because a mean that passes can hide a highlight that fails.
