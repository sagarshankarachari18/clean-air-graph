
import pandas as pd
from pathlib import Path

# Input file
input_file = Path("data/raw/eea/eea_measurements_metadata.csv")

# Output directory
output_dir = Path("data/processed")
output_dir.mkdir(parents=True, exist_ok=True)

print("Reading EEA metadata...")

# IMPORTANT: The source is TAB-separated
df = pd.read_csv(
    input_file,
    sep="\t",
    low_memory=False
)

# Clean column names
df.columns = df.columns.str.strip()

print("\nDataset loaded successfully!")
print("Total rows:", len(df))
print("Total columns:", len(df.columns))

print("\nAvailable columns:")
print(df.columns.tolist())

# Select Latvia
latvia = df[df["Countrycode"] == "LV"].copy()

print("\nLatvia metadata")
print("Total records:", len(latvia))

# Save Latvia metadata
latvia.to_csv(
    output_dir / "latvia_eea_metadata.csv",
    index=False
)

# Identify PM2.5 records
pm25 = latvia[
    latvia["AirPollutant"].astype(str).str.strip().str.upper()
    == "PM2.5"
].copy()

print("\nLatvia PM2.5 metadata")
print("Total records:", len(pm25))

print("\nPM2.5 monitoring stations:")
print(
    pm25[
        [
            "AirQualityStation",
            "AirQualityStationEoICode",
            "AirPollutant",
            "Longitude",
            "Latitude"
        ]
    ].drop_duplicates().to_string(index=False)
)

# Save PM2.5 metadata
pm25.to_csv(
    output_dir / "latvia_pm25_metadata.csv",
    index=False
)

print("\nFiles saved successfully!")
print("1. data/processed/latvia_eea_metadata.csv")
print("2. data/processed/latvia_pm25_metadata.csv")
