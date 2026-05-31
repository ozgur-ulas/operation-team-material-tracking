import os
import pandas as pd
import numpy as np

def setup_directories():
    """Ensures the processed data directory exists."""
    processed_dir = os.path.join("data", "processed")
    os.makedirs(processed_dir, exist_ok=True)
    return processed_dir

def load_raw_data():
    """Loads the raw synthetic material usage dataset."""
    raw_path = os.path.join("data", "raw", "material_usage_raw.csv")
    if not os.path.exists(raw_path):
        raise FileNotFoundError(
            f"Raw data not found at {raw_path}. Please run data_generation.py first."
        )
    print(f"Loading raw data from: {raw_path}")
    return pd.read_csv(raw_path)

def clean_data(df):
    """
    Cleans and preprocesses the material usage dataset.
    
    - Converts dates to datetime objects
    - Standardizes categorical strings
    - Ensures numerical constraints (e.g., quantities shouldn't be negative)
    - Corrects production output logic (only operators should have production output)
    """
    print("Beginning data cleaning and preprocessing...")
    df_clean = df.copy()

    # 1. Handle Dates
    df_clean['date'] = pd.to_datetime(df_clean['date'])

    # 2. Enforce Data Types & Formatting
    df_clean['shift'] = df_clean['shift'].astype(int)
    df_clean['employee_id'] = df_clean['employee_id'].astype(str).str.upper().str.strip()
    df_clean['role'] = df_clean['role'].astype(str).str.lower().str.strip()
    df_clean['department'] = df_clean['department'].astype(str).str.upper().str.strip()
    df_clean['material_name'] = df_clean['material_name'].astype(str).str.strip()
    df_clean['unit'] = df_clean['unit'].astype(str).str.lower().str.strip()

    # 3. Handle Missing Values / Logical Anomalies
    # Quantities must be positive numbers
    df_clean['quantity_used'] = pd.to_numeric(df_clean['quantity_used'], errors='coerce')
    df_clean['quantity_used'] = df_clean['quantity_used'].fillna(0).clip(lower=0)

    # Production output logic: Only 'operator' role should have a production output.
    # Non-operators (technicians, quality, lab) have 0 production units for a shift.
    df_clean['production_output'] = pd.to_numeric(df_clean['production_output'], errors='coerce')
    df_clean['production_output'] = np.where(
        df_clean['role'] == 'operator',
        df_clean['production_output'].fillna(0).clip(lower=0),
        0
    )

    # 4. Drop any rows that completely lack essential tracking fields
    df_clean = df_clean.dropna(subset=['date', 'employee_id', 'material_name'])

    print(f"Data cleaning complete. Processed {len(df_clean)} rows.")
    return df_clean

def save_processed_data(df, processed_dir):
    """Saves the cleaned dataframe to a CSV file for KPI mapping and Power BI."""
    output_path = os.path.join(processed_dir, "material_usage_clean.csv")
    df.to_csv(output_path, index=False)
    print(f"Successfully saved clean dataset to: {output_path}")

def main():
    try:
        # Step 1: Ensure directories are ready
        processed_dir = setup_directories()
        
        # Step 2: Load the raw synthetic data
        raw_df = load_raw_data()
        
        # Step 3: Run preprocessing pipeline
        cleaned_df = clean_data(raw_df)
        
        # Step 4: Export for the next pipeline stages
        save_processed_data(cleaned_df, processed_dir)
        
    except Exception as e:
        print(f"Error during data processing execution: {e}")

if __name__ == "__main__":
    main()
