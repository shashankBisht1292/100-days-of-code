import requests
from datetime import datetime

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
print((data.get("iss_position")["latitude"], data.get("iss_position")["longitude"]))

parameters = {
    "lat": 30.325213,
    "lng": 78.008079,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

utc_sunrise = datetime.fromisoformat(sunrise)
local_sunrise = utc_sunrise.astimezone()
print(local_sunrise)

utc_sunset = datetime.fromisoformat(sunset)
local_sunset = utc_sunset.astimezone()
print(local_sunset)


print(datetime.now())