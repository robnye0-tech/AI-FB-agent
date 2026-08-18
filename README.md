# Steadyline — Brand Launch Package v1.0

Done-for-you AI phone/text answering and booking for owner-operator local
service businesses (contractors, salons/spas, gyms/studios). A static
marketing site: no build step, no framework, no backend — matches the v1.0
brief's "simple one-page site + direct outreach" channel.

Full brand spec this build implements: [`docs/brand-launch-package.md`](docs/brand-launch-package.md).

## Structure

```
index.html              Homepage — promise, problem, how it works, CTA
offer.html               Core Offer — what's included, cost, expected results
book-a-call.html         Booking page (calendar embed placeholder)
for/contractors.html     Reserved nav slot — redirects to homepage
for/salons.html          Reserved nav slot — redirects to homepage
for/gyms.html             Reserved nav slot — redirects to homepage
results.html              Reserved nav slot — redirects to homepage
pricing.html               Reserved nav slot — redirects to book-a-call
resources.html              Reserved nav slot — redirects to homepage
404.html                 Not-found page
assets/css/styles.css    Full design system (colors, type, components)
assets/js/main.js        Mobile nav toggle only — no other JS
assets/img/              Brand mark + flat line icons (no stock imagery)
docs/brand-launch-package.md  Full transcribed brief (source of truth)
```

## Brand system

| Token | Hex | Use |
|---|---|---|
| Deep Navy | `#1B2A41` | Header, hero, footer, headings |
| Signal Orange | `#FF6B35` | CTAs, accents, icons |
| Warm White | `#F7F5F2` | Page background |
| Charcoal | `#2E2E2E` | Body text, footer background |

Headlines use **Archivo** (falls back to Inter), body text uses **Inter**,
both loaded from Google Fonts. Per the brief: navy/charcoal/white never
change — a new vertical page only swaps the one `--accent` custom property
in `assets/css/styles.css` (e.g. teal `#2A9D8F` for gyms), one accent color
per page, maximum.

No stock "AI robot" imagery is used anywhere — icons are flat, custom SVGs
(`assets/img/`). Swap in real photos of trucks, tools, salons, and gyms when
available; there's no photography in this v1.0 build to replace stock with.

## Before this goes live

1. **Booking embed** — `book-a-call.html` has a clearly marked placeholder
   (search for `TODO (launch)`) where a real Calendly/Cal.com/Acuity embed
   needs to go. The fallback `mailto:hello@steadyline.com` link should also
   be swapped for a real inbox once that domain/address exists.
2. **Deploy target** — every internal link and asset path is root-relative
   (`/index.html`, `/assets/...`), which assumes the site is served from a
   domain root (Netlify, Vercel, Cloudflare Pages, or a custom domain all
   work as-is). If deploying to a GitHub Pages *project* site
   (`user.github.io/repo/`), either add a custom domain or prefix every
   root-relative path with `/repo/`.
3. **Analytics/forms** — none wired up yet; add before running paid traffic.

## Reserved nav slots (v2.0)

Per the site architecture spec, `/for/contractors`, `/for/salons`,
`/for/gyms`, `/results`, and `/resources` exist as real files but redirect
to the homepage (`/pricing` redirects to `/book-a-call.html`, since pricing
isn't public yet). This reserves the URL/nav slot now so nothing 404s once
outreach starts, without publishing content that isn't ready. Replace the
redirect with real content in v2.0 — see the backlog in
[`docs/brand-launch-package.md`](docs/brand-launch-package.md).

## Local preview

No build step required — any static file server works:

```
python3 -m http.server 8000
# then open http://localhost:8000
```

## Launch checklist status

See the **Launch Checklist** section of
[`docs/brand-launch-package.md`](docs/brand-launch-package.md) for the full,
up-to-date checklist. Everything under "Brand Foundation" and "Website" is
done except wiring a real calendar into the booking page; "Go-To-Market"
(content calendar drafts, outreach list) is out of scope for this build —
it's a live-copywriting/outreach task, not a code task.
