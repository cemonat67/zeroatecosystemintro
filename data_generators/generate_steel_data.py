"""
Zero@Steel Dummy Data Generator
Generates realistic steel production data for demo
"""

import random
import json
from datetime import datetime, timedelta
from typing import List, Dict

# Furnace configurations
FURNACES = [
    {"id": "FNC-001", "name": "Blast Furnace Alpha", "capacity": 2500, "type": "blast"},
    {"id": "FNC-002", "name": "Blast Furnace Beta", "capacity": 2500, "type": "blast"},
    {"id": "FNC-003", "name": "Electric Arc Gamma", "capacity": 150, "type": "electric"},
    {"id": "FNC-004", "name": "Electric Arc Delta", "capacity": 150, "type": "electric"},
]

# Steel grades
STEEL_GRADES = [
    "A36", "A572-50", "304 Stainless", "316 Stainless", 
    "4140 Alloy", "1045 Carbon", "A514 High Strength"
]

def generate_timestamp_series(days_back: int = 30, interval_minutes: int = 15) -> List[datetime]:
    """Generate timestamp series for the last N days"""
    end = datetime.now()
    start = end - timedelta(days=days_back)
    timestamps = []
    current = start
    while current <= end:
        timestamps.append(current)
        current += timedelta(minutes=interval_minutes)
    return timestamps

def generate_furnace_metrics(furnace: Dict, timestamp: datetime) -> Dict:
    """Generate realistic furnace metrics"""
    base_temp = 1600 if furnace["type"] == "blast" else 1800
    temp_variance = random.uniform(-50, 50)
    
    # Simulate daily patterns
    hour = timestamp.hour
    load_factor = 0.7 + 0.3 * (1 - abs(hour - 12) / 12)  # Peak at noon
    
    capacity = furnace["capacity"]
    current_load = capacity * load_factor * random.uniform(0.85, 0.98)
    
    # CO2 emissions (kg/hour)
    if furnace["type"] == "blast":
        co2_per_ton = random.uniform(1.8, 2.2)  # Blast furnace higher emissions
    else:
        co2_per_ton = random.uniform(0.4, 0.6)  # Electric arc lower emissions
    
    co2_emissions = current_load * co2_per_ton
    
    # Energy consumption (MWh)
    if furnace["type"] == "blast":
        energy_per_ton = random.uniform(0.5, 0.7)
    else:
        energy_per_ton = random.uniform(0.35, 0.45)
    
    energy = current_load * energy_per_ton
    
    return {
        "furnace_id": furnace["id"],
        "timestamp": timestamp.isoformat(),
        "temperature": round(base_temp + temp_variance, 1),
        "current_load_tons": round(current_load, 2),
        "capacity_utilization": round((current_load / capacity) * 100, 1),
        "co2_emissions_kg": round(co2_emissions, 2),
        "energy_consumption_mwh": round(energy, 3),
        "power_mw": round(energy * random.uniform(0.9, 1.1), 2),
        "status": random.choices(
            ["operational", "maintenance", "idle"],
            weights=[0.85, 0.10, 0.05]
        )[0]
    }

def generate_production_batches(num_batches: int = 100) -> List[Dict]:
    """Generate steel production batch records"""
    batches = []
    end_date = datetime.now()
    
    for i in range(num_batches):
        start_time = end_date - timedelta(days=random.randint(0, 30))
        duration_hours = random.uniform(4, 12)
        end_time = start_time + timedelta(hours=duration_hours)
        
        furnace = random.choice(FURNACES)
        tonnage = random.uniform(50, furnace["capacity"] * 0.4)
        
        batch = {
            "batch_id": f"BATCH-{start_time.strftime('%Y%m%d')}-{i:03d}",
            "furnace_id": furnace["id"],
            "steel_grade": random.choice(STEEL_GRADES),
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "tonnage": round(tonnage, 2),
            "target_tonnage": round(tonnage * random.uniform(0.95, 1.05), 2),
            "yield_percentage": round(random.uniform(94, 98), 2),
            "energy_used_mwh": round(tonnage * random.uniform(0.4, 0.7), 2),
            "co2_emitted_kg": round(tonnage * random.uniform(400, 2200), 2),
            "quality_grade": random.choices(
                ["A", "B", "C"],
                weights=[0.7, 0.25, 0.05]
            )[0],
            "notes": random.choice([
                "Standard production run",
                "High quality output",
                "Minor temperature fluctuations",
                "Optimal conditions",
                ""
            ])
        }
        batches.append(batch)
    
    return sorted(batches, key=lambda x: x["start_time"], reverse=True)

def generate_alerts(num_alerts: int = 50) -> List[Dict]:
    """Generate alert/alarm history"""
    alert_types = [
        {"type": "temperature_high", "severity": "warning", "message": "Temperature exceeded threshold"},
        {"type": "temperature_critical", "severity": "critical", "message": "Critical temperature - immediate action required"},
        {"type": "co2_spike", "severity": "warning", "message": "CO2 emissions spike detected"},
        {"type": "power_fluctuation", "severity": "info", "message": "Power consumption fluctuation"},
        {"type": "maintenance_due", "severity": "info", "message": "Scheduled maintenance approaching"},
        {"type": "capacity_low", "severity": "warning", "message": "Operating below optimal capacity"},
    ]
    
    alerts = []
    end_date = datetime.now()
    
    for i in range(num_alerts):
        alert_time = end_date - timedelta(hours=random.randint(0, 720))  # Last 30 days
        alert_info = random.choice(alert_types)
        furnace = random.choice(FURNACES)
        
        # Some alerts get resolved
        is_resolved = random.random() < 0.7
        
        alert = {
            "alert_id": f"ALERT-{alert_time.strftime('%Y%m%d%H%M')}-{i:03d}",
            "furnace_id": furnace["id"],
            "alert_type": alert_info["type"],
            "severity": alert_info["severity"],
            "message": f"{furnace['name']}: {alert_info['message']}",
            "timestamp": alert_time.isoformat(),
            "resolved": is_resolved,
            "resolved_at": (alert_time + timedelta(hours=random.uniform(0.5, 4))).isoformat() if is_resolved else None,
            "resolved_by": random.choice(["operator_1", "operator_2", "system_auto"]) if is_resolved else None
        }
        alerts.append(alert)
    
    return sorted(alerts, key=lambda x: x["timestamp"], reverse=True)

def generate_maintenance_records(num_records: int = 30) -> List[Dict]:
    """Generate maintenance history"""
    maintenance_types = [
        "Routine Inspection",
        "Refractory Repair",
        "Sensor Calibration",
        "Cooling System Maintenance",
        "Electrical System Check",
        "Safety System Test"
    ]
    
    records = []
    end_date = datetime.now()
    
    for i in range(num_records):
        maint_date = end_date - timedelta(days=random.randint(0, 180))
        duration_hours = random.uniform(2, 24)
        
        record = {
            "maintenance_id": f"MAINT-{maint_date.strftime('%Y%m%d')}-{i:03d}",
            "furnace_id": random.choice(FURNACES)["id"],
            "maintenance_type": random.choice(maintenance_types),
            "scheduled_date": maint_date.isoformat(),
            "completed_date": (maint_date + timedelta(hours=duration_hours)).isoformat(),
            "duration_hours": round(duration_hours, 1),
            "cost_usd": round(random.uniform(5000, 50000), 2),
            "technician": random.choice(["Tech-A", "Tech-B", "Tech-C", "External Contractor"]),
            "notes": random.choice([
                "All systems nominal",
                "Minor adjustments made",
                "Replaced worn components",
                "Preventive maintenance completed",
                "Emergency repair successful"
            ]),
            "next_maintenance_due": (maint_date + timedelta(days=random.randint(30, 90))).isoformat()
        }
        records.append(record)
    
    return sorted(records, key=lambda x: x["scheduled_date"], reverse=True)

def main():
    """Generate all steel data"""
    print("🏭 Generating Zero@Steel Demo Data...")
    
    # Generate time series data (last 30 days, 15-minute intervals)
    print("\n📊 Generating furnace metrics time series...")
    timestamps = generate_timestamp_series(days_back=30, interval_minutes=15)
    
    all_metrics = []
    for furnace in FURNACES:
        print(f"   - {furnace['name']}")
        for ts in timestamps:
            metrics = generate_furnace_metrics(furnace, ts)
            all_metrics.append(metrics)
    
    print(f"   ✅ Generated {len(all_metrics):,} metric records")
    
    # Generate production batches
    print("\n🔥 Generating production batches...")
    batches = generate_production_batches(100)
    print(f"   ✅ Generated {len(batches)} batches")
    
    # Generate alerts
    print("\n⚠️  Generating alerts...")
    alerts = generate_alerts(50)
    print(f"   ✅ Generated {len(alerts)} alerts")
    
    # Generate maintenance records
    print("\n🔧 Generating maintenance records...")
    maintenance = generate_maintenance_records(30)
    print(f"   ✅ Generated {len(maintenance)} maintenance records")
    
    # Save to JSON files
    print("\n💾 Saving to JSON files...")
    
    with open('steel_furnace_metrics.json', 'w') as f:
        json.dump(all_metrics, f, indent=2)
    print("   ✅ steel_furnace_metrics.json")
    
    with open('steel_production_batches.json', 'w') as f:
        json.dump(batches, f, indent=2)
    print("   ✅ steel_production_batches.json")
    
    with open('steel_alerts.json', 'w') as f:
        json.dump(alerts, f, indent=2)
    print("   ✅ steel_alerts.json")
    
    with open('steel_maintenance.json', 'w') as f:
        json.dump(maintenance, f, indent=2)
    print("   ✅ steel_maintenance.json")
    
    # Generate summary statistics
    total_production = sum(b["tonnage"] for b in batches)
    total_co2 = sum(b["co2_emitted_kg"] for b in batches)
    total_energy = sum(b["energy_used_mwh"] for b in batches)
    
    summary = {
        "total_batches": len(batches),
        "total_production_tons": round(total_production, 2),
        "total_co2_emissions_kg": round(total_co2, 2),
        "total_energy_consumption_mwh": round(total_energy, 2),
        "avg_co2_per_ton": round(total_co2 / total_production, 2),
        "avg_energy_per_ton": round(total_energy / total_production, 3),
        "active_furnaces": len(FURNACES),
        "date_range": f"{timestamps[0].date()} to {timestamps[-1].date()}"
    }
    
    with open('steel_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)
    print("   ✅ steel_summary.json")
    
    print("\n" + "="*60)
    print("📈 SUMMARY STATISTICS")
    print("="*60)
    for key, value in summary.items():
        print(f"{key:.<40} {value}")
    print("="*60)
    print("\n✅ All Zero@Steel demo data generated successfully!")
    print("📁 Files ready for Supabase import\n")

if __name__ == "__main__":
    main()
