import tkinter

import customtkinter as ctk

from BackEnd.FetchApiData import fetch_api_data
from FrontEnd.ClearForms import clear_forms
from PIL import Image


def create_button(master, text, function) -> ctk.CTkButton:
    def onEnter(event):
        button.configure(fg_color = "#fff4e4")
        button.configure(text_color = "#231942")

    def onLeave(event):
        button.configure(fg_color = "#231942")
        button.configure(text_color = "#fff4e4")

    button = ctk.CTkButton(
        master, width = 150, height = 50, font = ("Century Gothic", 20),
        fg_color = "#231942", bg_color = "#231942", text_color = "#fff4e4", hover_color = "#fff4e4",
        border_color = "#fff4e4", border_width = 1, text = text, corner_radius = 25, cursor = "hand2",
        command = function
    )

    button.bind("<Enter>", onEnter)
    button.bind("<Leave>", onLeave)

    return button


def configure_app(app: ctk.CTk) -> None:
    """ INSERT APP SETTINGS & ATTRIBUTES HERE """

    WIDTH, HEIGHT = (750, 450)
    MIDDLE_X, MIDDLE_Y = (555, 255)

    app.geometry(f"{WIDTH}x{HEIGHT}+{MIDDLE_X}+{MIDDLE_Y}")
    app.resizable(False, False)
    app.title("WeatherApp")
    app.iconbitmap("FrontEnd/static/01d@2x.ico")
    attributes: dict[ctk.CTkBaseClass, tuple[int, int]] = {}

    def change_focus(event) -> None:
        event.widget.focus_set()

    app.bind_all('<Button>', change_focus)

    background_color = ctk.CTkImage(Image.open("FrontEnd/static/background_color.jpg"), size = (WIDTH, HEIGHT))
    ctk.CTkLabel(app, image = background_color, text = '').pack()

    background_frame = ctk.CTkFrame(
        app, width = 575, height = 385, fg_color = "#231942",
        bg_color = "#fff4e4", corner_radius = 25
    ).place(
        relx = 0.500, rely = 0.500, anchor = tkinter.CENTER
    )

    city = ctk.CTkEntry(
        background_frame, width = 234, height = 40, border_width = 0, corner_radius = 0,
        fg_color = "#231942", text_color = "#fff4e4", font = ("Century Gothic", 20),
        placeholder_text = "City", placeholder_text_color = "#fff4e4"
    )

    ctk.CTkFrame(
        background_frame, width = 234, height = 2, fg_color = "#fff4e4"
    ).place(
        relx = 0.360, rely = 0.215, anchor = background_frame
    )

    find_button = create_button(
        background_frame, "FIND", lambda: fetch_api_data(city, weather_details, weather_icon, country_flag)
    )

    clear_button = create_button(
        background_frame, "CLEAR", lambda: clear_forms(city, weather_details, weather_icon, country_flag)
    )

    NA = ctk.CTkImage(Image.open("FrontEnd/static/NA.jpg"), size = (75, 75))
    weather_icon = ctk.CTkLabel(
        app, text = "", image = NA,
        width = 120, height = 120, fg_color = "#231942"
    )

    country_flag = ctk.CTkLabel(
        app, text = "", image = NA,
        width = 75, height = 20
    )

    weather_details = ctk.CTkLabel(
        background_frame, width = 350, height = 200, font = ("Century Gothic", 25),
        text = "Select a city!", text_color = "#fff4e4", fg_color = "#231942"
    )

    attributes[city] = (270, 57)
    attributes[find_button] = (220, 340)
    attributes[clear_button] = (400, 340)
    attributes[weather_icon] = (130, 160)
    attributes[weather_details] = (270, 120)
    attributes[country_flag] = (529, 49)

    for attr, coords in attributes.items():
        attr.place(x = coords[0], y = coords[1])
