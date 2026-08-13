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
4. **Template** — [`content/templates/carousel-template.md`](content/templates/carousel-template.md)
   is the structure every draft follows, plus the grounding rule: every
   tool name, price, and feature claim must trace back to the JSON data.
5. **Daily draft generation** — two scheduled Cowork Routines run each day
   (10am and 5pm ET), each picking the next topic and writing a full
   carousel draft into `content/drafts/YYYY-MM-DD-am.md` or
   `content/drafts/YYYY-MM-DD-pm.md`, updating `topics.json`, and
   committing/pushing the result.
6. **Review & post** — drafts land in `content/drafts/`. Nothing posts to
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
bio copy, and category to use when setting up the page.
[`brand/assets/`](brand/assets/) has the logo: `profile-icon-1080.png`
for the IG profile picture and `wordmark-logo.png` for anywhere a
horizontal logo is needed, with editable `.svg` sources for both.

## Keeping tool data current

Pricing changes. `tools.json` has a `verified_date`. If it's been more
than ~60 days, double-check any price before it goes out in a post — spot
edits to the JSON are all that's needed, the generator picks them up
automatically on the next run.

## Repo layout

```
brand/
  profile.md                 IG name, username, bio, category
  assets/                    Logo files (PNG + editable SVG)
content/
  brand-guide.md              Voice, audience, pillars, visual rules
  data/
    tools.json                 20 vetted AI tools with verified pricing
    comparisons.json           Tool-vs-tool pairs for Head-to-Head posts
    stacks.json                Tool bundles by business type for Shortlist posts
    topics.json                Rotating topic queue, tied to tool IDs
  templates/
    carousel-template.md      Structure + grounding rule every draft follows
  drafts/
    YYYY-MM-DD-am.md           Morning draft
    YYYY-MM-DD-pm.md           Evening draft
```
