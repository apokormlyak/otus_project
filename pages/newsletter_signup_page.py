from pages.home_page import BasePage
from selenium.webdriver.common.by import By


class UserLoginPage(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    LOGO = (By.XPATH, "//img[@title='OpenCart']")
    LINK = (By.LINK_TEXT, "OpenCart")

    def login(self, username, password):
        self.element(self.SUBMIT_BUTTON).find_element(*self.USERNAME_INPUT)\
            .send_keys(username)
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(password)
        self.driver.find_element(*self.SUBMIT_BUTTON).click()
        return self
