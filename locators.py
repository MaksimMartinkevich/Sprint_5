from selenium.webdriver.common.by import By


class Locators:
    logo = By.XPATH, './/*[@href = "/"]' # Лого
    header_pack_burger = By.XPATH, './/h1[text() = "Соберите бургер"]' # Заголовок Соберите бургер
    header_profile = By.XPATH, './/a[text() = "Профиль"]' # Заголовок Профиль
    header_login = By.XPATH, './/h2[text() = "Вход"]' # Заголовок Вход
    header_registration = By.XPATH, './/h2[text() = "Регистрация"]' # Заголовок Регистрация
    header_incorrect_password = By.XPATH, './/p[text() = "Некорректный пароль"]' # Валидационное сообщение "Некорректный пароль"
    header_exist_user = By.XPATH, './/p[text() = "Такой пользователь уже существует"]' # Валидационное сообщение "Такой пользователь уже существует"
    input_name = By.XPATH, './/label[text() = "Имя"]/following-sibling::input' # Поле Имя
    input_email = By.XPATH, './/label[text() = "Email"]/following-sibling::input' # Поле Email
    input_password = By.XPATH, './/label[text() = "Пароль"]/following-sibling::input' # Поле Password
    login_button_main_page = By.XPATH, './/button[text()="Войти в аккаунт"]' # Кнопка "Войти в аккаунт" на главной странице
    login_button_login_page = By.XPATH, './/button[text() = "Войти"]' # Кнопка Войти на главной странице
    order_button = By.XPATH, './/button[text() = "Оформить заказ"]' # Кнопка "Оформить заказ"
    account_button = By.XPATH, './/p[text() = "Личный Кабинет"]' # Кнопка "Личный кабинет"
    login_button_registration_page = By.XPATH, './/a[text() = "Войти"]' # Кнопка Войти (стр-ца регистрации)
    forgot_password_button = By.XPATH, './/a[text() = "Восстановить пароль"]' # Кнопка Восстановить пароль
    recovery_button = By.XPATH, './/button[text() = "Восстановить"]' # Кнопка Восстановить (стр-ца восстановления пароля)
    registration_button = By.XPATH, './/button[text() = "Зарегистрироваться"]' # Кнопка Зарегистрироваться
    constructor_button = By.XPATH, './/p[text() = "Конструктор"]' # Кнопка Конструктор
    logout_button = By.XPATH, './/button[text() = "Выход"]' # Кнопка Выход
    sauces_span = By.XPATH, './/span[text() = "Соусы"]' # Вкладка Соусы
    fil_span = By.XPATH, './/span[text() = "Начинки"]' # Вкладка Начинки
    buns_span = By.XPATH, './/span[text() = "Булки"]' # Вкладка Булки
    active_div_in_constructor = By.XPATH, './/div[contains(@class, "current")]/span' # Активный раздел конструктора

