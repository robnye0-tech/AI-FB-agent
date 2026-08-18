"use client";

import { useActionState } from "react";
import { createBusiness, type CreateBusinessState } from "./actions";

export function BusinessForm() {
  const [state, formAction, pending] = useActionState<CreateBusinessState, FormData>(
    createBusiness,
    { error: null },
  );

  return (
    <div className="card">
      <h2 style={{ marginTop: 0 }}>Tell us about your business</h2>
      <form action={formAction}>
        {state?.error && <p className="error">{state.error}</p>}
        <div className="field">
          <label htmlFor="name">Business name</label>
          <input id="name" name="name" type="text" required />
        </div>
        <div className="field">
          <label htmlFor="industry">Industry</label>
          <select id="industry" name="industry" required defaultValue="">
            <option value="" disabled>
              Choose one
            </option>
            <option value="contractor">Contractor</option>
            <option value="salon">Salon / Spa</option>
            <option value="gym">Gym / Studio</option>
            <option value="other">Other</option>
          </select>
        </div>
        <div className="field">
          <label htmlFor="timezone">Timezone</label>
          <select id="timezone" name="timezone" defaultValue="America/New_York">
            <option value="America/New_York">Eastern</option>
            <option value="America/Chicago">Central</option>
            <option value="America/Denver">Mountain</option>
            <option value="America/Los_Angeles">Pacific</option>
          </select>
        </div>
        <button className="btn" type="submit" disabled={pending}>
          {pending ? "Saving…" : "Continue"}
        </button>
      </form>
    </div>
  );
}
