from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Admin(BasePage):
    USERNAME_INPUT = (By.CSS_SELECTOR, "#input-username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    FORGOTTEN_PASSWORD = (By.LINK_TEXT, "Forgotten Password")
    CATALOG = (By.CSS_SELECTOR, '#menu-catalog')
    COLLAPSE_MENU = (By.CSS_SELECTOR, 'collapse1')
    PRODUCTS = (By.CLASS_NAME, 'active')
    PRODUCT_PANEL = (By.CLASS_NAME, 'panel_body')
    PRODUCT_CHECK_BOX = (By.NAME, 'selected[]')
    ADD_PRODUCT_BUTTON = (By.XPATH, '//*[@title="Add New"]')
    DELETE_PRODUCT_BUTTON = (By.XPATH, '//*[@title="Delete"]')

    def login(self, username, password):
        self.element(self.LOGIN_BUTTON).find_element(*self.USERNAME_INPUT)\
            .send_keys(username)
        self.driver.find_element(*self.USERNAME_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return self

    def open_product_list(self):
        self.driver.find_element(*self.CATALOG).click()
        self.element(self.COLLAPSE_MENU).find_element(*self.PRODUCTS).click()
        return self

    def add_product(self):
        self.element(self.PRODUCT_PANEL).find_element(*self.PRODUCTS).click()
        return self

    def delete_product(self):
        self.element(self.PRODUCT_PANEL).find_element(*self.PRODUCT_CHECK_BOX)\
            .click()
        self.driver.find_element(*self.DELETE_PRODUCT_BUTTON).click()
        return self
