#!/usr/bin/env python3
"""
Assembles the SHUMI wireframe pages from one shared header/footer/dialog so the
chrome cannot drift between screens. Output is plain static HTML that opens by
double-clicking. 9ja LDA.
"""
import os, io

OUT = os.path.dirname(os.path.abspath(__file__))

# --------------------------------------------------------------------------
# Shared pieces
# --------------------------------------------------------------------------

SWOOSH = ('<span class="swoosh">{word}'
          '<svg viewBox="0 0 200 12" preserveAspectRatio="none" aria-hidden="true" focusable="false">'
          '<path d="M2 8.5C28 2.6 60 2.2 96 5.6c34 3.2 66 6.4 102 -2.1" '
          'stroke="currentColor" stroke-width="5.5" fill="none" stroke-linecap="round"/>'
          '</svg></span>')

EXT = ('<svg class="ext-icon" viewBox="0 0 16 16" aria-hidden="true" focusable="false">'
       '<path d="M6 2h8v8" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/>'
       '<path d="M14 2 7 9" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/>'
       '<path d="M12 10v3a1 1 0 0 1-1 1H3a1 1 0 0 1-1-1V5a1 1 0 0 1 1-1h3" '
       'stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/></svg>')

NEW_TAB = '<span class="sr-only"> (opens Eventbrite in a new tab)</span>'

# The five groups. Everything else is nested or in the footer.
NAV = [
    ("About", "about.html", [
        ("Our story", "about.html"),
        ("Meet the team", "about.html#team"),
        ("Our impact", "about.html#impact"),
        ("Partners &amp; organizations we support", "about.html#partners"),
    ], None),
    ("What we do", "#", [], "Room for one child page per program as they launch"),
    ("Events", "event.html", [
        ("Upcoming events", "event.html"),
        ("Past events &amp; recaps", "#"),
    ], None),
    ("Stories", "stories.html", [
        ("SHUMI stories &amp; news", "stories.html"),
        ("Resources &amp; blog", "stories.html"),
        ("Photo gallery", "stories.html"),
    ], None),
    ("Get involved", "#", [
        ("Volunteer", "#"),
        ("Partner with SHUMI", "#"),
    ], "Reserved: Donate &middot; Membership &middot; Vendors &middot; Sponsors &middot; Speakers"),
]

TICKET_NOTE = ('<p class="form-note" id="tickets-note">Placeholder link &mdash; '
               'the Eventbrite event has not been created yet.</p>')


def ticket_btn(cls="btn btn-primary", label="Get tickets", note=False):
    html = (f'<a class="{cls}" href="#" data-eventbrite '
            f'aria-describedby="tickets-note">{label}{EXT}{NEW_TAB}</a>')
    return html + (TICKET_NOTE if note else "")


def header(current):
    items = []
    for label, href, kids, reserved in NAV:
        cid = "drop-" + label.lower().replace(" ", "-")
        cur = ' aria-current="page"' if label == current else ""
        if kids or reserved:
            panel = "".join(f'<li><a href="{h}">{t}</a></li>' for t, h in kids)
            if reserved:
                panel += f'<li><span class="reserved">{reserved}</span></li>'
            items.append(
                f'<li class="nav-item">'
                f'<button class="nav-link" data-drop aria-expanded="false" aria-controls="{cid}"{cur}>'
                f'{label}<svg class="nav-caret" viewBox="0 0 10 10" aria-hidden="true" focusable="false">'
                f'<path d="M1 3l4 4 4-4" stroke="currentColor" stroke-width="1.6" fill="none" '
                f'stroke-linecap="round"/></svg></button>'
                f'<ul class="nav-panel" id="{cid}" hidden>{panel}</ul></li>')
        else:
            items.append(f'<li class="nav-item"><a class="nav-link" href="{href}"{cur}>{label}</a></li>')
    desktop = "".join(items)

    groups = []
    for label, href, kids, reserved in NAV:
        pid = "m-" + label.lower().replace(" ", "-")
        if kids or reserved:
            kid_html = "".join(f'<li><a href="{h}">{t}</a></li>' for t, h in kids)
            if reserved:
                kid_html += f'<li><span class="reserved">{reserved}</span></li>'
            groups.append(
                f'<li class="m-group"><div class="m-row"><a href="{href}">{label}</a>'
                f'<button data-acc aria-expanded="false" aria-controls="{pid}" '
                f'aria-label="Show {label} pages">+</button></div>'
                f'<ul class="m-children" id="{pid}" hidden>{kid_html}</ul></li>')
        else:
            groups.append(f'<li class="m-group"><div class="m-row"><a href="{href}">{label}</a></div></li>')
    mobile = "".join(groups)

    return f'''
<a class="sr-only" href="#main">Skip to main content</a>

<div class="event-bar">
  <div class="wrap">
    <span><b>Women&rsquo;s Empowerment Event</b> <span class="dot">&middot;</span>
      Sat 11 October 2026 <span class="dot">&middot;</span> Brockton, MA</span>
    <a class="bar-cta" href="#" data-eventbrite aria-describedby="tickets-note">Get tickets{EXT}{NEW_TAB}</a>
  </div>
</div>

<header class="site-header">
  <div class="wrap">
    <a class="logo" href="index.html" aria-label="SHUMI Women's Empowerment, home">
      <span>
        <span class="logo-mark"><span class="heart">&#9825;</span> SHUMI</span>
        <small>Women&rsquo;s Empowerment</small>
      </span>
    </a>
    <nav class="nav-desktop" aria-label="Main"><ul style="display:flex;gap:2px;">{desktop}</ul></nav>
    <div class="header-actions">
      <button class="btn btn-outline btn-contact-header" data-contact-open>Contact</button>
      {ticket_btn()}
      <button class="btn-menu" data-menu-open aria-expanded="false" aria-controls="mobile-menu">
        <svg width="18" height="14" viewBox="0 0 18 14" aria-hidden="true" focusable="false">
          <path d="M1 1h16M1 7h16M1 13h16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>Menu
      </button>
    </div>
  </div>
</header>

<div class="mobile-menu" id="mobile-menu" hidden role="dialog" aria-modal="true" aria-label="Menu">
  <div class="mobile-menu-top">
    <span class="logo-mark"><span class="heart">&#9825;</span> SHUMI</span>
    <button class="btn-close" data-menu-close>Close</button>
  </div>
  <div class="mobile-menu-body"><ul>{mobile}</ul></div>
  <div class="mobile-menu-foot">
    {ticket_btn()}
    <button class="btn btn-outline" data-contact-open>Contact SHUMI</button>
  </div>
</div>'''


FOOTER = f'''
<footer class="site-footer">
  <div class="wrap">
    <div class="foot-cols">
      <div>
        <h2>SHUMI</h2>
        <ul>
          <li><a href="about.html">Our story</a></li>
          <li><a href="about.html#team">Meet the team</a></li>
          <li><a href="about.html#impact">Our impact</a></li>
          <li><a href="#">What we do</a></li>
        </ul>
      </div>
      <div>
        <h2>Take part</h2>
        <ul>
          <li><a href="event.html">Upcoming events</a></li>
          <li><a href="#">Volunteer</a></li>
          <li><a href="#">Partner with SHUMI</a></li>
          <li><a href="#" data-contact-open>Contact us</a></li>
        </ul>
      </div>
      <div>
        <h2>Read</h2>
        <ul>
          <li><a href="stories.html">SHUMI stories &amp; news</a></li>
          <li><a href="stories.html">Resources &amp; blog</a></li>
          <li><a href="stories.html">Photo gallery</a></li>
        </ul>
      </div>
      <div class="signup-mini">
        <h2>Mailing list</h2>
        <form class="stack" onsubmit="return false;">
          <div class="field">
            <label for="foot-email">Email address</label>
            <input id="foot-email" type="email" name="email" autocomplete="email" inputmode="email">
            <span class="hint">Event news and updates. Unsubscribe any time.</span>
          </div>
          <button class="btn btn-on-ink" type="submit">Join the mailing list</button>
        </form>
      </div>
    </div>
    <div class="foot-base">
      <div class="socials">
        <a href="#" aria-label="SHUMI on Instagram (opens in a new tab)">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="none" stroke="currentColor" stroke-width="2">
            <rect x="2.5" y="2.5" width="19" height="19" rx="5"/><circle cx="12" cy="12" r="4.2"/>
            <circle cx="17.6" cy="6.4" r="1.2" fill="currentColor" stroke="none"/></svg>Instagram</a>
        <a href="#" aria-label="SHUMI on Facebook (opens in a new tab)">
          <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false" fill="currentColor">
            <path d="M13.5 22v-8h2.7l.4-3.1h-3.1V8.9c0-.9.25-1.5 1.55-1.5H16.7V4.6A21 21 0 0 0 14.3 4.5c-2.4 0-4 1.45-4 4.1v2.3H7.6V14h2.7v8z"/></svg>Facebook</a>
      </div>
      <span class="spacer"></span>
      <span>&copy; 2026 SHUMI Women&rsquo;s Empowerment</span>
      <a href="#">Accessibility</a>
      <a href="#">Privacy</a>
    </div>
  </div>
</footer>

<dialog class="contact" id="contact-dialog" aria-labelledby="contact-title">
  <div class="dialog-top">
    <div>
      <h2 id="contact-title">Contact SHUMI</h2>
      <p class="t-meta">We read every message and reply within a few days.</p>
    </div>
    <button class="btn-close" data-contact-close aria-label="Close contact form">Close</button>
  </div>
  <div class="dialog-body">
    <div class="form-ok" hidden tabindex="-1" role="status">
      <strong>Thank you &mdash; your message has been sent.</strong>
      <p>Someone from SHUMI will reply to the email address you gave us.</p>
    </div>
    <form novalidate>
      <div class="field">
        <label for="c-name">Your name</label>
        <input id="c-name" name="name" type="text" autocomplete="name" data-required data-label="your name">
        <span class="err" hidden></span>
      </div>
      <div class="field">
        <label for="c-email">Email address</label>
        <input id="c-email" name="email" type="email" autocomplete="email" inputmode="email"
               data-required data-label="your email address">
        <span class="err" hidden></span>
      </div>
      <div class="field">
        <label for="c-topic">What is this about?</label>
        <select id="c-topic" name="topic">
          <option>A general question</option>
          <option>The 11 October event</option>
          <option>Volunteering</option>
          <option>Partnering with SHUMI</option>
          <option>Services and inquiries</option>
        </select>
      </div>
      <div class="field">
        <label for="c-msg">Your message</label>
        <textarea id="c-msg" name="message" data-required data-label="a message"></textarea>
        <span class="err" hidden></span>
      </div>
      <button class="btn btn-primary" type="submit">Send message</button>
      <p class="form-note" style="margin-top:12px;">
        Goes to <span class="tbd">[client to supply: recipient email]</span>
      </p>
    </form>
  </div>
</dialog>'''


def page(title, current, body, tool=None, body_class=""):
    toolhtml = (f'<div class="wf-tool" id="wf-tool"><div class="wf-top"><b>WIREFRAME PREVIEW</b>'
                f'<button class="wf-hide" data-wf-hide aria-label="Hide the wireframe preview panel">Hide</button>'
                f'</div>{tool}</div>'
                f'<button class="wf-show" id="wf-show" hidden data-wf-show>Preview tools</button>') if tool else ""
    bc = f' class="{body_class}"' if body_class else ""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="assets/fonts.css">
<link rel="stylesheet" href="assets/shumi.css">
</head>
<body{bc}>
{header(current)}
<main id="main">
{body}
</main>
{FOOTER}
{toolhtml}
<script src="assets/shumi.js"></script>
</body>
</html>'''

# ==========================================================================
# HOMEPAGE
# ==========================================================================

HOME = f'''
<section class="hero">
  <div class="wrap hero-grid">
    <div>
      <p class="kriolu">Bem-vindu</p>
      <h1>A place for Cape Verdean women to {SWOOSH.format(word="belong")}</h1>
      <p class="t-lead">SHUMI brings together Cape Verdean women in Brockton and across
        southeastern Massachusetts &mdash; grandmothers, mothers and daughters &mdash; for
        connection, resources and events.</p>
      <p>Everyone is welcome, whatever your age and whatever language you speak at home.</p>
      <div class="hero-actions">
        {ticket_btn(label="Get tickets for 11 October")}
        <a class="link-plain" href="#what-we-do">See what SHUMI does</a>
      </div>
      {TICKET_NOTE}
    </div>
    <figure class="hero-figure" style="margin:0;">
      <span class="ph"><img src="public/images/hero-home-three-generations.jpg" width="1600" height="1200"
        alt="Four women of three generations sitting close together at a round table in a community hall, mid-conversation."></span>
    </figure>
  </div>
</section>

<!-- The 11 October event. Same band, two states. -->
<section class="event-band" id="state-before" aria-labelledby="ev-h">
  <div class="wrap inner">
    <div>
      <h2 id="ev-h">SHUMI Women&rsquo;s Empowerment Event</h2>
      <p>An afternoon of connection, conversation and practical resources, for Cape
         Verdean women of every generation. Bring your mother. Bring your daughter.</p>
      <dl class="event-facts">
        <div><dt>Date</dt><dd>Saturday 11 October 2026</dd></div>
        <div><dt>Time</dt><dd><span class="tbd">[client to supply]</span></dd></div>
        <div><dt>Where</dt><dd>Brockton, MA &mdash; <span class="tbd">[client to supply: venue and address]</span></dd></div>
        <div><dt>Tickets</dt><dd><span class="tbd">[client to supply: price]</span></dd></div>
      </dl>
      <div class="actions">
        {ticket_btn()}
        <a class="link-plain" href="event.html">Full event details</a>
      </div>
      {TICKET_NOTE}
    </div>
    <div>
      <span class="ph"><img src="public/images/event-hero-arrivals.jpg" width="1800" height="1012"
        alt="Women greeting and embracing each other as they arrive at a community function hall."
        style="border-radius:4px;"></span>
    </div>
  </div>
</section>

<!-- 12 October onwards: identical band, identical position, different content. -->
<section class="event-band" id="state-after" hidden aria-labelledby="ev-h2">
  <div class="wrap inner">
    <div>
      <h2 id="ev-h2">That was the 11 October event</h2>
      <p>Thank you to everyone who came, and to the women who made it happen.</p>
      <div class="recap-photos">
        <img src="public/images/gallery-row-listening.jpg" width="800" height="800" alt="Women seated in a row listening to a speaker.">
        <img src="public/images/gallery-porch-laughing.jpg" width="800" height="800" alt="Two women laughing together on a porch step.">
        <img src="public/images/gallery-hands-table.jpg" width="800" height="800" alt="Hands of women of different ages resting together on a table.">
      </div>
      <p><strong>Next event:</strong> <span class="tbd">[client to supply]</span></p>
      <div class="actions">
        <a class="btn btn-primary" href="stories.html">See all photos from the day</a>
        <a class="link-plain" href="#mailing-list">Join the mailing list to hear first</a>
      </div>
    </div>
    <div>
      <span class="ph"><img src="public/images/expect-coffee-break.jpg" width="1100" height="825"
        alt="Women talking in small groups over coffee during a break at a community event."
        style="border-radius:4px;"></span>
    </div>
  </div>
</section>

<section id="what-we-do">
  <div class="wrap">
    <div class="section-head">
      <h2>What SHUMI does</h2>
      <p>Four things, and they all come back to the same idea: no woman should have to
         work it out on her own.</p>
    </div>
    <div class="programs">
      <div class="program"><h3>Connection</h3>
        <p>Gatherings where women of every generation actually meet each other, not just
           sit in the same room.</p></div>
      <div class="program"><h3>Resources</h3>
        <p>Practical help and clear information, in plain language, for the things women
           ask us about most.</p></div>
      <div class="program"><h3>Opportunities</h3>
        <p>Introductions, openings and space to be seen &mdash; for women building
           something of their own.</p></div>
      <div class="program"><h3>Education</h3>
        <p>Workshops and sessions led by women from this community, on what this
           community said it needed.</p></div>
    </div>
    <p class="note-editorial" style="margin-top:26px;">
      <strong>Note for SHUMI</strong>
      These four headings are from the brief and they are still abstract. Once you tell us
      the real programs you run, each block should be named after an actual thing a woman
      can turn up to.
    </p>
  </div>
</section>

<section class="ground-blush">
  <div class="wrap">
    <div class="section-head">
      <h2>SHUMI stories</h2>
      <p>The women of this community, in their own words.</p>
    </div>
    <div class="card-row">
      <article class="story">
        <span class="ph shot"><img src="public/images/story-grandmother-granddaughter.jpg" width="900" height="1350"
          alt="An older woman sitting on a sofa beside her granddaughter, mid-conversation."></span>
        <span class="tag">Story</span>
        <h3><a href="#">Two generations, one kitchen table</a></h3>
        <p><span class="tbd">[client to supply: 40&ndash;60 word summary]</span></p>
      </article>
      <article class="story">
        <span class="ph shot"><img src="public/images/story-two-women-basement.jpg" width="900" height="1350"
          alt="Two women in their fifties talking seriously in a community hall."></span>
        <span class="tag">News</span>
        <h3><a href="#">What we heard from you this year</a></h3>
        <p><span class="tbd">[client to supply: 40&ndash;60 word summary]</span></p>
      </article>
      <article class="story">
        <span class="ph shot"><img src="public/images/story-kitchen-coffee.jpg" width="900" height="1350"
          alt="A woman standing at a kitchen counter holding a mug, laughing at something off camera."></span>
        <span class="tag">Resource</span>
        <h3><a href="#">Where to start when you need help</a></h3>
        <p><span class="tbd">[client to supply: 40&ndash;60 word summary]</span></p>
      </article>
    </div>
    <p style="margin-top:28px;"><a class="link-plain" href="stories.html">Read all stories</a></p>
  </div>
</section>

<section id="impact">
  <div class="wrap">
    <div class="section-head">
      <h2>Our impact</h2>
      <p>We will only publish numbers we can stand behind.</p>
    </div>
    <div class="impact-grid">
      <div class="impact-cell">
        <span class="value"><span class="tbd">[number]</span></span>
        <p><span class="tbd">[client to supply: what this counts]</span></p>
      </div>
      <div class="impact-cell">
        <span class="value"><span class="tbd">[number]</span></span>
        <p><span class="tbd">[client to supply: what this counts]</span></p>
      </div>
      <div class="impact-cell">
        <span class="value"><span class="tbd">[number]</span></span>
        <p><span class="tbd">[client to supply: what this counts]</span></p>
      </div>
    </div>
    <p class="note-editorial" style="margin-top:28px;">
      <strong>Note for SHUMI</strong>
      Nothing has been invented here. This section is built and ready, and it stays empty
      until you give us real figures. If SHUMI does not have numbers yet, that is normal
      for a new organisation &mdash; we would remove this section at launch and add it back
      after the 11 October event, rather than fill it with something that is not true.
    </p>
  </div>
</section>

<section class="ground-blush">
  <div class="wrap">
    <div class="section-head">
      <h2>Ways to get involved</h2>
      <p>However much time you have.</p>
    </div>
    <div class="involve">
      <div class="involve-cell">
        <h3>Volunteer</h3>
        <p>Help at an event, welcome people at the door, or give a few hours a month to
           something you care about.</p>
        <a class="btn btn-outline" href="#">Volunteer with SHUMI</a>
      </div>
      <div class="involve-cell">
        <h3>Partner with SHUMI</h3>
        <p>For organisations, businesses and community groups who want to work with us or
           support an event.</p>
        <a class="btn btn-outline" href="#">Talk to us about partnering</a>
      </div>
      <div class="involve-cell soon">
        <h3>Space held for what is coming</h3>
        <p>Donations, membership, vendors, sponsors and speakers all drop into this row
           later without changing the navigation.</p>
        <span class="tbd">Structure only &mdash; not built</span>
      </div>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head">
      <h2>From our gatherings</h2>
      <p>Every photograph here is a placeholder until SHUMI&rsquo;s own event photography exists.</p>
    </div>
    <div class="gallery">
      <span class="ph"><img src="public/images/gallery-row-listening.jpg" width="800" height="800" alt="Women of mixed ages seated in a row, listening to a speaker."></span>
      <span class="ph"><img src="public/images/gallery-grandmother-shoulder.jpg" width="800" height="800" alt="A young woman resting her head on her grandmother's shoulder at a table."></span>
      <span class="ph"><img src="public/images/gallery-porch-laughing.jpg" width="800" height="800" alt="Two women laughing together on the front steps of a house."></span>
      <span class="ph"><img src="public/images/gallery-hands-table.jpg" width="800" height="800" alt="The hands of women of different ages resting together on a table."></span>
    </div>
  </div>
</section>

<section class="signup" id="mailing-list">
  <div class="wrap inner">
    <div>
      <h2>Stay in touch</h2>
      <p>One email when something is happening. Event dates, new resources, and nothing else.</p>
      <p class="t-meta">If Kriolu is used on the site, this heading is one of the three
         places it belongs: <span class="tbd">[Kriolu greeting &mdash; to be written and
         checked by a Kriolu writer]</span>. We have not guessed at it.</p>
    </div>
    <form class="stack" onsubmit="return false;">
      <div class="field">
        <label for="ml-name">First name</label>
        <input id="ml-name" type="text" name="firstname" autocomplete="given-name">
      </div>
      <div class="field">
        <label for="ml-email">Email address</label>
        <input id="ml-email" type="email" name="email" autocomplete="email" inputmode="email">
        <span class="hint">We will never share your address. Unsubscribe any time.</span>
      </div>
      <button class="btn btn-primary" type="submit">Join the mailing list</button>
    </form>
  </div>
</section>
'''

HOME_TOOL = ('<button data-state-toggle>Now showing: before 11&nbsp;Oct '
             '&mdash; switch to after</button>')

# ==========================================================================
# EVENT PAGE
# ==========================================================================

EVENT = f'''
<div class="event-hero">
  <span class="ph"><img src="public/images/event-hero-arrivals.jpg" width="1800" height="1012"
    alt="Women greeting each other as they arrive at a bright community function hall set with round tables."></span>
  <div class="wrap titleblock">
    <p class="kriolu" style="font-family:var(--font-display);font-style:italic;font-size:21px;color:var(--rose);margin-bottom:6px;">Bem-vindu</p>
    <h1>SHUMI Women&rsquo;s Empowerment {SWOOSH.format(word="Event")}</h1>
    <p class="when">Saturday 11 October 2026 &middot; Brockton, MA</p>
  </div>
</div>

<section style="padding-top:36px;">
  <div class="wrap" style="display:grid;gap:34px;">
    <div class="facts-panel">
      <h2 style="font-size:26px;">The details</h2>
      <dl class="facts-list">
        <div><dt>Date</dt><dd>Saturday 11 October 2026</dd></div>
        <div><dt>Time</dt><dd><span class="tbd">[client to supply: start and end time]</span></dd></div>
        <div><dt>Venue</dt><dd><span class="tbd">[client to supply: venue name]</span></dd></div>
        <div><dt>Address</dt><dd><span class="tbd">[client to supply: street address, Brockton, MA]</span></dd></div>
        <div><dt>Tickets</dt><dd><span class="tbd">[client to supply: price, and any tiers]</span></dd></div>
        <div><dt>Who it&rsquo;s for</dt><dd>Cape Verdean women of every generation, and the women who come with them.</dd></div>
      </dl>
      {ticket_btn(label="Get tickets on Eventbrite", note=True)}
    </div>

    <div class="prose">
      <h2>What to expect</h2>
      <p>A Saturday afternoon with other women, built around conversation rather than
         a stage. You do not need to know anyone to come.</p>
    </div>

    <div class="expect">
      <div class="expect-item">
        <span class="ph shot"><img src="public/images/expect-workshop-circle.jpg" width="1100" height="825"
          alt="Women sitting in a circle of chairs while one of them speaks."></span>
        <div>
          <h3>Sessions led by women from this community</h3>
          <p>Small groups, chairs in a circle, real questions. Nothing you have to prepare
             for and nothing you have to say out loud if you would rather listen.</p>
        </div>
      </div>
      <div class="expect-item">
        <span class="ph shot"><img src="public/images/expect-coffee-break.jpg" width="1100" height="825"
          alt="Women talking in small groups holding paper cups of coffee during a break."></span>
        <div>
          <h3>Time to actually talk to each other</h3>
          <p>Long breaks on purpose. Most of what women tell us they got from the last
             gathering happened over coffee, not in a session.</p>
        </div>
      </div>
      <div class="expect-item">
        <span class="ph shot"><img src="public/images/gallery-row-listening.jpg" width="800" height="800"
          alt="Women of mixed ages seated together listening attentively."></span>
        <div>
          <h3>Resources you can take home</h3>
          <p><span class="tbd">[client to supply: what women leave with &mdash; a
             directory, a contact list, a workbook?]</span></p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="ground-blush">
  <div class="wrap" style="display:grid;gap:34px;">
    <div class="prose">
      <h2>Getting there</h2>
      <div class="stack">
        <p><strong>Parking.</strong> <span class="tbd">[client to supply: parking, and whether it is free]</span></p>
        <p><strong>Public transport.</strong> <span class="tbd">[client to supply: nearest stop or station]</span></p>
        <p><strong>Step-free access.</strong> <span class="tbd">[client to supply: is the venue step-free, and where are the accessible toilets]</span></p>
        <p><strong>Getting dropped off.</strong> <span class="tbd">[client to supply]</span></p>
      </div>
      <p class="note-editorial" style="margin-top:22px;">
        <strong>Why this section exists</strong>
        These are the questions that quietly stop older women coming. Answering them on
        the page removes a reason not to buy a ticket.
      </p>
    </div>
  </div>
</section>

<section>
  <div class="wrap">
    <div class="section-head"><h2>Questions</h2>
      <p>Open on the page, not hidden behind a click.</p></div>
    <div class="qa prose">
      <div><h3>Can I come on my own?</h3>
        <p>Yes, and many women do. There will be someone at the door whose job is to
           introduce you to other people.</p></div>
      <div><h3>Can I bring my mother or my daughter?</h3>
        <p>Yes. This event is built for women of different generations to be in the same
           room, so bringing family is the point rather than the exception.</p></div>
      <div><h3>What should I wear?</h3>
        <p>Whatever you are comfortable in. There is no dress code.</p></div>
      <div><h3>Is there food?</h3>
        <p><span class="tbd">[client to supply]</span></p></div>
      <div><h3>Is there childcare?</h3>
        <p><span class="tbd">[client to supply &mdash; and if the answer is no, we should
           still say so here]</span></p></div>
      <div><h3>What if I cannot afford a ticket?</h3>
        <p><span class="tbd">[client to supply &mdash; is there a concession or a
           supported place? This is worth answering.]</span></p></div>
    </div>
  </div>
</section>

<div class="ticket-bar">
  <span class="when">Sat 11 Oct 2026<br>Brockton, MA</span>
  {ticket_btn(label="Get tickets")}
</div>
'''

EVENT_TOOL = ('<p style="margin:0 0 8px;">The 12 October state of this page is shown '
              'on the homepage band. Use the toggle there.</p>')

# ==========================================================================
# STORIES — the growing collection. Populated, and with its empty state.
# ==========================================================================

_STORY_ITEMS = [
    ("story-grandmother-granddaughter", "Story", "Two generations, one kitchen table", "story",
     "An older woman sitting on a sofa beside her granddaughter, mid-conversation."),
    ("story-two-women-basement", "News", "What we heard from you this year", "news",
     "Two women in their fifties talking seriously in a community hall."),
    ("story-kitchen-coffee", "Resource", "Where to start when you need help", "resource",
     "A woman standing at a kitchen counter holding a mug, laughing at something off camera."),
    ("gallery-porch-laughing", "Story", "The women who kept the door open", "story",
     "Two women laughing together on the front steps of a house."),
    ("expect-workshop-circle", "News", "Notes from our last gathering", "news",
     "Women sitting in a circle of chairs while one of them speaks."),
    ("gallery-grandmother-shoulder", "Story", "What my grandmother carried over", "story",
     "A young woman resting her head on her grandmother's shoulder at a table."),
    ("expect-coffee-break", "Resource", "A plain-language guide to getting support", "resource",
     "Women talking in small groups over coffee during a break."),
    ("team-portrait-2", "Story", "Fifty years in Brockton", "story",
     "Portrait of a woman in her sixties wearing a patterned headwrap."),
    ("gallery-row-listening", "News", "What is coming after 11 October", "news",
     "Women of mixed ages seated in a row, listening to a speaker."),
]

_cards = []
for img, tag, title, cat, alt in _STORY_ITEMS:
    _cards.append(f'''      <article class="story" data-cat="{cat}">
        <span class="ph shot"><img src="public/images/{img}.jpg" loading="lazy" alt="{alt}"></span>
        <span class="tag">{tag}</span>
        <h3><a href="#">{title}</a></h3>
        <p><span class="tbd">[client to supply: 40&ndash;60 word summary]</span></p>
        <p class="t-meta"><span class="tbd">[date]</span></p>
      </article>''')

STORIES = f'''
<div class="page-head">
  <div class="wrap">
    <h1>SHUMI {SWOOSH.format(word="stories")}</h1>
    <p class="t-lead prose">Stories, news and resources from the women of this community.
       This page grows &mdash; it is built to look right with three items and with thirty.</p>
  </div>
</div>

<section style="padding-top:20px;">
  <div class="wrap">
    <h2 class="sr-only">Filter stories</h2>
    <div class="filters" role="group" aria-label="Filter by type">
      <button class="filter" data-filter="all" aria-pressed="true">All</button>
      <button class="filter" data-filter="story" aria-pressed="false">Stories</button>
      <button class="filter" data-filter="news" aria-pressed="false">News</button>
      <button class="filter" data-filter="resource" aria-pressed="false">Resources</button>
    </div>
    <p class="result-count" id="result-count" role="status">{len(_STORY_ITEMS)} stories</p>

    <div class="card-row" id="story-grid">
{chr(10).join(_cards)}
    </div>

    <!-- Empty state. An empty screen invites action; it does not look broken. -->
    <div class="empty" id="empty-state" hidden>
      <h3>Nothing here yet</h3>
      <p>There are no stories in this category at the moment. New writing goes up after
         each gathering &mdash; the mailing list is the quickest way to hear about it.</p>
      <a class="btn btn-primary" href="#mailing-list">Join the mailing list</a>
    </div>

    <div class="pager">
      <button class="btn btn-outline" type="button">Show more stories</button>
      <span class="t-meta">Showing {len(_STORY_ITEMS)} of <span class="tbd">[all]</span></span>
    </div>
  </div>
</section>

<section class="signup" id="mailing-list">
  <div class="wrap inner">
    <div>
      <h2>Hear about new stories</h2>
      <p>One email when something is happening. Nothing else.</p>
    </div>
    <form class="stack" onsubmit="return false;">
      <div class="field">
        <label for="s-email">Email address</label>
        <input id="s-email" type="email" name="email" autocomplete="email" inputmode="email">
        <span class="hint">Unsubscribe any time.</span>
      </div>
      <button class="btn btn-primary" type="submit">Join the mailing list</button>
    </form>
  </div>
</section>
'''

STORIES_TOOL = ('<p style="margin:0 0 8px;">Filter to a category, then use it again to '
                'see the empty state.</p>')

# ==========================================================================
# ABOUT / MEET THE TEAM
# ==========================================================================

ABOUT = f'''
<div class="page-head">
  <div class="wrap">
    <h1>About {SWOOSH.format(word="SHUMI")}</h1>
    <p class="t-lead prose">SHUMI is a women&rsquo;s empowerment organisation for the Cape
       Verdean community in Brockton and across southeastern Massachusetts.</p>
  </div>
</div>

<section style="padding-top:26px;">
  <div class="wrap" style="display:grid;gap:40px;">
    <div class="prose stack">
      <h2>Our story</h2>
      <p><span class="tbd">[client to supply: 150&ndash;250 words. How SHUMI started, who
         started it, and why. Written in SHUMI&rsquo;s own voice.]</span></p>
      <p><span class="tbd">[client to supply: what SHUMI is growing into &mdash;
         100&ndash;150 words.]</span></p>
    </div>
    <span class="ph"><img src="public/images/expect-coffee-break.jpg" width="1100" height="825"
      alt="Women talking in small groups over coffee at a community event."
      style="border-radius:4px;"></span>
  </div>
</section>

<section class="ground-blush" id="team">
  <div class="wrap">
    <div class="section-head">
      <h2>Meet the team</h2>
      <p>The women who run SHUMI.</p>
    </div>
    <div class="team">
      <article class="member">
        <span class="ph shot"><img src="public/images/team-portrait-1.jpg" loading="lazy"
          alt="Portrait of a woman in her forties standing in a community centre hallway."></span>
        <h3><span class="tbd">[name]</span></h3>
        <p class="role"><span class="tbd">[role]</span></p>
        <p><span class="tbd">[client to supply: 30&ndash;50 word bio]</span></p>
      </article>
      <article class="member">
        <span class="ph shot"><img src="public/images/team-portrait-2.jpg" loading="lazy"
          alt="Portrait of a woman in her sixties wearing a patterned headwrap, seated in a hall."></span>
        <h3><span class="tbd">[name]</span></h3>
        <p class="role"><span class="tbd">[role]</span></p>
        <p><span class="tbd">[client to supply: 30&ndash;50 word bio]</span></p>
      </article>
      <article class="member">
        <span class="ph shot"><img src="public/images/team-portrait-3.jpg" loading="lazy"
          alt="Portrait of a woman in her thirties standing near a window in a community centre."></span>
        <h3><span class="tbd">[name]</span></h3>
        <p class="role"><span class="tbd">[role]</span></p>
        <p><span class="tbd">[client to supply: 30&ndash;50 word bio]</span></p>
      </article>
    </div>
    <p class="note-editorial" style="margin-top:28px;">
      <strong>Note for SHUMI</strong>
      Three shown. The row reflows cleanly at any number &mdash; one member or fifteen.
      Headshots should be photographed in the same light and at the same distance as each
      other; we can shoot all of them in twenty minutes at the 11 October event.
    </p>
  </div>
</section>

<section id="impact">
  <div class="wrap">
    <div class="section-head">
      <h2>Our impact</h2>
      <p>We will only publish numbers we can stand behind.</p>
    </div>
    <div class="impact-grid">
      <div class="impact-cell"><span class="value"><span class="tbd">[number]</span></span>
        <p><span class="tbd">[client to supply: what this counts]</span></p></div>
      <div class="impact-cell"><span class="value"><span class="tbd">[number]</span></span>
        <p><span class="tbd">[client to supply: what this counts]</span></p></div>
      <div class="impact-cell"><span class="value"><span class="tbd">[number]</span></span>
        <p><span class="tbd">[client to supply: what this counts]</span></p></div>
    </div>

    <h3 style="margin-top:44px;">In her own words</h3>
    <blockquote style="border-left:3px solid var(--rose);margin:14px 0 0;padding:4px 0 4px 20px;max-width:60ch;">
      <p style="font-family:var(--font-display);font-size:24px;line-height:1.4;">
        <span class="tbd">[client to supply: a real quotation from a named woman, no more
        than 30 words, and her permission to use it]</span></p>
      <footer class="t-meta"><span class="tbd">[her name]</span></footer>
    </blockquote>
    <p class="note-editorial" style="margin-top:28px;">
      <strong>Note for SHUMI</strong>
      We have not written a testimonial for you. Any quotation on this site has to be
      something a real woman actually said, kept short, and attributed to her by name with
      her permission. SHUMI&rsquo;s own message belongs in SHUMI&rsquo;s voice, not dressed
      up as a quote.
    </p>
  </div>
</section>

<section class="ground-blush" id="partners">
  <div class="wrap">
    <div class="section-head">
      <h2>Partners and organizations we support</h2>
      <p>Built as a filterable grid so it still works at thirty entries.</p>
    </div>
    <div class="involve">
      <div class="involve-cell"><h3><span class="tbd">[partner name]</span></h3>
        <p><span class="tbd">[client to supply: one line on what they do]</span></p>
        <span class="tbd">[link]</span></div>
      <div class="involve-cell"><h3><span class="tbd">[partner name]</span></h3>
        <p><span class="tbd">[client to supply: one line on what they do]</span></p>
        <span class="tbd">[link]</span></div>
      <div class="involve-cell"><h3><span class="tbd">[partner name]</span></h3>
        <p><span class="tbd">[client to supply: one line on what they do]</span></p>
        <span class="tbd">[link]</span></div>
    </div>
    <p class="note-editorial" style="margin-top:28px;">
      <strong>Note for SHUMI</strong>
      No partner names or logos have been invented. Send us the real list and we will
      confirm each one is happy to be named before it goes live.
    </p>
  </div>
</section>
'''

# ==========================================================================
# Write
# ==========================================================================

pages = [
    ("index.html",   "SHUMI Women's Empowerment &mdash; a place for Cape Verdean women to belong", None,      HOME,    HOME_TOOL,    ""),
    ("event.html",   "Women's Empowerment Event, 11 October 2026 &mdash; SHUMI",                   "Events",  EVENT,   EVENT_TOOL,   "has-ticket-bar"),
    ("stories.html", "SHUMI stories, news and resources",                                          "Stories", STORIES, STORIES_TOOL, ""),
    ("about.html",   "About SHUMI and the team behind it",                                         "About",   ABOUT,   None,         ""),
]

for fn, title, cur, body, tool, bc in pages:
    html = page(title, cur, body, tool, bc)
    with io.open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"{fn:14} {len(html):>7,} bytes")
