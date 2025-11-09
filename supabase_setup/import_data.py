"""
Supabase Data Import Script
Imports all generated JSON data to Supabase
"""

import json
import os
from supabase import create_client, Client
from typing import List, Dict
import time

# Supabase credentials (you need to provide these)
SUPABASE_URL = os.getenv("SUPABASE_URL", "YOUR_SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY", "YOUR_SUPABASE_ANON_KEY")

# Initialize Supabase client
def init_supabase() -> Client:
    """Initialize Supabase client"""
    if SUPABASE_URL == "YOUR_SUPABASE_URL":
        print("⚠️  WARNING: Please set SUPABASE_URL and SUPABASE_KEY environment variables")
        print("   export SUPABASE_URL='your-project-url'")
        print("   export SUPABASE_KEY='your-anon-key'")
        return None
    
    return create_client(SUPABASE_URL, SUPABASE_KEY)

def batch_insert(supabase: Client, table_name: str, data: List[Dict], batch_size: int = 100):
    """Insert data in batches to avoid timeouts"""
    total = len(data)
    inserted = 0
    
    print(f"   Inserting {total} records into {table_name}...")
    
    for i in range(0, total, batch_size):
        batch = data[i:i + batch_size]
        try:
            result = supabase.table(table_name).insert(batch).execute()
            inserted += len(batch)
            print(f"   Progress: {inserted}/{total} ({(inserted/total)*100:.1f}%)")
            time.sleep(0.1)  # Rate limiting
        except Exception as e:
            print(f"   ❌ Error inserting batch {i//batch_size + 1}: {str(e)}")
            continue
    
    print(f"   ✅ Inserted {inserted}/{total} records")
    return inserted

def import_steel_data(supabase: Client, data_dir: str):
    """Import Zero@Steel data"""
    print("\n🏭 Importing Zero@Steel Data...")
    
    # Furnace metrics
    with open(f"{data_dir}/steel_furnace_metrics.json") as f:
        metrics = json.load(f)
    batch_insert(supabase, "steel_furnace_metrics", metrics, batch_size=500)
    
    # Production batches
    with open(f"{data_dir}/steel_production_batches.json") as f:
        batches = json.load(f)
    batch_insert(supabase, "steel_production_batches", batches)
    
    # Alerts
    with open(f"{data_dir}/steel_alerts.json") as f:
        alerts = json.load(f)
    batch_insert(supabase, "steel_alerts", alerts)
    
    # Maintenance
    with open(f"{data_dir}/steel_maintenance.json") as f:
        maintenance = json.load(f)
    batch_insert(supabase, "steel_maintenance_records", maintenance)
    
    print("✅ Zero@Steel data imported!")

def import_production_data(supabase: Client, data_dir: str):
    """Import Zero@Production data"""
    print("\n👕 Importing Zero@Production Data...")
    
    # Orders
    with open(f"{data_dir}/production_orders.json") as f:
        orders = json.load(f)
    batch_insert(supabase, "production_orders", orders)
    
    # Stage tracking
    with open(f"{data_dir}/production_stage_tracking.json") as f:
        tracking = json.load(f)
    batch_insert(supabase, "production_stage_tracking", tracking, batch_size=200)
    
    # DPP records
    with open(f"{data_dir}/production_dpp.json") as f:
        dpp = json.load(f)
    batch_insert(supabase, "production_dpp", dpp, batch_size=100)
    
    # Quality checks
    with open(f"{data_dir}/production_quality.json") as f:
        quality = json.load(f)
    batch_insert(supabase, "production_quality_checks", quality, batch_size=100)
    
    print("✅ Zero@Production data imported!")

def import_dryfood_data(supabase: Client, data_dir: str):
    """Import Zero@DryFood data"""
    print("\n🍎 Importing Zero@DryFood Data...")
    
    # Batches
    with open(f"{data_dir}/dryfood_batches.json") as f:
        batches = json.load(f)
    batch_insert(supabase, "dryfood_dehydration_batches", batches)
    
    # Temperature logs
    with open(f"{data_dir}/dryfood_logs.json") as f:
        logs = json.load(f)
    batch_insert(supabase, "dryfood_temperature_humidity_logs", logs, batch_size=200)
    
    # Waste impact
    with open(f"{data_dir}/dryfood_waste_impact.json") as f:
        impact = json.load(f)
    batch_insert(supabase, "dryfood_waste_impact_analysis", impact)
    
    print("✅ Zero@DryFood data imported!")

def import_design_data(supabase: Client, data_dir: str):
    """Import Zero@Design data"""
    print("\n🎨 Importing Zero@Design Data...")
    
    # Projects
    with open(f"{data_dir}/design_projects.json") as f:
        projects = json.load(f)
    batch_insert(supabase, "design_projects", projects)
    
    # Material alternatives
    with open(f"{data_dir}/design_material_alternatives.json") as f:
        alternatives = json.load(f)
    batch_insert(supabase, "design_material_alternatives", alternatives)
    
    # LCA reports
    with open(f"{data_dir}/design_lca_reports.json") as f:
        lca = json.load(f)
    batch_insert(supabase, "design_lifecycle_assessments", lca)
    
    print("✅ Zero@Design data imported!")

def main():
    """Main import function"""
    print("=" * 60)
    print("🚀 SUPABASE DATA IMPORT")
    print("=" * 60)
    
    # Initialize Supabase
    supabase = init_supabase()
    if not supabase:
        print("\n❌ Cannot proceed without Supabase credentials")
        print("\nTo set credentials:")
        print("  export SUPABASE_URL='https://your-project.supabase.co'")
        print("  export SUPABASE_KEY='your-anon-key'")
        return
    
    data_dir = "../data_generators/generated_data"
    
    try:
        # Import all modules
        import_steel_data(supabase, data_dir)
        import_production_data(supabase, data_dir)
        import_dryfood_data(supabase, data_dir)
        import_design_data(supabase, data_dir)
        
        print("\n" + "=" * 60)
        print("✅ ALL DATA IMPORTED SUCCESSFULLY!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Import failed: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
