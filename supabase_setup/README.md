# Supabase Setup Guide

## 📋 Prerequisites

1. Supabase account (https://supabase.com)
2. Python 3.8+ with pip
3. Supabase Python client

## 🚀 Quick Setup (5 minutes)

### Step 1: Create Supabase Project

1. Go to https://supabase.com/dashboard
2. Click "New Project"
3. Fill in:
   - Name: `zero-ecosystem-demo`
   - Database Password: (save this!)
   - Region: Choose closest
4. Wait 2-3 minutes for provisioning

### Step 2: Get API Credentials

1. In your project dashboard, go to **Settings** → **API**
2. Copy these values:
   - **Project URL**: `https://xxxxxxxxxxxxx.supabase.co`
   - **anon public key**: `eyJhbGc...` (long string)

### Step 3: Install Dependencies

```bash
pip install supabase python-dotenv
```

Or with uv:
```bash
uv pip install supabase python-dotenv
```

### Step 4: Set Environment Variables

Create a `.env` file in this directory:

```bash
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key-here
```

Or export directly:
```bash
export SUPABASE_URL='https://your-project.supabase.co'
export SUPABASE_KEY='your-anon-key'
```

### Step 5: Run SQL Schemas

In Supabase Dashboard → **SQL Editor**, run each schema file:

1. `../data_generators/zero_steel_schema.sql`
2. `../data_generators/zero_production_schema.sql`
3. `../data_generators/zero_dryfood_schema.sql`
4. `../data_generators/zero_design_schema.sql`

**Copy-paste each file content and click "Run"**

### Step 6: Import Data

```bash
python import_data.py
```

This will import all demo data (may take 5-10 minutes).

## 📊 Verify Import

After import, check in Supabase:

1. Go to **Table Editor**
2. Check record counts:
   - `steel_furnace_metrics`: ~11,524 records
   - `steel_production_batches`: 100 records
   - `production_orders`: 150 records
   - `production_dpp`: 610 records
   - `dryfood_dehydration_batches`: 100 records
   - `design_projects`: 50 records

## 🔧 Troubleshooting

### "Cannot connect to Supabase"
- Check URL format: must start with `https://`
- Verify anon key is correct (it's very long)
- Check project is not paused

### "Rate limit exceeded"
- Script has built-in delays
- If still failing, increase batch_size delay in `import_data.py`

### "Table does not exist"
- Make sure all 4 SQL schemas are run first
- Check for errors in SQL Editor

## 🎯 Next Steps

After successful import:

1. ✅ Test API access:
```bash
curl "https://your-project.supabase.co/rest/v1/steel_furnace_metrics?select=*&limit=5" \
  -H "apikey: your-anon-key" \
  -H "Authorization: Bearer your-anon-key"
```

2. ✅ Update frontend to use your Supabase URL
3. ✅ Test demo pages

## 📝 Frontend Configuration

In your HTML files, update Supabase config:

```javascript
const SUPABASE_URL = 'https://your-project.supabase.co';
const SUPABASE_ANON_KEY = 'your-anon-key';

const supabase = window.supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
```

## 🔒 Security Notes

- ✅ `anon` key is safe for frontend (read-only by default)
- ❌ Never commit `.env` file to git
- ✅ Use Row Level Security (RLS) for production
- ✅ Keep service_role key secret (server-side only)
