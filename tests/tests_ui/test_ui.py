import time

from tests.tests_ui.data_store import urls, users
from pages.home_page import HomePage
from pages.page_factory import CommonFooter, CommonHeader
from pages.newsletter_signup_page import UserSignupPage
from pages.brewerie_page import BreweriesPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


@allure.title("Тест: успешная подписка")
def test_correct_mail_signup(browser):
    browser.get(urls.SIGNUP_PAGE_URL)
    UserSignupPage(browser).correct_mail_signup(users.get_correct_email())


@allure.title("Тест: неуспешная подписка")
def test_wrong_mail_signup(browser):
    browser.get(urls.SIGNUP_PAGE_URL)
    UserSignupPage(browser).wrong_mail_signup(users.get_wrong_email())


@allure.title("Тест: главная страница")
def test_check_homepage_elements(browser, url):
    browser.get(url=url)
    HomePage(browser).check_homepage_elements()
    HomePage(browser).get_button_to_documentation()
    browser.forward()
    WebDriverWait(browser, 5).until(EC.url_contains("documentation"))
    browser.back()
    CommonHeader(browser).check_common_header()
    CommonFooter(browser).check_common_footer()


@allure.title("Тест: brewery page")
def test_brewery_page(browser, url):
    browser.get(url=url+BreweriesPage(browser).URL)
    random_brewery = BreweriesPage(browser).get_random_brewery().text
    browser.get(url=url+BreweriesPage(browser).URL+'/' + random_brewery)
    browser.forward()



