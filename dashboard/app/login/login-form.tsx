"use client";

import { useActionState } from "react";
import { useSearchParams } from "next/navigation";
import Link from "next/link";
import { login, type LoginState } from "./actions";

export function LoginForm() {
  const searchParams = useSearchParams();
  const redirectTo = searchParams.get("redirectTo") || "/onboarding";
  const [state, formAction, pending] = useActionState<LoginState, FormData>(login, {
    error: null,
  });

  return (
    <div className="card">
      <h1>Log in</h1>
      <form action={formAction}>
        <input type="hidden" name="redirectTo" value={redirectTo} />
        {state?.error && <p className="error">{state.error}</p>}
        <div className="field">
          <label htmlFor="email">Email</label>
          <input id="email" name="email" type="email" required autoComplete="email" />
        </div>
        <div className="field">
          <label htmlFor="password">Password</label>
          <input
            id="password"
            name="password"
            type="password"
            required
            autoComplete="current-password"
          />
        </div>
        <button className="btn" type="submit" disabled={pending}>
          {pending ? "Logging in…" : "Log in"}
        </button>
      </form>
      <p style={{ marginTop: 16, fontSize: 14 }}>
        Need an account? <Link href="/signup">Sign up</Link>
      </p>
    </div>
  );
}
