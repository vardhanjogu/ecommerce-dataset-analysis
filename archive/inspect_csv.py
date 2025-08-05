import pandas as pd
import os

# Define the folder path where CSVs are located
folder_path = "archive"

# Get list of all files in the archive folder
files = os.listdir(folder_path)

# Filter out CSV files
csv_files = [file for file in files if file.endswith('.csv')]

# Loop through and inspect each CSV
for csv_file in csv_files:
    print(f"\n🔍 Inspecting file: {csv_file}")
    try:
        file_path = os.path.join(folder_path, csv_file)
        df = pd.read_csv(file_path)
        print("✅ Shape:", df.shape)
        print("✅ Columns:", df.columns.tolist())
        print("-" * 40)
    except Exception as e:
        print(f"❌ Error reading {csv_file}: {e}")
