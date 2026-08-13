# Carousel Post Template

Use this structure for every draft in `content/drafts/`. 6–8 slides.

## Grounding rule (read this first)

Every tool name, price, and feature claim in the draft MUST come from
`content/data/tools.json` (and `comparisons.json`/`stacks.json` where the
topic references one). Do not invent a price, a feature, or a tool that
isn't in that file. If a topic needs a fact that isn't in the data files,
write the slide without that specific number rather than guessing — never
state a price or feature you can't point to in the JSON.

## Affiliate rule (check this every time)

For every tool_id in the topic, look it up in `content/data/affiliate-links.json`.

- If `affiliate_url` is non-null for a tool in this post: the caption MUST
  include a visible disclosure sentence (not just a hashtag) — see
  `disclosure_rule` in that file — and the CTA slide/caption should point
  to "link in bio" rather than naming a raw URL (Instagram captions can't
  hold clickable links). Add `#affiliate` or `#ad` to the hashtags. Add or
  update that tool's line in `content/link-in-bio.md` so the bio-link page
  stays in sync with what the post references.
- If `affiliate_url` is null (whether or not a program exists), just mention
  the tool normally — no disclosure needed, no link-in-bio edit, no
  affiliate hashtag. Never state or imply a tool has an affiliate
  relationship that isn't reflected by a non-null `affiliate_url`.

## Structure

```
TOPIC: <one-line topic, from content/data/topics.json>
PILLAR: <Tool Spotlight | Head-to-Head | Shortlist | Mistake to Avoid | Free vs Paid>
TOOLS USED: <tool id(s) from tools.json this draft draws facts from, or "none" for a Mistake to Avoid post>
AFFILIATE: <tool id(s) with a non-null affiliate_url used in this post, or "none">

SLIDE 1 (hook):
<Bold question or claim that stops the scroll. No branding, no title.>

SLIDE 2..N-1 (body):
<One idea per slide. Short headline + 1-2 supporting lines. For tool
slides: tool name (from tools.json), the ONE thing it's good for
(from best_for/description), and the pricing note verbatim from
tools.json's "pricing" field if the slide mentions a price.>

SLIDE N (CTA):
<Save/Follow prompt tied back to the page's promise. If any tool in this
post has a live affiliate_url, this is "link in bio to get started with
[tool]" instead of a generic save/follow prompt.>

CAPTION:
<3-5 sentences expanding on the slides. End with a question to prompt
comments. No emojis in every sentence — use sparingly if at all. If any
tool in this post has a live affiliate_url, include the disclosure
sentence from affiliate-links.json's disclosure_rule.>

HASHTAGS:
<8-15 relevant hashtags, mix of broad (#smallbusiness) and specific
(#aiforbusiness, #notionai, etc.). Add #affiliate if this post uses an
affiliate link.>

IMAGE BRIEF:
<Short note per slide on visual treatment if it's not just text-on-background,
e.g. "Slide 3: side-by-side comparison layout">
```
