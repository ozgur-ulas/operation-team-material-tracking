# Operation Team Material Tracking

Production team material usage tracking and optimization for a 3‑shift, 6‑day manufacturing shopfloor.

## Project overview

This project tracks and analyzes the consumption of personal protective equipment (PPE) and related materials for a production team under strong management pressure to reduce usage without compromising safety or quality.

- **Total headcount:** 120 operators + 50 support staff (technicians, quality, etc.)
- **Shifts:** 3 shifts
- **Schedule:** 6 days per week
- **Goal:** Reduce material usage per person and per output unit, identify waste, and support data‑driven decisions.

### Tracked materials

- Gloves_type_1  
- Gloves_type_2  
- T_shirt_type_1  
- T_shirt_type_2  
- T_shirt_type_3  
- Pants_type_1  
- Pants_type_2  
- Shoe_covers  
- Oil  
- Shell_liquid  
- Lubrication_chemical  
- Ear_plugs  
- Cleaning_chemical  
- Cleaning_stick  
- Wiper  
- Plastic_cover  
- Safety_shoes  
- Winter_jacket  
- Office_materials  
- Lab_apron  

## Data model

Each record represents material usage for a person (or group) in a given time period.

Example fields:

- `date`
- `shift` (1, 2, 3)
- `employee_id`
- `role` (operator, technician, quality, shift_leaders, planners, etc.)
- `department` / `line`
- `material_name`
- `quantity_used`
- `unit` (pair, piece, liter, etc.)
- `production_output` (optional: units produced in that period)
- `remarks` (optional: reason, abnormal usage, etc.)

## KPIs

Some key indicators calculated in this project:

- **Usage per person per shift**  
- **Usage per 1000 units produced**  
- **Top materials by cost and volume**  
- **Abnormal spikes by shift / line / role**  
- **Trend before vs. after improvement actions**

## Tech stack

- **Python**: data generation, cleaning, aggregation
- **Pandas / NumPy**: data processing
- **Tableau or Power BI**: interactive dashboards for management and shopfloor reviews

## Repository structure

See the folder structure in this README’s top section.

## How to run

1. **Create environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
