import customtkinter as ctk
from PIL import Image


def load_weather_icons() -> dict[str, ctk.CTkImage]:
    """LOADING AND RETURNING A DICT CONTAINING THE ICON IDs
       AND THE RENDERED ICONS"""

    ImageSize = (150, 150)

    _01d = ctk.CTkImage(Image.open("static/01d@2x.png"), size = ImageSize)
    _02d = ctk.CTkImage(Image.open("static/02d@2x.png"), size = ImageSize)
    _03d = ctk.CTkImage(Image.open("static/03d@2x.png"), size = ImageSize)
    _04d = ctk.CTkImage(Image.open("static/04d@2x.png"), size = ImageSize)
    _09d = ctk.CTkImage(Image.open("static/09d@2x.png"), size = ImageSize)
    _10d = ctk.CTkImage(Image.open("static/10d@2x.png"), size = ImageSize)
    _11d = ctk.CTkImage(Image.open("static/11d@2x.png"), size = ImageSize)
    _13d = ctk.CTkImage(Image.open("static/13d@2x.png"), size = ImageSize)
    _50d = ctk.CTkImage(Image.open("static/50d@2x.png"), size = ImageSize)

    _01n = ctk.CTkImage(Image.open("static/01n@2x.png"), size = ImageSize)
    _02n = ctk.CTkImage(Image.open("static/02n@2x.png"), size = ImageSize)
    _03n = ctk.CTkImage(Image.open("static/03n@2x.png"), size = ImageSize)
    _04n = ctk.CTkImage(Image.open("static/04n@2x.png"), size = ImageSize)
    _09n = ctk.CTkImage(Image.open("static/09n@2x.png"), size = ImageSize)
    _10n = ctk.CTkImage(Image.open("static/10n@2x.png"), size = ImageSize)
    _11n = ctk.CTkImage(Image.open("static/11n@2x.png"), size = ImageSize)
    _13n = ctk.CTkImage(Image.open("static/13n@2x.png"), size = ImageSize)
    _50n = ctk.CTkImage(Image.open("static/50n@2x.png"), size = ImageSize)

    return {
        "01d": _01d, "02d": _02d, "03d": _03d, "04d": _04d, "50d": _50d,
        "09d": _09d, "10d": _10d, "11d": _11d, "13d": _13d, "50n": _50n,
        "01n": _01n, "02n": _02n, "03n": _03n, "04n": _04n,
        "09n": _09n, "10n": _10n, "11n": _11n, "13n": _13n,
    }
