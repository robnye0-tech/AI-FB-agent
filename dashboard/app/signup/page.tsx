"use client";

import { useActionState } from "react";
import Link from "next/link";
import { signup, type SignupState } from "./actions";

export default function SignupPage() {
  const [state, formAction, pending] = useActionState<SignupState, FormData>(signup, {
    error: null,
  });

  if (state?.confirmEmailSent) {
    return (
      <main className="page">
        <div className="card">
          <h1>Check your email</h1>
          <p>
            We sent a confirmation link. Click it to finish creating your
            account, then come back and log in.
          </p>
        </div>
      </main>
    );
  }

  return (
    <main className="page">
      <div className="card">
        <h1>Create your Steadyline account</h1>
        <form action={formAction}>
          {state?.error && <p className="error">{state.error}</p>}
          <div className="field">
            <label htmlFor="email">Work email</label>
            <input id="email" name="email" type="email" required autoComplete="email" />
          </div>
          <div className="field">
            <label htmlFor="password">Password</label>
            <input
              id="password"
              name="password"
              type="password"
              required
              minLength={8}
              autoComplete="new-password"
            />
          </div>
          <button className="btn" type="submit" disabled={pending}>
            {pending ? "Creating account…" : "Create account"}
          </button>
        </form>
        <p style={{ marginTop: 16, fontSize: 14 }}>
          Already have an account? <Link href="/login">Log in</Link>
        </p>
      </div>
    </main>
  );
}
