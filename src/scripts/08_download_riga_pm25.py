
import pandas as pd
import requests
from pathlib import Path
from io import BytesIO

# Read the URLs returned by the EEA API
url_file = Path("data/raw/eea/riga_pm25_parquet_urls.csv")
output_dir = Path("data/raw/eea/riga_pm25")
output_dir.mkdir(parents=True, exist_ok=True)

urls = pd.read_csv(url_file, encoding="utf-8-sig")[
    "ParquetFileUrl"
].dropna().tolist()

print(f"Found {len(urls)} Parquet files.")

for i, url in enumerate(urls, start=1):
    filename = url.split("/")[-1]
    output_file = output_dir / filename

    print(f"\nDownloading {i}/{len(urls)}: {filename}")

    response = requests.get(url, timeout=120)
    response.raise_for_status()

    output_file.write_bytes(response.content)

    print(f"Saved: {output_file}")
    print(f"Size: {len(response.content):,} bytes")

    # Read and inspect the downloaded data
    df = pd.read_parquet(BytesIO(response.content))

    print("Rows:", len(df))
    print("Columns:", df.columns.tolist())
    print(df.head(3).to_string(index=False))

print("\nDownload and inspection completed.")
