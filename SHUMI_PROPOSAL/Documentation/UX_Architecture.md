# SHUMI — UX architecture

TedcanLabs · September 2026

---

## 01. Information architecture

Nine sections. Nine because SHUMI is being designed as a platform that grows: a section
added in 2027 must not force a navigation redesign in 2027.

```
HOME

ABOUT ──────────── Our Story · Mission & Vision · Values · Team

PROGRAMS ───────── All Programs · Program Detail
                   filters: Region · Theme · Type · Status

STORIES ────────── Women · Communities · Impact
                   every story tagged: Region · Theme · Programme

GLOBAL ─────────── Regions · Communities · Global Impact

EVENTS ─────────── Upcoming · Event Detail · Past Events
                   architected to accept Eventbrite; not integrated today

RESOURCES ──────── Articles · Reports · Guides · Media

GET INVOLVED ───── Donate · Partner · Volunteer · Participate

CONTACT ────────── General · Service inquiries

CONNECT ────────── Instagram · Facebook · Newsletter
                   footer and persistent — never navigation
```

**Nine sections cannot all sit in a navigation bar.** Six are visible; Resources,
Gallery and Contact live in the footer and in an editorial index panel opened from the
header. Contact is a button that opens a dialog, not a page in a list of pages.

### Growth slots designed in from the start

Membership · Chapters · Regional hubs · Speakers · Vendors · Directory · Mentorship ·
Grants — each maps onto an existing section rather than needing a new one. **This is the
scalability requirement, answered structurally rather than promised.**

---

## 02. The homepage as a journey

Not twelve blocks. One argument, told in order, with each section handing off to the next.

| # | Section | What it does | Hands off by |
|---|---|---|---|
| 01 | **Hero** | One editorial statement over one image. Who, and why it matters. | Asking a question the next section answers |
| 02 | **Introduction** | Manifesto, not a paragraph. Who SHUMI is. | Naming the work |
| 03 | **Global impact** | The far end of the chain — figures, honestly empty until real | Immediately grounding a number in a person |
| 04 | **Women / Stories** | The near end — one woman, told properly | Showing what she took part in |
| 05 | **Programs** | Named, concrete things a woman can join | Showing where they run |
| 06 | **Global connection** | Where SHUMI is. Region list, honest at three countries | Showing when you can come |
| 07 | **Events** | The 11 October event, given a full band | Offering something to take away |
| 08 | **Resources** | Practical material | Offering a way in |
| 09 | **Partners** | Names until logos are earned | — |
| 10 | **Get involved** | Learn → Connect → Act | The soft ask |
| 11 | **Newsletter** | "Stay close to the movement" | — |
| 12 | **Footer** | Full IA, region switcher slot reserved | — |

**The transition rule:** consecutive sections never share a ground colour or a layout
shape. Bone gives way to wine; a full-bleed image gives way to a typographic band. The
rhythm is what stops twelve sections reading as twelve boxes.

### The impact → story mechanism

The single most important interaction on the homepage, and the clearest expression of
*The world through her*:

```
XX,XXX WOMEN REACHED          ← the far end of the chain
        │
        ▼  "one of them is [WOMAN'S NAME]"
HER PORTRAIT, HER WORDS       ← the near end
        │
        ▼
HER COMMUNITY  →  HER REGION  →  THE WORLD
```

A statistic that hands directly to a person is worth more than four statistics in tiles.
It also degrades gracefully: **with the number still a placeholder, the story alone
carries the section.**

---

## 03. Hero

The hero must communicate WOMEN · GLOBAL · IMPACT · MOVEMENT before any reading.

**Headline directions explored** (creative territory, not approved copy):

| Direction | Line | Note |
|---|---|---|
| Consequence | *When women move forward, the world moves with them.* | Strongest. Says impact without a statistic. |
| Lens | *The world through her.* | Most ownable; ties to the whole architecture. |
| Scale | *One woman. Then everything around her.* | Best sets up the impact → story mechanism. |
| Plain | *A global community for women.* | Safest, least memorable. Baseline to beat. |

**Recommended: the consequence line for the hero, with *The world through her* as the
organising idea beneath it.**

Structure: immersive visual · headline · one supporting sentence · primary CTA ·
secondary CTA · subtle motion. Composition briefed so **the left two thirds are negative
space** — the type never needs a scrim to be legible.

CTA pairing: **Explore SHUMI** (primary) · **Meet the women** (secondary).

---

## 04. Global experience

```
WORLD → REGION → COMMUNITY → PROGRAM → WOMAN → STORY
```

**Interaction:** select a region → reveal its communities → its programmes → its women →
open a story. The chain is navigable in both directions; a story links back up to its
region.

**Deliberately not a glowing animated globe.** A filterable typeset region index is the
default view; a map is progressive enhancement where supported, never the only way in.

**Why:** a list is honest at three countries and still works at sixty. A world map with
four pins advertises how few pins there are — the exact opposite of the intended effect.
It is also keyboard-navigable and screen-reader legible, which a map is not without
significant extra work.

---

## 05. Content systems

### Stories — the most important system

```
FULL-BLEED PORTRAIT
[WOMAN'S NAME]
[LOCATION] · [REGION]
Short introduction, 40–60 words
"[Her quotation — real, short, attributed, with permission]"
READ HER STORY
```

Editorial treatment: one story at full width beats six in a grid. Index pages lead with a
double-width feature and follow with a filtered set. Every story carries region, theme and
programme as metadata — which is what makes the global architecture real.

**Categories** (subject to SHUMI's approval — placeholders until then): Leadership ·
Opportunity · Community · Education · Entrepreneurship · Health · Culture · Innovation ·
Advocacy.

### Programs
`[PROGRAM NAME]` · Category · Region · Description · Impact · Image · CTA.
Filters: Region · Theme · Type · Status. Works at six and at sixty.

### Events
`Date · [EVENT NAME] · [LOCATION] · Description · Register`.
Named events are destinations with their own identity and URL — the one structural idea
worth taking from the reference. **Eventbrite is architected for, not claimed:** the
ticket action is a slot with a clean contract, so integration later is configuration
rather than a rebuild. A post-event state is designed so the section never looks stale.

### Get involved
Not six buttons. An emotional progression: **LEARN → CONNECT → ACT.**
Donate · Partner · Volunteer · Attend · Participate · Share, ordered by commitment, each
with a plain-words CTA that says what happens.

### Newsletter
Not "subscribe to our newsletter." Editorial positioning — *Stay close to the movement* —
then what actually arrives: stories, events, ideas, opportunities.

---

## 06. Mobile

Designed intentionally, not scaled down. Most visitors arrive from Instagram or Facebook
on a phone.

| Concern | Decision |
|---|---|
| Navigation | Header carries logo, the word **"Menu"** (not a bare icon), and the primary CTA. Full-screen panel, 56px rows, visible +/− toggles. No hover anywhere. |
| Thumb reach | Primary action always in the lower third. Sticky event CTA on event pages. |
| Hierarchy | Single column. Display type steps 112px → 44px but *scale relationships hold* — that is what preserves the editorial feel. |
| Image cropping | Art-directed per breakpoint. A 21:9 desktop hero becomes 4:5 on mobile — not the same file letterboxed. |
| Scroll rhythm | Full-bleed image, then type, then ground change. Alternation prevents the endless-scroll feeling. |
| Forms | 52px controls, correct `inputmode`, labels above fields, errors that name the fix. |

Wireframes: Home · Story · Program · Event · Get Involved.

---

## 07. CMS architecture

Structured content, so SHUMI updates the site without a developer for everyday changes.

| Entity | Key fields | Relationships |
|---|---|---|
| **Story** | Name, Location, Portrait, Intro, Quote, Body, Date | → Region, Programme, Theme |
| **Program** | Name, Category, Description, Impact, Image, Status | → Region, Stories |
| **Event** | Name, Date, Location, Description, Ticket URL, Status | → Region, Programme |
| **Resource** | Title, Type, File/URL, Description | → Theme |
| **Region** | Name, Description, Communities | → Stories, Programmes |
| **Community** | Name, Description | → Region |
| **Impact metric** | Label, Value, Source, As-of date | → Region, Programme |
| **Partner** | Name, Logo, URL, Consent flag | — |
| **Team** | Name, Role, Bio, Portrait, Consent flag | — |

**Two fields that are not decoration.** `Impact metric.Source` and `.As-of date` make it
structurally awkward to publish a number nobody can stand behind. `Partner.Consent flag`
and `Team.Consent flag` do the same for naming people and organisations. The content
model enforces the honesty policy rather than relying on whoever is editing that day.

---

## 08. Technical foundation

Recommended, with reasons rather than résumé:

| Layer | Recommendation | Why |
|---|---|---|
| Framework | **Next.js + TypeScript** | Editorial sites live or die on image performance and SEO; server rendering and the image pipeline are the actual reasons, not fashion. |
| Styling | **Tailwind + design tokens** | Tokens map 1:1 to the design system, so contrast rules survive contact with developers. |
| CMS | **Headless** (Sanity or Payload) | The content model above is relational; a page-based CMS cannot express story → region → programme. |
| Motion | A single animation library, used sparingly | One system, not three. |
| Images | Next/Image, AVIF + WebP, art-directed per breakpoint | Cinematic must not mean slow. |
| Forms | Progressive enhancement — works without JS | Accessibility floor. |
| Analytics | Privacy-respecting, cookieless where possible | Appropriate to the audience. |
| Events | Eventbrite adapter behind a clean interface | Swappable; not claimed as built. |

**Performance targets:** LCP < 2.5s on 4G · CLS < 0.1 · no layout shift from webfonts
(self-hosted, `font-display: swap`, metric-matched fallbacks) · lazy-load below the fold ·
video posters always, autoplay never with sound.

**SEO:** semantic HTML, metadata and Open Graph per template, `Article` and `Event`
schema, clean URLs, sitemap, canonicals.

---

## 09. Wireframe set

| # | Screen | Priority |
|---|---|---|
| 01 | Homepage | 🔴 |
| 02 | About | |
| 03 | Programs index | |
| 04 | Program detail | |
| 05 | Stories index | 🔴 |
| 06 | Story detail | 🔴 |
| 07 | Global | |
| 08 | Events index | 🔴 |
| 09 | Event detail | 🔴 |
| 10 | Resources | |
| 11 | Get involved | |
| 12 | Contact | |
| 13 | Mobile homepage | 🔴 |

Six marked 🔴 carry the argument and the conversion; they are wireframed first.
