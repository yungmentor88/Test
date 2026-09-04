#!/usr/bin/env python3
"""
Renders the three concept wireframe pages. Each concept's markup is written once
and rendered twice — desktop frame and mobile frame — so the two can never drift.
Mid-fidelity: real type and colour, marked image slots. 9ja LDA.
"""
import os, io
OUT = os.path.dirname(os.path.abspath(__file__))

FONTS = '<link rel="stylesheet" href="../assets/fonts.css">'

def slot(label, src=None, cls=""):
    img = f'<img src="images/{src}" alt="">' if src else ""
    return f'<div class="slot {cls}" data-slot="{label}">{img}</div>'

def anno(title, body):
    return f'<div class="anno"><b>{title}</b>{body}</div>'

NAV1 = ["About", "What We Do", "Events", "Stories", "Impact"]
NAV2 = ["About", "What We Do", "Events", "Stories", "Get Involved"]
NAV3 = ["About", "What We Do", "Events", "Stories", "Impact", "Get Involved"]

FOOT_COLS = [
    ("About", ["About SHUMI", "Mission &amp; Vision", "Values", "Meet the Team"]),
    ("What We Do", ["Programs", "Education", "Wellness", "Community"]),
    ("Take Part", ["Events", "Volunteer", "Partner", "Sponsor"]),
    ("More", ["Stories", "Resources", "Gallery", "Contact"]),
]

def footer(cls):
    cols = "".join(
        f'<div><h4>{h}</h4><ul>' + "".join(f'<li><a href="#">{i}</a></li>' for i in items) + '</ul></div>'
        for h, items in FOOT_COLS)
    extra = ('<p class="muted" style="margin-top:28px;font-size:15px;">'
             'Region &amp; language switcher slot reserved &mdash; designed, not built.</p>'
             if cls == "c3" else "")
    return f'<footer class="foot"><div class="wrap"><div class="cols">{cols}</div>{extra}</div></footer>'

# ---------------------------------------------------------------- CONCEPT 1
def concept1():
    nav = "".join(f'<li><a href="#">{n}</a></li>' for n in NAV1)
    feats = ""
    for i, (t, d) in enumerate([
        ("Programs that travel", "Built once, run by women in any country that wants them."),
        ("Education", "Practical learning, led by women from the community it serves."),
        ("Wellness", "Support that treats rest as infrastructure, not indulgence."),
    ]):
        feats += f'<article>{slot("EDITORIAL 3:2")}<h3>{t}</h3><p style="color:var(--grey);font-size:17px">{d}</p></article>'
    stories = ""
    for i, c in enumerate(["Ghana", "Brazil", "India", "Portugal"]):
        src = ["c1-portrait-a.jpg", "c1-portrait-b.jpg", "c1-group.jpg", "c1-hero.jpg"][i]
        stories += (f'<article>{slot("PORTRAIT 3:4", src)}'
                    f'<p style="font-size:15px;color:var(--pink);font-weight:600">{c}</p>'
                    f'<h3>[client to supply]</h3></article>')
    countries = "".join(f"<li>{c}</li>" for c in
        ["Ghana", "Brazil", "India", "Portugal", "Kenya", "United States", "Cabo Verde", "[client to supply]"])
    return f'''
<div class="eventbar"><div class="wrap">
  <span><b>11 October 2026</b> &middot; Women&rsquo;s Empowerment Event</span>
  <a class="cta" href="#">Get your ticket</a>
</div></div>
<div class="nav"><div class="wrap">
  <span class="mark">SHUMI</span>
  <ul>{nav}</ul>
  <button class="burger">Menu</button>
</div></div>

<div class="hero">
  <div class="hero-copy">
    <h1>Women everywhere. One community.</h1>
    <div class="rule"></div>
    <p style="color:var(--grey);font-size:20px">SHUMI connects women across countries and
       generations &mdash; through programmes, gatherings and the people they meet here.</p>
    <p style="margin-top:26px"><a class="btn btn-primary" href="#">Get your ticket</a>
       &nbsp;&nbsp;<a href="#" style="font-weight:600">What SHUMI does</a></p>
  </div>
  {slot("FULL-BLEED EDITORIAL PORTRAIT", "c1-hero.jpg")}
</div>

<div class="manifesto"><div class="wrap">
  <p>A woman&rsquo;s horizon should not be decided by where she was born.</p>
</div></div>

<div class="band"><div class="wrap">
  <h2>Who SHUMI is</h2>
  <div class="twocol">
    <p>Long-form is a credibility signal when it is set well, and this section is where
       Concept 01 earns its authority. It assumes SHUMI can write, or can be written for.
       Set as a leader column with a drop cap, running across two columns at an editorial
       measure, it reads as a considered statement rather than as website copy.</p>
    <p>The real text goes here: how SHUMI started, who started it, why it exists, and what
       it intends to become. <span class="tbd">[client to supply: 150&ndash;250 words]</span></p>
  </div>
</div></div>

<div class="band"><div class="wrap">
  <h2>Where we work</h2>
  <ul class="index">{countries}</ul>
</div></div>

<div class="band"><div class="wrap">
  <h2>What we do</h2>
  <div class="feat">{feats}</div>
</div></div>

<div class="event"><div class="wrap">
  <div class="date">11.10.26</div>
  <h3>Women&rsquo;s Empowerment Event</h3>
  <p style="max-width:52ch;color:#D8D3D6">A day of programmes, conversation and
     connection. <span class="tbd">[client to supply: venue, time, price]</span></p>
  <p style="margin-top:24px"><a class="btn btn-primary" href="#">Get your ticket</a></p>
</div></div>

<div class="band"><div class="wrap">
  <h2>SHUMI stories</h2>
  <div class="stories">{stories}</div>
</div></div>

<div class="band"><div class="wrap">
  <h2>Impact</h2>
  <p style="font-family:var(--serif);font-size:32px;line-height:1.3;max-width:26ch">
     <span class="tbd">[client to supply]</span></p>
  <p style="color:var(--grey);max-width:60ch;margin-top:16px">Set as a typeset statement
     rather than a stat band, so it reads honestly with no numbers at all.</p>
</div></div>

<div class="quote"><div class="wrap">
  <p>&ldquo;<span class="tbd">[a real quotation from a named woman]</span>&rdquo;</p>
  <p style="font-size:16px;color:var(--grey)"><span class="tbd">[her name, her country]</span></p>
</div></div>
{footer("c1")}'''

# ---------------------------------------------------------------- CONCEPT 2
def concept2():
    nav = "".join(f'<li><a href="#">{n}</a></li>' for n in NAV2)
    six = ""
    for t, d in [("Meet women near you", "Local gatherings, run by women who live there."),
                 ("Learn something useful", "Practical sessions on what women asked for."),
                 ("Get real support", "Someone to talk to, and somewhere to start."),
                 ("Wellness", "Rest, health and the permission to take both seriously."),
                 ("Opportunities", "Work, introductions and space to be seen."),
                 ("Community", "The part that keeps women coming back.")]:
        six += f'<div><h3>{t}</h3><p>{d}</p></div>'
    mosaic = "".join(slot("SQUARE", s) for s in
        ["c2-hero.jpg", "c2-doorway.jpg", "c2-generations.jpg", "c2-hands.jpg", "c1-group.jpg", "c3-speaker.jpg"])
    involve = "".join(
        f'<div><h3>{t}</h3><p style="color:var(--grey);font-size:17px">{d}</p>'
        f'<p style="margin-top:16px"><a class="btn btn-ghost" href="#">{c}</a></p></div>'
        for t, d, c in [
            ("Volunteer", "Help at an event or give a few hours a month.", "Volunteer with SHUMI"),
            ("Partner with SHUMI", "For organisations who want to work with us.", "Talk to us"),
            ("Space held for what is coming", "Donations and membership drop in here later.", "Reserved")])
    return f'''
<div class="eventbar"><div class="wrap">
  <span><b>Sat 11 October 2026</b> &middot; Everyone welcome</span>
  <a class="cta" href="#">Get your ticket</a>
</div></div>
<div class="nav"><div class="wrap">
  <span class="mark">SHUMI</span>
  <ul>{nav}</ul>
  <button class="burger">Menu</button>
</div></div>

{slot("WIDE WARM PHOTOGRAPH — women of many nationalities together", "c2-hero.jpg", "hero-photo")}
<div class="wrap"><div class="hero-copy">
  <h1>Where women meet, and stay.</h1>
  <p class="lead">SHUMI is a community for women, in the United States and around the
     world. Come to an event, find people, get support.</p>
  <div class="acts">
    <a class="btn btn-primary" href="#">Get your ticket</a>
    <a href="#" style="font-weight:600">See what happens at SHUMI</a>
  </div>
</div></div>

<div class="promises"><div class="wrap"><div class="row">
  <div><h3>Meet women near you</h3><p>Wherever you are, there is a way in.</p></div>
  <div><h3>Learn something useful</h3><p>Sessions led by women from the community.</p></div>
  <div><h3>Get real support</h3><p>Practical help, in plain language.</p></div>
</div></div></div>

<div class="band"><div class="wrap">
  <h2>The 11 October event</h2>
  <p class="sub">Everyone is welcome. You can come on your own.</p>
  <div class="invite">
    {slot("EVENT PHOTOGRAPH", "c2-doorway.jpg")}
    <div class="body">
      <dl class="facts">
        <div><dt>Date</dt><dd>Saturday 11 October 2026</dd></div>
        <div><dt>Time</dt><dd><span class="tbd">[client to supply]</span></dd></div>
        <div><dt>Where</dt><dd><span class="tbd">[client to supply]</span></dd></div>
        <div><dt>Tickets</dt><dd><span class="tbd">[client to supply]</span></dd></div>
      </dl>
      <p class="reassure">You can come on your own. You can bring your mother or your
         daughter. There is someone at the door whose job is to introduce you.</p>
      <p style="margin-top:22px"><a class="btn btn-primary" href="#">Get your ticket</a></p>
    </div>
  </div>
</div></div>

<div class="band"><div class="wrap">
  <h2>What we do</h2>
  <p class="sub">Six things, named after what they actually are.</p>
  <div class="six">{six}</div>
</div></div>

<div class="band" style="background:var(--blush)"><div class="wrap">
  <h2>One woman&rsquo;s story</h2>
  <p class="sub">Told properly, at length. One story beats six cards.</p>
  <div class="story">
    {slot("PORTRAIT 3:4", "c2-generations.jpg")}
    <div>
      <blockquote>&ldquo;<span class="tbd">[a real quotation, up to 30 words, with her permission]</span>&rdquo;</blockquote>
      <p style="margin-top:18px;color:var(--grey)"><span class="tbd">[her name, her country]</span></p>
      <p style="margin-top:14px"><a href="#" style="font-weight:600">Read her story</a></p>
    </div>
  </div>
</div></div>

<div class="band"><div class="wrap">
  <h2>Women around the world</h2>
  <p class="sub">Many countries, several generations, in the same frames.</p>
  <div class="mosaic">{mosaic}</div>
</div></div>

<div class="band"><div class="wrap">
  <h2>Ways to get involved</h2>
  <p class="sub">However much time you have.</p>
  <div class="involve">{involve}</div>
</div></div>

<div class="signup"><div class="wrap">
  <h2>Stay in touch</h2>
  <p class="sub">One email a month. Nothing else.</p>
  <div class="field"><label for="e2">Email address</label><input id="e2" type="email"></div>
  <a class="btn btn-primary" href="#">Join the mailing list</a>
</div></div>
{footer("c2")}'''

# ---------------------------------------------------------------- CONCEPT 3
def concept3():
    nav = "".join(f'<li><a href="#">{n}</a></li>' for n in NAV3)
    chips = "".join(f'<span class="chip{" on" if i == 0 else ""}">{c}</span>' for i, c in enumerate(
        ["All regions", "Africa", "Americas", "Asia", "Europe", "Middle East"]))
    counters = "".join(
        f'<div><div class="n"><span class="tbd">[--]</span></div><p>{l}</p></div>'
        for l in ["Women reached", "Countries", "Programmes", "Events held"])
    progs = "".join(
        f'<div class="prog"><span class="tag">{tag}</span><h3>{t}</h3><p>{d}</p></div>'
        for tag, t, d in [
            ("EDUCATION", "Learning programmes", "Run locally, designed once."),
            ("WELLNESS", "Health and rest", "Support that treats rest as infrastructure."),
            ("ECONOMIC", "Work and opportunity", "Introductions, training and visibility."),
            ("COMMUNITY", "Local chapters", "Women organising where they live.")])
    rail = "".join(
        f'<article>{slot("SQUARE", s)}<span class="country">{c}</span>'
        f'<h3>[client to supply]</h3></article>'
        for s, c in [("c3-speaker.jpg", "KENYA"), ("c3-work.jpg", "VIETNAM"),
                     ("c3-study.jpg", "BRAZIL"), ("c1-group.jpg", "PORTUGAL")])
    return f'''
<div class="announce"><div class="wrap">
  <span><b>11 Oct 2026</b> &middot; Women&rsquo;s Empowerment Event</span>
  <a class="cta" href="#">Get your ticket</a>
</div></div>
<div class="nav"><div class="wrap">
  <span class="mark">SHUMI</span>
  <ul>{nav}</ul>
  <button class="burger" style="color:#fff">Menu</button>
</div></div>

<div class="hero">
  {slot("FULL-BLEED DARK PHOTOGRAPH", "c3-hero.jpg")}
  <div class="over"><div class="wrap">
    <h1>Women everywhere.<br>One movement.</h1>
    <p>SHUMI connects women across <span class="tbd">[--]</span> countries.</p>
    <div class="acts">
      <a class="btn btn-primary" href="#">Get your ticket</a>
      <a class="btn btn-ghost" href="#">Find SHUMI near you</a>
    </div>
  </div></div>
</div>

<div class="dark-band"><div class="wrap">
  <h2>Where SHUMI is</h2>
  <p class="muted">A filterable list first, an interactive map only where it is supported.
     Honest at three countries; still works at sixty.</p>
  <div class="presence">
    <div><div class="chips">{chips}</div></div>
    <div><p class="muted"><span class="tbd">[client to supply: the countries SHUMI
       operates in today]</span></p></div>
  </div>
  <div class="counters">{counters}</div>
  <p class="muted" style="font-size:15px;margin-top:20px">Counters animate once on first
     view and are present as static text before any script runs.</p>
</div></div>

<div class="band"><div class="wrap">
  <h2>Programmes</h2>
  <p class="sub">A filtered grid that works at six and at sixty.</p>
  <div class="grid4">{progs}</div>
</div></div>

<div class="event">
  {slot("EVENT PHOTOGRAPH", "c3-hero.jpg")}
  <div class="over"><div class="wrap">
    <h2>Women&rsquo;s Empowerment Event</h2>
    <div class="count">
      <div><div class="n">37</div><span>DAYS</span></div>
      <div><div class="n">11</div><span>HOURS</span></div>
      <div><div class="n">04</div><span>MINS</span></div>
    </div>
    <a class="btn btn-primary" href="#">Get your ticket</a>
  </div></div>
</div>

<div class="band"><div class="wrap">
  <h2>Stories from women</h2>
  <p class="sub">Every story tagged with its country. Geography as metadata.</p>
  <div class="rail">{rail}</div>
</div></div>
{footer("c3")}'''

CONCEPTS = [
    ("concept-01-editorial.html", "c1", "Concept 01 — Global Editorial",
     "SHUMI as a publication with a point of view. Credibility through craft rather than statistics.",
     concept1(),
     [("HERO", "Asymmetric split. Type owns the left third, a single full-bleed portrait owns the rest. No text on the photograph, which removes a whole class of contrast problem."),
      ("COLOUR", "Working pink #C61065 &mdash; 5.73:1 on white, and 5.73:1 under white text. The brand pink #E85D9E appears only on the ink event band, where it reads 5.96:1."),
      ("WHAT TO WATCH", "Coldest of the three. Depends almost entirely on photographic quality.")]),
    ("concept-02-community.html", "c2", "Concept 02 — Human Community",
     "SHUMI as a room you are welcome in. Optimised for belonging over admiration.",
     concept2(),
     [("HERO", "Photograph first, full width, type below. Emotional recognition happens before any reading is required &mdash; the right order for a visitor arriving cold from social media."),
      ("COLOUR", "Working pink #AE2967 &mdash; 5.99:1 on the warm paper, 6.34:1 under white text. No pure white anywhere; the whole surface is warmed a few degrees."),
      ("TYPE", "19px body at 1.7 line-height. The smallest type here is larger than most sites' body type. That is the concept's clearest single decision.")]),
    ("concept-03-movement.html", "c3", "Concept 03 — Global Movement",
     "SHUMI as infrastructure for a movement. Designed for what SHUMI intends to become.",
     concept3(),
     [("HERO", "The only concept with type over the image. Permitted because the grade is controlled and the type is huge. Two primary CTAs &mdash; the second one is the whole platform thesis."),
      ("COLOUR", "The only concept where SHUMI's real brand pink does real work: #E85D9E is 5.84:1 on the #121016 ground, so it passes AA as text. On white it would be 3.24:1 and fail."),
      ("WHAT TO WATCH", "Requires the most content and looks worst when empty. An impact counter reading zero is more damaging than no counter at all.")]),
]

def page(fn, cls, title, standfirst, body, notes):
    notes_html = "".join(anno(t, b) for t, b in notes)
    return f'''<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} — SHUMI Global</title>
{FONTS}
<link rel="stylesheet" href="wireframe.css">
<style>
  body{{background:#DFD9DC}}
  .intro{{background:#fff;padding:36px 0 30px;border-bottom:1px solid #C9BFC5}}
  .intro .wrap{{max-width:900px}}
  .intro h1{{font-family:'Figtree',sans-serif;font-size:34px;font-weight:800;
    letter-spacing:-.02em;color:#1B141A;margin-bottom:8px}}
  .intro p.stand{{font-size:20px;color:#5A5157;margin-bottom:22px}}
  .back{{font-family:ui-monospace,monospace;font-size:13px;color:#7A2348;
    display:inline-block;margin-bottom:18px}}
</style>
</head><body>
<div class="intro"><div class="wrap">
  <a class="back" href="index.html">&larr; All three concepts</a>
  <h1>{title}</h1>
  <p class="stand">{standfirst}</p>
  {notes_html}
</div></div>

<div class="stage">
  <p class="device-cap">Desktop &mdash; 1240px</p>
  <div class="device device-desktop {cls}">{body}</div>

  <p class="device-cap">Mobile &mdash; 390px</p>
  <div class="device device-mobile {cls}">{body}</div>
</div>
</body></html>'''

for fn, cls, title, stand, body, notes in CONCEPTS:
    html = page(fn, cls, title, stand, body, notes)
    with io.open(os.path.join(OUT, fn), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"{fn:32} {len(html):>8,} bytes")
