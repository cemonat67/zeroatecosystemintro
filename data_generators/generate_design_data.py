"""
Zero@Design Dummy Data Generator
Multi-industry design carbon tracking system
"""

import random
import json
from datetime import datetime, timedelta
from typing import List, Dict

# Design industries
INDUSTRIES = ["Textile", "Industrial", "Product", "Packaging"]

# Material library with carbon footprint
MATERIALS = [
    # Textile materials
    {"name": "Organic Cotton", "category": "Textile", "co2_kg_per_kg": 1.8, "price_per_kg": 12.0, "recyclable": True, "renewable": True},
    {"name": "Recycled Polyester", "category": "Textile", "co2_kg_per_kg": 3.2, "price_per_kg": 8.0, "recyclable": True, "renewable": False},
    {"name": "Bamboo Fiber", "category": "Textile", "co2_kg_per_kg": 1.2, "price_per_kg": 10.0, "recyclable": True, "renewable": True},
    {"name": "Linen", "category": "Textile", "co2_kg_per_kg": 1.5, "price_per_kg": 15.0, "recyclable": True, "renewable": True},
    {"name": "Virgin Polyester", "category": "Textile", "co2_kg_per_kg": 6.4, "price_per_kg": 5.0, "recyclable": False, "renewable": False},
    
    # Industrial materials
    {"name": "Recycled Steel", "category": "Industrial", "co2_kg_per_kg": 0.8, "price_per_kg": 1.5, "recyclable": True, "renewable": False},
    {"name": "Virgin Steel", "category": "Industrial", "co2_kg_per_kg": 2.1, "price_per_kg": 1.2, "recyclable": True, "renewable": False},
    {"name": "Aluminum Recycled", "category": "Industrial", "co2_kg_per_kg": 1.2, "price_per_kg": 2.5, "recyclable": True, "renewable": False},
    {"name": "Aluminum Virgin", "category": "Industrial", "co2_kg_per_kg": 8.5, "price_per_kg": 2.8, "recyclable": True, "renewable": False},
    {"name": "Cast Iron", "category": "Industrial", "co2_kg_per_kg": 1.9, "price_per_kg": 0.8, "recyclable": True, "renewable": False},
    
    # Product materials
    {"name": "ABS Plastic", "category": "Product", "co2_kg_per_kg": 3.5, "price_per_kg": 3.2, "recyclable": True, "renewable": False},
    {"name": "Bio-plastic (PLA)", "category": "Product", "co2_kg_per_kg": 1.8, "price_per_kg": 4.5, "recyclable": True, "renewable": True},
    {"name": "Wood (Sustainable)", "category": "Product", "co2_kg_per_kg": 0.5, "price_per_kg": 2.0, "recyclable": True, "renewable": True},
    {"name": "Glass", "category": "Product", "co2_kg_per_kg": 0.9, "price_per_kg": 1.5, "recyclable": True, "renewable": False},
    {"name": "Ceramic", "category": "Product", "co2_kg_per_kg": 1.2, "price_per_kg": 3.0, "recyclable": False, "renewable": False},
    
    # Packaging materials
    {"name": "Recycled Cardboard", "category": "Packaging", "co2_kg_per_kg": 0.5, "price_per_kg": 0.8, "recyclable": True, "renewable": True},
    {"name": "Virgin Cardboard", "category": "Packaging", "co2_kg_per_kg": 1.2, "price_per_kg": 0.6, "recyclable": True, "renewable": True},
    {"name": "Biodegradable Plastic", "category": "Packaging", "co2_kg_per_kg": 2.0, "price_per_kg": 3.5, "recyclable": True, "renewable": True},
    {"name": "Virgin Plastic Film", "category": "Packaging", "co2_kg_per_kg": 4.5, "price_per_kg": 2.0, "recyclable": False, "renewable": False},
]

# Manufacturing processes
PROCESSES = [
    # Textile processes
    {"name": "Weaving", "industry": "Textile", "co2_kg_per_unit": 0.5, "duration_hours": 2, "energy_kwh_per_unit": 1.2},
    {"name": "Knitting", "industry": "Textile", "co2_kg_per_unit": 0.4, "duration_hours": 1.5, "energy_kwh_per_unit": 1.0},
    {"name": "Dyeing", "industry": "Textile", "co2_kg_per_unit": 1.5, "duration_hours": 4, "energy_kwh_per_unit": 3.5},
    {"name": "Finishing", "industry": "Textile", "co2_kg_per_unit": 0.8, "duration_hours": 2, "energy_kwh_per_unit": 2.0},
    
    # Industrial processes
    {"name": "Casting", "industry": "Industrial", "co2_kg_per_unit": 5.0, "duration_hours": 8, "energy_kwh_per_unit": 50.0},
    {"name": "Machining", "industry": "Industrial", "co2_kg_per_unit": 2.0, "duration_hours": 4, "energy_kwh_per_unit": 15.0},
    {"name": "Welding", "industry": "Industrial", "co2_kg_per_unit": 1.5, "duration_hours": 3, "energy_kwh_per_unit": 8.0},
    {"name": "Surface Treatment", "industry": "Industrial", "co2_kg_per_unit": 1.0, "duration_hours": 2, "energy_kwh_per_unit": 5.0},
    
    # Product processes
    {"name": "Injection Molding", "industry": "Product", "co2_kg_per_unit": 0.8, "duration_hours": 0.5, "energy_kwh_per_unit": 2.5},
    {"name": "3D Printing", "industry": "Product", "co2_kg_per_unit": 0.3, "duration_hours": 8, "energy_kwh_per_unit": 1.5},
    {"name": "Assembly", "industry": "Product", "co2_kg_per_unit": 0.2, "duration_hours": 1, "energy_kwh_per_unit": 0.5},
    {"name": "Quality Control", "industry": "Product", "co2_kg_per_unit": 0.1, "duration_hours": 0.5, "energy_kwh_per_unit": 0.3},
]

# Design companies/clients
COMPANIES = [
    {"name": "Nike", "industry": "Textile", "sustainability_target": 95},
    {"name": "Adidas", "industry": "Textile", "sustainability_target": 92},
    {"name": "H&M", "industry": "Textile", "sustainability_target": 88},
    {"name": "Siemens", "industry": "Industrial", "sustainability_target": 90},
    {"name": "ABB", "industry": "Industrial", "sustainability_target": 85},
    {"name": "Apple", "industry": "Product", "sustainability_target": 98},
    {"name": "Samsung", "industry": "Product", "sustainability_target": 93},
    {"name": "IKEA", "industry": "Product", "sustainability_target": 95},
    {"name": "Unilever", "industry": "Packaging", "sustainability_target": 90},
    {"name": "P&G", "industry": "Packaging", "sustainability_target": 88},
]

def generate_design_projects(num_projects: int = 50) -> List[Dict]:
    """Generate design projects across industries"""
    projects = []
    end_date = datetime.now()
    
    for i in range(num_projects):
        # Project start date (last 180 days)
        start_date = end_date - timedelta(days=random.randint(0, 180))
        
        company = random.choice(COMPANIES)
        industry = company["industry"]
        
        # Select materials appropriate for industry
        industry_materials = [m for m in MATERIALS if m["category"] == industry or m["category"] == "Packaging"]
        selected_materials = random.sample(industry_materials, k=random.randint(2, 4))
        
        # Select processes
        industry_processes = [p for p in PROCESSES if p["industry"] == industry]
        num_processes = min(random.randint(2, 4), len(industry_processes))
        selected_processes = random.sample(industry_processes, k=num_processes) if industry_processes else []
        
        # Project phase
        days_since_start = (end_date - start_date).days
        if days_since_start < 30:
            phase = random.choice(["concept", "design"])
            progress = random.uniform(10, 40)
        elif days_since_start < 60:
            phase = random.choice(["design", "prototyping"])
            progress = random.uniform(40, 70)
        elif days_since_start < 90:
            phase = random.choice(["prototyping", "testing"])
            progress = random.uniform(70, 90)
        else:
            phase = random.choice(["testing", "completed"])
            progress = random.uniform(90, 100)
        
        # Calculate total carbon footprint
        # Material carbon
        material_weights = {m["name"]: random.uniform(0.5, 5.0) for m in selected_materials}
        material_co2 = sum(m["co2_kg_per_kg"] * material_weights[m["name"]] for m in selected_materials)
        
        # Process carbon
        units_produced = random.randint(100, 5000)
        process_co2 = sum(p["co2_kg_per_unit"] * units_produced for p in selected_processes)
        
        # Transport carbon (estimated)
        transport_co2 = random.uniform(50, 200)
        
        # End-of-life carbon
        # Recycling reduces impact
        recyclable_weight = sum(material_weights[m["name"]] for m in selected_materials if m["recyclable"])
        total_weight = sum(material_weights.values())
        recyclability_factor = recyclable_weight / total_weight if total_weight > 0 else 0
        eol_co2 = total_weight * (0.5 * (1 - recyclability_factor))  # Lower if recyclable
        
        total_co2 = material_co2 + process_co2 + transport_co2 + eol_co2
        
        # Sustainability score
        sustainability_score = (
            (recyclability_factor * 30) +  # Recyclability
            (sum(1 for m in selected_materials if m["renewable"]) / len(selected_materials) * 20) +  # Renewable
            (max(0, 100 - total_co2) / 100 * 30) +  # Low carbon
            (random.uniform(15, 20))  # Other factors
        )
        
        # Cost calculation
        material_cost = sum(m["price_per_kg"] * material_weights[m["name"]] for m in selected_materials)
        labor_cost = sum(p["duration_hours"] * 50 * units_produced for p in selected_processes)  # $50/hour
        total_cost = material_cost * units_produced + labor_cost
        
        project = {
            "project_id": f"PRJ-{start_date.strftime('%Y%m')}-{i:04d}",
            "project_name": f"{industry} Design {random.choice(['Alpha', 'Beta', 'Gamma', 'Delta', 'Omega'])}",
            "client": company["name"],
            "industry": industry,
            "start_date": start_date.isoformat(),
            "target_completion": (start_date + timedelta(days=random.randint(90, 180))).isoformat(),
            "phase": phase,
            "progress_percentage": round(progress, 1),
            "materials_used": json.dumps([
                {"name": m["name"], "weight_kg": round(material_weights[m["name"]], 2)}
                for m in selected_materials
            ]),
            "processes_used": json.dumps([p["name"] for p in selected_processes]),
            "units_planned": units_produced,
            "material_co2_kg": round(material_co2, 2),
            "process_co2_kg": round(process_co2, 2),
            "transport_co2_kg": round(transport_co2, 2),
            "eol_co2_kg": round(eol_co2, 2),
            "total_co2_kg": round(total_co2, 2),
            "co2_per_unit": round(total_co2 / units_produced, 3),
            "sustainability_score": round(sustainability_score, 1),
            "recyclability_percentage": round(recyclability_factor * 100, 1),
            "renewable_content_percentage": round(sum(1 for m in selected_materials if m["renewable"]) / len(selected_materials) * 100, 1),
            "total_cost_usd": round(total_cost, 2),
            "cost_per_unit": round(total_cost / units_produced, 2),
            "designer": random.choice(["Designer-A", "Designer-B", "Designer-C", "Designer-D"]),
            "sustainability_target": company["sustainability_target"],
            "target_met": sustainability_score >= company["sustainability_target"],
            "notes": random.choice([
                "Optimizing material selection",
                "Exploring alternative processes",
                "Meeting all sustainability targets",
                "Cost-carbon balance analysis ongoing",
                "Prototype testing successful",
                ""
            ])
        }
        projects.append(project)
    
    return sorted(projects, key=lambda x: x["start_date"], reverse=True)

def generate_material_alternatives(projects: List[Dict]) -> List[Dict]:
    """Generate material alternative comparisons"""
    alternatives = []
    
    # For each project, generate alternative material scenarios
    for project in random.sample(projects, k=min(20, len(projects))):
        industry = project["industry"]
        industry_materials = [m for m in MATERIALS if m["category"] == industry]
        
        # Current materials
        current_materials = json.loads(project["materials_used"])
        
        # Generate 2-3 alternatives
        for alt_num in range(random.randint(2, 3)):
            alt_materials = random.sample(industry_materials, k=len(current_materials))
            
            # Calculate alternative scenario metrics
            alt_co2 = sum(
                m["co2_kg_per_kg"] * cm["weight_kg"]
                for m, cm in zip(alt_materials, current_materials)
            )
            
            alt_cost = sum(
                m["price_per_kg"] * cm["weight_kg"] * project["units_planned"]
                for m, cm in zip(alt_materials, current_materials)
            )
            
            alt_recyclability = sum(1 for m in alt_materials if m["recyclable"]) / len(alt_materials)
            
            co2_difference = alt_co2 - project["material_co2_kg"]
            cost_difference = alt_cost - (project["total_cost_usd"] * 0.4)  # Assuming materials are 40% of cost
            
            alternative = {
                "alternative_id": f"{project['project_id']}-ALT-{alt_num}",
                "project_id": project["project_id"],
                "scenario_name": f"Alternative {alt_num + 1}",
                "materials": json.dumps([
                    {"name": m["name"], "weight_kg": cm["weight_kg"]}
                    for m, cm in zip(alt_materials, current_materials)
                ]),
                "estimated_co2_kg": round(alt_co2, 2),
                "co2_difference_kg": round(co2_difference, 2),
                "co2_reduction_percentage": round((co2_difference / project["material_co2_kg"]) * 100, 1) if project["material_co2_kg"] > 0 else 0,
                "estimated_cost_usd": round(alt_cost, 2),
                "cost_difference_usd": round(cost_difference, 2),
                "recyclability_percentage": round(alt_recyclability * 100, 1),
                "recommendation": "Recommended" if co2_difference < 0 and cost_difference < project["total_cost_usd"] * 0.1 else "Consider",
                "notes": f"{'Lower' if co2_difference < 0 else 'Higher'} carbon, {'Lower' if cost_difference < 0 else 'Higher'} cost"
            }
            alternatives.append(alternative)
    
    return alternatives

def generate_lifecycle_assessments(projects: List[Dict]) -> List[Dict]:
    """Generate lifecycle assessment reports"""
    lca_reports = []
    
    for project in projects:
        if project["phase"] in ["testing", "completed"]:
            # Full lifecycle breakdown
            lca = {
                "lca_id": f"LCA-{project['project_id']}",
                "project_id": project["project_id"],
                "assessment_date": datetime.now().isoformat(),
                "lifecycle_stages": json.dumps({
                    "raw_material_extraction": {
                        "co2_kg": project["material_co2_kg"],
                        "percentage": round((project["material_co2_kg"] / project["total_co2_kg"]) * 100, 1)
                    },
                    "manufacturing": {
                        "co2_kg": project["process_co2_kg"],
                        "percentage": round((project["process_co2_kg"] / project["total_co2_kg"]) * 100, 1)
                    },
                    "transportation": {
                        "co2_kg": project["transport_co2_kg"],
                        "percentage": round((project["transport_co2_kg"] / project["total_co2_kg"]) * 100, 1)
                    },
                    "use_phase": {
                        "co2_kg": 0,  # Assuming no emissions during use
                        "percentage": 0
                    },
                    "end_of_life": {
                        "co2_kg": project["eol_co2_kg"],
                        "percentage": round((project["eol_co2_kg"] / project["total_co2_kg"]) * 100, 1)
                    }
                }),
                "total_co2_kg": project["total_co2_kg"],
                "co2_per_unit": project["co2_per_unit"],
                "water_usage_liters": round(project["units_planned"] * random.uniform(10, 50), 2),
                "energy_consumption_kwh": round(project["process_co2_kg"] * random.uniform(2, 4), 2),
                "recyclability_score": project["recyclability_percentage"],
                "circularity_score": round(random.uniform(60, 90), 1),
                "improvement_recommendations": json.dumps([
                    "Consider recycled materials" if project["recyclability_percentage"] < 70 else "Maintain recycled content",
                    "Optimize transportation routes" if project["transport_co2_kg"] > 150 else "Transport emissions acceptable",
                    "Explore renewable energy for manufacturing" if project["process_co2_kg"] > 1000 else "Energy efficiency good"
                ])
            }
            lca_reports.append(lca)
    
    return lca_reports

def main():
    """Generate all design data"""
    print("🎨 Generating Zero@Design Demo Data...")
    
    # Generate design projects
    print("\n📐 Generating design projects...")
    projects = generate_design_projects(50)
    print(f"   ✅ Generated {len(projects)} projects")
    
    # Generate material alternatives
    print("\n🔄 Generating material alternatives...")
    alternatives = generate_material_alternatives(projects)
    print(f"   ✅ Generated {len(alternatives)} alternative scenarios")
    
    # Generate LCA reports
    print("\n♻️  Generating lifecycle assessments...")
    lca_reports = generate_lifecycle_assessments(projects)
    print(f"   ✅ Generated {len(lca_reports)} LCA reports")
    
    # Save to JSON files
    print("\n💾 Saving to JSON files...")
    
    with open('design_projects.json', 'w') as f:
        json.dump(projects, f, indent=2)
    print("   ✅ design_projects.json")
    
    with open('design_material_alternatives.json', 'w') as f:
        json.dump(alternatives, f, indent=2)
    print("   ✅ design_material_alternatives.json")
    
    with open('design_lca_reports.json', 'w') as f:
        json.dump(lca_reports, f, indent=2)
    print("   ✅ design_lca_reports.json")
    
    # Generate summary
    completed_projects = [p for p in projects if p["phase"] == "completed"]
    
    total_co2 = sum(p["total_co2_kg"] for p in projects)
    avg_sustainability = sum(p["sustainability_score"] for p in projects) / len(projects)
    targets_met = len([p for p in projects if p["target_met"]])
    
    summary = {
        "total_projects": len(projects),
        "by_industry": {
            industry: len([p for p in projects if p["industry"] == industry])
            for industry in INDUSTRIES
        },
        "completed_projects": len(completed_projects),
        "in_progress_projects": len([p for p in projects if p["phase"] != "completed"]),
        "total_co2_emissions_kg": round(total_co2, 2),
        "avg_sustainability_score": round(avg_sustainability, 1),
        "sustainability_targets_met": targets_met,
        "target_achievement_rate": round((targets_met / len(projects)) * 100, 1),
        "avg_recyclability": round(sum(p["recyclability_percentage"] for p in projects) / len(projects), 1),
        "material_alternatives_analyzed": len(alternatives),
        "lca_reports_completed": len(lca_reports),
    }
    
    with open('design_summary.json', 'w') as f:
        json.dump(summary, f, indent=2)
    print("   ✅ design_summary.json")
    
    print("\n" + "="*60)
    print("📈 SUMMARY STATISTICS")
    print("="*60)
    for key, value in summary.items():
        print(f"{key:.<40} {value}")
    print("="*60)
    print("\n✅ All Zero@Design demo data generated successfully!")
    print("📁 Files ready for Supabase import\n")

if __name__ == "__main__":
    main()
