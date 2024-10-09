from random import randint


class Url:
    MAIN_PAGE = "https://stellarburgers.nomoreparties.site/"
    LOGIN_PAGE = f"{MAIN_PAGE}login"
    REGISTRATION_PAGE = f"{MAIN_PAGE}register"
    PROFILE_PAGE = f"{MAIN_PAGE}account/profile"


class Data:
    NAME = 'Maksim'
    EMAIL = 'm.martinkevich_1999@gmail.com'
    PASSWORD = '123456'


class RandomUser:
    name = f"nickname{randint(0, 999)}"
    email = f"random{randint(000, 999)}mail@gmail.com"
    password = f"psw{randint(000, 999)}"