create extension if not exists pgcrypto;

create table if not exists public.site_users (
  id uuid primary key default gen_random_uuid(),
  username text not null unique,
  email text not null unique,
  email_is_generated boolean not null default false,
  site_origin text not null default 'unknown',
  registered_site text,
  source_site text,
  password_salt text not null,
  password_hash text not null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  last_login_at timestamptz
);

create unique index if not exists site_users_username_lower_key
  on public.site_users (lower(username));

alter table public.site_users
  add column if not exists site_origin text not null default 'unknown',
  add column if not exists registered_site text,
  add column if not exists source_site text;

create table if not exists public.user_entitlements (
  id uuid primary key default gen_random_uuid(),
  email text not null unique,
  site_origin text not null default 'unknown',
  source_site text,
  grant_source text,
  source_plan_code text,
  source_reference text,
  plan text not null default 'free',
  status text not null default 'inactive',
  lifetime boolean not null default false,
  paddle_customer_id text,
  paddle_subscription_id text,
  paddle_transaction_id text,
  paddle_last_event_id text,
  paddle_last_occurred_at timestamptz,
  current_period_end timestamptz,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

alter table public.user_entitlements
  add column if not exists site_origin text not null default 'unknown',
  add column if not exists source_site text,
  add column if not exists grant_source text,
  add column if not exists source_plan_code text,
  add column if not exists source_reference text,
  add column if not exists paddle_last_event_id text,
  add column if not exists paddle_last_occurred_at timestamptz;

create index if not exists user_entitlements_email_updated_at_idx
  on public.user_entitlements (email, updated_at desc);

create unique index if not exists user_entitlements_paddle_customer_id_key
  on public.user_entitlements (paddle_customer_id)
  where paddle_customer_id is not null and paddle_customer_id <> '';

create unique index if not exists user_entitlements_paddle_subscription_id_key
  on public.user_entitlements (paddle_subscription_id)
  where paddle_subscription_id is not null and paddle_subscription_id <> '';

create table if not exists public.report_purchases (
  id uuid primary key default gen_random_uuid(),
  email text not null,
  report_id text not null,
  source text not null default 'catalog',
  title text,
  status text not null default 'active',
  paddle_customer_id text,
  paddle_transaction_id text,
  purchased_at timestamptz not null default now(),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  unique (email, report_id, source)
);

create index if not exists report_purchases_email_updated_at_idx
  on public.report_purchases (email, updated_at desc);

create table if not exists public.usage_events (
  id uuid primary key default gen_random_uuid(),
  email text not null,
  site_origin text not null default 'unknown',
  event_type text not null,
  units integer not null default 1,
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

alter table public.usage_events
  add column if not exists site_origin text not null default 'unknown';

create index if not exists usage_events_email_created_at_idx
  on public.usage_events (email, created_at desc);

-- These tables are reached only through the Worker service-role client. Raw
-- SQL-created tables do not automatically inherit Dashboard RLS settings.
alter table public.site_users enable row level security;
alter table public.user_entitlements enable row level security;
alter table public.report_purchases enable row level security;
alter table public.usage_events enable row level security;

revoke all on table public.site_users from public, anon, authenticated;
revoke all on table public.user_entitlements from public, anon, authenticated;
revoke all on table public.report_purchases from public, anon, authenticated;
revoke all on table public.usage_events from public, anon, authenticated;

grant select, insert, update, delete on table public.site_users to service_role;
grant select, insert, update, delete on table public.user_entitlements to service_role;
grant select, insert, update, delete on table public.report_purchases to service_role;
grant select, insert, update, delete on table public.usage_events to service_role;
