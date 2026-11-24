
import requests
import pandas as pd
from pathlib import Path

# EEA official spatial station service
URL = (
    "https://air.discomap.eea.europa.eu/arcgis/rest/services/"
    "AirQuality/AirQualityDownloadServiceEUMonitoringStations/"
    "MapServer/0/query"
)

# Our eight candidate PM2.5 station codes
station_codes = [
    "LV00010",
    "LV00016",
    "LV000L1",
    "LV00RM4",
    "LV00RZ1",
    "LV00VN3",
    "LV0RBR6",
    "LV0RKR9"
]

where_clause = (
    "CountryCode = 'LV' AND AirQualityStationEoICode IN ("
    + ",".join(f"'{code}'" for code in station_codes)
    + ")"
)

params = {
    "where": where_clause,
    "outFields": "AirQualityStation,CountryCode,"
                 "AirQualityStationEoICode,AQStationName",
    "returnGeometry": "true",
    "outSR": "4326",
    "f": "geojson"
}

print("Searching EEA station locations...")

response = requests.get(URL, params=params, timeout=60)
response.raise_for_status()

result = response.json()

if "features" not in result:
    raise ValueError(f"Unexpected EEA response: {result}")

records = []

for feature in result["features"]:
    properties = feature["properties"]
    geometry = feature.get("geometry")

    coordinates = (
        geometry.get("coordinates")
        if geometry else None
    )

    longitude = coordinates[0] if coordinates else None
    latitude = coordinates[1] if coordinates else None

    records.append({
        "station_id": properties.get("AirQualityStation"),
        "eoi_code": properties.get("AirQualityStationEoICode"),
        "station_name": properties.get("AQStationName"),
        "longitude": longitude,
        "latitude": latitude
    })

df = pd.DataFrame(records)

output_dir = Path("data/processed")
output_dir.mkdir(parents=True, exist_ok=True)

output_file = output_dir / "latvia_pm25_station_locations.csv"

df.to_csv(output_file, index=False)

print("\nStations found:", len(df))
print("\nStation coordinates:")
print(df.to_string(index=False))

print("\nSaved:", output_file)

missing = set(station_codes) - set(df["eoi_code"].dropna())

print("\nCodes not found in spatial service:")
print(sorted(missing))
