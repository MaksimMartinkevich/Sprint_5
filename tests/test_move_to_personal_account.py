from data import Data, Url
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestPersonalAccount:

    def test_move_to_personal_account(self, driver):
        driver.get(Url.MAIN_PAGE)
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_LOGIN_PAGE).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(Locators.ACCOUNT_BUTTON))
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.presence_of_element_located(Locators.HEADER_PROFILE))
        assert driver.current_url == Url.PROFILE_PAGE
