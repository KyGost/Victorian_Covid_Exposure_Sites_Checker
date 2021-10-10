import requests
import json

# Gets COVID-19 Exposure data from CKAN API as dictionary "data"
url = "https://discover.data.vic.gov.au/api/3/action/datastore_search?resource_id=afb52611-6061-4a2b-9110-74c920bede77"
data = requests.get(url).json()

# Opens locations.json as dictionary "locations"
with open("actual_locations_dont_publish_to_github.json", "r") as locations_file:
    locations = json.load(locations_file)['locations']

# Compares "locations" and "data" and prints matches
for exposure in data["result"]["records"]:
    print("\n\033[1m" + f"{exposure['Site_title']}" + "\033[0m")
    print(f"Suburb\t\t-   {exposure['Suburb']}")
    print(f"Exposure Date\t-   {exposure['Exposure_date']}")
    print(f"Exposure Time\t-   {exposure['Exposure_time']}")