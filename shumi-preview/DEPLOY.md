# SHUMI preview — putting it on Hostinger

Two self-contained static sites. No build step, no Node, no database, no environment
variables. Anything that can serve a folder can serve these.

    SHUMI-concept-a.zip   1.9 MB   Concept A — "Sanctuary"
    SHUMI-concept-b.zip   2.0 MB   Concept B — "Circle"

Each zip contains `index.html`, `.htaccess`, and an `assets/` folder (images, the
hero film as .webm + .mp4, and the two self-hosted fonts). Nothing loads from an
external CDN, so the pages render identically offline and on any host.

## Upload with hPanel File Manager (5 minutes, no credentials to share)

1. hPanel → **Files → File Manager** → open `public_html`.
2. Make a folder `shumi`, and inside it `a` and `b`.
3. Open `public_html/shumi/a`, click **Upload**, choose `SHUMI-concept-a.zip`.
4. Right-click the uploaded zip → **Extract** → into the current folder → delete the zip.
5. Repeat in `public_html/shumi/b` with `SHUMI-concept-b.zip`.
6. Visit `https://yourdomain.com/shumi/a/` and `https://yourdomain.com/shumi/b/`.

If File Manager will not show `.htaccess`, turn on **Settings → Show hidden files**.

## Upload over FTP instead

hPanel → **Files → FTP Accounts** gives the host, username and port. Point FileZilla
at it and drag the *contents* of each unzipped folder into `public_html/shumi/a`
and `public_html/shumi/b`. Upload `assets/` as a folder, not file by file.

## Before you send the link to the client

- **hPanel → Security → Force HTTPS: on.** The video will not autoplay over plain HTTP
  on some browsers.
- **hPanel → Advanced → Password Protect Directories** on `shumi` if this preview
  should not be public yet. The `.htaccess` already sends `X-Robots-Tag: noindex,
  nofollow` and the pages carry a `noindex` meta tag, so search engines stay out
  either way — but a password is the only thing that stops a forwarded link.
- Both pages are marked `noindex` deliberately. **Remove that meta tag and the
  `X-Robots-Tag` header when the chosen concept goes live**, or the real site will
  never appear in Google.

## What the `.htaccess` does

Turns off directory listing, sends the no-index headers, gzips HTML/CSS/JS, and sets
long cache lifetimes on images, video and fonts. If your plan does not have
`mod_headers` or `mod_expires`, the file degrades quietly — nothing breaks.

## Notes on the hero film

- 10-second loop, encoded twice: `.webm` (VP9) for Chrome/Firefox/Edge and `.mp4`
  (H.264) for Safari and iOS. The browser picks one; it never downloads both.
- It is a ping-pong encode — the second half is the first half reversed — so the loop
  has no visible seam.
- `preload="none"` until the JavaScript asks for it, it pauses when scrolled out of
  view or the tab is hidden, and it never plays at all for a visitor whose system
  is set to *reduce motion*. Those visitors get the poster frame, which is frame one
  of the film, so the page looks composed either way.
- Total weight of the heaviest page on first view is under 1.2 MB.
