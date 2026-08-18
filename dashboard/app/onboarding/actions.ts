"use server";

import { revalidatePath } from "next/cache";
import { redirect } from "next/navigation";
import { createClient } from "@/lib/supabase/server";

export type CreateBusinessState = { error: string | null };

export async function createBusiness(
  _prevState: CreateBusinessState,
  formData: FormData,
): Promise<CreateBusinessState> {
  const name = String(formData.get("name") || "").trim();
  const industry = String(formData.get("industry") || "");
  const timezone = String(formData.get("timezone") || "America/New_York");

  if (!name) {
    return { error: "Business name is required." };
  }
  if (!["contractor", "salon", "gym", "other"].includes(industry)) {
    return { error: "Please choose an industry." };
  }

  const supabase = await createClient();
  const {
    data: { user },
  } = await supabase.auth.getUser();

  if (!user) {
    redirect("/login");
  }

  const { error } = await supabase.from("businesses").insert({
    owner: user.id,
    name,
    industry,
    timezone,
  });

  if (error) {
    return { error: error.message };
  }

  revalidatePath("/onboarding");
  return { error: null };
}

export async function logout() {
  const supabase = await createClient();
  await supabase.auth.signOut();
  redirect("/login");
}
