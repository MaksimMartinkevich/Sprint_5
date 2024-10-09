from data import Data, Url, RandomUser
import pytest
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestRegistration:

    def test_registration_success(self, driver):
        driver.get(Url.REGISTRATION_PAGE)
        driver.find_element(*Locators.INPUT_NAME).send_keys(RandomUser.name)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(RandomUser.email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(RandomUser.password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.HEADER_LOGIN))
        assert driver.find_element(*Locators.HEADER_LOGIN).text == 'Вход'

    def test_registration_without_name(self, driver):
        driver.get(Url.REGISTRATION_PAGE)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(RandomUser.email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(RandomUser.password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))
        assert driver.find_element(*Locators.HEADER_REGISTRATION).text == 'Регистрация'

    def test_registration_without_email(self, driver):
        driver.get(Url.REGISTRATION_PAGE)
        driver.find_element(*Locators.INPUT_NAME).send_keys(RandomUser.name)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(RandomUser.password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))
        assert driver.find_element(*Locators.HEADER_REGISTRATION).text == 'Регистрация'

    def test_registration_without_password(self, driver):
        driver.get(Url.REGISTRATION_PAGE)
        driver.find_element(*Locators.INPUT_NAME).send_keys(RandomUser.name)
        driver.find_element(*Locators.INPUT_NAME).send_keys(RandomUser.email)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.REGISTRATION_BUTTON))
        assert driver.find_element(*Locators.HEADER_REGISTRATION).text == 'Регистрация'

    @pytest.mark.parametrize('password', ['1', '12345'])
    def test_registration_password_less_6_symbols(self, driver, password):
        driver.get(Url.REGISTRATION_PAGE)
        driver.find_element(*Locators.INPUT_NAME).send_keys(RandomUser.name)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(RandomUser.email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.HEADER_INCORRECT_PASSWORD))
        assert driver.find_element(*Locators.HEADER_INCORRECT_PASSWORD).text == 'Некорректный пароль'

    @pytest.mark.parametrize('email', ['@gmail.com', 'm.martinkevich_1999'])
    def test_registration_with_incorrect_email(self, driver, email):
        driver.get(Url.REGISTRATION_PAGE)
        driver.find_element(*Locators.INPUT_NAME).send_keys(RandomUser.name)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(email)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(RandomUser.password)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(Locators.HEADER_EXIST_USER))
        assert driver.find_element(*Locators.HEADER_EXIST_USER).text == 'Такой пользователь уже существует'

    def test_registration_with_exist_user(self, driver):
        driver.get(Url.REGISTRATION_PAGE)
        driver.find_element(*Locators.INPUT_NAME).send_keys(Data.NAME)
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 6).until(expected_conditions.visibility_of_element_located(Locators.HEADER_EXIST_USER))
        assert driver.find_element(*Locators.HEADER_EXIST_USER).text == 'Такой пользователь уже существует'
