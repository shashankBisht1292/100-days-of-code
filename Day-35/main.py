import requests
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
API_KEY = ""

account_sid = ''
auth_token = ''

parameters = {
    "lat": 24.71,
    "lon": 46.68,
    "appid": API_KEY,
    "cnt": 4
}
response = requests.get(OWM_ENDPOINT, params=parameters)
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body='Its going to rain today. Reminder to bring an umbrella ☔️',
        to='whatsapp:+918884000438'
    )
    print(message.status)