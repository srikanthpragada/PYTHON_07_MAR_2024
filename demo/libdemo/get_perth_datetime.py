import requests

resp = requests.get("https://worldtimeapi.org/api/timezone/australia/perth")
if resp.status_code == 200:   # OK
    details = resp.json()  # Convert JSON to dict
    print(details['datetime'])
else:
    print("Sorry! Could not get details!")

