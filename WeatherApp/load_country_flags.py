import customtkinter as ctk
from PIL import Image


def load_country_flags() -> dict[str, ctk.CTkImage]:
    """LOADING AND RETURNING A DICT CONTAINING THE COUNTRY CODES
        AND THE RENDERED FLAGS"""

    ImageSize = (90, 50)

    bg = ctk.CTkImage(Image.open("static/bg.jpg"), size = ImageSize)
    de = ctk.CTkImage(Image.open("static/de.png"), size = ImageSize)
    gr = ctk.CTkImage(Image.open("static/gr.png"), size = ImageSize)
    fr = ctk.CTkImage(Image.open("static/fr.png"), size = ImageSize)
    ch = ctk.CTkImage(Image.open("static/ch.jpg"), size = ImageSize)
    dk = ctk.CTkImage(Image.open("static/dk.png"), size = ImageSize)
    fi = ctk.CTkImage(Image.open("static/fi.png"), size = ImageSize)
    gb = ctk.CTkImage(Image.open("static/gb.png"), size = ImageSize)
    nl = ctk.CTkImage(Image.open("static/nl.jpg"), size = ImageSize)
    no = ctk.CTkImage(Image.open("static/no.png"), size = ImageSize)
    ru = ctk.CTkImage(Image.open("static/ru.jpg"), size = ImageSize)
    se = ctk.CTkImage(Image.open("static/se.jpg"), size = ImageSize)
    es = ctk.CTkImage(Image.open("static/es.jpg"), size = ImageSize)
    it = ctk.CTkImage(Image.open("static/it.png"), size = ImageSize)
    tr = ctk.CTkImage(Image.open("static/tr.jpg"), size = ImageSize)
    at = ctk.CTkImage(Image.open("static/at.png"), size = ImageSize)
    be = ctk.CTkImage(Image.open("static/be.JPG"), size = ImageSize)
    cz = ctk.CTkImage(Image.open("static/cz.png"), size = ImageSize)
    ee = ctk.CTkImage(Image.open("static/ee.JPG"), size = ImageSize)
    lt = ctk.CTkImage(Image.open("static/lt.png"), size = ImageSize)
    lv = ctk.CTkImage(Image.open("static/lv.jpg"), size = ImageSize)
    ro = ctk.CTkImage(Image.open("static/ro.png"), size = ImageSize)
    pt = ctk.CTkImage(Image.open("static/pt.png"), size = ImageSize)
    cn = ctk.CTkImage(Image.open("static/cn.png"), size = ImageSize)
    kr = ctk.CTkImage(Image.open("static/kr.jpg"), size = ImageSize)
    jp = ctk.CTkImage(Image.open("static/jp.png"), size = ImageSize)
    tw = ctk.CTkImage(Image.open("static/tw.JPG"), size = ImageSize)
    us = ctk.CTkImage(Image.open("static/us.png"), size = ImageSize)
    ca = ctk.CTkImage(Image.open("static/ca.JPG"), size = ImageSize)
    au = ctk.CTkImage(Image.open("static/au.png"), size = ImageSize)
    hu = ctk.CTkImage(Image.open("static/hu.png"), size = ImageSize)
    ie = ctk.CTkImage(Image.open("static/ie.png"), size = ImageSize)
    pl = ctk.CTkImage(Image.open("static/pl.JPG"), size = ImageSize)
    sk = ctk.CTkImage(Image.open("static/sk.png"), size = ImageSize)
    ua = ctk.CTkImage(Image.open("static/ua.JPG"), size = ImageSize)

    return {
        "BG": bg, "CH": ch, "DK": dk, "FI": fi, "AT": at, "TW": tw, "HU": hu,
        "DE": de, "GB": gb, "NL": nl, "NO": no, "BE": be, "PT": pt, "IE": ie,
        "GR": gr, "RU": ru, "SE": se, "TR": tr, "CZ": cz, "US": us, "PL": pl,
        "FR": fr, "ES": es, "IT": it, "EE": ee, "LT": lt, "CA": ca, "SK": sk,
        "LV": lv, "RO": ro, "CN": cn, "KR": kr, "JP": jp, "AU": au, "UA": ua
    }
