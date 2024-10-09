# Sprint_5 UI-testing for Stellar Burgers website

## Tests Directory - сценарии, покрытые тестами

### test_registration.py - Регистрация пользователя

1. test_registration_success - успешная регистрация пользователя
2. test_registration_without_name - регистрация без указания имени
3. test_registration_without_email - регистрация без указания email
4. test_registration_without_password - регистрация без указания пароля
5. test_registration_password_less_6_symbols - регистрация с невалидным паролем (меньше 6 символов)
6. test_registration_with_incorrect_email - регистрация с некорректным email
7. test_registration_with_exist_user - регистрация по данным существующего пользователя

### test_login.py - Авторизация

1. test_login_from_main_page - авторизация с главной страницы
2. test_login_via_account_button - вход через кнопку Личный кабинет
3. test_login_via_registration_page - вход через форму регистрации
4. test_login_via_password_recovery - вход через форму восстановления пароля

### test_logout.py - Выход из аккаунта

1. test_logout - выход по кнопке Выйти в личном кабинете

### test_move_to_personal_account.py - Переход в личный кабинет

1. test_move_to_personal_account - переход по клику на кнопку Личный кабинет

### test_move_to_constructor_from_personal_account.py - Переход из личного кабинета в конструктор

1. test_move_to_constructor_from_account_by_click_on_constructor - переход по клику на Конструктор
2. test_move_to_constructor_from_account_by_click_on_logo - переход по клику на логотип Stellar Burgers

### test_constructor.py - Переходы в конструкторе

1. test_go_to_buns - переход к разделу Булки
2. test_go_to_sauces - переход к разделу Соусы
3. test_go_to_fil - переход к разделу Начинки

## data.py - Тестовые данные пользователя, URL, Генератор данных пользователя

1. class Url - список URLs страниц
2. class Data - валидные данные пользователя (созданный)
3. class RandomUser - генератор данных пользователя

## conftest.py - Фикстуры

1. driver - настройки webdriver



