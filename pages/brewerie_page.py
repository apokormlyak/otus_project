import random

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class BreweriesPage(BasePage):
    URL = 'breweries'
    LIST_OF_BREWERIES = (By.TAG_NAME, 'li')
    BREWERY_NAME = (By.XPATH, '//h1[contains(text(), "Breweries in")]')
    BREWERIES_ON_PAGE = (By.XPATH, '//p[contains(text(), "1 - ")]')
    BREWERIES_TABLE = (By.TAG_NAME, 'table')
    NEXT_PAGE_BUTTON = (By.LINK_TEXT, 'Next')
    PREVIOUS_PAGE_BUTTON = (By.LINK_TEXT, 'Previous')

    def get_list_of_breweries(self):
        return self.driver.find_elements(*self.LIST_OF_BREWERIES)

    def get_random_brewery(self):
        return random.choice(self.get_list_of_breweries())

    def get_title_of_brewery_page(self):
        return self.driver.find_element(*self.BREWERY_NAME)

    def get_breweries_on_page(self):
        return self.driver.find_element(*self.BREWERIES_ON_PAGE)

    def get_next_page_button(self):
        self.driver.find_element(*self.NEXT_PAGE_BUTTON).click()
        return self

    def get_previous_page_button(self):
        self.driver.find_element(*self.PREVIOUS_PAGE_BUTTON).click()
        return self

    def get_brewery_table(self):
        self.driver.find_element(*self.BREWERIES_TABLE)
        return self
