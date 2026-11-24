
import requests
from pathlib import Path

BASE_URL = (
    "https://eeadmz1-downloads-api-appservice.azurewebsites.net"
)

OUTPUT_DIR = Path("data/raw/eea")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "riga_pm25_parquet_urls.csv"

# EEA verified historical measurements (E1a)
request_body = {
    "countries": ["LV"],
    "cities": ["Riga"],
    "pollutants": ["PM2.5"],
    "dataset": 2
}

print("Requesting Riga PM2.5 measurement URLs...")
print("Country: Latvia")
print("City: Riga")
print("Pollutant: PM2.5")
print("Dataset: E1a - Verified historical data")

try:
    response = requests.post(
        f"{BASE_URL}/ParquetFile/urls",
        json=request_body,
        timeout=120
    )

    response.raise_for_status()

    # Save the original API response
    OUTPUT_FILE.write_bytes(response.content)

    print("\nRequest successful!")
    print("HTTP status:", response.status_code)
    print("Content type:", response.headers.get("Content-Type"))
    print("Response size:", len(response.content), "bytes")
    print("Saved:", OUTPUT_FILE)

    print("\nFirst part of response:")
    print(response.text[:2000])

    if len(response.content) == 0:
        print("\nWARNING: API returned an empty response.")

except requests.RequestException as error:
    print("\nDownload URL request failed:")
    print(error)

    if getattr(error, "response", None) is not None:
        print(error.response.text[:2000])
