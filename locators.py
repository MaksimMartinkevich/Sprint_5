from selenium.webdriver.common.by import By


class Locators:
    LOGO = By.XPATH, './/*[@href = "/"]' # Лого
    HEADER_PACK_BURGER = By.XPATH, './/h1[text() = "Соберите бургер"]' # Заголовок Соберите бургер
    HEADER_PROFILE = By.XPATH, './/a[text() = "Профиль"]' # Заголовок Профиль
    HEADER_LOGIN = By.XPATH, './/h2[text() = "Вход"]' # Заголовок Вход
    HEADER_REGISTRATION = By.XPATH, './/h2[text() = "Регистрация"]' # Заголовок Регистрация
    HEADER_INCORRECT_PASSWORD = By.XPATH, './/p[text() = "Некорректный пароль"]' # Валидационное сообщение "Некорректный пароль"
    HEADER_EXIST_USER = By.XPATH, './/p[text() = "Такой пользователь уже существует"]' # Валидационное сообщение "Такой пользователь уже существует"
    INPUT_NAME = By.XPATH, './/label[text() = "Имя"]/following-sibling::input' # Поле Имя
    INPUT_EMAIL = By.XPATH, './/label[text() = "Email"]/following-sibling::input' # Поле Email
    INPUT_PASSWORD = By.XPATH, './/label[text() = "Пароль"]/following-sibling::input' # Поле Password
    LOGIN_BUTTON_MAIN_PAGE = By.XPATH, './/button[text()="Войти в аккаунт"]' # Кнопка "Войти в аккаунт" на главной странице
    LOGIN_BUTTON_LOGIN_PAGE = By.XPATH, './/button[text() = "Войти"]' # Кнопка Войти на главной странице
    ORDER_BUTTON = By.XPATH, './/button[text() = "Оформить заказ"]' # Кнопка "Оформить заказ"
    ACCOUNT_BUTTON = By.XPATH, './/p[text() = "Личный Кабинет"]' # Кнопка "Личный кабинет"
    LOGIN_BUTTON_REGISTRATION_PAGE = By.XPATH, './/a[text() = "Войти"]' # Кнопка Войти (стр-ца регистрации)
    FORGOT_PASSWORD_BUTTON = By.XPATH, './/a[text() = "Восстановить пароль"]' # Кнопка Восстановить пароль
    RECOVERY_BUTTON = By.XPATH, './/button[text() = "Восстановить"]' # Кнопка Восстановить (стр-ца восстановления пароля)
    REGISTRATION_BUTTON = By.XPATH, './/button[text() = "Зарегистрироваться"]' # Кнопка Зарегистрироваться
    CONSTRUCTOR_BUTTON = By.XPATH, './/p[text() = "Конструктор"]' # Кнопка Конструктор
    LOGOUT_BUTTON = By.XPATH, './/button[text() = "Выход"]' # Кнопка Выход
    SAUSES_SPAN = By.XPATH, './/span[text() = "Соусы"]' # Вкладка Соусы
    FIL_SPAN = By.XPATH, './/span[text() = "Начинки"]' # Вкладка Начинки
    BUNS_SPAN = By.XPATH, './/span[text() = "Булки"]' # Вкладка Булки
    ACTIVE_DIV_IN_CONSTRUCTOR = By.XPATH, './/div[contains(@class, "current")]/span' # Активный раздел конструктора

