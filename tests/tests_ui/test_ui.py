from tests.tests_ui.data_store import urls, users
from pages.home_page import HomePage
from pages.page_factory import CommonFooter, CommonHeader
from pages.newsletter_signup_page import UserSignupPage
import allure


# @allure.title("Тест: успешная подписка")
# def test_correct_mail_signup(browser):
#     browser.get(urls.SIGNUP_PAGE_URL)
#     UserSignupPage(browser).correct_mail_signup('apokormlyak@yandex.ru')
#
#
# @allure.title("Тест: неуспешная подписка")
# def test_wrong_mail_signup(browser):
#     browser.get(urls.SIGNUP_PAGE_URL)
#     UserSignupPage(browser).wrong_mail_signup('apokormlyak@u')


@allure.title("Тест: главная страница")
def test_add_new_product(browser, url):
    browser.get(url=url)
    CommonHeader(browser).check_common_header()
    CommonFooter(browser).check_common_footer()

#
#
# @allure.title("Тест: удаление товара")
# def test_delete_product(browser, url):
#     browser.get(url=url+'admin')
#     Admin(browser).login(username=users.get_username('admin'),
#                          password=users.get_password('admin'))
#     Admin(browser).open_product_list()
#     Admin(browser).delete_product()
#
#
# @allure.title("Тест: регистрация нового пользователя")
# def test_register_new_user(browser, url):
#     browser.get(url=url+'index.php?route=account/register')
#     user = users.get_new_user()
#     NewUser(browser).fill_personal_details(firstname=user['firstname'],
#                                            lastname=user['lastname'],
#                                            email=user['email'],
#                                            telephone=user['telephone'])
#     NewUser(browser).fill_password_fields(password=user['password'])
#     NewUser(browser).submit()
#
#
# @allure.title("Тест: выбор валюты")
# def test_change_currency(browser, url):
#     browser.get(url=url)
#     CurrencyBox(browser).open_currency_box()
#     usd = CurrencyBox(browser).usd
#     gbp = CurrencyBox(browser).gbp
#     eur = CurrencyBox(browser).eur
