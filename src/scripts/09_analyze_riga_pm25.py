
import pandas as pd
from pathlib import Path

data_dir = Path("data/raw/eea/riga_pm25")

files = list(data_dir.glob("*.parquet"))

for file in files:
    print("\n" + "=" * 60)
    print("FILE:", file.name)
    print("=" * 60)

    df = pd.read_parquet(file)

    df["Start"] = pd.to_datetime(df["Start"])
    df["Value"] = pd.to_numeric(df["Value"], errors="coerce")

    total = len(df)
    valid = df[df["Validity"] == 1].copy()
    invalid = df[df["Validity"] != 1].copy()

    # Exclude obvious placeholder values from valid records too
    valid = valid[~valid["Value"].isin([-999, 999])]

    print("Total records:", total)
    print("Valid records:", len(valid))
    print("Invalid records:", len(invalid))
    print("Valid percentage:", round(len(valid) / total * 100, 2), "%")

    print("\nMeasurement type:")
    print(df["AggType"].value_counts().to_string())

    print("\nDate coverage:")
    print("First date:", df["Start"].min())
    print("Last date:", df["Start"].max())

    print("\nValid PM2.5 statistics (ug/m3):")
    if len(valid) > 0:
        print(valid["Value"].describe())

    print("\nValidity counts:")
    print(df["Validity"].value_counts().to_string())

    print("\nSampling points:")
    print(df["Samplingpoint"].unique())

print("\nAnalysis completed.")
