from random import randint


class Url:
    main_page = "https://stellarburgers.nomoreparties.site/"
    login_page = f"{main_page}login"
    registration_page = f"{main_page}register"
    profile_page = f"{main_page}account/profile"


class Data:
    name = 'Maksim'
    email = 'm.martinkevich_1999@gmail.com'
    password = '123456'


class RandomUser:
    name = f"nickname{randint(0, 999)}"
    email = f"random{randint(000, 999)}mail@gmail.com"
    password = f"psw{randint(000, 999)}"