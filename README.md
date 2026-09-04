# SHUMI Women's Empowerment — website wireframe

Prepared by **9ja LDA** for SHUMI. 4 September 2026.

**Start here:** open `index.html` by double-clicking it. Everything links together and
works offline — there are no external dependencies.

## For the client

| File | What it is |
|---|---|
| **`presentation-note.md`** | **Read this first.** Plain-language explanation of what you are looking at and why it is built this way. |
| `content-checklist.md` | The 53 things we need from SHUMI, by page and section, marked required or optional. |

## The screens

| File | Screen |
|---|---|
| `index.html` | Homepage, full length. Includes the 11 October event band and its post-event state. |
| `event.html` | The 11 October event page. |
| `stories.html` | A growing collection — populated, filterable, with its empty state. |
| `about.html` | About SHUMI, Meet the team, Our impact, Partners. |

The **contact form** is a dialog, opened from the `Contact` button in the header or the
footer, on any page.

**Mobile** is the real design, not a squeezed desktop. Narrow the window, or open it on a
phone. Screenshots of both are in `design/screenshots/`.

**The post-event state:** click the dark *"Wireframe preview"* box on the homepage to
switch the event band between its before and after states.

## The reasoning

| File | What it is |
|---|---|
| `design/direction.md` | The full design direction: navigation, colour with measured contrast ratios, type scale, section order, photography art direction. |
| `public/images/manifest.md` | Every placeholder image, the prompt behind it, and what replaces it. |
| `design/critique.md` | My own critique of what is built, and what I would fix with more time. |
| `design/screenshots/` | Desktop and mobile screenshots. |

## Build

Static HTML and CSS. Vanilla JavaScript only where an interaction needs it — the mobile
menu, the nav dropdowns, the contact dialog, the story filters. No framework, no build
step required to view.

```
assets/shumi.css     design tokens and all styling
assets/shumi.js      the four interactions
assets/fonts.css     self-hosted Figtree + Newsreader (no network needed)
build.py             regenerates the four HTML files from one shared header/footer
```

`build.py` exists so the header, footer and contact dialog cannot drift between pages.
Edit it and run `python3 build.py` rather than editing the HTML files by hand.

## Two things to know

1. **Every photograph is an AI-generated placeholder.** None are real women, none are
   SHUMI members, none can go live. Each is labelled on the page. See
   `public/images/manifest.md`.
2. **Nothing has been invented.** No statistics, testimonials, partner names, or attendee
   counts. Where a fact was missing it is a visible `[client to supply]` marker.
