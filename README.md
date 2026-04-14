# Operation Team Material Tracking 📦

Data-driven tracking of PPE and shopfloor material usage for a 3‑shift manufacturing operation, built with **Python + Power BI**.

---

## 1. Project snapshot

**Goal:** Reduce over‑consumption of PPE and indirect materials (gloves, chemicals, clothing, etc.) while keeping safety and quality intact.

**Context:**

- 120 operators + 50 support staff (technicians, quality, lab)
- 3 shifts, 6‑day schedule (Sunday off)
- Strong management pressure to **decrease material usage**
- Materials include PPE, chemicals, clothing, and office/lab items

**What I built:**

- A **synthetic but realistic dataset** simulating 90 days of material usage
- **Python pipeline** for data generation, cleaning, and KPI aggregation
- A **Power BI dashboard** to monitor usage by shift, department, role, and material
- Portfolio‑ready documentation focused on **business impact**

---

## 2. Business problem & impact

### Problem

Material usage on the shopfloor was perceived as “too high”, but:

- No consolidated view across **shifts / departments / roles**
- No baseline for **usage per person** or **per production output**
- No easy way for management to see **where waste actually occurs**

### Impact (what this solution enables)

With this project, a manufacturing team could:

- Track **usage per 1000 units produced** by material and shift  
- Identify **outlier departments** or roles with unusually high consumption  
- Run **before/after comparisons** when new rules or training are introduced  
- Turn “we think usage is high” into **measurable, visual evidence**

---

## 3. Data design

Because I cannot share real factory data, I created a **synthetic dataset** that mimics a real environment.

### 3.1. Key entities

Each row represents **material usage by one employee in one shift on one day**.

**Columns:**

- `date` – calendar date (90‑day range)
- `shift` – 1, 2, or 3
- `employee_id` – anonymized ID (E001–E170)
- `role` – `operator`, `technician`, `quality`
- `department` – `LINE_A`, `LINE_B`, `LINE_C`, `MAINTENANCE`, `LAB`
- `material_name` – one of 20 tracked materials
- `quantity_used` – numeric quantity
- `unit` – `pair`, `piece`, or `liter`
- `production_output` – units produced in that shift (for operators only)

### 3.2. Tracked materials

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

---

## 4. Tech stack & skills demonstrated

- **Python**
  - Synthetic data generation
  - Data cleaning & preprocessing
  - KPI calculation with `pandas`
- **Power BI**
  - Data modeling from CSV
  - DAX measures (usage metrics, ratios)
  - Interactive dashboards with slicers and drill‑downs
- **Data skills**
  - Designing a data model from a business problem
  - Translating shopfloor reality into structured data
  - Building metrics that management can act on

---

## 5. Project structure

```text
operation-team-material-tracking/
├─ data/
│  ├─ raw/
│  │  └─ material_usage_raw.csv
│  └─ processed/
│     ├─ material_usage_clean.csv
│     └─ material_usage_agg.csv
├─ src/
│  ├─ data_generation.py
│  ├─ data_processing.py
│  └─ kpi_calculation.py
├─ dashboards/
│  └─ powerbi/
│     └─ material_usage_dashboard.pbix
├─ notebooks/
│  └─ exploration.ipynb
├─ reports/
│  └─ findings.md
└─ README.md
