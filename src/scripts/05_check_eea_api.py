
import requests
import json

BASE_URL = (
    "https://eeadmz1-downloads-api-appservice.azurewebsites.net"
)

session = requests.Session()
session.headers.update({
    "User-Agent": "Riga-Air-Quality-Research/1.0"
})

def check_endpoint(name, method, url, **kwargs):
    print(f"\nChecking {name}...")

    try:
        response = session.request(
            method,
            url,
            timeout=60,
            **kwargs
        )

        response.raise_for_status()
        result = response.json()

        print(f"{name}: SUCCESS")
        return result

    except requests.RequestException as error:
        print(f"{name}: FAILED")
        print(error)
        return None


# 1. Get available countries
countries = check_endpoint(
    "Countries",
    "GET",
    f"{BASE_URL}/Country"
)

if countries:
    print("\nLatvia country information:")
    for country in countries:
        if country.get("countryCode") == "LV":
            print(country)


# 2. Get available pollutants
pollutants = check_endpoint(
    "Pollutants",
    "GET",
    f"{BASE_URL}/Pollutant"
)

if pollutants:
    print("\nPM2.5 pollutant information:")
    for pollutant in pollutants:
        if pollutant.get("notation", "").upper() == "PM2.5":
            print(pollutant)


# 3. Get cities available for Latvia
cities = check_endpoint(
    "Latvian cities",
    "POST",
    f"{BASE_URL}/City",
    json=["LV"]
)

if cities:
    print("\nAvailable Latvian cities:")

    for city in cities:
        print(
            "City:",
            city.get("cityName"),
            "| Country:",
            city.get("countryCode")
        )


print("\nAPI discovery completed.")
