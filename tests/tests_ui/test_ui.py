import logging

import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from pages.about_page import AboutPage
from pages.brewerie_page import BreweriesPage
from pages.docs_page import DocsPage
from pages.faq_page import FaqPage
from pages.home_page import HomePage
from pages.newsletter_signup_page import UserSignupPage
from pages.page_factory import CommonFooter, CommonHeader
from pages.projects_page import ProjectsPage
from tests.tests_ui.data_store import urls, users

logger = logging.getLogger(__name__)


@allure.title("Тест: успешная подписка")
@allure.tag('UI')
def test_correct_mail_signup(browser):
    browser.get(urls.SIGNUP_PAGE_URL)
    with allure.step('Поиск сообщения при корректном входе'):
        try:
            UserSignupPage(browser).correct_mail_signup(users.get_correct_email())
        except NoSuchElementException as er:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(er.msg)


@allure.title("Тест: неуспешная подписка")
@allure.tag('UI')
def test_wrong_mail_signup(browser):
    browser.get(urls.SIGNUP_PAGE_URL)
    with allure.step('Поиск сообщения при некорректном входе'):
        try:
            UserSignupPage(browser).wrong_mail_signup(users.get_wrong_email())
        except NoSuchElementException as er:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(er.msg)


@allure.title("Тест: главная страница")
@allure.tag('UI')
def test_check_homepage_elements(browser, url):
    browser.get(url=url)
    with allure.step('Поиск основных элементов на главной странице'):
        try:
            HomePage(browser).check_homepage_elements()
            HomePage(browser).get_button_to_documentation()
        except NoSuchElementException as er:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(er.msg)
        browser.forward()
        WebDriverWait(browser, 5).until(EC.url_contains("documentation"))
        browser.back()
        with allure.step('Поиск элементов хэддера и футэра'):
            try:
                CommonHeader(browser).check_common_header()
                CommonFooter(browser).check_common_footer()
            except NoSuchElementException as er:
                allure.attach(
                    body=browser.get_screenshot_as_png(),
                    name="screenshot_image",
                    attachment_type=allure.attachment_type.PNG)
                raise AssertionError(er.msg)


@allure.title("Тест: brewery page")
@allure.tag('UI')
def test_brewery_page(browser, url):
    browser.get(url=url+BreweriesPage(browser).URL)
    with allure.step('Поиск элементов на странице brewery'):
        try:
            random_brewery = BreweriesPage(browser).get_random_brewery().text
            browser.get(url=url+BreweriesPage(browser).URL+'/' + random_brewery)
            browser.forward()
            WebDriverWait(browser, 5)
            brewery_title = BreweriesPage(browser).get_title_of_brewery_page().text
            brewery_title = brewery_title.replace('Breweries in ', '')
            assert random_brewery == brewery_title

            breweries_on_page = BreweriesPage(browser).get_breweries_on_page().text
            pages_count = breweries_on_page.split()[-1][0]
            BreweriesPage(browser).get_brewery_table()
            if int(pages_count) == 1:
                try:
                    BreweriesPage(browser).get_next_page_button()
                except NoSuchElementException as e:
                    logger.info(e)
            else:
                BreweriesPage(browser).get_next_page_button()
                browser.back()
                WebDriverWait(browser, 10).until(EC.element_to_be_clickable(BreweriesPage(browser)
                                                                            .get_previous_page_button()))
                BreweriesPage(browser).get_previous_page_button()
                browser.back()
        except NoSuchElementException as er:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(er.msg)

    with allure.step('Поиск элементов хэддера и футэра'):
        try:
            CommonHeader(browser).check_common_header()
            CommonFooter(browser).check_common_footer()
        except NoSuchElementException as er:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(er.msg)


@allure.title("Тест: docs page")
@allure.tag('UI')
def test_docs_page(browser, url):
    browser.get(url=url + DocsPage(browser).URL)
    with allure.step('Поиск элементов на странице документации'):
        try:
            DocsPage(browser).get_page_name()
            DocsPage(browser).get_navigation_buttons()
            CommonHeader(browser).check_common_header()
            CommonFooter(browser).check_common_footer()
        except NoSuchElementException as er:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(er.msg)


@allure.title("Тест: faq page")
@allure.tag('UI')
def test_faq_page(browser, url):
    browser.get(url=url + FaqPage(browser).URL)
    with allure.step('Поиск элементов на странице Вопрос-ответ'):
        try:
            FaqPage(browser).get_page_name()
            CommonHeader(browser).check_common_header()
            CommonFooter(browser).check_common_footer()
        except NoSuchElementException as er:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(er.msg)


@allure.title("Тест: projects page")
@allure.tag('UI')
def test_projects_page(browser, url):
    browser.get(url=url + ProjectsPage(browser).URL)
    with allure.step('Поиск элементов на странице Проекты'):
        try:
            ProjectsPage(browser).get_page_name()
            CommonHeader(browser).check_common_header()
            CommonFooter(browser).check_common_footer()
        except NoSuchElementException as er:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(er.msg)


@allure.title("Тест: about page")
@allure.tag('UI')
def test_about_page(browser, url):
    browser.get(url=url + AboutPage(browser).URL)
    with allure.step('Поиск элементов на странице About'):
        try:
            AboutPage(browser).get_page_name()
            CommonHeader(browser).check_common_header()
            CommonFooter(browser).check_common_footer()
        except NoSuchElementException as er:
            allure.attach(
                body=browser.get_screenshot_as_png(),
                name="screenshot_image",
                attachment_type=allure.attachment_type.PNG)
            raise AssertionError(er.msg)
