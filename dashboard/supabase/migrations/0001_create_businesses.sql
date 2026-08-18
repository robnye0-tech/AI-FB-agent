-- Businesses: one row per subscribing business, owned by the Supabase auth
-- user who signed up. Later phases add calendar_connections, phone_numbers,
-- subscriptions, call_logs, conversation_state, and appointments, each
-- referencing businesses(id).

create table if not exists public.businesses (
  id uuid primary key default gen_random_uuid(),
  owner uuid not null references auth.users (id) on delete cascade,
  name text not null,
  industry text not null check (industry in ('contractor', 'salon', 'gym', 'other')),
  timezone text not null default 'America/New_York',
  business_hours jsonb not null default '{}'::jsonb,
  services jsonb not null default '[]'::jsonb,
  faqs jsonb not null default '[]'::jsonb,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index if not exists businesses_owner_idx on public.businesses (owner);

-- One business per owner for now; revisit if an owner ever needs multiple
-- businesses under one login.
create unique index if not exists businesses_owner_unique on public.businesses (owner);

alter table public.businesses enable row level security;

create policy "Owners can view their own business"
  on public.businesses for select
  using (auth.uid() = owner);

create policy "Owners can insert their own business"
  on public.businesses for insert
  with check (auth.uid() = owner);

create policy "Owners can update their own business"
  on public.businesses for update
  using (auth.uid() = owner)
  with check (auth.uid() = owner);

-- Keep updated_at current on every row change.
create or replace function public.set_updated_at()
returns trigger as $$
begin
  new.updated_at = now();
  return new;
end;
$$ language plpgsql;

create trigger businesses_set_updated_at
  before update on public.businesses
  for each row
  execute function public.set_updated_at();
