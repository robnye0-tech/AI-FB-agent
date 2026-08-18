import { createClient as createSupabaseClient } from "@supabase/supabase-js";

// Privileged client for server-only code (e.g. Stripe/Twilio webhook handlers)
// that must write data on behalf of a business without a signed-in user
// session. Bypasses Row Level Security — never import this into anything
// that runs in the browser, and never pass user-supplied filters straight
// through without validating the target row belongs to the right business.
export function createAdminClient() {
  return createSupabaseClient(
    process.env.NEXT_PUBLIC_SUPABASE_URL!,
    process.env.SUPABASE_SERVICE_ROLE_KEY!,
    {
      auth: {
        autoRefreshToken: false,
        persistSession: false,
      },
    },
  );
}
