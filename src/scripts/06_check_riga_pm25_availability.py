
import requests
import json

BASE_URL = (
    "https://eeadmz1-downloads-api-appservice.azurewebsites.net"
)

# Request for Riga PM2.5 verified data
request_body = {
    "countries": ["LV"],
    "cities": ["Riga"],
    "pollutants": ["PM2.5"],
    "dataset": 2,
    "source": "API",
    "method": "classic",
    "dateTimeStart": "2013-01-01T00:00:00Z",
    "dateTimeEnd": "2025-12-31T23:59:59Z",
    "aggregationType": "hour",
    "compress": True
}

print("Checking Riga PM2.5 data availability...")
print("Dataset: E1a (verified)")
print("Period: 2013-2025")
print("Pollutant: PM2.5")

try:
    response = requests.post(
        f"{BASE_URL}/DownloadSummary",
        json=request_body,
        timeout=120
    )

    response.raise_for_status()

    print("\nAPI response:")
    print("Status:", response.status_code)

    try:
        result = response.json()
        print(json.dumps(result, indent=4))

        with open(
            "data/processed/riga_pm25_availability.json",
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(result, file, indent=4)

        print("\nAvailability summary saved!")

    except ValueError:
        print(response.text)

except requests.RequestException as error:
    print("\nAPI request failed:")
    print(error)

    if getattr(error, "response", None) is not None:
        print(error.response.text)
