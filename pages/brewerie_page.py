from pages.base_page import BasePage
from selenium.webdriver.common.by import By
import random


class BreweriesPage(BasePage):
    URL = 'breweries'
    LIST_OF_BREWERIES = (By.TAG_NAME, 'li')
    BREWERIES_ON_PAGE = (By.TAG_NAME, 'p')
    BREWERIES_TABLE = (By.TAG_NAME, 'table')
    NEXT_PAGE_BUTTON = (By.LINK_TEXT, 'Next')
    PREVIOUS_PAGE_BUTTON = (By.LINK_TEXT, 'Previous')

    def get_list_of_breweries(self):
        return self.driver.find_elements(*self.LIST_OF_BREWERIES)

    def get_random_brewery(self):
        return random.choice(self.get_list_of_breweries())
