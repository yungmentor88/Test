# What you are looking at

**A note for Melanie, Gabriella and the SHUMI team**
From 9ja LDA · 4 September 2026

---

## In one paragraph

This is a **wireframe** — a working draft of the SHUMI website that you can click through
like a real site. It is deliberately built to look close to finished rather than as grey
boxes, because it is much easier to say "no, not that" when you can actually see it. Some
of it is real and some of it is scaffolding, and this note tells you which is which.

**Open `index.html`** to start. Everything links together: the menu works, the contact
form opens, the story filters work, and it all works on a phone.

---

## What is real, and what is waiting for you

| Real and decided | Waiting for you |
|---|---|
| The navigation and how it is grouped | All the words in the grey `[client to supply]` boxes |
| The colours, the type, and the spacing | Every photograph |
| How every page is laid out | The event venue, time and ticket price |
| How it behaves on a phone | The Eventbrite link |
| The accessibility work | Team names, roles and bios |

Wherever you see a **grey striped box** like `[client to supply]`, that is a fact we did
not have. We chose to leave those visibly empty rather than fill them with something
invented — see "Two things we did not do" at the end.

---

## Why the navigation looks like this

Your brief listed twelve things the site needs to cover. Twelve items will not fit in a
menu bar, and a menu that long stops people finding anything.

So we grouped them into **five**, based on the five questions a stranger actually asks:

| The menu says | Because she is asking | It contains |
|---|---|---|
| **About** | Who are you, and are you real? | Our story · Meet the team · Our impact · Partners |
| **What we do** | What do you actually offer? | The programs |
| **Events** | When can I come? | Upcoming · Past events and recaps |
| **Stories** | What have you been up to? | Stories & news · Resources & blog · Photo gallery |
| **Get involved** | How do I join in? | Volunteer · Partner with SHUMI |

**Contact** is a button rather than a menu item, because you asked for it to open as a
pop-up rather than as its own page. **The mailing list** sits in the footer and on the
homepage, because it is a thing to do, not a place to go.

**Room to grow.** Donations, membership, vendors, sponsors and speakers all drop into
*Get involved* when you are ready. Adding them will not mean redesigning the menu. New
programs slot under *What we do* the same way. This was one of your requirements and it is
the main reason for grouping things this way rather than listing them flat.

---

## Why this pink

You said the pink should not feel loud or overly bright, and that was the hardest single
thing to get right — because a pink pale enough to feel calm is usually too pale to read.

We landed on **one deep rose, `#A8325A`**. It is unusual in a useful way: it is dark
enough to be read as text on white *and* light enough for white text to be read on top of
it. That means the whole site needs only one working pink, so nothing drifts.

**The pink is capped at about 5% of any screen** and only appears where a finger goes — a
button, a link, the focus outline. There are no pink backgrounds and no pink gradients.
The pale pink you see behind some sections is so light it reads as a warm white; its job
is to give the page rhythm without turning it pink.

The rest is white, near-black for text, and warm neutrals.

> One thing to know: we do not have your logo file, so we could not sample your actual
> pink. When you send the artwork we will re-check this against it. The shade may shift
> slightly — the accessibility requirement will not.

---

## Why this type

Your logo uses a **dramatic, high-contrast serif** — thin hairlines, heavy strokes, an
outline and a drop shadow. You also asked for typography that feels **soft and
approachable**. Those two things pull in opposite directions.

Rather than split the difference, we let the logo stay the boldest thing on the page and
made everything around it quieter:

- **Headings use a soft, low-contrast serif** (Newsreader). It keeps the site feeling
  elegant, but it is gentler than the logo, so the two do not compete. It is used only at
  the largest sizes.
- **Everything you actually read uses a warm, open sans-serif** (Figtree) — body text,
  buttons, forms, labels.
- **The outline and drop shadow stay on the logo only.** They do not appear on buttons,
  cards or headings. That treatment is your logo's signature and repeating it everywhere
  would cheapen it.

**On reading comfort.** Body text is set at 18 pixels, not the usual 16, with generous
space between the lines, and it does not get smaller on a computer. This is deliberate.
For a reader in her sixties on a phone, the thing that makes text hard is not usually the
letter size — it is losing your place at the end of a line. The extra line spacing fixes
that. Nothing anywhere on the site is smaller than 16 pixels.

---

## The 11 October event

Until that date, selling tickets is the site's main job, so it appears in three places:

1. **A dark bar across the very top of every page**, with the date and a ticket button. It
   is visible before anyone scrolls, on every screen.
2. **The main button in the top right**, on every page.
3. **A full band on the homepage**, immediately under the opening section.

On a phone, the event page also keeps a **ticket bar fixed at the bottom of the screen**,
so the button is always under the reader's thumb no matter how far down she has scrolled.

**We also designed what happens on 12 October.** The event band does not go stale or
disappear — it becomes a recap with photographs from the day and a pointer to what is
next. You can see this: click the dark **"Wireframe preview"** box in the bottom-right
corner of the homepage to switch between the before and after versions.

> The ticket buttons currently say *"Placeholder link — the Eventbrite event has not been
> created yet."* Send us the Eventbrite address and they go live.

---

## About the photographs — please read this one

**Every image on the wireframe is a stand-in that we generated. None of them are real
women, none of them are SHUMI members, and none of them can go on the live site.**

They exist so you can judge the *style* of photography we are recommending before anyone
books a photographer. You will see a small **"Placeholder image"** label on each one.

What we were aiming at, and what we would like your reaction to:

- Cape Verdean-American women, with the real range that community has — the point was
  deliberately **not** to make everyone look alike
- **Different generations in the same photograph**, rather than a "young" set and an
  "older" set
- Real rooms: a function hall, a church basement, somebody's kitchen, a front porch
- Natural light, nothing posed, nobody smiling on cue at the camera

If this is the wrong feeling, now is the cheap moment to say so.

**The plan:** photograph the 11 October event properly and replace all fourteen images
with real ones. We can also take every team headshot on the day, in about twenty minutes.

---

## Accessibility

You mentioned this twice in your brief, so we treated it as a specification rather than a
nice-to-have. In practice:

- Every colour combination on the site has been **measured**, not eyeballed, and passes
  the AA international standard. Most pass the stricter AAA level.
- Everything can be operated **without a mouse**, and you can always see where you are.
- Every button and link is **at least 44 pixels**, with real space between them, so they
  are easy to hit with a thumb.
- The menu says the word **"Menu"** rather than only showing three lines, and opens full
  screen so there is no doubt whether it is open.
- **Nothing is hidden behind hovering.** Menus open on a tap. The event questions are
  open on the page rather than folded away.
- If someone has switched off animations on their device, the site respects that.
- Form errors say **what to fix**, in plain words, and send you to the field.

---

## Two things we did not do

**1. We did not invent anything.** No visitor numbers, no impact figures, no testimonials,
no partner names, no awards, no press logos. It is very tempting on a site like this —
a row of big numbers reads as credibility — but a number you cannot stand behind is a
problem waiting to happen, and this community will know. The "Our impact" and quotation
sections are **built and ready** and sitting empty until you give us something true.

If SHUMI does not have figures yet, our recommendation is to launch without that section
and add it after October. That is a normal position for a young organisation.

**2. We did not copy the three reference sites.** We studied all three and took the
structural ideas that work — the announcement bar, the way the menu is grouped, the
event-first layout, the filterable grid that still works at thirty items. We deliberately
left the things that would not be honest here, in particular the large statistics banner
and the press logos on one of them. None of the three should be recognisable in this.

---

## What we need to move forward

The full list is in **`content-checklist.md`**, organised page by page — 53 items, each
marked required or optional, written to be worked through a bit at a time.

**The six things that block the event page** are at the top of that list:

1. The Eventbrite link
2. The venue name
3. The full street address
4. Start and end time
5. Ticket price
6. Confirmation of the city (we assumed Brockton)

Plus, as soon as you can: **your logo artwork**, so we can sample your real pink.

**One decision only you can make:** should Kriolu appear on the site? We are recommending
yes, in three places only — the welcome, the mailing-list heading, and the footer — with
everything functional staying in English. There is a fuller explanation at the end of the
checklist. If you would rather not, nothing else changes.

You will see **"Bem-vindu"** used on the homepage and the event page. The other two slots
are left as marked empty boxes on purpose: we are not confident enough in our written
Kriolu to guess at them, and getting a phrase subtly wrong in front of this community
would be worse than leaving it in English. We would rather a Kriolu writer gave us the
wording.

---

## Where to click

| File | What it is |
|---|---|
| `index.html` | The homepage — start here |
| `event.html` | The 11 October event page |
| `stories.html` | Stories and news. Use the filters, including to see the "nothing here yet" screen |
| `about.html` | About SHUMI and the team |
| `content-checklist.md` | Everything we need from you |
| `design/direction.md` | The full design reasoning, if you want the detail |
| `public/images/manifest.md` | Every placeholder image and what replaces it |

Two things worth trying: **make the window narrow**, or open it on your phone, to see the
mobile design. And click the **"Wireframe preview"** box on the homepage to see what the
event section becomes on 12 October.

We would rather hear the awkward reactions now than after it is built. Nothing here is
precious.
