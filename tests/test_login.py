from data import Data, Url
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:

    def test_login_from_main_page(self, driver):
        driver.get(Url.MAIN_PAGE)
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_LOGIN_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert driver.find_element(*Locators.ORDER_BUTTON).is_displayed()

    def test_login_via_account_button(self, driver):
        driver.get(Url.MAIN_PAGE)
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_LOGIN_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert driver.find_element(*Locators.ORDER_BUTTON).is_displayed()

    def test_login_via_registration_page(self, driver):
        driver.get(Url.REGISTRATION_PAGE)
        driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION_PAGE).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_LOGIN_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert driver.find_element(*Locators.ORDER_BUTTON).is_displayed()

    def test_login_via_password_recovery(self, driver):
        driver.get(Url.MAIN_PAGE)
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*Locators.FORGOT_PASSWORD_BUTTON).click()
        driver.find_element(*Locators.LOGIN_BUTTON_REGISTRATION_PAGE).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_LOGIN_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        assert driver.find_element(*Locators.ORDER_BUTTON).is_displayed()
