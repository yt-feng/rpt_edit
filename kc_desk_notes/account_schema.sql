create extension if not exists pgcrypto;

create table if not exists public.site_users (
  id uuid primary key default gen_random_uuid(),
  username text not null unique,
  email text not null unique,
  email_is_generated boolean not null default false,
  password_salt text not null,
  password_hash text not null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  last_login_at timestamptz
);

create unique index if not exists site_users_username_lower_key
  on public.site_users (lower(username));

create table if not exists public.user_entitlements (
  id uuid primary key default gen_random_uuid(),
  email text not null unique,
  plan text not null default 'free',
  status text not null default 'inactive',
  lifetime boolean not null default false,
  paddle_customer_id text,
  paddle_subscription_id text,
  paddle_transaction_id text,
  current_period_end timestamptz,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now()
);

create index if not exists user_entitlements_email_updated_at_idx
  on public.user_entitlements (email, updated_at desc);

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
  event_type text not null,
  units integer not null default 1,
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now()
);

create index if not exists usage_events_email_created_at_idx
  on public.usage_events (email, created_at desc);
