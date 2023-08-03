from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage


class UserSignupPage(BasePage):
    MAIL_INPUT = (By.ID, "MERGE0")
    SUBSCRIBE_FORM = (By.ID, "templateBody")
    SUBSCRIBE_BUTTON = (By.CLASS_NAME, "formEmailButton")
    SIGNUP_HEADLINE = (By.CLASS_NAME, "masthead")
    ERROR_STATUS = (By.XPATH, '//*[@id="templateBody"]/div[3]')
    ERROR_MESSAGE = (By.CLASS_NAME, "errorText")
    CONFIRM_HUMANITY = (By.TAG_NAME, "h2")

    def signup(self, mail):
        self.element(self.SUBSCRIBE_FORM).find_element(*self.MAIL_INPUT)\
            .send_keys(mail)
        self.driver.find_element(*self.SUBSCRIBE_BUTTON).click()
        return self

    def wrong_mail_signup(self, mail):
        self.signup(mail)
        self.driver.forward()
        WebDriverWait(self.driver, 5).until(EC
                                            .visibility_of_element_located(self.ERROR_MESSAGE))
        self.driver.find_element(*self.ERROR_MESSAGE)
        self.driver.find_element(*self.ERROR_STATUS)
        return self

    def correct_mail_signup(self, mail):
        self.signup(mail)
        self.driver.forward()
        WebDriverWait(self.driver, 5).until(EC
                                            .visibility_of_element_located(self.CONFIRM_HUMANITY))
        text = self.driver.find_element(*self.CONFIRM_HUMANITY).text
        assert text == 'Confirm Humanity'
        return self
