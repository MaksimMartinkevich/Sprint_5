from data import Url
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestConstructor:

    def test_move_to_buns(self, driver):
        driver.get(Url.MAIN_PAGE)
        driver.find_element(*Locators.FIL_SPAN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.FIL_SPAN))
        driver.find_element(*Locators.BUNS_SPAN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.BUNS_SPAN))
        assert driver.find_element(*Locators.ACTIVE_DIV_IN_CONSTRUCTOR).text == 'Булки'

    def test_move_to_sauces(self, driver):
        driver.get(Url.MAIN_PAGE)
        driver.find_element(*Locators.SAUSES_SPAN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.SAUSES_SPAN))
        assert driver.find_element(*Locators.ACTIVE_DIV_IN_CONSTRUCTOR).text == 'Соусы'

    def test_move_to_fil(self, driver):
        driver.get(Url.MAIN_PAGE)
        driver.find_element(*Locators.FIL_SPAN).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.FIL_SPAN))
        assert driver.find_element(*Locators.ACTIVE_DIV_IN_CONSTRUCTOR).text == 'Начинки'
