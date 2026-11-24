
import requests
import pandas as pd
from pathlib import Path
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Official EEA metadata CSV
URL = (
    "https://ereporting.blob.core.windows.net/"
    "downloadservice/metadata.csv"
)

# Project directory
OUTPUT_DIR = Path("data/raw/eea")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "eea_measurements_metadata.csv"

# Retry configuration
session = requests.Session()

retry = Retry(
    total=3,
    backoff_factor=2,
    status_forcelist=[429, 500, 502, 503, 504],
    allowed_methods=["GET"]
)

session.mount("https://", HTTPAdapter(max_retries=retry))

print("Connecting to EEA...")
print("Downloading metadata...")

try:
    response = session.get(URL, timeout=180)
    response.raise_for_status()

    OUTPUT_FILE.write_bytes(response.content)

    print("\nDownload successful!")
    print("File saved:", OUTPUT_FILE)

    # Read CSV
    df = pd.read_csv(OUTPUT_FILE, low_memory=False)

    print("\nDataset overview")
    print("----------------")
    print("Rows:", len(df))
    print("Columns:", len(df.columns))

    print("\nColumn names:")
    print(df.columns.tolist())

    print("\nFirst five records:")
    print(df.head())

except requests.exceptions.RequestException as error:
    print("\nEEA download failed:", error)

except Exception as error:
    print("\nData processing error:", error)
