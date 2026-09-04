# SHUMI — Website design proposal

TedcanLabs · September 2026

**Start here:** `PowerPoint/SHUMI_Website_Design_Proposal.pptx` — 32 slides, 16:9,
fully editable, six embedded cinematic assets, speaker notes on every slide.

| Path | What it is |
|---|---|
| `PowerPoint/SHUMI_Website_Design_Proposal.pptx` | The deck |
| `PowerPoint/..._preview.pdf` | Flat PDF preview (video frames appear as posters) |
| `PowerPoint/deck_contact_sheet.jpg` | All 32 slides at a glance |
| `Documentation/Creative_Strategy.md` | Reference analysis, the idea, the three directions |
| `Documentation/UX_Architecture.md` | IA, homepage journey, content systems, CMS, stack |
| `Documentation/Design_System.md` | Colour with measured contrast, type, motion, photography |
| `Documentation/Proposal_Content.md` | Slide-by-slide copy and every placeholder |
| `Higgsfield/Higgsfield_Prompts.md` | Structured prompts for all six motion assets |
| `Higgsfield/Videos/` | The six clips + poster frames |
| `build_deck.py` | Rebuilds the deck from source. Edit and re-run. |

## Three things to know

1. **Nothing about SHUMI has been invented.** No statistics, countries, programmes,
   partners, testimonials, awards or pricing. Every unknown is a visible placeholder
   (`XX,XXX`, `[PROGRAM NAME]`, `$XX,XXX`) designed to look deliberate.
2. **Every image and video is AI-generated design exploration**, not documentary evidence
   of SHUMI's work, and the deck says so where it matters.
3. **Colour is provisional.** The logo arrived as a chat image rather than a file, so the
   brand pink is read visually. Send the artwork and the palette is re-derived.

## The open question

🔴 **Is SHUMI global, or a Cape Verdean-American organisation in Brockton, Massachusetts?**
Earlier material in this project said the latter; this brief says the former. They need
different websites. This is worth settling before anything is built.

## Rebuilding

```bash
pip install python-pptx pillow
python3 build_deck.py            # writes PowerPoint/SHUMI_Website_Design_Proposal.pptx
```

Fonts are Georgia + Corbel — the closest Office-safe pairing to the production site's
Bodoni Moda + Jost, so the deck renders identically on the client's machine instead of
silently substituting.
