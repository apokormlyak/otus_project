from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class HomePage(BasePage):
    IMAGE = (By.TAG_NAME, 'img')
    HEADLINE_TEXT = (By.TAG_NAME, "h1")
    PARAGRAPHS = (By.TAG_NAME, "p")
    HEADLINE2_TEXT = (By.TAG_NAME, "h2")
    BUTTON_TO_DOCUMENTATION = (By.LINK_TEXT, "Read API Documentation")

    def get_image(self):
        self.driver.find_element(*self.IMAGE)
        return self

    def get_headline_text(self):
        self.driver.find_elements(*self.HEADLINE_TEXT)
        return self

    def get_headline2_text(self):
        self.driver.find_elements(*self.HEADLINE2_TEXT)
        return self

    def get_all_paragraphs_text(self):
        self.driver.find_elements(*self.PARAGRAPHS)
        return self

    def get_button_to_documentation(self):
        self.driver.find_element(*self.BUTTON_TO_DOCUMENTATION).click()

    def check_homepage_elements(self):
        self.get_image()
        self.get_headline_text()
        self.get_headline2_text()
        self.get_all_paragraphs_text()
