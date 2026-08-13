# The AI Shortlist

Content engine for **The AI Shortlist**, a faceless Instagram page helping
small business owners and solo entrepreneurs cut through the noise on AI
tools.

## How it works

1. **Brand & voice** — [`content/brand-guide.md`](content/brand-guide.md)
   defines the audience, tone, content pillars, and visual style.
2. **Topic backlog** — [`content/topics-backlog.md`](content/topics-backlog.md)
   is the rotating list of post ideas. Each automated run picks the next
   unchecked topic and checks it off.
3. **Template** — [`content/templates/carousel-template.md`](content/templates/carousel-template.md)
   is the structure every draft follows: hook slide, body slides, CTA
   slide, caption, hashtags, image brief.
4. **Daily draft generation** — two scheduled Cowork Routines run each day
   (10am and 5pm ET), each picking the next topic and writing a full
   carousel draft into `content/drafts/YYYY-MM-DD-am.md` or
   `content/drafts/YYYY-MM-DD-pm.md`, checking off the topic in the
   backlog, and committing/pushing the result.
5. **Review & post** — drafts land in `content/drafts/`. Nothing posts to
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

## Repo layout

```
content/
  brand-guide.md          Voice, audience, pillars, visual rules
  topics-backlog.md       Rotating list of post topics
  templates/
    carousel-template.md  Structure every draft follows
  drafts/
    YYYY-MM-DD.md          One generated draft per day
```
