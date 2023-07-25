from pages.home_page import BasePage
from selenium.webdriver.common.by import By


class CommonHeader(BasePage):
    LOGO = (By.CSS_SELECTOR, "#logo")
    SEARCH_INPUT = (By.NAME, "search")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[type='button']")
    CART = (By.ID, "cart")
    DROPDOWNS = (By.CLASS_NAME, "dropdown")


class NewProduct(BasePage):
    GENERAL_TAB = (By.LINK_TEXT, '#tab-general')
    DATA_TAB = (By.LINK_TEXT, '#tab-data')
    PRODUCT_NAME = (By.ID, 'input-name1')
    PRODUCT_META = (By.ID, 'input-meta-title1')
    PRODUCT_MODEL = (By.ID, 'input-model')
    SAVE_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def fill_product_name(self, name, meta):
        self.element(self.GENERAL_TAB).find_element(*self.PRODUCT_NAME)\
            .send_keys(name)
        self.driver.find_element(*self.PRODUCT_NAME).send_keys(name)
        self.driver.find_element(*self.PRODUCT_META).send_keys(meta)
        return self

    def fill_product_model(self, model):
        self.element(self.DATA_TAB).find_element(*self.PRODUCT_MODEL)\
            .send_keys(model)
        return self

    def save_new_product(self):
        self.driver.find_element(*self.SAVE_BUTTON)\
            .click()
        return self
