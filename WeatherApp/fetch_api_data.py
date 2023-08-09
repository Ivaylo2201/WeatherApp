import customtkinter as ctk
import requests
from PIL import Image

from load_weather_icons import load_weather_icons
from load_country_flags import load_country_flags
from clear_data import clear_data


def fetch_api_data(city_textbox: ctk.CTkEntry, weather_details: ctk.CTkLabel, weather_icon: ctk.CTkLabel,
                   country_icon: ctk.CTkLabel) -> None:
    """REQUESTING API DATA ABOUT THE
       CITY SELECTED BY THE USER"""

    city = city_textbox.get()

    if city == '':
        clear_data(city_textbox, weather_details, weather_icon, country_icon)
        weather_details.configure(text = "City field cannot be empty!")
        return None

    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=bbb9969b7ee53258f810992bf37f2e80"
    api_data = requests.get(api_url).json()

    try:
        updated_weather_image = load_weather_icons()[api_data['weather'][0]['icon']]

        main = api_data['weather'][0]['main']
        temp = api_data['main']['temp'] - 273.15  # Kelvin -> Celsius
        pressure = api_data['main']['pressure']
        cloudiness = api_data['clouds']['all']
        humidity = api_data['main']['humidity']
        wind = api_data['wind']['speed']
        country_domain = api_data['sys']['country']

        updated_data = '\n'.join([
            f"Weather: {main}",
            f"Temperature: {temp:.1f} C°",
            f"Pressure: {pressure}hPa",
            f"Cloudiness: {cloudiness}%",
            f"Humidity: {humidity}%",
            f"Wind: {wind} m/s"
        ])

        # If the flag is not yet uploaded, instead of throwing an exception,
        # reset the picture box to blank

        try:
            updated_country_flag = load_country_flags()[country_domain]
            country_icon.configure(image = updated_country_flag)
        except KeyError:
            no_country_flag = ctk.CTkImage(Image.open("static/no-country-flag.png"), size = (90, 50))
            country_icon.configure(image = no_country_flag)

        weather_details.configure(text = updated_data)
        weather_icon.configure(image = updated_weather_image)

    except KeyError:
        clear_data(city_textbox, weather_details, weather_icon, country_icon)
        weather_details.configure(text = "City not found!")
