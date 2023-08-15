import customtkinter as ctk
from PIL import Image


def clear_forms(city_textbox: ctk.CTkEntry, weather_details: ctk.CTkLabel, weather_icon: ctk.CTkLabel,
                country_icon: ctk.CTkLabel) -> None:
    """EMPTYING THE SEARCH BAR, THE WEATHER DATA TEXTBOX,
       THE WEATHER CONDITION PICTURE BOX AND FLAG PICTURE BOX """

    city_textbox.delete(0, 'end')
    weather_details.configure(text = '')

    NA = ctk.CTkImage(Image.open("FrontEnd/static/NA.jpg"), size = (75, 75))

    weather_icon.configure(image = NA)
    country_icon.configure(image = NA)
    weather_details.configure(text = "Select a city!")
