from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class DocsPage(BasePage):
    URL = 'documentation'
    PAGE_NAME = (By.XPATH, '//h1[contains(text(), "Documentation")]')
    SINGLE_BREWERY_BUTTON = (By.LINK_TEXT, "Single Brewery")
    LIST_BREWERIES_BUTTON = (By.LINK_TEXT, 'List Breweries')
    RANDOM_BREWERY_BUTTON = (By.LINK_TEXT, 'Random Brewery')
    SEARCH_BREWERIES_BUTTON = (By.LINK_TEXT, 'Search Breweries')
    METADATA_BUTTON = (By.LINK_TEXT, 'Metadata')
    RUN_BUTTON = (By.XPATH, '//button[contains(text(), "Run")]')

    def get_page_name(self):
        self.driver.find_element(*self.PAGE_NAME)
        return self

    def get_run_button(self):
        self.driver.find_element(*self.RUN_BUTTON)
        return self

    def get_navigation_buttons(self):
        self.driver.find_element(*self.SINGLE_BREWERY_BUTTON)
        self.driver.find_element(*self.LIST_BREWERIES_BUTTON)
        self.driver.find_element(*self.RANDOM_BREWERY_BUTTON)
        self.driver.find_element(*self.SEARCH_BREWERIES_BUTTON)
        self.driver.find_element(*self.METADATA_BUTTON)
        return self
