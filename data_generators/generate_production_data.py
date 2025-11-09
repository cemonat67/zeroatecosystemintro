"""
Zero@Production (Textile DPP) Dummy Data Generator
Generates end-to-end textile production data
"""

import random
import json
from datetime import datetime, timedelta
from typing import List, Dict

# Production stages
STAGES = [
    {"id": 1, "name": "Fibre", "duration_hours": (12, 24), "co2_per_kg": 0.8},
    {"id": 2, "name": "Fabric", "duration_hours": (24, 48), "co2_per_kg": 1.2},
    {"id": 3, "name": "Chemicals & Dyes", "duration_hours": (4, 8), "co2_per_kg": 2.5},
    {"id": 4, "name": "Finishing", "duration_hours": (8, 16), "co2_per_kg": 1.5},
    {"id": 5, "name": "Garment", "duration_hours": (16, 32), "co2_per_kg": 0.5},
    {"id": 6, "name": "Packaging", "duration_hours": (2, 4), "co2_per_kg": 0.3},
    {"id": 7, "name": "Order Delivery", "duration_hours": (48, 120), "co2_per_kg": 0.4},
    {"id": 8, "name": "Employee Transport", "duration_hours": (1, 2), "co2_per_kg": 0.2},
]

# Fabric types
FABRIC_TYPES = [
    {"name": "Cotton Poplin", "price_per_kg": 8.5, "water_liters_per_kg": 10000},
    {"name": "Polyester Blend", "price_per_kg": 6.2, "water_liters_per_kg": 3000},
    {"name": "Denim", "price_per_kg": 9.8, "water_liters_per_kg": 8000},
    {"name": "Jersey Knit", "price_per_kg": 7.3, "water_liters_per_kg": 6000},
    {"name": "Organic Cotton", "price_per_kg": 12.5, "water_liters_per_kg": 7000},
    {"name": "Linen", "price_per_kg": 15.0, "water_liters_per_kg": 5000},
    {"name": "Silk Blend", "price_per_kg": 25.0, "water_liters_per_kg": 4000},
    {"name": "Bamboo Fabric", "price_per_kg": 11.0, "water_liters_per_kg": 2500},
]

# Garment types
GARMENT_TYPES = [
    "T-Shirt", "Polo Shirt", "Dress Shirt", "Blouse", 
    "Dress", "Pants", "Jeans", "Jacket", "Sweater"
]

# Suppliers
SUPPLIERS = [
    {"id": "SUP-001", "name": "Anadolu Tekstil", "country": "Turkey", "sustainability_score": 8.5},
    {"id": "SUP-002", "name": "Global Fibers Ltd", "country": "India", "sustainability_score": 7.2},
    {"id": "SUP-003", "name": "EcoThread Co", "country": "Bangladesh", "sustainability_score": 9.1},
    {"id": "SUP-004", "name": "Premium Fabrics", "country": "Italy", "sustainability_score": 8.9},
    {"id": "SUP-005", "name": "Green Textiles", "country": "Portugal", "sustainability_score": 9.3},
]

# Customers
CUSTOMERS = [
    {"id": "CUST-001", "name": "Zara", "country": "Spain", "tier": "A"},
    {"id": "CUST-002", "name": "H&M", "country": "Sweden", "tier": "A"},
    {"id": "CUST-003", "name": "Uniqlo", "country": "Japan", "tier": "A"},
    {"id": "CUST-004", "name": "Next", "country": "UK", "tier": "B"},
    {"id": "CUST-005", "name": "Mango", "country": "Spain", "tier": "B"},
    {"id": "CUST-006", "name": "LC Waikiki", "country": "Turkey", "tier": "B"},
]

def generate_orders(num_orders: int = 150) -> List[Dict]:
    """Generate production orders"""
    orders = []
    end_date = datetime.now()
    
    for i in range(num_orders):
        # Order date (last 90 days)
        order_date = end_date - timedelta(days=random.randint(0, 90))
        
        fabric = random.choice(FABRIC_TYPES)
        garment_type = random.choice(GARMENT_TYPES)
        customer = random.choice(CUSTOMERS)
        supplier = random.choice(SUPPLIERS)
        
        quantity = random.randint(500, 5000)
        kg_per_unit = random.uniform(0.3, 0.8)
        total_kg = quantity * kg_per_unit
        
        # Calculate total production time
        total_duration_hours = sum(random.uniform(*stage["duration_hours"]) for stage in STAGES)
        
        # Order status based on age
        days_old = (end_date - order_date).days
        if days_old < 7:
            status = random.choice(["in_progress", "planning"])
            current_stage = random.randint(1, 4)
        elif days_old < 30:
            status = random.choice(["in_progress", "completed"])
            current_stage = random.randint(4, 8) if status == "in_progress" else 8
        else:
            status = "completed"
            current_stage = 8
        
        # Calculate CO2 emissions
        total_co2 = sum(stage["co2_per_kg"] * total_kg for stage in STAGES)
        
        # Calculate water usage
        water_usage = fabric["water_liters_per_kg"] * total_kg
        
        order = {
            "order_id": f"ORD-{order_date.strftime('%Y%m')}-{i:04d}",
            "order_date": order_date.isoformat(),
            "customer_id": customer["id"],
            "customer_name": customer["name"],
            "garment_type": garment_type,
            "fabric_type": fabric["name"],
            "quantity": quantity,
            "weight_kg": round(total_kg, 2),
            "supplier_id": supplier["id"],
            "supplier_name": supplier["name"],
            "status": status,
            "current_stage": current_stage,
            "current_stage_name": STAGES[current_stage - 1]["name"],
            "progress_percentage": round((current_stage / len(STAGES)) * 100, 1),
            "estimated_completion": (order_date + timedelta(hours=total_duration_hours)).isoformat(),
            "total_co2_kg": round(total_co2, 2),
            "water_usage_liters": round(water_usage, 2),
            "energy_usage_kwh": round(total_kg * random.uniform(15, 25), 2),
            "total_cost_usd": round(total_kg * fabric["price_per_kg"] * random.uniform(1.5, 2.5), 2),
            "quality_score": round(random.uniform(85, 99), 1),
            "sustainability_score": round(random.uniform(70, 95), 1),
        }
        orders.append(order)
    
    return sorted(orders, key=lambda x: x["order_date"], reverse=True)

def generate_stage_tracking(orders: List[Dict]) -> List[Dict]:
    """Generate detailed stage tracking for each order"""
    tracking_records = []
    
    for order in orders:
        order_start = datetime.fromisoformat(order["order_date"])
        current_time = order_start
        
        # Generate records for each completed stage
        for stage_num in range(1, order["current_stage"] + 1):
            stage = STAGES[stage_num - 1]
            
            duration_hours = random.uniform(*stage["duration_hours"])
            stage_start = current_time
            stage_end = stage_start + timedelta(hours=duration_hours)
            
            stage_co2 = stage["co2_per_kg"] * order["weight_kg"]
            
            # Stage status
            if stage_num < order["current_stage"]:
                stage_status = "completed"
            elif stage_num == order["current_stage"] and order["status"] == "in_progress":
                stage_status = "in_progress"
            else:
                stage_status = "completed"
            
            record = {
                "tracking_id": f"{order['order_id']}-STG{stage_num}",
                "order_id": order["order_id"],
                "stage_id": stage["id"],
                "stage_name": stage["name"],
                "stage_status": stage_status,
                "start_time": stage_start.isoformat(),
                "end_time": stage_end.isoformat() if stage_status == "completed" else None,
                "duration_hours": round(duration_hours, 1),
                "co2_emissions_kg": round(stage_co2, 2),
                "energy_kwh": round(order["weight_kg"] * random.uniform(2, 4), 2),
                "water_liters": round(order["water_usage_liters"] * 0.15, 2),  # Distributed across stages
                "defect_rate": round(random.uniform(0, 3), 2),
                "operator": random.choice(["Operator-A", "Operator-B", "Operator-C", "Operator-D"]),
                "notes": random.choice([
                    "Normal operation",
                    "Slight delay due to machine calibration",
                    "High quality output",
                    "Completed ahead of schedule",
                    ""
                ])
            }
            tracking_records.append(record)
            
            current_time = stage_end
    
    return tracking_records

def generate_dpp_records(orders: List[Dict]) -> List[Dict]:
    """Generate Digital Product Passport records"""
    dpp_records = []
    
    for order in orders:
        if order["status"] == "completed":
            # Create DPP for completed orders
            for unit_num in range(min(5, order["quantity"])):  # Sample 5 units per order
                dpp = {
                    "dpp_id": f"DPP-{order['order_id']}-{unit_num:04d}",
                    "order_id": order["order_id"],
                    "product_type": order["garment_type"],
                    "fabric_type": order["fabric_type"],
                    "manufacturing_date": order["order_date"],
                    "completion_date": order["estimated_completion"],
                    "total_co2_kg": round(order["total_co2_kg"] / order["quantity"], 3),
                    "water_liters": round(order["water_usage_liters"] / order["quantity"], 2),
                    "energy_kwh": round(order["energy_usage_kwh"] / order["quantity"], 2),
                    "materials": json.dumps([
                        {"type": order["fabric_type"], "weight_kg": round(order["weight_kg"] / order["quantity"], 3)},
                        {"type": "Thread", "weight_kg": 0.05},
                        {"type": "Buttons/Accessories", "weight_kg": 0.02}
                    ]),
                    "certifications": json.dumps(random.sample([
                        "GOTS", "OEKO-TEX", "Fair Trade", "Organic", "Recycled", "Carbon Neutral"
                    ], k=random.randint(2, 4))),
                    "supplier_info": json.dumps({
                        "supplier_id": order["supplier_id"],
                        "supplier_name": order["supplier_name"],
                        "origin": random.choice(["Turkey", "India", "Bangladesh", "Portugal"])
                    }),
                    "recycling_info": "100% recyclable. Return to authorized collection points.",
                    "care_instructions": "Machine wash cold. Tumble dry low. Do not bleach.",
                    "qr_code": f"QR-{order['order_id']}-{unit_num:04d}",
                    "blockchain_hash": f"0x{random.randbytes(32).hex()}",
                }
                dpp_records.append(dpp)
    
    return dpp_records

def generate_quality_checks(orders: List[Dict]) -> List[Dict]:
    """Generate quality inspection records"""
    quality_records = []
    
    for order in orders:
        # Quality checks at key stages
        check_stages = [2, 4, 5, 6]  # Fabric, Finishing, Garment, Packaging
        
        for stage_id in check_stages:
            if stage_id <= order["current_stage"]:
                stage = STAGES[stage_id - 1]
                
                # Inspection date
                check_date = datetime.fromisoformat(order["order_date"]) + timedelta(
                    hours=sum(random.uniform(*STAGES[i]["duration_hours"]) for i in range(stage_id))
                )
                
                passed = random.random() < 0.92  # 92% pass rate
                
                record = {
                    "check_id": f"QC-{order['order_id']}-STG{stage_id}",
                    "order_id": order["order_id"],
                    "stage_id": stage_id,
                    "stage_name": stage["name"],
                    "check_date": check_date.isoformat(),
                    "inspector": random.choice(["Inspector-1", "Inspector-2", "Inspector-3"]),
                    "result": "pass" if passed else "fail",
                    "defects_found": 0 if passed else random.randint(1, 5),
                    "defect_types": json.dumps(
                        random.sample(["stitching", "color mismatch", "sizing", "fabric defect", "stains"], 
                                    k=random.randint(1, 3))
                    ) if not passed else json.dumps([]),
                    "corrective_action": random.choice([
                        "Rework required",
                        "Minor adjustment",
                        "Reprocess",
                        "Material replacement"
                    ]) if not passed else None,
                    "notes": "All parameters within specification" if passed else "Quality issues detected"
                }
                quality_records.append(record)
    
    return quality_records

def main():
    """Generate all textile production data"""
    print("👕 Generating Zero@Production (Textile DPP) Demo Data...")
    
    # Generate orders
    print("\n📦 Generating production orders...")
    orders = generate_orders(150)
    print(f"   ✅ Generated {len(orders)} orders")
    
    # Generate stage tracking
    print("\n🔄 Generating stage tracking records...")
    tracking = generate_stage_tracking(orders)
    print(f"   ✅ Generated {len(tracking)} tracking records")
    
    # Generate DPP records
    print("\n📋 Generating Digital Product Passports...")
    dpp_records = generate_dpp_records(orders)
    print(f"   ✅ Generated {len(dpp_records)} DPP records")
    
    # Generate quality checks
    print("\n✓ Generating quality inspection records...")
    quality_checks = generate_quality_checks(orders)
    print(f"   ✅ Generated {len(quality_checks)} quality checks")
    
    # Save to JSON files
    print("\n💾 Saving to JSON files...")
    
    with open('production_orders.json', 'w') as f:
        json.dump(orders, f, indent=2)
    print("   ✅ production_orders.json")
    
    with open('production_stage_tracking.json', 'w') as f:
        json.dump(tracking, f, indent=2)
    print("   ✅ production_stage_tracking.json")
    
    with open('production_dpp.json', 'w') as f:
        json.dump(dpp_records, f, indent=2)
    print("   ✅ production_dpp.json")
    
    with open('production_quality.json', 'w') as f:
        json.dump(quality_checks, f, indent=2)
    print("   ✅ production_quality.json")
    
    # Generate summary
    completed_orders = [o for o in orders if o["status"] == "completed"]
    in_progress = [o for o in orders if o["status"] == "in_progress"]
    
    total_co2 = sum(o["total_co2_kg"] for o in completed_orders)
    total_water = sum(o["water_usage_liters"] for o in completed_orders)
    total_quantity = sum(o["quantity"] for o in completed_orders)
    
    summary = {
        "total_orders": len(orders),
        "completed_orders": len(completed_orders),
        "in_progress_orders": len(in_progress),
        "total_garments_produced": total_quantity,
        "total_co2_emissions_kg": round(total_co2, 2),
        "total_water_usage_liters": round(total_water, 2),
        "avg_co2_per_garment": round(total_co2 / total_quantity, 3) if total_quantity > 0 else 0,
        "avg_water_per_garment": round(total_water / total_quantity, 2) if total_quantity > 0 else 0,
        "dpp_records_issued": len(dpp_records),
        "quality_pass_rate": round(len([q for q in quality_checks if q["result"] == "pass"]) / len(quality_checks) * 100, 1)
    }
    
    with open('production_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)
    print("   ✅ production_summary.json")
    
    print("\n" + "="*60)
    print("📈 SUMMARY STATISTICS")
    print("="*60)
    for key, value in summary.items():
        print(f"{key:.<40} {value}")
    print("="*60)
    print("\n✅ All Zero@Production demo data generated successfully!")
    print("📁 Files ready for Supabase import\n")

if __name__ == "__main__":
    main()
