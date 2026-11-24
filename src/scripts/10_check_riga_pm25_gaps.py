
import pandas as pd
from pathlib import Path

data_dir = Path("data/raw/eea/riga_pm25")

for file in sorted(data_dir.glob("*.parquet")):
    print("\n" + "=" * 60)
    print(file.name)
    print("=" * 60)

    df = pd.read_parquet(file)
    df["Start"] = pd.to_datetime(df["Start"])

    valid = df[df["Validity"] == 1].copy()

    # Check negative valid measurements
    negative = valid[valid["Value"] < 0]

    print("\nNegative valid measurements:", len(negative))

    if len(negative) > 0:
        print(
            negative[["Start", "Value", "Unit", "Validity"]]
            .head(10).to_string(index=False)
        )

    # Count records by year
    print("\nRecords by year:")
    print(df.groupby(df["Start"].dt.year).size().to_string())

    print("\nValid records by year:")
    print(valid.groupby(valid["Start"].dt.year).size().to_string())

    # Check duplicate timestamps
    print("\nDuplicate Start timestamps:", df["Start"].duplicated().sum())

    # Check missing time intervals
    if df["AggType"].iloc[0] == "hour":
        expected = pd.date_range(
            df["Start"].min(), df["Start"].max(), freq="h"
        )
    else:
        expected = pd.date_range(
            df["Start"].min(), df["Start"].max(), freq="D"
        )

    actual = pd.DatetimeIndex(df["Start"].unique())
    missing = expected.difference(actual)

    print("\nExpected time intervals:", len(expected))
    print("Missing time intervals:", len(missing))

    if len(missing) > 0:
        print("First missing intervals:")
        print(missing[:10].to_list())

print("\nGap analysis completed.")

