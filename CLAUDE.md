# SHUMI — project constitution

**Client:** SHUMI Women's Empowerment · **Studio:** 9ja LDA
Every prompt in this project inherits what follows. Do not re-derive it.

---

## §1 — PROJECT IDENTITY

### Who SHUMI is
A women's empowerment organisation in the United States serving women of the Cape
Verdean diaspora and the wider community. It runs events, programs and gatherings and is
growing into a hub: connection, resources, opportunities, education, support.

The feeling the site must carry: **women bonding, togetherness, healing, connection,
personal growth, sisterhood, collective empowerment.** Warm and welcoming, but clean,
modern, polished, premium.

### Who uses the site
Women across a wide age range with **very different levels of technology confidence**,
arriving mostly **from Instagram and Facebook, on a phone.** This single fact outranks
every aesthetic decision below it. **If a choice looks beautiful and confuses a
68-year-old on an iPhone SE, the choice is wrong.**

Non-negotiable consequences:
- Body text starts at **18px mobile, 19px desktop.** Not 16.
- Every tap target **≥ 44×44 CSS px**, with 8px clear space.
- Nav is **five items maximum** at top level. Everything else nests inside.
- Nothing important behind hover, scroll position, or a gesture.
- Every action says what it does. "Get tickets on Eventbrite", never "Learn more".

### The one date that matters
**Women's Empowerment Event — Sunday 11 October 2026.** Tickets via Eventbrite.
Reachable in **one tap from anywhere** until the date passes. Build the event module so
the next event drops into the same slot without a redesign.

### Voice
Direct, warm, unhurried. Short sentences. Second person. No corporate abstraction, no
hype, no therapy-speak. Write like a woman inviting another woman to something real.

---

## §2 — ANTI-GENERIC CONSTRAINTS

Hard bans, not preferences.

**Banned typefaces:** Inter, Poppins, Montserrat, Playfair Display, Space Grotesk, Lato,
Open Sans, Raleway.

**Banned visual moves:** purple→blue or pink→orange gradient heroes · glassmorphism ·
the same radius+shadow stamped on every block · everything centered · a 100vh hero ·
emoji as icons or bullets · off-the-shelf icon sets as the identity · `01/02/03` markers
on non-sequential content · stock-photo energy (high-fives, laptops in cafés, stacked
hands from above) · tri-word hero headlines · custom cursors, scroll-jacking,
preloaders, entry animations that delay reading · text baked into images · anything
reachable only by hovering.

**Banned copy:** "Welcome to our website." "We are passionate about…" Lorem ipsum
anywhere, at any stage. Write real SHUMI copy. Mark invented facts
`<!-- 9ja: confirm with client -->`.

**The ship test:** swap the logo and the pink for another organisation's — does anything
still say SHUMI? If not, it isn't finished.

---

## §3 — DESIGN SYSTEM

### Colour — brand pink is exactly `#E85CA3`

**The rule with teeth:** `#E85CA3` is an accent surface and a graphic mark. It is
**never a text colour below 24px**, and appears **no more than six times on any screen.**
Pink text and links use `--rose-deep`.

```css
:root {
  --bone:        #FBF8F6;  /* page ground */
  --shell:       #F3EBE8;  /* alternate section surface */
  --rose-mist:   #FAECF3;  /* pink wash, tint only */
  --ink:         #1A0F14;  /* headings, body */
  --ink-soft:    #4A3A42;  /* secondary body */
  --ink-muted:   #6E5A63;  /* captions — LIGHTEST allowed text */
  --rose:        #E85CA3;  /* THE brand pink. Fills, marks, one CTA. */
  --rose-deep:   #9E2A63;  /* pink TEXT and links */
  --rose-quiet:  #C98AAE;  /* dividers, decorative rules only */
  --ink-panel:   #1A0F14;
  --on-panel:    #FBF8F6;
  --rose-on-dark:#F0A8CE;
  --hairline:    #E3D8D3;
}
```

**Verified contrast (WCAG 2.1 — do not substitute values):**

| Pair | Ratio | Verdict |
|---|---|---|
| `--ink` on `--bone` | 17.69 | AAA |
| `--ink-soft` on `--bone` | 10.06 | AAA |
| `--ink-muted` on `--bone` | 6.01 | AA — floor for body text |
| `--rose-deep` on `--bone` | 6.70 | AA — links, eyebrows |
| **`--rose` on `--bone`** | **3.06** | **FAILS for text. Fills only.** |
| **`--ink` on `--rose`** | **5.78** | **Passes — pink button carries near-black text, never white** |
| `--rose-on-dark` on `--ink-panel` | 9.98 | AAA |
| `--ink` on `--shell` | 15.91 | AAA |

**The pink CTA button has black text.** That is a design decision, and it is also what
stops the pink shouting.

No literal hex in a component — every colour behind a variable.

### Typography

**Direction A — SANCTUARY:** Fraunces display (`font-variation-settings: 'SOFT' 100,
'WONK' 1`, weights 300–500, headlines at 400, never bold) + Karla body.
**Direction B — CIRCLE:** Bricolage Grotesque display (500–700) + Figtree body. No serif.

Both: fluid scale base 18/19px, ratio 1.2 mobile → 1.26 desktop.

```css
--step--1: clamp(0.94rem, 0.92rem + 0.1vw, 1rem);
--step-0:  clamp(1.125rem, 1.1rem + 0.15vw, 1.1875rem);
--step-1:  clamp(1.35rem, 1.28rem + 0.35vw, 1.5rem);
--step-2:  clamp(1.62rem, 1.5rem + 0.6vw, 1.9rem);
--step-3:  clamp(1.94rem, 1.74rem + 1vw, 2.4rem);
--step-4:  clamp(2.33rem, 2rem + 1.65vw, 3.02rem);
--step-5:  clamp(2.8rem, 2.28rem + 2.6vw, 3.8rem);
```

Line height 1.6 body, 1.12 display, 1.35 large intros. Measure capped **68ch**.
`text-wrap: balance` on headings, `pretty` on paragraphs. Eyebrows: body face, uppercase,
`letter-spacing: .14em`, `--step--1`, `--rose-deep`. `tabular-nums` on all figures.

### Space and structure
8px base: `4 8 12 16 24 32 48 64 96 128 160 224`.
Section rhythm `clamp(72px, 10vw, 160px)`. Container
`min(1240px, 100% - 2 * clamp(20px, 5vw, 64px))`.

**Radius as meaning:** photographs are **square-cornered**. Pills (999px) only on tags and
countdown chips. Cards get a hairline, not a shadow. **Shadow is reserved for exactly one
thing** — the floating mobile ticket bar — so it reads as elevated because nothing else is.

### Motion — *motion confirms, it never performs*

```css
--dur-micro: 160ms; --dur-state: 240ms; --dur-reveal: 480ms; --dur-hero: 900ms;
--ease-out-soft:   cubic-bezier(0.22, 1, 0.36, 1);
--ease-quiet:      cubic-bezier(0.65, 0, 0.35, 1);
--ease-gentle-pop: cubic-bezier(0.34, 1.36, 0.64, 1);
--stagger: 60ms;
```

**Physical limits:** no translate > **24px** · no scale > **1.03** · nothing overshoots
except buttons and chips · stagger maxes at 6 children · only `transform` and `opacity`
animate · parallax capped at 60px, rAF-driven, off below 1024px.

**The inventory — build these and no others:** 1 header condense · 2 hero line-mask
reveal · 3 hero image clip-path wipe + settle · 4 section entrance (below the fold only —
the first viewport renders at rest) · 5 link underline draw · 6 button fill wipes up ·
7 photo hover scale 1.03 + rule extends · 8 quote rotator crossfade with real controls ·
9 countdown, only the changed digit slides · 10 impact figures count up once ·
11 film grain 3% overlay on photo blocks — **do not skip this, it is what stops
photography looking rendered** · 12 focus ring `2px solid var(--ink)`, offset 3px, never
removed.

**Reduced motion is a first-class mode.** CSS override *plus* JS branching via
`matchMedia`: parallax off, rotator does not auto-advance, counters render final values,
marquee becomes a static grid, hero renders in final state.

---

## §4 — WHITE-LABEL DELIVERY

Concepts ship on **9ja LDA infrastructure under a 9ja LDA URL.** Nothing in the
deliverable references the tooling used to make it.

- No comments, strings, class names, attributes, IDs or filenames mentioning the toolchain
- No "Made with", no attribution block
- `<meta name="generator">` removed · `<html lang="en">` · author meta 9ja LDA
- `<meta name="robots" content="noindex, nofollow">` — these are private previews
- Favicon from the SHUMI shield mark, inlined as a data URI
- OG tags set so a WhatsApp or email preview shows SHUMI, not a blank card
- Placeholder notes read `<!-- 9ja: confirm with client -->`

### On the imagery
Photographs in the concepts are **AI-generated art direction** — they show the *kind* of
photography the design needs, at the right crop and tone. Two rules:
1. **They do not ship.** Real SHUMI photography replaces every one before launch.
2. **Never present them as photographs of SHUMI's community.** Call them "art direction"
   or "reference imagery".
