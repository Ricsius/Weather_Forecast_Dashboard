import os
import requests

API_KEY = os.getenv("Weather_API_Key")

def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if data["cod"] != "200":
        return []

    number_of_values = 8 * forecast_days
    filtered_data = data["list"]
    filtered_data = filtered_data[:number_of_values]

    return filtered_data