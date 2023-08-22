from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class AboutPage(BasePage):
    URL = 'about'
    PAGE_NAME = (By.XPATH, '//h1[contains(text(), "About")]')

    def get_page_name(self):
        self.driver.find_element(*self.PAGE_NAME)
        return self
