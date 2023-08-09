import customtkinter as ctk
from PIL import Image


def clear_data(city_textbox: ctk.CTkEntry, weather_details: ctk.CTkLabel, weather_icon: ctk.CTkLabel,
               country_icon: ctk.CTkLabel) -> None:
    """EMPTYING THE SEARCH BAR, THE WEATHER DATA TEXTBOX,
       THE WEATHER CONDITION PICTURE BOX AND FLAG PICTURE BOX """

    city_textbox.delete(0, 'end')
    weather_details.configure(text = '')

    no_city_selected = ctk.CTkImage(Image.open("static/no-city-selected.png"), size = (150, 150))
    weather_icon.configure(image = no_city_selected)

    no_country_flag = ctk.CTkImage(Image.open("static/no-country-flag.png"), size = (90, 50))
    country_icon.configure(image = no_country_flag)
