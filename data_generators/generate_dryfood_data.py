"""
Zero@DryFood Dummy Data Generator
Generates dehydration process and food waste reduction data
"""

import random
import json
from datetime import datetime, timedelta
from typing import List, Dict

# Food types with their characteristics
FOOD_TYPES = [
    {
        "name": "Apple Slices",
        "category": "Fruit",
        "initial_moisture": 85,
        "target_moisture": 5,
        "price_per_kg_fresh": 2.5,
        "price_per_kg_dried": 15.0,
        "shelf_life_fresh_days": 14,
        "shelf_life_dried_days": 365
    },
    {
        "name": "Banana Chips",
        "category": "Fruit",
        "initial_moisture": 75,
        "target_moisture": 3,
        "price_per_kg_fresh": 1.8,
        "price_per_kg_dried": 12.0,
        "shelf_life_fresh_days": 7,
        "shelf_life_dried_days": 360
    },
    {
        "name": "Tomato",
        "category": "Vegetable",
        "initial_moisture": 94,
        "target_moisture": 10,
        "price_per_kg_fresh": 3.0,
        "price_per_kg_dried": 25.0,
        "shelf_life_fresh_days": 10,
        "shelf_life_dried_days": 540
    },
    {
        "name": "Carrot Pieces",
        "category": "Vegetable",
        "initial_moisture": 88,
        "target_moisture": 8,
        "price_per_kg_fresh": 1.5,
        "price_per_kg_dried": 10.0,
        "shelf_life_fresh_days": 21,
        "shelf_life_dried_days": 365
    },
    {
        "name": "Beef Jerky",
        "category": "Meat",
        "initial_moisture": 70,
        "target_moisture": 25,
        "price_per_kg_fresh": 15.0,
        "price_per_kg_dried": 45.0,
        "shelf_life_fresh_days": 3,
        "shelf_life_dried_days": 730
    },
    {
        "name": "Mushroom",
        "category": "Vegetable",
        "initial_moisture": 92,
        "target_moisture": 7,
        "price_per_kg_fresh": 8.0,
        "price_per_kg_dried": 60.0,
        "shelf_life_fresh_days": 7,
        "shelf_life_dried_days": 365
    },
    {
        "name": "Herbs Mix",
        "category": "Herbs",
        "initial_moisture": 80,
        "target_moisture": 5,
        "price_per_kg_fresh": 12.0,
        "price_per_kg_dried": 80.0,
        "shelf_life_fresh_days": 5,
        "shelf_life_dried_days": 540
    },
    {
        "name": "Mango Slices",
        "category": "Fruit",
        "initial_moisture": 83,
        "target_moisture": 10,
        "price_per_kg_fresh": 4.0,
        "price_per_kg_dried": 20.0,
        "shelf_life_fresh_days": 7,
        "shelf_life_dried_days": 365
    },
]

# Dehydrator equipment
DEHYDRATORS = [
    {"id": "DH-001", "name": "Solar Dehydrator A", "capacity_kg": 50, "energy_type": "solar"},
    {"id": "DH-002", "name": "Solar Dehydrator B", "capacity_kg": 50, "energy_type": "solar"},
    {"id": "DH-003", "name": "Electric Dehydrator A", "capacity_kg": 100, "energy_type": "electric"},
    {"id": "DH-004", "name": "Electric Dehydrator B", "capacity_kg": 100, "energy_type": "electric"},
    {"id": "DH-005", "name": "Gas Dehydrator", "capacity_kg": 150, "energy_type": "gas"},
]

def generate_dehydration_batches(num_batches: int = 100) -> List[Dict]:
    """Generate dehydration batch records"""
    batches = []
    end_date = datetime.now()
    
    for i in range(num_batches):
        # Batch start time (last 60 days)
        start_time = end_date - timedelta(days=random.randint(0, 60))
        
        food = random.choice(FOOD_TYPES)
        dehydrator = random.choice(DEHYDRATORS)
        
        # Batch size
        fresh_weight_kg = random.uniform(20, dehydrator["capacity_kg"])
        
        # Calculate dried weight
        moisture_loss = food["initial_moisture"] - food["target_moisture"]
        dried_weight_kg = fresh_weight_kg * (1 - moisture_loss / 100)
        
        # Dehydration duration (depends on moisture content and food type)
        duration_hours = random.uniform(6, 24) * (moisture_loss / 80)
        end_time = start_time + timedelta(hours=duration_hours)
        
        # Energy consumption
        if dehydrator["energy_type"] == "solar":
            energy_kwh = random.uniform(0.5, 2) * duration_hours
            co2_kg = energy_kwh * 0.05  # Very low emissions for solar
        elif dehydrator["energy_type"] == "electric":
            energy_kwh = random.uniform(3, 6) * duration_hours
            co2_kg = energy_kwh * 0.5  # Grid electricity
        else:  # gas
            energy_kwh = random.uniform(4, 8) * duration_hours
            co2_kg = energy_kwh * 0.4
        
        # Temperature profile
        target_temp = random.uniform(50, 70) if food["category"] != "Meat" else random.uniform(60, 75)
        
        # Quality metrics
        quality_score = random.uniform(85, 98)
        
        # Economic metrics
        fresh_value = fresh_weight_kg * food["price_per_kg_fresh"]
        dried_value = dried_weight_kg * food["price_per_kg_dried"]
        value_added = dried_value - fresh_value
        
        # Waste prevention calculation
        # Without dehydration, food would spoil
        days_saved = food["shelf_life_dried_days"] - food["shelf_life_fresh_days"]
        waste_prevented_kg = fresh_weight_kg * 0.3  # 30% would have been wasted
        
        batch = {
            "batch_id": f"DH-{start_time.strftime('%Y%m%d')}-{i:04d}",
            "dehydrator_id": dehydrator["id"],
            "dehydrator_name": dehydrator["name"],
            "food_type": food["name"],
            "food_category": food["category"],
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "duration_hours": round(duration_hours, 1),
            "fresh_weight_kg": round(fresh_weight_kg, 2),
            "dried_weight_kg": round(dried_weight_kg, 2),
            "weight_loss_percentage": round((1 - dried_weight_kg / fresh_weight_kg) * 100, 1),
            "initial_moisture_percent": food["initial_moisture"],
            "final_moisture_percent": round(food["target_moisture"] + random.uniform(-1, 1), 1),
            "target_temperature_c": round(target_temp, 1),
            "actual_temperature_c": round(target_temp + random.uniform(-2, 2), 1),
            "humidity_percent": round(random.uniform(5, 15), 1),
            "energy_consumption_kwh": round(energy_kwh, 2),
            "co2_emissions_kg": round(co2_kg, 2),
            "energy_type": dehydrator["energy_type"],
            "quality_score": round(quality_score, 1),
            "fresh_value_usd": round(fresh_value, 2),
            "dried_value_usd": round(dried_value, 2),
            "value_added_usd": round(value_added, 2),
            "waste_prevented_kg": round(waste_prevented_kg, 2),
            "shelf_life_extension_days": days_saved,
            "status": random.choices(
                ["completed", "in_progress", "quality_check"],
                weights=[0.85, 0.10, 0.05]
            )[0],
            "operator": random.choice(["Operator-A", "Operator-B", "Operator-C"]),
            "notes": random.choice([
                "Optimal conditions",
                "Slight temperature variation",
                "Extended drying time",
                "Perfect batch",
                "Minor quality issues addressed",
                ""
            ])
        }
        batches.append(batch)
    
    return sorted(batches, key=lambda x: x["start_time"], reverse=True)

def generate_temperature_humidity_logs(batches: List[Dict]) -> List[Dict]:
    """Generate detailed temperature and humidity logs for batches"""
    logs = []
    
    # Sample 20 batches for detailed logging
    sample_batches = random.sample(batches, min(20, len(batches)))
    
    for batch in sample_batches:
        start = datetime.fromisoformat(batch["start_time"])
        end = datetime.fromisoformat(batch["end_time"])
        duration_hours = (end - start).total_seconds() / 3600
        
        # Log every 30 minutes
        intervals = int(duration_hours * 2)
        
        for interval in range(intervals):
            log_time = start + timedelta(minutes=30 * interval)
            
            # Temperature gradually increases then stabilizes
            progress = interval / intervals
            if progress < 0.2:  # Heating phase
                temp = batch["target_temperature_c"] * progress / 0.2
            else:  # Stable phase with small variations
                temp = batch["target_temperature_c"] + random.uniform(-2, 2)
            
            # Humidity decreases over time
            initial_humidity = 60
            humidity = initial_humidity * (1 - progress) + random.uniform(5, 15) * progress
            
            log = {
                "log_id": f"{batch['batch_id']}-LOG-{interval:03d}",
                "batch_id": batch["batch_id"],
                "timestamp": log_time.isoformat(),
                "temperature_c": round(temp, 1),
                "humidity_percent": round(humidity, 1),
                "fan_speed_percent": round(50 + progress * 30 + random.uniform(-5, 5), 1),
                "power_kw": round(random.uniform(2, 5), 2),
            }
            logs.append(log)
    
    return logs

def generate_waste_impact_records(batches: List[Dict]) -> List[Dict]:
    """Generate waste prevention impact analysis"""
    impact_records = []
    
    for batch in batches:
        if batch["status"] == "completed":
            # Calculate comprehensive waste prevention metrics
            food = next(f for f in FOOD_TYPES if f["name"] == batch["food_type"])
            
            # Without dehydration scenario
            potential_waste = batch["fresh_weight_kg"] * 0.35  # 35% typical food waste
            waste_saved = batch["waste_prevented_kg"]
            
            # Carbon impact
            # Food waste in landfill produces methane
            landfill_co2_per_kg = 2.5  # kg CO2e per kg food waste
            co2_prevented = waste_saved * landfill_co2_per_kg
            
            # Net carbon impact (dehydration emissions - waste prevention savings)
            net_co2_impact = batch["co2_emissions_kg"] - co2_prevented
            
            impact = {
                "impact_id": f"IMP-{batch['batch_id']}",
                "batch_id": batch["batch_id"],
                "analysis_date": batch["end_time"],
                "fresh_weight_kg": batch["fresh_weight_kg"],
                "potential_food_waste_kg": round(potential_waste, 2),
                "waste_prevented_kg": round(waste_saved, 2),
                "waste_reduction_percentage": round((waste_saved / potential_waste) * 100, 1),
                "landfill_co2_prevented_kg": round(co2_prevented, 2),
                "dehydration_co2_kg": batch["co2_emissions_kg"],
                "net_co2_impact_kg": round(net_co2_impact, 2),
                "carbon_positive": net_co2_impact < 0,
                "economic_value_saved_usd": round(waste_saved * food["price_per_kg_fresh"], 2),
                "value_added_through_processing_usd": batch["value_added_usd"],
                "total_value_created_usd": round(batch["value_added_usd"] + (waste_saved * food["price_per_kg_fresh"]), 2),
                "shelf_life_extension_factor": round(food["shelf_life_dried_days"] / food["shelf_life_fresh_days"], 1),
                "storage_efficiency_improvement": "Requires 80% less storage space",
                "transportation_efficiency": "60% lighter - reduced transport emissions"
            }
            impact_records.append(impact)
    
    return impact_records

def main():
    """Generate all dry food data"""
    print("🍎 Generating Zero@DryFood Demo Data...")
    
    # Generate dehydration batches
    print("\n🌡️  Generating dehydration batches...")
    batches = generate_dehydration_batches(100)
    print(f"   ✅ Generated {len(batches)} batches")
    
    # Generate temperature/humidity logs
    print("\n📊 Generating temperature & humidity logs...")
    logs = generate_temperature_humidity_logs(batches)
    print(f"   ✅ Generated {len(logs)} log entries")
    
    # Generate waste impact records
    print("\n♻️  Generating waste prevention impact analysis...")
    impact_records = generate_waste_impact_records(batches)
    print(f"   ✅ Generated {len(impact_records)} impact records")
    
    # Save to JSON files
    print("\n💾 Saving to JSON files...")
    
    with open('dryfood_batches.json', 'w') as f:
        json.dump(batches, f, indent=2)
    print("   ✅ dryfood_batches.json")
    
    with open('dryfood_logs.json', 'w') as f:
        json.dump(logs, f, indent=2)
    print("   ✅ dryfood_logs.json")
    
    with open('dryfood_waste_impact.json', 'w') as f:
        json.dump(impact_records, f, indent=2)
    print("   ✅ dryfood_waste_impact.json")
    
    # Generate summary
    completed = [b for b in batches if b["status"] == "completed"]
    
    total_fresh = sum(b["fresh_weight_kg"] for b in completed)
    total_dried = sum(b["dried_weight_kg"] for b in completed)
    total_waste_prevented = sum(b["waste_prevented_kg"] for b in completed)
    total_value_added = sum(b["value_added_usd"] for b in completed)
    total_co2 = sum(b["co2_emissions_kg"] for b in completed)
    total_co2_prevented = sum(i["landfill_co2_prevented_kg"] for i in impact_records)
    
    summary = {
        "total_batches": len(batches),
        "completed_batches": len(completed),
        "total_fresh_weight_kg": round(total_fresh, 2),
        "total_dried_weight_kg": round(total_dried, 2),
        "avg_weight_loss_percent": round(((total_fresh - total_dried) / total_fresh) * 100, 1),
        "total_waste_prevented_kg": round(total_waste_prevented, 2),
        "total_value_added_usd": round(total_value_added, 2),
        "dehydration_co2_emissions_kg": round(total_co2, 2),
        "landfill_co2_prevented_kg": round(total_co2_prevented, 2),
        "net_co2_impact_kg": round(total_co2 - total_co2_prevented, 2),
        "carbon_positive": (total_co2 - total_co2_prevented) < 0,
        "avg_shelf_life_extension_days": round(sum(b["shelf_life_extension_days"] for b in completed) / len(completed), 0),
        "food_categories_processed": len(set(b["food_category"] for b in batches)),
    }
    
    with open('dryfood_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)
    print("   ✅ dryfood_summary.json")
    
    print("\n" + "="*60)
    print("📈 SUMMARY STATISTICS")
    print("="*60)
    for key, value in summary.items():
        print(f"{key:.<40} {value}")
    print("="*60)
    print("\n✅ All Zero@DryFood demo data generated successfully!")
    print("📁 Files ready for Supabase import\n")

if __name__ == "__main__":
    main()
