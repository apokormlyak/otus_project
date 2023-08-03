from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class ProjectsPage(BasePage):
    URL = 'projects'
    PAGE_NAME = (By.XPATH, '//h1[contains(text(), "Projects")]')

    def get_page_name(self):
        self.driver.find_element(*self.PAGE_NAME)
        return self
