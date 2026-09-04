# SHUMI GLOBAL — UI/UX design exploration

**Three design directions, compared, with a recommended hybrid.**
9ja LDA · 4 September 2026

---

## Read this first

This is **not the website**. It is the stage before it: research, three genuinely
different design directions, mid-fidelity wireframes for each, a scored comparison, and a
recommendation.

**Nothing here should be built until SHUMI picks a direction.** That is the approval gate
at the end of this document, and it is deliberate — the cost of changing direction now is
a conversation; after development starts it is weeks.

| File | What it is |
|---|---|
| `concepts/index.html` | **Start here.** All three concepts side by side, with the comparison. |
| `concepts/concept-01-editorial.html` | Concept 1 — Global Editorial. Desktop + mobile. |
| `concepts/concept-02-community.html` | Concept 2 — Human Community. Desktop + mobile. |
| `concepts/concept-03-movement.html` | Concept 3 — Global Movement. Desktop + mobile. |
| `brand/LOGO.md` | The logo record, and what is still needed. |

### Two limits on this work, stated plainly

1. **Firecrawl was not available in this session.** The reference site was analysed by
   direct fetch instead (it blocks standard crawlers and needs a browser user-agent).
   The analysis in Phase 2 is from its real HTML, not from memory.
2. **The logo arrived as a chat image, not a file.** Every colour derived from it is
   marked provisional. Send the artwork and the palettes are re-derived in an hour.

---

# PHASE 1 — Audit

## What exists

A complete high-fidelity wireframe for **SHUMI as a local organisation**, built earlier in
this project and living in the repository root: `index.html`, `event.html`,
`stories.html`, `about.html`, one stylesheet, one small JS file, 14 placeholder images, a
content checklist and a presentation note.

| | |
|---|---|
| Stack | Static HTML + CSS, vanilla JS. No framework, no build step. `build.py` assembles pages from one shared header/footer. |
| Fonts | Newsreader + Figtree, self-hosted, no network dependency |
| Colour | Deep rose `#A8325A`, ink `#1B141A`, blush `#FDF4F2` |
| Images | 14 AI placeholders, all labelled, all replaceable |
| Accessibility | Verified: zero contrast failures, correct heading order, labelled fields, 44px targets |
| Content | Nothing invented — missing facts are visible `[client to supply]` markers |

## Why it does not answer the new brief

The existing wireframe is **well built for a different organisation.** It was designed
around a specific, verified premise: Cape Verdean-American women in Brockton,
Massachusetts. The new brief describes a **United States-based organisation serving women
globally**. Those are not the same product and the difference is structural, not cosmetic.

| Existing build | What "global" requires |
|---|---|
| One city, named in the hero | No geographic limitation in the primary message |
| One diaspora community | Many nationalities, cultures and languages |
| Photography of one community | Photography that spans continents without tokenism |
| One event, one place | Events that could be anywhere, or online |
| IA of 5 groups, ~12 pages | IA of 9 sections that must scale to a platform |
| A community organisation | An organisation that can grow into a movement |

**This is worth saying directly:** the earlier direction is not wrong, it is *narrower*.
If SHUMI is genuinely a Cape Verdean-American organisation in Brockton, that build is
closer to right than anything in this document, and the specificity is a strength rather
than a limitation. If SHUMI is global, it needs replacing. **These two briefs contradict
each other and only SHUMI can say which is true.** That is the first question at the
approval gate.

## What carries forward regardless of direction

These were solved once and do not need re-solving:

- The **content discipline** — no invented statistics, testimonials, partner names or
  press logos; visible `[client to supply]` markers instead.
- The **accessibility method** — measuring contrast rather than eyeballing it, and
  auditing heading order, labels and targets programmatically.
- The **October 11 2026 event** treatment: persistent bar, above-fold placement, mobile
  sticky CTA, and a designed post-event state so 12 October does not look broken.
- The **self-hosted font** approach, so the deliverable works offline on a client machine.
- The **content checklist** structure.

## Technical limitations to note before development

- No CMS exists. Every concept below assumes one is chosen; the IA is designed to map onto
  a CMS content model rather than hand-built pages.
- No analytics, no mailing list account, no Eventbrite event, no logo source file.
- Static HTML is right for a wireframe and wrong for a platform. Concept 3 in particular
  implies a real framework and a real backend.

---

# PHASE 2 — Research

## Reference analysed: moderndaywife.com

Fetched directly (the site returns 403 to standard crawlers). Findings from its actual
markup, not from impression.

### Structure

- **Navigation: 4 items.** Who We Are · Events (with 4 children: Upcoming Events, WSS
  Dallas, WSS W Scottsdale, Soireé en Blanc) · Magazine · Contact. Genuinely restrained,
  and the events dropdown does the heavy lifting.
- **Homepage order:** all-caps hero statement → who we are → a four-figure statistics band
  → mission paragraph → five pillar blocks each with "Learn More" → scrolling adjective
  animation → testimonials → press-logo marquee → footer.
- **Event architecture is the spine of the site.** Individual named events are
  first-class destinations in the navigation, not rows on a listing page. This is the
  single best idea on the site.

### What is worth taking

| Pattern | Why |
|---|---|
| **Named events as navigation destinations** | An event with its own identity and URL converts far better than an entry in a list. SHUMI's 11 October event should be a destination, not a row. |
| **Event-first information architecture** | The whole site is organised around "when can I come", which is the correct priority for an organisation that runs gatherings. |
| **Named, attributed testimonials** | Real names against real quotes — the credibility mechanism is right even where the execution is not. |
| **Pillar blocks with a single consistent CTA** | Scannable, scalable, and each one can grow into a section later. |

### What must not be copied

| Pattern | Why not |
|---|---|
| **The statistics band** (8000+ attendees, 55K followers, 250K+ viewers, 10+ events) | SHUMI has no such figures. Inventing them is out of the question and a soft number is worse than none. |
| **The press-logo marquee** (New Beauty, Modern Luxury, Angeleno, US Weekly, The LA Tribune, The US Sun, Know Women, Issuu) | SHUMI has no press coverage yet. A row of logos SHUMI has not earned is a lie with a design system around it. |
| **The all-caps hero** | "DESIGNED FOR WOMEN, INSPIRED BY LIFE." set in caps is harder to read, and the brief explicitly rules out tracked-out all-caps. |
| **Four typefaces** | The site loads Montserrat, Darker Grotesque, Lato *and* Open Sans. That is not a type system, it is an accident. |
| **Broken heading order** | The document goes `h1 → h3 → h4 → h2`. A screen-reader user navigating by heading gets a scrambled outline. This is a real accessibility defect and a useful reminder that a site can look premium and still be badly built. |
| **The scrolling adjective animation** | "The modern day wife is Ambitious / Hard-working…" is decoration that costs motion budget and says nothing. |
| **Testimonials from men on a women's brand** | Their testimonial set includes male names. Whatever the reason, on SHUMI it would undercut the entire premise. |

### The strategic lesson

Modern Day Wife converts because **the event is the product and the site knows it.**
Everything else — magazine, podcast, social — is secondary architecture pointing back at
attendance. SHUMI should take that clarity. It should not take the credibility scaffolding
(numbers, press, adjectives) that Modern Day Wife has earned and SHUMI has not.

**None of the three concepts below should be recognisable as this site.**

---

# Shared foundations

These are constant across all three concepts. Only the expression differs.

## Information architecture

Nine sections. The point of nine rather than five is that SHUMI is being designed as a
**platform that grows**, and a section added later must not force a navigation redesign.

```
ABOUT              About SHUMI · Mission · Vision · Values · Meet the Team
WHAT WE DO         Programs · Initiatives · Education · Wellness · Empowerment · Community
EVENTS             Upcoming · Event detail · Ticketing · Past events
STORIES            SHUMI Stories · Community Stories · News · Articles · Testimonials
IMPACT             Our Impact · Statistics · Reports · Communities reached
GET INVOLVED       Volunteer · Partner · Sponsor · Organizations we support · Opportunities
RESOURCES          Resources · Guides · Educational content · Blog
GALLERY            Photos · Events · Community
CONTACT            Contact · Service inquiries · General inquiries
CONNECT            Instagram · Facebook · Newsletter   (footer + persistent, never nav)
```

**Nine sections cannot all be top-level navigation.** Each concept solves that
differently, and how it solves it is one of the real differences between them.

Growth slots designed in from the start: **Membership · Donations · Chapters · Regional
hubs · Speakers · Vendors · Directory · Mentorship · Grants.** Each maps to an existing
section rather than needing a new one.

## The colour problem, and its solution

Sampled visually from the logo (provisional until the artwork arrives):

**The logo pink `#E85D9E` measures 3.24:1 against white. It fails WCAG AA for text.**

This is the single most important technical fact in this document. It is not a reason to
change the logo — it is a reason to build a two-pink system, which every concept does:

| Role | Behaviour |
|---|---|
| **Brand pink** `#E85D9E` | The logo, large display type, non-text UI, and anything on a dark ground. Never body text or a small button on white. |
| **Working pink** (varies by concept) | Carries meaning: links, buttons, focus rings. Deepened along the same hue (H=332) until it passes AA both as text on white and as a fill under white text. |

A useful consequence: **on a dark ground the brand pink passes AA at 5.84:1.** Concept 3
is built on that, which is why its pink can be the real one rather than a substitute.

## Typography principle

The logo's wordmark is a **heavy high-contrast Didone serif**. The brief asks for soft,
sophisticated, readable and explicitly *not* decorative-feminine.

The rule across all three concepts: **the site never repeats the logo's voice.** The logo
stays the most dramatic piece of type anywhere, and the page around it is calmer. Each
concept picks a different counterpoint, which is a genuine difference between them, not a
palette swap.

Non-negotiable in every concept: **body text 18px minimum, line-height 1.6+, nothing below
16px anywhere.** SHUMI serves women across a wide age range and a wide range of technical
confidence. This is a floor, not a preference.

## Accessibility floor

Applies to all three; not a differentiator, a requirement.

WCAG 2.1 AA contrast on everything · visible focus in the brand palette · 44px touch
targets · keyboard operable throughout · nothing discoverable only on hover · semantic
landmarks and ordered headings · descriptive alt text · labelled fields with error
messages that say what to fix · `prefers-reduced-motion` honoured · plain language.

---

# PHASE 3 — The three concepts

---

## CONCEPT 01 — GLOBAL EDITORIAL

### Design philosophy

**SHUMI as a publication with a point of view.** The organisation earns global authority
by looking like it already has it — the way a serious international title does. Editorial
design signals *intelligence and permanence*, which is exactly what a young organisation
with global ambitions needs and cannot yet claim with numbers.

The bet: **credibility through craft rather than through statistics.** Modern Day Wife
buys credibility with a stat band. SHUMI cannot. But a site that is composed, confident
and beautifully typeset reads as serious without asserting anything untrue.

### Visual personality

Assured. Cultured. Unhurried. Slightly severe. A woman who has read the article, not
skimmed the infographic. Cool rather than warm; respect rather than affection.

### Homepage wireframe

```
┌──────────────────────────────────────────────────────────────────────────┐
│ EVENT BAR   11 October 2026 · Women's Empowerment Event   [Get your ticket]│
├──────────────────────────────────────────────────────────────────────────┤
│ SHUMI ⬦        About   What We Do   Events   Stories   Impact      ☰ More │  Thin rule. Wordmark left, 5 items, "More" opens the full IA.
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   Women everywhere.          ┌────────────────────────────────────────┐  │  Asymmetric split. Type owns the left third; a single
│   One community.             │                                        │  │  full-bleed editorial portrait owns the right two-thirds
│   ───────────────            │    FULL-BLEED EDITORIAL PORTRAIT       │  │  and runs off the edge of the page.
│                              │    single subject, strong daylight     │  │
│   SHUMI connects women       │    deep shadow, direct gaze            │  │  One primary CTA. The secondary is a quiet underline.
│   across countries and       │                                        │  │
│   generations.               │                                        │  │  No scrim, no text over the photo — the photo is
│                              │                                        │  │  allowed to be a photograph.
│   [ Get your ticket ]        │                                        │  │
│   What SHUMI does            │                                        │  │
│                              └────────────────────────────────────────┘  │
├──────────────────────────────────────────────────────────────────────────┤
│  MANIFESTO — one sentence, 48px, centred, enormous whitespace            │  A statement, not a slogan. The page's thesis.
│  "A woman's horizon should not be decided by where she was born."        │  Written by SHUMI, in SHUMI's voice, attributed to SHUMI.
├──────────────────────────────────────────────────────────────────────────┤
│  WHO SHUMI IS — two columns, editorial measure, drop-cap opening         │  Reads like a leader column. Long-form is a signal
│                                                                          │  of seriousness, not a usability failure, if it is set well.
├──────────────────────────────────────────────────────────────────────────┤
│  WHERE WE WORK — a quiet index, not a map                                │  Countries as a typeset list, treated as a colophon.
│  Ghana · Brazil · India · Portugal · Kenya · United States · …           │  Honest at 6 countries and at 60. No dots on a globe.
├──────────────────────────────────────────────────────────────────────────┤
│  WHAT WE DO — 3 editorial features, unequal weight                       │  Deliberately NOT a grid of identical cards. First
│  ┌──────────────┐ ┌──────┐ ┌──────┐                                      │  feature is double-width. Hierarchy through size.
│  │  lead story  │ │ two  │ │three │                                      │
│  └──────────────┘ └──────┘ └──────┘                                      │
├──────────────────────────────────────────────────────────────────────────┤
│  THE 11 OCTOBER EVENT — full-bleed dark band, campaign treatment         │  Treated as a magazine cover story: a poster, not a card.
│  Large date, title, one line, [ Get your ticket ]                        │  Its own visual language inside the page.
├──────────────────────────────────────────────────────────────────────────┤
│  SHUMI STORIES — 4 items, first at double width, portrait crops          │  Faces at scale. Editorial crop, generous captions.
├──────────────────────────────────────────────────────────────────────────┤
│  IMPACT — set as a typeset statement, not a stat band                    │  Numbers when they exist; prose when they do not.
│  [client to supply]                                                      │  Degrades honestly — this is the point.
├──────────────────────────────────────────────────────────────────────────┤
│  PARTNERS — a restrained typeset list, no logo wall                      │  Names, not logos, until there are enough logos to earn a wall.
├──────────────────────────────────────────────────────────────────────────┤
│  PULL QUOTE — full-bleed, 64px, one attributed voice                     │  A real woman, named, with permission. Never fabricated.
├──────────────────────────────────────────────────────────────────────────┤
│  NEWSLETTER — a single rule, a single field, no box                      │  Understated on purpose.
├──────────────────────────────────────────────────────────────────────────┤
│  FOOTER — full IA in four typeset columns on ink                         │
└──────────────────────────────────────────────────────────────────────────┘
```

### Navigation concept

**Five visible items plus a "More" panel.** About · What We Do · Events · Stories ·
Impact stay in the bar. "More" opens a full-width editorial panel — a typeset index of the
entire IA, set like a magazine contents page, with Get Involved, Resources, Gallery and
Contact given equal weight. Not a mega-menu of link soup: a designed page of its own.

**Why this and not a mega-menu:** a mega-menu is a confession that you have too many pages
and no hierarchy. A contents page is a statement that the hierarchy is deliberate.

### Hero strategy

Asymmetric split, type against a single full-bleed portrait. **"Women everywhere. One
community."** — two short sentences, one idea, no verb-noun slogan.

The photograph does the emotional work; the type does the explaining. Critically, **no
text sits on the image** — this both preserves the photograph and removes an entire class
of contrast problem.

### Typography

| | |
|---|---|
| Display | A restrained modern serif with low stroke contrast, used at 56–96px. Deliberately the *opposite* of the logo's Didone drama — a calm relative, not a rival. |
| Text | A humanist sans with a tall x-height for all reading and UI. |
| Signature move | Very large display sizes against very generous leading in body copy. The size gap is the hierarchy. |
| Body | 18px / 1.65, measure capped at 68 characters. |

### Colour

| Token | Value | Share |
|---|---|---|
| Paper | `#FFFFFF` | ~62% |
| Ink | `#0E0E10` | ~26% |
| Working pink | `#C61065` — 5.73:1 on white, 5.73:1 under white text | ~5% |
| Brand pink | `#E85D9E` — display type and dark grounds only (5.96:1 on ink) | ~4% |
| Warm grey | `#6B6B70` — 5.30:1, captions and metadata | ~3% |

Highest ink share of the three concepts. Pink is a punctuation mark, never a mood.

### Photography strategy

**Editorial portraiture.** Single subjects, strong directional daylight, deep shadow, rich
saturated colour, medium-format sharpness. Subjects are composed and often looking
directly into the lens with authority — not caught candidly. Generous negative space
designed into the frame for type.

Global range is carried by **individual women photographed with equal seriousness**, not
by crowd shots. The argument: photographing one Ghanaian woman with the same care a
magazine gives a cover subject says more about respect than a group photo of six
nationalities.

**Risk to manage:** editorial portraiture can read as cold or as fashion. Every frame must
show a real person in a real context, never a model.

### CTA strategy

One primary per screen, always `Get your ticket` while the event is live. Secondary
actions are underlined text links, never a second button. Buttons are rectangular with a
1px rule — restrained, editorial, not a rounded pill.

### Event presentation

**Campaign treatment.** A full-bleed dark band with the date set enormous, functioning as
a magazine cover story inside the homepage. The event gets its own visual identity — a
poster that lives in the page — rather than being a card in a list. Its own page continues
that identity.

### Mobile strategy

The asymmetric split collapses to: photograph full-bleed, then type below. Display sizes
step down hard (96px → 34px) but the *size relationships* hold, which is what preserves
the editorial feel. Nav collapses to a full-screen typeset index. Event bar persists.
Sticky ticket bar on the event page.

### Motion philosophy

**Minimal and slow.** Images fade in over 600ms on first view only. No parallax, no
counters, no scroll-jacking. The restraint *is* the sophistication signal. One exception:
the "More" panel opens with a deliberate 300ms reveal, because it is a destination.

### How it communicates global sisterhood

Through **equal editorial treatment.** Every woman photographed gets the same care,
lighting and scale, whether she is in Accra or Lisbon. The "Where we work" index lists
countries as a plain typeset colophon — no flags, no map pins, no first-world-centre. The
implicit statement: these women are equally serious subjects, and SHUMI is the publication
that treats them so.

### Strengths

- Highest perceived premium and international credibility of the three
- **Degrades honestly** — works beautifully with no statistics, no press, no partners
- Most differentiated from every other women's nonprofit site
- Long content lifespan; ages slowly
- Cheapest to keep looking good as SHUMI grows

### Weaknesses

- **Coldest of the three.** "Impressive" is not "I belong here."
- Depends almost entirely on photographic quality; mediocre photography destroys it
- Long-form copy demands writing SHUMI may not have capacity to produce
- Editorial restraint can read as corporate or distant to a less confident visitor
- The least immediately warm to a woman arriving from Instagram

### Best use case

If SHUMI's near-term priority is **legitimacy with partners, sponsors, press and
institutions** — the audience that decides whether SHUMI is taken seriously — this is the
strongest direction.

---

## CONCEPT 02 — HUMAN COMMUNITY

### Design philosophy

**SHUMI as a room you are welcome in.** The first job is not to impress; it is to make a
woman — any woman, any age, any level of technical confidence — feel she is in the right
place within seconds. Every decision optimises for *belonging* over *admiration*.

The bet: **warmth converts.** A woman arriving from a Facebook post does not need SHUMI to
look like Vogue. She needs to recognise herself and find the one thing she came for.

### Visual personality

Warm. Generous. Unpretentious. Calm. Soft without being sweet, and never childish. Like a
well-made community space: comfortable, but clearly cared for.

### Homepage wireframe

```
┌──────────────────────────────────────────────────────────────────────────┐
│ EVENT BAR   Sat 11 October 2026 · Everyone welcome   [Get your ticket]   │  Warm ground, not black. Reads as an invitation.
├──────────────────────────────────────────────────────────────────────────┤
│ SHUMI ⬦   About  What We Do  Events  Stories  Get Involved  [Contact][🎟]│  6 plain-word items. No cleverness. Words, not icons.
├──────────────────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────────────────────┐    │
│  │  WIDE WARM PHOTOGRAPH — women of many nationalities together     │    │  Photo first, at the very top, spanning the width.
│  │  soft daylight, mid-conversation, genuinely unposed              │    │  A woman sees people before she reads a word.
│  └──────────────────────────────────────────────────────────────────┘    │
│                                                                          │
│     Where women meet, and stay.                                          │  Plain-language hero BELOW the image. Sentence case.
│     SHUMI is a community for women, in the United States and around      │  No slogan, no abstraction.
│     the world. Come to an event, find people, get support.               │
│     [ Get your ticket ]   See what happens at SHUMI                      │
├──────────────────────────────────────────────────────────────────────────┤
│  THREE PLAIN PROMISES — no icons, no cards, generous space               │  What she actually gets. Concrete verbs.
│  Meet women near you · Learn something useful · Get real support         │
├──────────────────────────────────────────────────────────────────────────┤
│  THE 11 OCTOBER EVENT — warm invitation panel, photo + facts             │  An invitation, not a campaign. Reads like a letter.
│  Date · Time · Where · What it costs · [ Get your ticket ]               │  Facts before persuasion. "You can come on your own."
├──────────────────────────────────────────────────────────────────────────┤
│  WHAT WE DO — 6 soft blocks, generous padding, plain names               │  Six because the IA has six. Named after real things.
├──────────────────────────────────────────────────────────────────────────┤
│  A WOMAN'S STORY — one story, large, at length, one portrait             │  ONE story told properly beats six cards. The single
│  Quote pulled large, her name, her country                               │  most persuasive element on the page.
├──────────────────────────────────────────────────────────────────────────┤
│  WOMEN AROUND THE WORLD — soft photo mosaic, uneven sizes                │  Faces, many countries, no captions needed.
├──────────────────────────────────────────────────────────────────────────┤
│  IMPACT — plain sentences, numbers only where real                       │  "Women in 14 countries" reads warmer than a stat tile.
├──────────────────────────────────────────────────────────────────────────┤
│  GET INVOLVED — 3 warm blocks with plain-word CTAs                       │  Volunteer · Partner · [Donate slot reserved]
├──────────────────────────────────────────────────────────────────────────┤
│  PARTNERS — quiet row, names or logos                                    │
├──────────────────────────────────────────────────────────────────────────┤
│  NEWSLETTER — warm panel, one field, reassurance line                    │  "One email a month. Nothing else." Anxiety removal.
├──────────────────────────────────────────────────────────────────────────┤
│  FOOTER — warm dark, full IA, large tap targets                          │
└──────────────────────────────────────────────────────────────────────────┘
```

### Navigation concept

**Six plain-word items, no dropdowns on mobile hover, nothing hidden.** About · What We Do
· Events · Stories · Get Involved, plus Contact and a ticket button. Impact folds into
About; Resources and Gallery fold into Stories; Connect is footer-only.

Desktop dropdowns open on **click, never hover.** Mobile is a full-screen panel with a
button that says the word **"Menu"** and rows 56px tall with visible +/− toggles.

**Why fewer items than Concept 1's "More" panel:** this concept's user is the least
confident of the three. A contents-page overlay is elegant and would lose her. Six words
she understands beats nine categories she has to parse.

### Hero strategy

**Photograph first, at the top, full width.** Type below it, in sentence case, in plain
language. `Where women meet, and stay.` — then two sentences explaining exactly what SHUMI
is and what to do next.

This inverts Concept 1 deliberately: the emotional recognition happens before any reading
is required, which is the right order for a visitor arriving cold from social media.

### Typography

| | |
|---|---|
| Display | A soft humanist serif at moderate sizes (32–52px). Warm, low contrast, gentle terminals. |
| Text | The same warm humanist sans as the display's partner, used generously. |
| Signature move | **Larger body text than anyone else uses.** 19px body, 1.7 line-height. |
| Body | 19px / 1.7, measure 62 characters. Nothing below 16px. |

The smallest type on this site is larger than the *body* type on most sites. That is the
concept's clearest single decision.

### Colour

| Token | Value | Share |
|---|---|---|
| Warm paper | `#FBF8F5` | ~55% |
| Blush | `#FBEFEA` | ~18% |
| Warm ink | `#241C20` — 15.73:1 on paper | ~15% |
| Working pink | `#AE2967` — 5.99:1 on paper, 6.34:1 under white text | ~6% |
| Warm grey | `#5C5057` — 7.24:1 | ~4% |
| Brand pink | `#E85D9E` — decorative only, never carries meaning | ~2% |

No pure white anywhere. The whole surface is warmed a few degrees, which is most of why
the concept feels different from the other two.

### Photography strategy

**Warm documentary.** Groups and pairs rather than single portraits. Soft diffused
daylight, warm neutral grade, gentle grain, shallow depth of field. Subjects are
mid-conversation, mid-laugh, mid-listening — caught, never posed, rarely looking at the
lens.

Global range is carried by **who is in the room together**: many nationalities in one
frame, several generations in one frame. The argument is the opposite of Concept 1's —
here, proximity between different women *is* the message.

**Risk to manage:** warm documentary photography of diverse groups is exactly where
tokenism lives. The defence is specificity — real contexts, real clothes, real rooms, and
prompts that name actual nationalities rather than "diverse women."

### CTA strategy

Buttons are soft-cornered, generously padded, and say what happens in plain words:
`Get your ticket`, `Join the mailing list`, `Send a message`. Never `Learn more`, never
`Discover`. Minimum 48px tall — above the 44px floor, because this concept's audience
skews older.

### Event presentation

**A warm invitation.** Photograph, then the facts in a plain list — date, time, place,
cost — then the reassurances that actually decide attendance: *you can come on your own,
you can bring your mother, here is where to park, here is what to do if you cannot afford
a ticket.*

This is the most conversion-effective event treatment of the three, because it removes
reasons not to come rather than adding reasons to want to.

### Mobile strategy

**The strongest mobile concept, and mobile is the design here rather than an adaptation.**
Single column throughout. Primary action always within thumb reach. Sticky ticket bar on
the event page. Forms that do not fight a mobile keyboard. Nothing depends on hover.
Everything is one tap from the top.

### Motion philosophy

**Almost none, and gentle where present.** Soft 400ms fades on scroll-in. No parallax, no
counters, no transforms. Motion here is a risk, not an asset — for a less confident user
it can make a page feel unstable. `prefers-reduced-motion` removes what little there is.

### How it communicates global sisterhood

Through **who is in the frame together.** Many nationalities and several generations in
one photograph, repeatedly, without ever captioning it. The site never says "we are
diverse"; it shows women who plainly are, being ordinary together. Language is kept plain
enough to survive translation and to be read by a woman whose English is her third
language.

### Strengths

- **Highest conversion likelihood**, especially from Instagram and Facebook
- **Best accessibility outcome** — large type and plain language are load-bearing
- Widest age range served; a 70-year-old is not an afterthought
- Most forgiving of imperfect photography and imperfect copy
- Fastest and cheapest to build; least that can break

### Weaknesses

- **Lowest premium ceiling.** Risks reading as a local nonprofit, which is the exact
  outcome the brief warns against
- Least differentiated — closest to the category default
- **Weakest at "global"**; warmth is universal but does not by itself say *international*
- Least impressive to a corporate sponsor or institutional partner
- Hardest to scale into a platform without a redesign

### Best use case

If SHUMI's near-term priority is **filling the 11 October event and growing a real
membership of women who come back** — actual humans rather than institutions — this
converts best.

---

## CONCEPT 03 — GLOBAL MOVEMENT

### Design philosophy

**SHUMI as infrastructure for a movement.** Not a site describing an organisation, but the
front door of a platform where women in different countries find each other, find
programmes, and find their way in. Designed for what SHUMI intends to become rather than
what it is today.

The bet: **ambition attracts.** Design the platform first and the organisation grows into
it. The risk is the mirror image: an empty platform looks emptier than an honest small site.

### Visual personality

Confident. Contemporary. Kinetic. Slightly serious. Dark-first, which is unusual in this
category and instantly separates SHUMI from every pastel women's nonprofit. Purposeful,
not corporate; a movement's infrastructure, not a SaaS dashboard.

### Homepage wireframe

```
┌──────────────────────────────────────────────────────────────────────────┐
│ ANNOUNCEMENT   11 Oct 2026 · Women's Empowerment Event  [Get your ticket] │  Pink on near-black. Brand pink is AA-legal here (5.84:1).
├──────────────────────────────────────────────────────────────────────────┤
│ SHUMI ⬦    About  What We Do  Events  Stories  Impact  Get Involved  [🎟]│  Dark persistent bar. 6 items + platform CTA.
├──────────────────────────────────────────────────────────────────────────┤
│ ████████████  DARK HERO — full-bleed wide photograph, dark grade  ███████ │
│                                                                          │
│    Women everywhere.                                                     │  Type ON the image, but only huge display type
│    One movement.                                                         │  at AA-safe contrast over a controlled dark area.
│                                                                          │
│    SHUMI connects women across 14 countries [client to supply]           │
│    [ Get your ticket ]   [ Find SHUMI near you ]                         │  TWO primary actions — the platform promise.
├──────────────────────────────────────────────────────────────────────────┤
│  WHERE SHUMI IS — interactive presence, NOT a spinning globe             │  Progressive: a plain country list that becomes an
│  ┌─────────────────────────────────────────────────────┐                 │  interactive map where supported. Filterable by region.
│  │  region filter · country list · counts per country  │                 │  Honest at 3 countries; still works at 60.
│  └─────────────────────────────────────────────────────┘                 │  Keyboard-navigable. Never map-only.
├──────────────────────────────────────────────────────────────────────────┤
│  IMPACT — animated counters, [client to supply] until real               │  The one place motion carries meaning. Counters
│  ██ women reached   ██ countries   ██ programs   ██ events               │  animate once, on first view, and respect reduced-motion.
├──────────────────────────────────────────────────────────────────────────┤
│  PROGRAMS — interactive filtered grid, scales 6 → 60                     │  The platform's core object. Filter by theme + region.
├──────────────────────────────────────────────────────────────────────────┤
│  THE 11 OCTOBER EVENT — full-bleed dark, countdown, speakers rail        │  Dynamic event experience. Countdown, speaker cards
│  [ Get your ticket ]                                                     │  when supplied, capacity signal, add-to-calendar.
├──────────────────────────────────────────────────────────────────────────┤
│  STORIES FROM WOMEN — horizontal rail, country-tagged                    │  Each story tagged with its country. Geography as metadata.
├──────────────────────────────────────────────────────────────────────────┤
│  WAYS IN — 4 participation paths, platform-styled                        │  Volunteer · Partner · Sponsor · [Membership reserved]
├──────────────────────────────────────────────────────────────────────────┤
│  PARTNERS — logo grid, filterable                                        │
├──────────────────────────────────────────────────────────────────────────┤
│  GLOBAL CTA — full-bleed, single statement, one action                   │
├──────────────────────────────────────────────────────────────────────────┤
│  FOOTER — dark, full IA, region switcher slot reserved                   │  Language/region switcher designed in, not built.
└──────────────────────────────────────────────────────────────────────────┘
```

### Navigation concept

**Six items in a persistent dark bar, plus a platform CTA.** Dropdowns are structured
panels with grouped children and short descriptions — closer to a product's navigation
than a brochure's. A **region switcher slot** sits in the footer, designed in from the
start so internationalisation later is a content problem, not a redesign.

### Hero strategy

Full-bleed dark photograph with **type over the image** — the only concept that does this.
It is permitted here because the grade is controlled and the type is huge; contrast is
verified against the actual darkened region rather than assumed.

**Two primary CTAs**, which no other concept allows: `Get your ticket` and `Find SHUMI
near you`. That second button is the entire platform thesis in one control.

### Typography

| | |
|---|---|
| Display | A tight contemporary grotesque, near-black weight, negative tracking, 64–110px. The only concept whose display face is a sans. |
| Text | The same family at text weights — one superfamily, many weights. |
| Signature move | Extreme weight contrast within one family: 900 against 400. |
| Body | 18px / 1.6. UI labels 16px minimum. |

Using one superfamily is a platform decision: it scales to dozens of UI states without the
type system fracturing.

### Colour

| Token | Value | Share |
|---|---|---|
| Near-black ground | `#121016` | ~48% |
| Paper (light sections) | `#FFFFFF` | ~30% |
| Brand pink | `#E85D9E` — **5.84:1 on the dark ground, AA-legal as text here** | ~8% |
| Soft pink | `#F49CC4` — 9.36:1 on dark, for emphasis | ~4% |
| Muted lilac-grey | `#A99FAE` — 7.43:1 on dark, metadata | ~6% |
| Working pink | `#B81E66` — 6.15:1, for the light sections only | ~4% |

**This is the only concept where SHUMI's actual brand pink does real work rather than
standing in as decoration.** That is a strong argument in its favour and worth weighing.

### Photography strategy

**Documentary photojournalism.** Wide gathering shots with real motion blur, women at work
in real environments across many countries, speakers mid-gesture, hands on actual tools.
Slightly cool contemporary grade, fine grain, available light only.

Global range is carried by **context**: a Vietnamese engineer on a rooftop, a Kenyan
organiser mid-sentence, students arguing over a laptop. Nationality is shown through what
women are *doing and where*, not through a line-up of faces.

**Risk to manage:** photojournalism of women in developing countries slides into
white-saviour imagery with almost no effort. The rule is strict — **women as agents, never
as recipients.** No one is being helped in any frame. Everyone is working, leading,
arguing, building.

### CTA strategy

Two-tier: solid pink primaries for conversion, outlined secondaries for exploration.
Buttons carry state (hover, active, loading, disabled) because a platform needs them.
Persistent ticket CTA in the bar at all times.

### Event presentation

**A dynamic event experience.** Countdown to 11 October, speaker rail as speakers are
confirmed, capacity or "tickets remaining" signal if Eventbrite exposes it,
add-to-calendar, and a designed post-event transformation into recap plus next event.

Highest ceiling of the three — and the most that must be supplied to avoid looking empty.

### Mobile strategy

Dark UI is genuinely better on a phone in low light, which is when a lot of Instagram
traffic arrives. Persistent bottom ticket bar. The presence section becomes a searchable
list rather than a map. Filters become a bottom sheet. Counters animate once.

**Watch item:** dark backgrounds with light text can cause halation for some readers with
astigmatism. Body text is 18px at a slightly reduced weight to mitigate it, and a light
mode is a genuine consideration rather than an afterthought.

### Motion philosophy

**The most motion of the three, all of it meaningful.** Impact counters animate once on
first view. The presence visual responds to interaction. Story rails scroll horizontally
with momentum. Filters transition. Hero image has a very slight scale-on-load.

No parallax, no scroll-jacking, no auto-advancing carousels, nothing that repeats on every
scroll. `prefers-reduced-motion` disables all of it, and every animated number is present
in the DOM as static text first.

### How it communicates global sisterhood

**Most explicitly of the three, and most at risk.** Geography is structural: countries are
metadata on stories, filters on programmes, a section of their own. A woman in Nairobi can
find what SHUMI does in Nairobi. That is a functional promise of belonging rather than an
aesthetic one.

The danger is that explicit global signalling with thin content reads as posturing. This
concept is the most honest of the three when SHUMI genuinely operates in many countries,
and the least honest when it does not.

### Strengths

- Highest ceiling; the only concept that can become a genuine platform
- **The only one where the real brand pink works as a functional colour**
- Most differentiated visually — dark-first is rare in this category
- Best at expressing global reach structurally, not decoratively
- Strongest for institutional partners and international sponsors
- Best long-term scalability

### Weaknesses

- **Requires the most content, and looks worst when empty.** An impact counter reading
  zero is more damaging than no counter
- Most expensive and slowest to build; implies a real framework and backend
- Dark UI plus heavy display type can read as cold or masculine to some of the audience
- Highest accessibility risk of the three — dark mode, motion, maps, filters each add
  surface area
- Weakest immediate warmth
- Assumes an international footprint SHUMI may not yet have

### Best use case

If SHUMI genuinely operates in multiple countries now, and intends to build a platform
connecting them, this is the only direction that will not need replacing in two years.

---

# PHASE 4 — Wireframes

Mid-fidelity, desktop and mobile, one HTML page per concept. They carry real type and real
colour because that is how three directions are actually told apart — but image slots are
marked blocks with a few real photographic samples showing the intended language, not
finished art direction.

Open `concepts/index.html` to see all three side by side.

---

# PHASE 5 — Comparison

Scored 1–10. These are my judgements, and the interesting part is not the totals — it is
how close they are.

| Category | C1 Editorial | C2 Community | C3 Movement |
|---|:--:|:--:|:--:|
| Premium feel | **10** | 6 | 8 |
| Global identity | 7 | 5 | **10** |
| Warmth | 4 | **10** | 5 |
| Accessibility | 8 | **10** | 6 |
| Storytelling | **9** | 8 | 7 |
| Event conversion | 6 | **9** | 8 |
| Mobile UX | 7 | **10** | 8 |
| Scalability | 7 | 6 | **10** |
| Brand differentiation | **9** | 5 | 8 |
| Emotional impact | 7 | **9** | 7 |
| Long-term potential | 8 | 6 | **10** |
| **Unweighted total** | **82** | **84** | **87** |

## Why the total is the wrong way to read this

Three points apart across eleven categories is noise. A flat total silently assumes every
category matters equally to SHUMI, and they do not. Weighted against what SHUMI actually
needs next, the answer changes completely:

**If the priority is filling the 11 October event** — weight event conversion, mobile UX,
warmth and accessibility:

| | C1 | C2 | C3 |
|---|:--:|:--:|:--:|
| Weighted | 25 | **38** | 27 |

**If the priority is credibility with sponsors, partners and press:**

| | C1 | C2 | C3 |
|---|:--:|:--:|:--:|
| Weighted | **35** | 22 | 30 |

**If the priority is building a genuine global platform:**

| | C1 | C2 | C3 |
|---|:--:|:--:|:--:|
| Weighted | 29 | 22 | **38** |

**Each concept wins decisively under one priority and loses under the others.** That is
the actual finding of this exercise, and it means the choice is a *strategy* decision for
SHUMI, not a taste decision for a designer.

## Honest notes on the scoring

- **C2's accessibility 10 and C3's 6** is the widest justified gap here. C3 adds dark UI,
  motion, maps and filters — four extra ways to fail — while C2's large type and plain
  language are load-bearing rather than decorative.
- **C1's warmth 4** is not a flaw in execution; it is the concept. Editorial design buys
  authority by holding the reader at a slight distance.
- **C3's global identity 10** is conditional. It scores 10 *if SHUMI genuinely operates in
  multiple countries.* If it does not, the same design scores about 3, because the
  structure openly advertises a footprint that is not there.
- **C2's differentiation 5** is the most uncomfortable score. It is the safest direction
  and the one most likely to look like every other women's organisation — which is the
  specific outcome the brief warns against.

---

# PHASE 6 — SHUMI HYBRID (recommended)

## The organising idea

A blend of three concepts is usually mush. This one is held together by a single rule that
resolves every conflict between them:

> **Warm and light where the site is about people. Dark and editorial where it is about
> scale.**

That is not a compromise; it is a system. Warmth for the human sections — hero, stories,
programmes, get involved. Dark, typographically confident treatment reserved for the two
moments that need to say *this is bigger than one room*: **the 11 October event** and
**global presence**. The contrast between the two modes does the work that neither the
all-warm nor the all-dark concept could do alone.

## What comes from where

| From | What | Why |
|---|---|---|
| **C2 Community** | The default surface: warm paper, generous 19px body, plain language, plain-word navigation, mobile-first structure, the invitation-style event facts | The audience arrives on a phone from social media and spans a wide age range. This is not negotiable and it is the base layer. |
| **C1 Editorial** | Typographic hierarchy and size contrast; asymmetric layouts instead of card grids; long-form "who we are"; the one-story-told-properly pattern; honest degradation with no statistics | Lifts C2 out of the category default without costing warmth. Type does the premium work, so photography does not have to carry it alone. |
| **C3 Movement** | Country as structural metadata on stories and programmes; the presence section; the dark full-bleed event band; growth slots for membership, chapters and regions; the region-switcher slot | Makes "global" a fact of the architecture rather than a claim in the copy — the single hardest requirement in the brief. |

## What is deliberately left behind

- **C1's coldness and its long-copy dependency.** The hybrid's default voice is plain and
  warm; editorial discipline shows up in *layout and type*, not in requiring essays.
- **C2's flat card grids and its lack of visual ambition.** Sections are deliberately
  unequal in weight.
- **C3's dark-everywhere UI, animated counters and interactive map.** Dark is rationed to
  two bands. Counters and maps are held back until SHUMI has real numbers and a real
  footprint — the components are designed, not built.

## Hybrid homepage architecture

```
1   Event bar — warm ground, persistent, ticket CTA           C2 tone, always visible
2   Header — 6 plain-word items + Contact + ticket            C2 clarity
3   Hero — wide warm photo, type below, sentence case         C2 structure, C1 type scale
4   Manifesto — one large typeset sentence                    C1 restraint
5   ★ THE 11 OCTOBER EVENT — dark full-bleed band             C3 treatment, C2 content
      photo · date · facts · reassurances · Get your ticket
6   What we do — 6 blocks, unequal weight, real names         C1 hierarchy, C2 language
7   One woman's story — told at length, one portrait          C2 emotion, C1 layout
8   ★ WHERE SHUMI IS — dark band, country list                C3 structure, honest at 3
9   Stories — 4 items, country-tagged, first double-width     C1 grid, C3 metadata
10  Impact — typeset sentences, [client to supply]            C1 honest degradation
11  Get involved — 3 blocks + reserved growth slot            C2 warmth
12  Partners — quiet row, names until logos are earned        C1 restraint
13  Newsletter — warm panel, one field, reassurance           C2
14  Footer — warm dark, full IA, region slot reserved         C3 scaffolding
```

Two dark bands (5 and 8), everything else warm and light. The rhythm is the design.

## Hybrid design system

**Colour** — logo-derived, provisional until the artwork arrives.

| Token | Value | Contrast | Role |
|---|---|---|---|
| `--paper` | `#FBF8F5` | — | Default ground |
| `--blush` | `#FBEFEA` | — | Alternate ground |
| `--ink` | `#241C20` | 15.73:1 on paper | All body text |
| `--ink-soft` | `#5C5057` | 7.24:1 on paper | Secondary text |
| `--pink` | `#AE2967` | 5.99:1 on paper · 6.34:1 under white | **The working pink** |
| `--brand-pink` | `#E85D9E` | 3.24:1 on white ✗ · 5.84:1 on dark ✓ | Logo, dark bands, display only |
| `--dark` | `#121016` | — | The two dark bands |
| `--pink-on-dark` | `#F49CC4` | 9.36:1 on dark | Accent inside dark bands |

**Type** — soft humanist serif for display (32–72px), warm humanist sans for everything
else. Body 19px / 1.7. Nothing below 16px.

**Spacing** — 4px base: 4 · 8 · 12 · 16 · 24 · 32 · 48 · 64 · 96 · 128.

**Grid** — 12 columns desktop (max 1240px), 8 tablet, 4 mobile. 20px gutters.

**Components to build first** — button (3 variants × 5 states) · nav + mobile panel ·
event band (light + dark) · story card · programme block · statement/manifesto ·
newsletter · contact dialog · footer · image slot with placeholder badge.

**Components designed but not built** — impact counters · presence map · programme
filters · speaker rail · countdown · region switcher · membership · donations.

---

# PHASE 7 — APPROVAL GATE

**Stopping here. No production code until SHUMI chooses a direction.**

## 1. Which concept should SHUMI choose?

**The SHUMI Hybrid**, built on Concept 2's foundation.

If SHUMI would rather not have a hybrid and wants one of the three as-is, then it depends
entirely on the priority — and by the weighting above: event first → **Concept 2**;
credibility first → **Concept 1**; platform first → **Concept 3**.

## 2. Why?

Because the two facts that matter most both point the same way. **Most visitors arrive on
a phone from Instagram or Facebook**, and **the audience spans a very wide age and
technical range** — which makes Concept 2's warmth, large type and plain language the
correct base layer, not a stylistic preference.

But Concept 2 alone would land SHUMI exactly where the brief says not to go: looking like
a small local nonprofit. So the base is lifted by C1's typographic ambition and C3's
structural globalism — **without taking on C3's content debt**, which is the real trap.
C3 is the most impressive concept and the one most likely to look embarrassing in
February, because an empty platform advertises its own emptiness.

The hybrid also fits **where SHUMI actually is**: warm and credible now, with the
architecture for the movement already in place and switched off.

## 3. What to borrow from the others

Already specified above: C1's type hierarchy, asymmetry, and honest degradation; C3's
country-as-metadata, dark event band, and reserved growth slots.

## 4. What to avoid

- Any invented statistic, testimonial, partner name, press logo or attendee count
- A stat band or logo wall before there is something true to put in it
- Dark UI beyond the two designated bands
- An interactive world map before SHUMI is in enough countries to fill one
- All-caps tracked-out labels; four typefaces; broken heading order
- Identical rounded cards with the same grey shadow for every content type
- Claiming a global footprint the organisation does not have

## 5. Final homepage architecture

The 14-section order above.

## 6. Mobile experience

Single column. Persistent event bar. Header carries logo, `Menu` as a word, and the ticket
button. Full-screen menu panel with 56px rows and visible +/− toggles; no hover anywhere.
Sticky ticket bar on the event page. 19px body, 48px touch targets. Images sized per
breakpoint. The dark bands stay dark on mobile — they are the moments of contrast.

## 7. Design system

As specified in Phase 6.

## 8. What to build first

1. Design tokens + the ten core components
2. Homepage
3. **The 11 October event page — this is the commercial priority and it is five weeks out**
4. Contact dialog + newsletter
5. Stories index and detail
6. About / Team
7. Get Involved
8. Everything else

## 9. What SHUMI still has to supply

### 🔴 Blocking, and blocking now

| # | What | Why it blocks |
|---|---|---|
| 1 | **Is SHUMI global, or is it a Cape Verdean-American organisation in Brockton?** | The earlier brief said one thing and this one says another. Every decision in this document rests on the answer. **Nothing should be built until this is settled.** |
| 2 | **The logo artwork** — `.ai`, `.svg` or `.eps` | Every colour here is estimated from a screenshot |
| 3 | **Which countries does SHUMI operate in today?** | Decides whether the presence section is honest or is a claim |
| 4 | **Eventbrite link, venue, address, time, ticket price** | The event page cannot ship |

### Required before launch

Mission, vision and values as written copy · the real names of SHUMI's programmes ·
team names, roles, bios and headshots with permission · at least three real stories ·
partner names with their written consent · any true impact figures · Instagram and
Facebook links · the contact form recipient · mailing list account.

### Decisions needed from SHUMI

- Hybrid, or one of the three concepts unmodified?
- Is SHUMI a registered non-profit? (decides whether Donate is near-term)
- Does the site need languages other than English?
- Is membership planned within 12 months? (decides how much of C3's scaffolding to build)

---

## One last thing, said plainly

The strongest version of this website is not the most beautiful one. It is the one that
tells the truth about what SHUMI is **right now** while leaving the door open to what it
becomes.

Concept 3 is the most exciting document in this folder and it is the one I would advise
against building today. Not because it is wrong — because it is early. Build the hybrid,
fill it with real content, run the October event, gather real photographs and real
numbers, and Concept 3 becomes available in eighteen months as an evolution rather than a
rebuild.
