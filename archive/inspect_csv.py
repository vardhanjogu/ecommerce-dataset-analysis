import pandas as pd
import os

# Get list of all files in the current directory
files = os.listdir()

# Filter out CSV files
csv_files = [file for file in files if file.endswith('.csv')]

# Loop through and inspect each CSV
for csv_file in csv_files:
    print(f"Inspecting file: {csv_file}")
    try:
        df = pd.read_csv(csv_file)
        print("Shape:", df.shape)
        print("Columns:", df.columns.tolist())
        print("-" * 40)
    except Exception as e:
        print(f"Error reading {csv_file}: {e}")
