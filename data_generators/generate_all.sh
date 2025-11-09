#!/bin/bash

# Zero@Ecosystem - Generate All Demo Data
# Run all data generators

echo "🚀 Zero@Ecosystem Demo Data Generation"
echo "======================================"
echo ""

# Create output directory
mkdir -p generated_data
cd generated_data

echo "📊 Starting data generation..."
echo ""

# Generate Steel data
echo "1/4 - Zero@Steel"
python3 ../generate_steel_data.py
echo ""

# Generate Production data
echo "2/4 - Zero@Production"
python3 ../generate_production_data.py
echo ""

# Generate DryFood data
echo "3/4 - Zero@DryFood"
python3 ../generate_dryfood_data.py
echo ""

# Generate Design data
echo "4/4 - Zero@Design"
python3 ../generate_design_data.py
echo ""

echo "======================================"
echo "✅ ALL DATA GENERATED SUCCESSFULLY!"
echo "======================================"
echo ""
echo "📁 Generated files:"
ls -lh *.json | wc -l | xargs echo "Total JSON files:"
du -sh . | awk '{print "Total size: " $1}'
echo ""
echo "📌 Next steps:"
echo "1. Review the generated JSON files"
echo "2. Import to Supabase database"
echo "3. Test the demo applications"
echo ""
