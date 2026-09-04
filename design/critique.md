# Self-critique of the wireframe

Written after looking at the screenshots in `design/screenshots/`, before handing this
over. 9ja LDA.

---

## What I checked and what it found

**Contrast, measured not eyeballed.** Every text element on all four pages, at desktop
and mobile widths, checked against its actual computed background: **zero failures.** The
lowest ratio on the site is 4.77:1 (still above the 4.5:1 requirement) and most text is
well past AAA. The deep rose `#A8325A` passes both as text on white (6.42:1) and as a
button fill under white text (6.42:1), which is why the whole site needs only one pink.

**Structure.** One `<h1>` per page, no skipped heading levels, correct landmarks, every
image carries alt text, every form field has a real label.

**Interactions.** Menu open/close with focus trapping, accordions, nav dropdowns, contact
validation (empty fields and malformed email), success state, story filters, empty state,
and the post-event toggle were all driven programmatically on every page. No console
errors.

## Four things the screenshots caught that I had got wrong

1. **Every cropped image was rendering at its full natural height.** An `<img>` with a
   `height` attribute ignores CSS `aspect-ratio` unless `height: auto` is also set. The
   event hero was 1012px tall instead of 548px, and the homepage story cards were 1350px
   tall. On desktop this pushed the event page's title, date and ticket button entirely
   below the fold — which defeats the one job that page has. Fixed in the base `img` rule.

2. **The event hero still ate the fold once the ratio was right.** Capped at 42vh on
   desktop so the title, the date and the top of the details panel are always visible.

3. **At 390px the header ticket button wrapped onto two lines** and crowded the logo. It
   is now hidden below 520px — the persistent event bar directly above it already carries
   a ticket button, and the event page adds a sticky one, so nothing is lost.

4. **Four generated images had men in the background**, and the first event hero was too
   dark and too distant to carry a page. Regenerated with the framing and the exclusion
   made explicit. The homepage hero was regenerated for the same reason.

Also fixed against my own written spec: the event-bar ticket button was 38px rather than
44px, footer links were 40px, the skip link was never actually visible on focus, and
several small labels were 15px when the spec says nothing goes below 16px.

## One decision I changed on reflection

The mailing-list heading originally read **"Fika di sabi — stay in touch."** I am not
confident that is correct Kriolu, and guessing at Kriolu in front of a Cape Verdean
client is the single place where being wrong would land hardest — it would undercut the
whole claim that this site was made for this community. It is now English, with a marked
empty slot and a note that a Kriolu writer should supply the wording. **"Bem-vindu"**
stays, because I am confident in it.

This is the same rule as the invented-statistics rule, applied to language.

---

## What I would fix with more time

**Design**

- **The four "What SHUMI does" blocks are still the brief's abstract nouns.** This is the
  weakest content on the site and I have flagged it in three places, but it stays weak
  until SHUMI names four real things a woman can turn up to. Highest-value fix available.
- **The swoosh sits a little low under the event page's h1**, where the date line follows
  closely. It wants about 0.1em more clearance, and ideally three hand-drawn variants
  cycled per page so it never looks like a repeated vector asset.
- **The homepage hero is still slightly airy on a large desktop.** The image column and
  the text column do not quite balance at 1440px+. I would either crop the hero image
  taller or set a max width on the text column.
- **The "Our impact" section is three empty boxes**, which is honest but not attractive.
  If SHUMI has no numbers, my real recommendation is to cut the section at launch rather
  than ship visible gaps — that is in the presentation note, but the wireframe currently
  shows the awkward version.

**Build**

- **The logo is a text stand-in.** Everything about the type and colour will be re-checked
  against the real artwork, and the pink may shift slightly.
- **`build.py` is the right call for four pages and the wrong one for forty.** Whoever
  builds the real site should take the tokens and components, not this generator.
- **The story filters are client-side and re-filter the whole DOM.** Fine at nine items,
  wrong at three hundred; the real build needs server-side filtering and pagination.
- **No focus-visible styling has been tested in Windows High Contrast Mode**, which some
  older users have switched on without knowing what it is called.

**Content**

- The event page's "Questions" are my best guess at what women will actually ask. They
  should be replaced with the questions SHUMI genuinely receives.
- Alt text on the placeholder images describes the placeholders. It must be rewritten
  when the real photographs arrive — describing what is actually in the picture.

**Untested**

- Real screen-reader passes (VoiceOver, NVDA). The structure is right on paper and I
  verified it programmatically, but that is not the same as listening to it.
- Real devices. Everything here was checked in Chromium at two widths.
- No user has touched it. The one interaction I would test first is the mobile accordion,
  where the row label and the +/− toggle do two different things — that split is
  defensible but it is exactly the kind of thing that confuses a less confident user.
