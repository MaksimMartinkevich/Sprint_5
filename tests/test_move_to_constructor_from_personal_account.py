from data import Data, Url
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructorCross:

    def test_move_to_constructor_from_account_by_click_on_constructor(self, driver):
        driver.get(Url.MAIN_PAGE)
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_LOGIN_PAGE).click()
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.HEADER_PROFILE))
        driver.find_element(*Locators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.HEADER_PACK_BURGER))
        assert driver.find_element(*Locators.HEADER_PACK_BURGER).is_displayed()

    def test_move_to_constructor_from_account_by_click_on_logo(self, driver):
        driver.get(Url.MAIN_PAGE)
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        driver.find_element(*Locators.INPUT_EMAIL).send_keys(Data.EMAIL)
        driver.find_element(*Locators.INPUT_PASSWORD).send_keys(Data.PASSWORD)
        driver.find_element(*Locators.LOGIN_BUTTON_LOGIN_PAGE).click()
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.HEADER_PROFILE))
        driver.find_element(*Locators.LOGO).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.HEADER_PACK_BURGER))
        assert driver.find_element(*Locators.HEADER_PACK_BURGER).is_displayed()
