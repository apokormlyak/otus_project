from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class FaqPage(BasePage):
    URL = 'faq'
    PAGE_NAME = (By.XPATH, '//h1[contains(text(), "Frequently Asked Questions")]')

    def get_page_name(self):
        self.driver.find_element(*self.PAGE_NAME)
        return self
