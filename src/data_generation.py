import random
import uuid
from datetime import datetime, timedelta
import pandas as pd

MATERIALS = [
    "Gloves_type_1",
    "Gloves_type_2",
    "T_shirt_type_1",
    "T_shirt_type_2",
    "T_shirt_type_3",
    "Pants_type_1",
    "Pants_type_2",
    "Shoe_covers",
    "Oil",
    "Shell_liquid",
    "Lubrication_chemical",
    "Ear_plugs",
    "Cleaning_chemical",
    "Cleaning_stick",
    "Wiper",
    "Plastic_cover",
    "Safety_shoes",
    "Winter_jacket",
    "Office_materials",
    "Lab_apron",
]

ROLES = ["operator", "technician", "quality"]
DEPARTMENTS = ["Line_A", "Line_B", "Line_C", "Maintenance", "Lab"]

NUM_OPERATORS = 120
NUM_OTHERS = 50

def generate_employees():
    employees = []
    for i in range(NUM_OPERATORS + NUM_OTHERS):
        role = random.choices(
            ROLES,
            weights=[0.7, 0.2, 0.1],
            k=1
        )[0]
        employees.append(
            {
                "employee_id": f"E{i+1:03d}",
                "role": role,
                "department": random.choice(DEPARTMENTS),
            }
        )
    return employees

def generate_date_range(start_date, end_date):
    current = start_date
    while current <= end_date:
        # 6-day schedule: skip Sundays
        if current.weekday() != 6:
            yield current
        current += timedelta(days=1)

def generate_usage_records(start_date, end_date):
    employees = generate_employees()
    records = []

    for date in generate_date_range(start_date, end_date):
        for shift in [1, 2, 3]:
            for emp in employees:
                # Not everyone uses material every shift
                if random.random() < 0.6:
                    continue

                # Base usage factor by role
                if emp["role"] == "operator":
                    base_items = random.randint(1, 3)
                elif emp["role"] == "technician":
                    base_items = random.randint(0, 2)
                else:  # quality
                    base_items = random.randint(0, 1)

                for _ in range(base_items):
                    material = random.choice(MATERIALS)

                    # Simple quantity logic
                    if "Gloves" in material or "Ear_plugs" in material:
                        qty = random.randint(1, 2)
                        unit = "pair"
                    elif material in ["Oil", "Shell_liquid", "Lubrication_chemical", "Cleaning_chemical"]:
                        qty = round(random.uniform(0.1, 1.0), 2)
                        unit = "liter"
                    else:
                        qty = 1
                        unit = "piece"

                    production_output = random.randint(500, 2000) if emp["role"] == "operator" else None

                    records.append(
                        {
                            "date": date,
                            "shift": shift,
                            "employee_id": emp["employee_id"],
                            "role": emp["role"],
                            "department": emp["department"],
                            "material_name": material,
                            "quantity_used": qty,
                            "unit": unit,
                            "production_output": production_output,
                        }
                    )

    return pd.DataFrame(records)

if __name__ == "__main__":
    start = datetime(2025, 1, 1)
    end = datetime(2025, 3, 31)

    df = generate_usage_records(start, end)
    df.to_csv("data/raw/material_usage_raw.csv", index=False)
    print(f"Generated {len(df)} records.")
