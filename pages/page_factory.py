from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CommonHeader(BasePage):
    LOGO = (By.TAG_NAME, "img")
    NEWSLETTER_SIGNUP_BUTTON = (By.LINK_TEXT, "Newsletter Signup")
    BREWERIES_PAGE = (By.LINK_TEXT, 'Breweries')
    DOCS_PAGE = (By.LINK_TEXT, 'Docs')
    FAQ_PAGE = (By.LINK_TEXT, 'FAQ')
    PROJECTS_PAGE = (By.LINK_TEXT, 'Projects')
    ABOUT_PAGE = (By.LINK_TEXT, 'About')

    def get_logo(self):
        self.driver.find_element(*self.LOGO).click()
        return self

    def get_navigation_menu(self):
        self.driver.find_element(*self.BREWERIES_PAGE).click()
        self.driver.find_element(*self.DOCS_PAGE).click()
        self.driver.find_element(*self.FAQ_PAGE).click()
        self.driver.find_element(*self.PROJECTS_PAGE).click()
        self.driver.find_element(*self.ABOUT_PAGE).click()
        return self

    def get_newsletter_signup_button(self):
        self.driver.find_element(*self.NEWSLETTER_SIGNUP_BUTTON).click()
        return self

    def check_common_header(self):
        self.get_logo()
        self.get_navigation_menu()
        self.get_newsletter_signup_button()
        self.driver.back()
        return self


class CommonFooter(BasePage):
    FOOTER_TEXT = (By.TAG_NAME, "p")
    HOME_PAGE = (By.LINK_TEXT, 'Home')
    DOCS_PAGE = (By.LINK_TEXT, 'Docs')
    FAQ_PAGE = (By.LINK_TEXT, 'FAQ')
    PROJECTS_PAGE = (By.LINK_TEXT, 'Projects')
    ABOUT_PAGE = (By.LINK_TEXT, 'About')
    TWITTER_LINK = (By.LINK_TEXT, 'Twitter')
    GITHUB_LINK = (By.LINK_TEXT, 'GitHub')
    DISCORD_LINK = (By.LINK_TEXT, 'Discord')

    def get_footer_text(self):
        self.driver.find_element(*self.FOOTER_TEXT)
        return self

    def get_footer_navigation_menu(self):
        self.driver.find_element(*self.HOME_PAGE).click()
        self.driver.find_element(*self.DOCS_PAGE).click()
        self.driver.find_element(*self.FAQ_PAGE).click()
        self.driver.find_element(*self.PROJECTS_PAGE).click()
        self.driver.find_element(*self.ABOUT_PAGE).click()
        return self

    def get_social_links_menu(self):
        self.driver.find_element(*self.TWITTER_LINK).click()
        self.driver.back()
        self.driver.find_element(*self.GITHUB_LINK).click()
        self.driver.back()
        self.driver.find_element(*self.DISCORD_LINK).click()
        return self

    def check_common_footer(self):
        self.get_footer_text()
        self.get_footer_navigation_menu()
        self.get_social_links_menu()
        return self
