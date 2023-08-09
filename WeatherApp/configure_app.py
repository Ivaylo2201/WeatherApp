import customtkinter as ctk
from typing import Dict

from customtkinter import CTkBaseClass
from fetch_api_data import fetch_api_data
from clear_data import clear_data
from PIL import Image


def configure_app(app: ctk.CTk) -> None:
    """INSERT APP SETTINGS & ATTRIBUTES HERE"""

    WIDTH, HEIGHT = (750, 450)
    MIDDLE_X, MIDDLE_Y = (555, 255)

    app.geometry(f"{WIDTH}x{HEIGHT}+{MIDDLE_X}+{MIDDLE_Y}")
    app.resizable(False, False)
    app.title("WeatherApp")
    app.iconbitmap("static/01d@2x.ico")

    def change_focus(event) -> None:
        event.widget.focus_set()

    app.bind_all('<Button>', change_focus)

    app_attributes: Dict[CTkBaseClass, tuple[int, int]] = {}

    city_textbox = ctk.CTkEntry(
        app, width = 250, height = 50, font = ("Verdana", 25),
        border_width = 3, border_color = "#EC6E4C", fg_color = "#343638",
        corner_radius = 15, placeholder_text = "Enter a city"
    )

    no_country_flag = ctk.CTkImage(Image.open("static/no-country-flag.png"), size = (90, 50))
    country_icon = ctk.CTkLabel(
        app, image = no_country_flag, text = "",
        width = 90, height = 50
    )

    no_city_selected = ctk.CTkImage(Image.open("static/no-city-selected.png"), size = (150, 150))
    weather_icon = ctk.CTkLabel(
        app, image = no_city_selected, text = "",
        width = 100, height = 200
    )

    weather_details = ctk.CTkLabel(
        app, width = 400, height = 200, font = ("Verdana", 25),
        text = "", text_color = "#EC6E4C", fg_color = "#343638",
    )

    fetch_data_button = ctk.CTkButton(
        app, width = 250, height = 50, font = ("Verdana", 25),
        text = "Check Weather", border_width = 3, border_color = "#EC6E4C",
        fg_color = "#343638", hover_color = "#EC6E4C", corner_radius = 15,
        command = lambda: fetch_api_data(city_textbox, weather_details, weather_icon, country_icon)
    )

    clear_data_button = ctk.CTkButton(
        app, width = 130, height = 50, font = ("Verdana", 25),
        text = "Clear", border_width = 3, border_color = "#EC6E4C",
        fg_color = "#343638", hover_color = "#EC6E4C", corner_radius = 15,
        command = lambda: clear_data(city_textbox, weather_details, weather_icon, country_icon)
    )

    app_attributes[city_textbox] = (250, 50)
    app_attributes[country_icon] = (540, 50)
    app_attributes[weather_icon] = (50, 125)
    app_attributes[fetch_data_button] = (250, 350)
    app_attributes[weather_details] = (250, 125)
    app_attributes[clear_data_button] = (520, 350)

    for attribute, coordinates in app_attributes.items():
        attribute.place(x = coordinates[0], y = coordinates[1])
