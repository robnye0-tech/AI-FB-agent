# The AI Shortlist

Content engine for **The AI Shortlist**, a faceless Instagram page helping
small business owners and solo entrepreneurs cut through the noise on AI
tools.

## How it works

1. **Brand & voice** — [`content/brand-guide.md`](content/brand-guide.md)
   defines the audience, tone, content pillars, and visual style.
2. **Tool database** — [`content/data/tools.json`](content/data/tools.json)
   is the vetted list of 20 real AI tools (what they do, who they're for,
   verified pricing) that every draft is required to pull facts from —
   no invented tools, features, or prices.
   [`comparisons.json`](content/data/comparisons.json) and
   [`stacks.json`](content/data/stacks.json) are pre-built tool pairings
   and business-type bundles built from that same list, for the
   Head-to-Head and Shortlist pillars.
3. **Topic queue** — [`content/data/topics.json`](content/data/topics.json)
   is the rotating list of post ideas, each tied to specific tool IDs.
   Each automated run picks the next `pending` entry, drafts it, and
   flips it to `used`. When the queue runs dry, the run invents one new
   on-brand topic and appends it.
4. **Affiliate links** — [`content/data/affiliate-links.json`](content/data/affiliate-links.json)
   tracks which of the 20 tools have an affiliate program, the signup URL,
   and (once Rob applies and is approved) the real tracking link. A draft
   only uses a tool's affiliate link, adds the FTC-required disclosure, and
   updates [`content/link-in-bio.md`](content/link-in-bio.md) when that
   tool's `affiliate_url` is filled in — see "Monetization" below.
5. **Template** — [`content/templates/carousel-template.md`](content/templates/carousel-template.md)
   is the structure every draft follows, plus the grounding rule (every
   tool name, price, and feature claim must trace back to the JSON data)
   and the affiliate/disclosure rule.
6. **Daily draft generation** — two scheduled Cowork Routines run each day
   (10am and 5pm ET), each picking the next topic and writing a full
   carousel draft into `content/drafts/YYYY-MM-DD-am.md` or
   `content/drafts/YYYY-MM-DD-pm.md`, updating `topics.json`, and
   committing/pushing the result.
7. **Review & post** — drafts land in `content/drafts/`. Nothing posts to
   Instagram automatically — you review each draft, adjust if needed, and
   publish it yourself in the IG app. This keeps a human check on every
   post before it goes live.

## Why draft-and-approve instead of full auto-posting

Auto-posting requires an Instagram Business account linked to a Facebook
Page and a reviewed Meta Developer app with a long-lived access token —
real setup overhead and an approval process on Meta's side. Starting with
draft-and-approve means content generation is running from day one with no
API setup, and full auto-posting can be added later once the account and
Meta app are in place.

## Brand assets

[`brand/profile.md`](brand/profile.md) has the Instagram name, username,
bio copy, and category. [`brand/facebook-page.md`](brand/facebook-page.md)
has the matching Facebook Page name, category, short bio, and longer
About/Story copy.
[`brand/assets/`](brand/assets/) has the logo: `profile-icon-1080.png`
for the IG profile picture and `wordmark-logo.png` for anywhere a
horizontal logo is needed, with editable `.svg` sources for both.

## Keeping tool data current

Pricing changes. A third Cowork Routine ("AI Shortlist Pricing Refresh")
re-checks all 20 tools' pricing every ~15 days (the 1st and 16th of each
month) and updates `tools.json`'s `pricing` fields and `verified_date`
automatically — no manual upkeep needed.

## Monetization (affiliate links)

`content/data/affiliate-links.json` has one entry per tool: whether it has
a public affiliate program, the signup URL where known, reported
commission terms, and an `affiliate_url` field that starts `null`.

- **13 of the 20 tools have a real, applicable-today program**: Canva Pro,
  Grammarly, Jasper, HubSpot Breeze AI, QuickBooks Online, Tidio, Freshdesk
  (Freddy AI), Nextiva, HeyGen, Motion, Durable, folk, Descript.
- **3 have no public affiliate option**: ChatGPT Business (OpenAI), Claude
  Team (Anthropic), Dialpad Ai — these still work fine as unmonetized Tool
  Spotlight content.
- **Zapier, Notion AI, Fathom, Loom** are edge cases — Zapier's only
  program targets agencies not media, Notion's program is reportedly
  paused, Fathom's affiliate terms for individual creators weren't
  confirmed, Loom wasn't confirmed either way. Check each `signup_url`
  directly before assuming.

Applying to each program (business info, tax form, payment details,
approval) is something only Rob can do — once approved, paste the real
tracking link into that tool's `affiliate_url` field. From then on, any
post that references that tool automatically includes the link, the FTC
disclosure sentence required by `disclosure_rule`, and an update to
`content/link-in-bio.md` (Instagram only allows one clickable link, in the
bio, so that file is what actually gets pasted into a Linktree-style page).

## Repo layout

```
brand/
  profile.md                 IG name, username, bio, category
  assets/                    Logo files (PNG + editable SVG)
content/
  brand-guide.md              Voice, audience, pillars, visual rules, disclosure policy
  link-in-bio.md              Bio-link page content, auto-updated when affiliate links go live
  data/
    tools.json                 20 vetted AI tools with verified pricing
    comparisons.json           Tool-vs-tool pairs for Head-to-Head posts
    stacks.json                Tool bundles by business type for Shortlist posts
    topics.json                Rotating topic queue, tied to tool IDs
    affiliate-links.json       Affiliate program status + tracking links per tool
  templates/
    carousel-template.md      Structure + grounding rule + affiliate rule every draft follows
  drafts/
    YYYY-MM-DD-am.md           Morning draft
    YYYY-MM-DD-pm.md           Evening draft
```
