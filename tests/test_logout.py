from data import Data, Url
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogout:

    def test_logout(self, driver):
        driver.get(Url.MAIN_PAGE)
        driver.find_element(*Locators.LOGIN_BUTTON_MAIN_PAGE).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_LOGIN_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.ORDER_BUTTON))
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.HEADER_PROFILE))
        driver.find_element(*Locators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.HEADER_LOGIN))
        assert driver.current_url == Url.LOGIN_PAGE
