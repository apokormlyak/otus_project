from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    IMAGE = (By.CLASS_NAME, '#tab-general')
    HEADLINE_TEXT_1 = (By.CLASS_NAME, "block xl:inline")
    HEADLINE_TEXT_2 = (By.CLASS_NAME, "block text-yellow-600 xl:inline")
    PARAGRAPHS = (By.CLASS_NAME, "mt-3 max-w-md mx-auto text-base text-gray-500 "
                                 "sm:text-lg md:mt-5 md:text-xl md:max-w-3xl")
    HEADLINE2_TEXT = (By.CLASS_NAME, "mt-6 tracking-tight font-extrabold "
                                     "text-gray-900 sm:text-3xl md:text-4xl")
    BUTTON_TO_DOCUMENTATION = (By.CLASS_NAME, "rounded-md shadow")

    # def fill_product_name(self, name, meta):
    #     self.element(self.GENERAL_TAB).find_element(*self.PRODUCT_NAME)\
    #         .send_keys(name)
    #     self.driver.find_element(*self.PRODUCT_NAME).send_keys(name)
    #     self.driver.find_element(*self.PRODUCT_META).send_keys(meta)
    #     return self
    #
    # def fill_product_model(self, model):
    #     self.element(self.DATA_TAB).find_element(*self.PRODUCT_MODEL)\
    #         .send_keys(model)
    #     return self
    #
    # def save_new_product(self):
    #     self.driver.find_element(*self.SAVE_BUTTON)\
    #         .click()
    #     return self
