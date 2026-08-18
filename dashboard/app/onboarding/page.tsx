import { redirect } from "next/navigation";
import { createClient } from "@/lib/supabase/server";
import { BusinessForm } from "./business-form";
import { logout } from "./actions";

export default async function OnboardingPage() {
  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();

  if (!user) {
    redirect("/login");
  }

  const { data: business } = await supabase
    .from("businesses")
    .select("id, name, industry")
    .eq("owner", user.id)
    .maybeSingle();

  return (
    <main className="page" style={{ maxWidth: 560 }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center" }}>
        <h1>Get set up</h1>
        <form action={logout}>
          <button className="btn" style={{ background: "transparent", color: "var(--charcoal)", border: "1px solid #ccc" }} type="submit">
            Log out
          </button>
        </form>
      </div>

      {!business ? (
        <BusinessForm />
      ) : (
        <div className="card">
          <p>
            <strong>{business.name}</strong> is set up. Here&apos;s what&apos;s next:
          </p>
          <ul className="step-list">
            <li className="done">✓ Business info</li>
            <li className="disabled">Connect your calendar (coming soon)</li>
            <li className="disabled">Connect your phone number (coming soon)</li>
            <li className="disabled">Configure your AI assistant (coming soon)</li>
          </ul>
          <p style={{ fontSize: 14, opacity: 0.8 }}>
            These steps unlock as we finish wiring calendar, phone, and AI
            integrations — you&apos;ll get an update here as each one goes live.
          </p>
        </div>
      )}
    </main>
  );
}
