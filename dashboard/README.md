# Steadyline Dashboard

The authenticated web app businesses use to sign up and configure their AI
phone/text answering service. Separate from the static marketing site at the
repo root — this is a Next.js (App Router) app with its own deploy pipeline
so a problem here can never break the marketing site.

Currently implemented (Phase 1 of the product build — see
`docs/brand-launch-package.md` in the repo root for the marketing brief):

- Business owner signup/login (Supabase Auth, email + password)
- A `businesses` table (Postgres, Row Level Security so each owner only sees
  their own row)
- An onboarding page: collects business name/industry/timezone, then shows a
  placeholder checklist for the steps that aren't built yet (calendar
  connection, phone number, AI configuration)

Not yet built: calendar connections (Google Calendar / Cal.com), phone
number provisioning (Twilio), voice AI (Vapi), SMS AI, Stripe subscription
sync. Those land in later phases.

## Setup

1. Create a free [Supabase](https://supabase.com) project.
2. In the Supabase SQL editor, run the migration in
   `supabase/migrations/0001_create_businesses.sql` (or use the Supabase CLI:
   `supabase link` then `supabase db push` from this directory).
3. Copy `.env.example` to `.env.local` and fill in the values from
   **Project Settings → API** in the Supabase dashboard:
   - `NEXT_PUBLIC_SUPABASE_URL`
   - `NEXT_PUBLIC_SUPABASE_ANON_KEY`
   - `SUPABASE_SERVICE_ROLE_KEY` (keep this secret — server-only, bypasses RLS)
   - `NEXT_PUBLIC_SITE_URL` (`http://localhost:3000` for local dev)
4. By default Supabase requires email confirmation before login works — for
   local testing you can disable that under **Authentication → Providers →
   Email → Confirm email** in the Supabase dashboard, or click the
   confirmation link Supabase emails to the signup address.

## Local development

```bash
npm install
npm run dev       # http://localhost:3000
npm run lint
npm run typecheck
npm run build      # production build
```

## Deploying

Deploy this directory as its **own** Vercel project (Root Directory =
`dashboard` in the Vercel project settings), separate from wherever the
static marketing site is hosted. Set the same environment variables from
`.env.example` in the Vercel project's settings, using
`NEXT_PUBLIC_SITE_URL=https://<your-dashboard-domain>`.

## Project structure

```
app/
  page.tsx                 Redirects to /login or /onboarding based on auth
  login/                   Login form + server action
  signup/                  Signup form + server action
  auth/callback/route.ts   Exchanges Supabase's email-confirmation code for a session
  onboarding/              Business info form, then the onboarding step checklist
lib/supabase/
  client.ts                Browser Supabase client
  server.ts                Server Component / Server Action / Route Handler client (RLS-respecting)
  admin.ts                 Service-role client for privileged server-only code (webhooks) — never import client-side
  middleware.ts             Session-refresh helper used by proxy.ts
proxy.ts                    Next.js request proxy (formerly "middleware"): refreshes the auth session cookie and gates /onboarding and /dashboard behind login
supabase/migrations/         SQL migrations, run manually or via the Supabase CLI
```
