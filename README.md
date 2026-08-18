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
pricing.html              Pricing — 14-day free trial, $299/mo, Stripe checkout
book-a-call.html         Booking page (calendar embed placeholder)
for/contractors.html     Reserved nav slot — redirects to homepage
for/salons.html          Reserved nav slot — redirects to homepage
for/gyms.html             Reserved nav slot — redirects to homepage
results.html              Reserved nav slot — redirects to homepage
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

## Payments (Stripe Payment Links)

Pricing is live: **14-day free trial, then $299/month**, billed via a
**Stripe Payment Link** — a hosted Stripe checkout page, so this stays a
static site with zero backend and no secret keys anywhere in the repo.
Payment Links natively support a free-trial period on a recurring price,
which is exactly this offer.

The site currently ships with a placeholder in place of the real link:
`https://buy.stripe.com/REPLACE_WITH_YOUR_PAYMENT_LINK`. It appears in
exactly two places — both in `pricing.html` (the pricing-card CTA button and
the mobile floating CTA bar). Every other "Start Free Trial" button
site-wide (nav, hero, CTA bands) links to `/pricing.html` itself rather than
straight to checkout, so visitors see the price before they see a payment
form — replace only those two placeholder occurrences and the whole funnel
is wired up.

**To finish setup:**

1. Create a Stripe account at [dashboard.stripe.com/register](https://dashboard.stripe.com/register)
   if you don't have one (needs your real business/bank details — this step
   has to be done by you, not by this build).
2. In the Stripe Dashboard: **Product catalog → Add product**.
   - Name: "Steadyline Monthly Service"
   - Price: `$299.00 USD`, **Recurring**, billed **monthly**
3. Create a **Payment Link** for that price. In the Payment Link's options,
   turn on **"Free trial"** and set it to **14 days**.
4. Copy the generated URL (looks like `https://buy.stripe.com/xxxxxxxx`).
5. Replace both occurrences of
   `https://buy.stripe.com/REPLACE_WITH_YOUR_PAYMENT_LINK` in `pricing.html`
   with that real URL.
6. Optional but recommended: in the Payment Link's settings, set an
   **after-payment confirmation redirect** to a real page on your domain
   (once deployed) so customers land on your site instead of Stripe's
   generic confirmation screen.

If you'd rather have a fully custom checkout (dynamic pricing, capturing
extra fields, etc.) instead of Stripe's hosted page, that needs a small
serverless backend (Netlify/Vercel function) to create Checkout Sessions
server-side with your Stripe secret key — a bigger scope change than what's
built here. Payment Links were chosen because they need no backend and
match the "simple static site" architecture the rest of this build follows.

## Before this goes live

1. **Stripe Payment Link** — see "Payments" above; the two placeholder
   occurrences in `pricing.html` need your real link before this can take
   money.
2. **Booking embed** — `book-a-call.html` has a clearly marked placeholder
   (search for `TODO (launch)`) where a real Calendly/Cal.com/Acuity embed
   needs to go. The fallback `mailto:hello@steadyline.com` link should also
   be swapped for a real inbox once that domain/address exists.
3. **Deploy target** — every internal link and asset path is root-relative
   (`/index.html`, `/assets/...`), which assumes the site is served from a
   domain root (Netlify, Vercel, Cloudflare Pages, or a custom domain all
   work as-is). If deploying to a GitHub Pages *project* site
   (`user.github.io/repo/`), either add a custom domain or prefix every
   root-relative path with `/repo/`.
4. **Analytics/forms** — none wired up yet; add before running paid traffic.

## Reserved nav slots (v2.0)

Per the site architecture spec, `/for/contractors`, `/for/salons`,
`/for/gyms`, `/results`, and `/resources` exist as real files but redirect
to the homepage. This reserves the URL/nav slot now so nothing 404s once
outreach starts, without publishing content that isn't ready. Replace the
redirect with real content in v2.0 — see the backlog in
[`docs/brand-launch-package.md`](docs/brand-launch-package.md).

`/pricing` is no longer one of these — it's a real, live page (see
"Payments" above), which supersedes the original brief's "reserved for when
pricing goes public" note.

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
done except wiring the real Stripe Payment Link and a real calendar embed
into the booking page; "Go-To-Market" (content calendar drafts, outreach
list) is out of scope for this build — it's a live-copywriting/outreach
task, not a code task.
