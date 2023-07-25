from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def element(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5)\
                .until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise AssertionError(f'Не дождались видимости элемента {locator}')

    def elements(self, locator: tuple):
        try:
            return WebDriverWait(self.driver, 5)\
                .until(EC.visibility_of_all_elements_located(locator))
        except TimeoutException:
            raise AssertionError(f'Не дождались видимости элемента {locator}')
