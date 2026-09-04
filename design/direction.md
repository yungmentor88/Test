# SHUMI — Design direction

Prepared by 9ja LDA for Melanie Semedo and Gabriella Spinola.
Status: **direction for approval.** No page has been built from this yet.

---

## 0. Project facts this direction assumes

These were blank in the brief. I have filled them with the most likely answer so the
work could proceed, and marked each one. **Anything marked `[ASSUMED]` needs a yes or
no from Melanie before build.**

| Fact | Value used | Status |
|---|---|---|
| Organisation | SHUMI Women's Empowerment | given |
| Built by | 9ja LDA | given |
| City | Brockton, Massachusetts, serving Greater Boston, New Bedford and Providence | `[ASSUMED]` — Brockton holds the largest Cape Verdean community in the US, so it is the safe default, but the event venue city decides this |
| Who the women are | Cape Verdean diaspora women in the US, spanning grandmothers born on the islands who speak Kriolu at home through to US-born daughters and granddaughters | given |
| Age range | 18–75+, designed for the older end | `[ASSUMED]` |
| Language | English throughout, with Kriolu used in three fixed places only (see §4.5) | `[ASSUMED]` |
| Existing photography | None | `[ASSUMED]` — every image in the build is an AI placeholder |
| Logo file | Not supplied | **blocking** — see §3.1 |
| Build stack | Not decided | does not affect this wireframe |
| Eventbrite URL | Not created | **blocking the event page** — button is built as a marked placeholder |
| Instagram / Facebook | Not supplied | needed for launch |
| Contact form recipient | Not supplied | needed for launch |
| Client review date | Not supplied | — |

---

## 1. Read of the brief

SHUMI's site is for Cape Verdean-American women who will arrive on a phone, from an
Instagram or Facebook post, knowing nothing about SHUMI, and who will decide in about
eight seconds whether this is for them. A large share of them are over fifty and are not
going to hunt. So the site has exactly two jobs, in order: sell tickets to the 11 October
event, and make a stranger understand what SHUMI is and how to join in. Everything
else — impact, partners, resources, blog — is real but secondary, and is structure being
laid now for a hub that does not fully exist yet.

The site fails if it looks like a generic women's-empowerment template: the woman it is
for has seen a hundred of those and none of them were for her. It fails if the pink
becomes a wall. It fails if a 65-year-old on an iPhone has to pinch to read the event
date. And it fails commercially if the Eventbrite button is more than one tap from
wherever she lands.

### Genuinely missing — I need answers, not guesses

1. **The logo file.** I cannot sample the real pink. Everything in §3 is built around a
   pink I chose for accessibility; when the file arrives I re-derive the palette from it.
2. **The event venue, time and address.** The event page cannot ship without them.
3. **The Eventbrite URL.** Currently a marked placeholder.
4. **Whether Kriolu appears at all.** This is a real identity decision and it is not mine
   to make — see §4.5.
5. **Who the team is.** Names, roles, headshots. The team page is structure only.
6. **Ticket price and whether there are tiers** (early bird, vendor, sponsor).
7. **Is SHUMI a 501(c)(3)?** It changes the footer, and it decides whether "Donate"
   is a near-term nav item or not.
8. **Anything true about the past.** Prior events, numbers of women served, real quotes.
   If none exists yet, say so — I will design the honest version rather than invent one.

---

## 2. Navigation

Twelve items becomes **five**, plus one ticket button and one contact button.

### The grouping logic

Everything a visitor could want falls into one of five questions: *who are you*,
*what do you do*, *when can I come*, *what have you been up to*, *how do I join in*.
The twelve requested items are answers to those five questions, so those five are the nav.

```
HEADER
├── Event bar (persistent, above the header, until 11 Oct)
│     "Women's Empowerment Event · Sat 11 October 2026 · Brockton"  [Get tickets ↗]
│
├── SHUMI logo → home
│
├── About                    — who we are
│     ├── Our story
│     ├── Meet the team
│     ├── Our impact
│     └── Partners & organizations we support
│
├── What we do               — the programs; standalone page today
│     └── (room for one child per program as they launch)
│
├── Events                   — when can I come
│     ├── Upcoming events
│     └── Past events & recaps
│
├── Stories                  — what have you been up to
│     ├── SHUMI stories & news
│     ├── Resources & blog
│     └── Photo gallery
│
├── Get involved             — how do I join in
│     ├── Volunteer
│     ├── Partner with SHUMI
│     └── (reserved slots: Donate · Membership · Vendors · Sponsors · Speakers)
│
├── [Contact]                — outlined button, opens the contact dialog
└── [Get tickets ↗]          — solid button, opens Eventbrite in a new tab

FOOTER
├── Column 1 — SHUMI          Our story · Meet the team · Our impact · What we do
├── Column 2 — Take part      Upcoming events · Volunteer · Partner with SHUMI · Contact
├── Column 3 — Read           SHUMI stories & news · Resources & blog · Photo gallery
├── Column 4 — Mailing list   one email field, one button, one line of reassurance
└── Base line — Instagram · Facebook · email · © · Accessibility · Privacy
```

**One line per decision:**

- **About** absorbs Meet the Team, Our Impact and Partners because all three are a
  stranger asking "are you real and who is behind you".
- **What we do** stays top-level and childless on purpose: it is the answer to the second
  question a stranger asks, and it is the shelf that future programs hang off.
- **Events** is top-level because it is the site's commercial job; Past events sits under
  it so 12 October has somewhere to put the recap.
- **Stories** groups the three growing content collections, which behave identically
  (cards, filters, pagination) and should therefore live together.
- **Get involved** is the whole conversion funnel in one place, and it is where Donate,
  Membership, Vendors, Sponsors and Speakers land later **without touching the nav bar** —
  that is the scalability requirement, answered.
- **Contact** is a button, not a nav item, because the client asked for a pop-up; a link
  that opens a dialog rather than a page should not sit in a list of pages.
- **Mailing list** is not navigation. It is a footer block and a homepage section.

### Mobile menu behaviour

- Header is 64px, sticky, and holds only: logo, `Contact`, `Get tickets`, and a **`Menu`
  button that says the word "Menu"** — not a bare hamburger. Older users tap words.
- Tapping `Menu` opens a full-screen panel, not a drawer, with a large `Close` button
  top-right. Full-screen removes all ambiguity about whether the menu is open.
- The five sections are **accordions, closed on open.** No hover, no flyout, nothing
  that requires a mouse. Each row is 56px tall with a visible + / − state.
- A parent row is tappable in two places, clearly separated: the label goes to the
  section page, the +/− opens the children. This is the one interaction I would test
  with a real user before build.
- `Get tickets` is pinned inside the panel footer as well, so it is thumb-reachable
  whether the menu is open or closed.
- Escape closes; focus is trapped while open; focus returns to `Menu` on close.

---

## 3. Colour

Six values. Every ratio below is computed, not estimated.

| Token | Hex | Role | Share of page |
|---|---|---|---|
| `--paper` | `#FFFFFF` | Primary background | ~60% |
| `--ink` | `#1B141A` | All body text, footer background | ~20% |
| `--blush` | `#FDF4F2` | Alternate section background | ~12% |
| `--rose` | `#A8325A` | **The working pink.** Links, buttons, focus | ~5% |
| `--rose-light` | `#F2C7D2` | **Decorative only.** The swoosh, footer accents | ~2% |
| `--ink-soft` | `#574A52` | Secondary text, captions, metadata | ~1% |

Support values: `--line #E6DCDC` (decorative hairlines), `--field-border #8C7E86`
(form controls — needs 3:1, hairlines do not), `--error #B3261E`.

### Which pink is safe, stated explicitly

**`--rose #A8325A` is the only pink allowed to carry meaning.** It is unusual and it is
why I chose it: at 6.42:1 it passes AA *both* as dark-on-white text **and** as a button
fill under white text. One pink does both jobs, so the site never needs a second
"button pink" that drifts from the first.

```
#1B141A on #FFFFFF   18.08:1   body text                     AA + AAA
#1B141A on #FDF4F2   16.70:1   body text on blush            AA + AAA
#574A52 on #FFFFFF    8.38:1   secondary text                AA + AAA
#A8325A on #FFFFFF    6.42:1   links, rose text              AA + AAA
#A8325A on #FDF4F2    5.93:1   links on blush                AA + AAA
#FFFFFF on #A8325A    6.42:1   white on the primary button   AA + AAA
#FFFFFF on #1B141A   18.08:1   footer text                   AA + AAA
#F2C7D2 on #1B141A   11.95:1   footer accent text            AA + AAA
#8C7E86 on #FFFFFF    3.86:1   input borders (3:1 needed)    AA non-text
#B3261E on #FFFFFF    6.54:1   error messages                AA + AAA
```

**The one rule that will otherwise get broken:** `--rose` on `--ink` is **2.81:1 and
fails.** The dark footer and any dark photo overlay must use `--rose-light #F2C7D2`
(11.95:1) for accent text, never `--rose`. This is the mistake every build makes and it
is in the stylesheet as a comment.

**`--rose-light` never carries information.** It is the swoosh, a hairline, a hover wash.
If removing it would lose the user anything, it is the wrong colour for that job.

### Keeping the pink from becoming a wall

The client's fear is loudness. The defence is arithmetic: pink is capped at roughly 7% of
any screen, and **there are no pink section backgrounds.** `--blush` is a pink so pale it
reads as warm white, and it alternates with pure white to give the page rhythm. Saturated
rose appears only where a finger goes. No pink gradients, ever — the brief forbids them
and they are also where "not overly bright" goes to die.

---

## 4. Typography

### 4.1 The families

| | Family | Fallback stack | Role |
|---|---|---|---|
| Display | **Newsreader** | `Georgia, 'Times New Roman', serif` | h1, h2, pull quotes. Nothing else. |
| Text | **Figtree** | `-apple-system, 'Segoe UI', Roboto, sans-serif` | Everything else: h3 down, body, UI, buttons, forms |

Both are open-licence and free to self-host on the real build.

### 4.2 Resolving the tension with the logo

The logo is a **high-contrast dramatic serif** — thin hairlines, heavy stems, outlined,
drop-shadowed. The client wants **soft and approachable.** Those are opposites, and the
usual mistake is to split the difference and get mush.

The resolution: **stop repeating the logo's voice and let it be the only one of its kind.**

- **Newsreader is deliberately the logo's opposite within the same family of forms.** It
  is a serif, so the page still reads as elegant rather than corporate, but it is
  *low-contrast* with soft, slightly blunt terminals. Set beside the logo it reads as a
  gentler relative, not a bad copy. The logo stays the most dramatic thing on the page,
  which is what a logo is for.
- **Newsreader is capped at h1 and h2 only.** The serif never appears at paragraph size,
  so it never has to do the work it is bad at.
- **Figtree does all the reading and all the tapping.** Tall x-height, open apertures,
  wide-set — the qualities that read as friendly and, not coincidentally, as legible.
- The logo's **outline and drop shadow appear nowhere else.** Not on buttons, not on
  cards, not on type. That treatment is the logo's signature and repeating it cheapens it.

### 4.3 The scale

Mobile first. Desktop values follow the arrow. Nothing on this site is smaller than 16px.

| Role | Mobile | Desktop | Family / weight | Tracking |
|---|---|---|---|---|
| Display (h1) | 34px / 1.15 | 60px / 1.08 | Newsreader 400 | −0.015em |
| Section (h2) | 26px / 1.2 | 38px / 1.15 | Newsreader 400 | −0.01em |
| Card title (h3) | 20px / 1.3 | 22px / 1.3 | Figtree 600 | 0 |
| Sub (h4) | 18px / 1.35 | 18px / 1.35 | Figtree 600 | 0 |
| Lead paragraph | 20px / 1.6 | 21px / 1.6 | Figtree 400 | 0 |
| **Body** | **18px / 1.65** | **18px / 1.65** | Figtree 400 | 0 |
| Meta / caption | 16px / 1.5 | 16px / 1.5 | Figtree 500 | 0 |
| Button label | 17px / 1 | 17px / 1 | Figtree 600 | +0.01em |

Measure is capped at **68 characters** on desktop. Headings never exceed 20 words.

### 4.4 The 65-year-old on a phone

**Body is 18px with 1.65 line-height, and it does not shrink on desktop.** Reasoning,
since the brief asked for it:

- 16px is the browser default — a floor, not a design decision. By the mid-sixties most
  people have lost most of their near-focus accommodation, and 18px is the smallest size
  that stays comfortable at arm's length on a phone held slightly further away than a
  younger reader holds it.
- 1.65 line-height matters more than size for this reader. The failure mode at fifty-plus
  is not "cannot see the letters", it is **losing your place on the return sweep.**
  Generous leading fixes that; tight leading defeats a large type size.
- Body does not shrink on desktop because the desktop user is often the *same* woman on a
  laptop, and 16px desktop body is a habit rather than a reason.
- Nothing anywhere is lighter than weight 400, and no body text ever sits on a photo.

### 4.5 Kriolu — a decision for Melanie

`[ASSUMED]` My recommendation is **yes, but in exactly three places**, so it reads as
identity rather than decoration: the homepage welcome (**"Bem-vindu"** above the English
headline), the mailing-list heading, and the footer sign-off. English carries every piece
of functional copy — every button, label, form field and error — without exception, so
a granddaughter who does not read Kriolu never loses her way.

If Melanie says no, the three slots take English and nothing else changes.
If Melanie says more, we should talk about full bilingual properly rather than sprinkling.

---

## 5. Homepage — section order

```
┌────────────────────────────────────────────────────────────────────────┐
│ EVENT BAR   Sat 11 Oct 2026 · Brockton        [ Get tickets ↗ ]        │  Ticket sale before anything else. Visible with zero scroll.
├────────────────────────────────────────────────────────────────────────┤
│ HEADER      SHUMI    About  What we do  Events  Stories  Get involved  │  Sticky. Five items. Contact + tickets pinned right.
│                                          [Contact]  [Get tickets ↗]    │
├────────────────────────────────────────────────────────────────────────┤
│                                                                        │
│   Bem-vindu                          ┌──────────────────────────┐      │  Photo is the material, not the garnish — a stranger
│   A place for Cape Verdean           │                          │      │  should recognise herself before she reads a word.
│   women to ___________               │   HERO PHOTOGRAPH        │      │
│           ‿‿‿‿‿ (the swoosh)         │   three generations,     │      │  One primary action. The secondary is a quiet text
│                                      │   one table              │      │  link, so the eye is never asked to choose twice.
│   Two plain sentences saying         │                          │      │
│   who SHUMI is.                      └──────────────────────────┘      │
│   [ Get tickets ↗ ]  See what SHUMI does                              │
│                                                                        │
├────────────────────────────────────────────────────────────────────────┤
│ THE 11 OCTOBER EVENT — full-width, blush ground                        │  The commercial job, given a whole band rather than a
│   Sat 11 Oct 2026 · 2–6pm · [venue TBC]                                │  card, because until 11 Oct it outranks everything.
│   What to expect · Who it's for · [ Get tickets ↗ ]  Full event details │  Swaps to the recap state on 12 Oct (§5.2).
├────────────────────────────────────────────────────────────────────────┤
│ WHAT SHUMI DOES — 4 plain cards, no icons-for-the-sake-of-it           │  The second question a stranger asks. Four so it
│   Connection · Resources · Opportunities · Education                   │  survives becoming six.
├────────────────────────────────────────────────────────────────────────┤
│ SHUMI STORIES — 3 portrait cards + "Read all stories"                  │  Proof by faces, not by numbers. Sits here because
│                                                                        │  the visitor now believes the offer and wants evidence.
├────────────────────────────────────────────────────────────────────────┤
│ OUR IMPACT — component built, values marked [client to supply]         │  Deliberately empty. Nothing invented. See §8.
├────────────────────────────────────────────────────────────────────────┤
│ GET INVOLVED — Volunteer · Partner with SHUMI · (Donate slot reserved) │  Conversion, after belief, before the ask to subscribe.
├────────────────────────────────────────────────────────────────────────┤
│ MAILING LIST — one field, one button, one reassurance line             │  The soft ask, for the visitor not ready to buy a ticket.
├────────────────────────────────────────────────────────────────────────┤
│ FOOTER — ink ground, 4 columns, social, accessibility, © SHUMI         │  rose-light accents only. --rose fails on ink.
└────────────────────────────────────────────────────────────────────────┘
```

### 5.1 Event page

```
┌────────────────────────────────────────────────────────────────────────┐
│ EVENT BAR + HEADER                                                     │
├────────────────────────────────────────────────────────────────────────┤
│ HERO — wide photograph, room title over it                             │  Sell the room she will walk into.
│   SHUMI Women's Empowerment Event                                      │
│   Saturday 11 October 2026                                             │
├────────────────────────────────────────────────────────────────────────┤
│ THE FACTS — date · time · venue · address · price, as a plain list     │  Above everything discursive. She is checking whether
│   [ Get tickets on Eventbrite ↗ ]   opens in a new tab, and says so    │  she can come, not reading an essay.
├────────────────────────────────────────────────────────────────────────┤
│ WHAT TO EXPECT — short blocks, each with a supporting image            │  Short scannable blocks, image beside text: the
├────────────────────────────────────────────────────────────────────────┤  accessibility requirement about mixed tech confidence.
│ WHO IT'S FOR — plain prose, names the actual community                 │
├────────────────────────────────────────────────────────────────────────┤
│ GETTING THERE — parking, transit, accessibility of the venue           │  The question that stops women coming, answered.
├────────────────────────────────────────────────────────────────────────┤
│ QUESTIONS — 4 or 5, open by default, not an accordion                  │  Hover-free, click-free. Nothing hidden.
├────────────────────────────────────────────────────────────────────────┤
│ STICKY BAR (mobile only) — date + [ Get tickets ↗ ]                    │  Thumb-reachable from any scroll position.
└────────────────────────────────────────────────────────────────────────┘
```

### 5.2 The 12 October state

The same band, same position, same height — **different content.** No layout shift, no
dead "this event has passed" notice.

```
┌────────────────────────────────────────────────────────────────────────┐
│ THAT WAS THE 11 OCTOBER EVENT                                          │
│   3 photographs from the day  ·  See all photos from the day           │
│   Next event: [client to supply]   ·  Join the mailing list to hear     │
│                                       about it first  [ Join ↗ ]       │
└────────────────────────────────────────────────────────────────────────┘
```

The event page itself keeps its URL, gains a "This event has happened" line at the top,
swaps the Eventbrite button for "See photos from the day", and becomes the recap. Nothing
is deleted, because the page is the record.

---

## 6. Photography direction

This is the Higgsfield brief. Every image on the site is a placeholder until SHUMI's own
event photography exists after 11 October.

**Subject.** Cape Verdean-American women in the Brockton / Greater Boston area. Cape
Verdean heritage is Afro-Portuguese creole and the range within a *single family* is
wide: deep brown through olive through fair, hair from tight coil to loose wave to
straight, features that read variously African, Portuguese and Brazilian. Any prompt that
does not force this range will collapse it into one narrow look, and the client will see
that immediately. Every prompt names the range explicitly.

**Generations together, in the same frame.** Not a "young" set and an "older" set. A
grandmother and a granddaughter at the same table is closer to what SHUMI is than either
alone, and it answers the age-range question without a word of copy. At least half the
set is mixed-age.

**Framing.** Close and mid. Two to four women, in real proximity — leaning in, a hand on
a forearm, one talking and two listening. Eye level, never above. Some backs of heads,
some partial faces, some out-of-focus foreground: the frame of someone who was in the
room, not someone documenting it.

**Light.** Available light only. Big soft window light, warm interior tungsten in the
evening scenes. Some shadow. No ring light, no flash, no rim light, nothing that looks
lit by a crew.

**Colour treatment.** Warm and slightly muted. Gentle film grain. Highlights held back
rather than blown. Skin rendered warm and true across every tone in frame — not lifted,
not orange, not ashy. Consistent across the entire set: same photographer, same day.

**Settings — this community's actual rooms.** A rented function hall with round tables
and folding chairs. A church basement with a low ceiling. Somebody's kitchen mid-cooking.
A community centre with a scuffed floor. A front porch in a triple-decker
neighbourhood. **Not** a Scandinavian co-working loft, not exposed brick, not a plant
wall, not a white cyclorama.

**Wardrobe and detail.** What women actually wear to a Saturday community event: a good
blouse, a church hat, jeans, a headwrap, a cardigan. Real coffee cups, paper plates,
handbags on the backs of chairs, a phone face-down on the table.

**Avoid, specifically:**
- Boardroom stock energy — arms crossed, blazers, a laptop nobody is using
- Forced laughter, especially the head-back openmouthed laugh at nothing
- Over-styled glamour, glossy retouching, uniform white teeth
- Anyone looking down the lens and smiling on cue
- Hands-in-a-circle, group-jump, or fists-raised empowerment clichés
- Everyone in the frame looking like they could be sisters — **regenerate if so**

**Style clause appended to every prompt, unchanged:**
> Documentary photograph, available natural light, warm slightly muted colour, fine film
> grain, shallow depth of field, eye-level, candid unposed moment, no studio lighting, no
> retouching, authentic community setting.

---

## 7. The one memorable thing

### The swoosh

The logo already contains something nobody else has: the **pink stroke that cuts across
the SHUMI wordmark.** It is being used once, on the logo, and then thrown away. It should
be the site's signature instead.

Lifted off the logo and drawn as a single hand-made ink stroke, it appears
**underneath one word, once per page** — the word the page turns on. *A place for Cape
Verdean women to **belong**.* Not a highlight, not a marker pen: one confident stroke, in
`--rose-light`, that looks drawn by a hand rather than a vector tool, with the slight
overshoot a real stroke has.

Why this and not something else:

- It is **already SHUMI's.** It comes off their own logo, so it cannot look like a trend
  borrowed from another site, which a floating shape or a wave divider always does.
- It carries the brief's actual meaning. SHUMI is about connection, and the swoosh is a
  line drawn *under and across* — the same gesture as an arm around a shoulder.
- It is **cheap to keep consistent** across a WordPress or Webflow build by a future
  editor, which a complex motif is not.

**The rule that makes it work: once per page. Never twice on one screen.** A signature
used everywhere is a pattern, and a pattern is wallpaper.

Everything else stays quiet, and that is the deal: no wave dividers, no floating blobs,
no gradient washes, no shapes behind headings, no decorative rules between sections.
Sections are separated by white space and by the blush/white alternation — nothing more.
The photography and the swoosh are the only two things on this site that are allowed to
be expressive.

---

## 8. Content that will not be invented

Recorded here so it is agreed before build, not argued after:

- **Our impact** ships as a working component with `[client to supply]` in every value
  slot, visibly marked. No numbers.
- **Testimonials** ship the same way. Any quote must be something a named woman actually
  said, short, and correctly attributed. SHUMI's own message is written in SHUMI's voice,
  not dressed up as a quote from a woman who does not exist.
- **No** partner logos, awards, press mentions, or attendee counts.
- Interface copy says what happens: *Get tickets*, *Join the mailing list*, *Send message*.
  Not *Empowering women to unlock their potential*.
- Sentence case throughout. No tracked-out all-caps eyebrow labels.

---

## 9. Self-review

I checked this against the trap the brief named — "would I have produced this for any
women's organisation?" — and changed three things.

1. **The background was cream and the accent was terracotta.** That is the default women's
   -organisation palette and the brief called it out by name. Worse, it was ignoring the
   client's actual brand. Changed to white and `--blush`, with the accent taken from
   SHUMI's own pink and deepened only as far as accessibility required. The palette is now
   derived from their logo rather than from the category.

2. **Every heading was in a high-contrast serif.** That is the same instinct that produces
   the cream-and-terracotta site, and here it also fought the logo — two dramatic serifs
   arguing on one page. Changed to a low-contrast serif capped at h1/h2 with a humanist
   sans doing all the reading, which is both softer, as the client asked, and lets the
   logo stay the loudest serif on the page.

3. **The decorative element was going to be a soft organic blob behind the hero.** It
   could have gone on any site in this category. Replaced with the swoosh taken from
   SHUMI's own logo, which cannot.

**Correction made during build.** The section-order sketch above originally wrote internal
links as *"Full details →"* and *"All stories →"*. Appending an arrow to link text is on
the brief's own avoid list, and I had reached for it out of habit. Internal links are now
plain underlined text. The one arrow that survives is the small ↗ on external links
(Eventbrite, social), which is not decoration — it warns the reader she is leaving the
site, and is paired with real "opens in a new tab" text for screen readers.

Also checked and confirmed absent: identical rounded cards with the same grey shadow
(cards here are differentiated by content type — the event band, story cards and program
blocks are three different objects), 01/02/03 markers on anything that is not a sequence,
all-caps eyebrow labels, and pink gradients.

One thing I would flag as still generic: **"Connection · Resources · Opportunities ·
Education"** in the What we do section is the brief's own language and it is abstract.
Once Melanie tells us what SHUMI actually runs — a specific workshop, a specific
gathering — those four blocks should be named after real things.

---

## 10. What happens next

On approval this becomes the high-fidelity wireframe: homepage, event page, a populated
growing-collection page with its empty state, about/team, the contact dialog, and mobile
views — as clickable HTML, with placeholder photography generated to §6, a content
checklist, and a presentation note for the team.
