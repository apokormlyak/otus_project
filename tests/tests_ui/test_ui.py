from data_store import products, users
from pages.page_factory import NewProduct
from pages.brewerie_page import Admin
from pages.currency_box import CurrencyBox
from pages.registration_page import NewUser
from pages.newsletter_signup_page import UserLoginPage
import allure


@allure.title("Тест: авторизация пользователя")
def test_user_login_page(browser, url):
    browser.get(url=url+'index.php?route=account/login')
    UserLoginPage(browser).login(username=users.get_username(),
                                 password=users.get_password())


@allure.title("Тест: добавление товара")
def test_add_new_product(browser, url):
    browser.get(url=url+'admin')
    Admin(browser).login(username=users.get_username('admin'),
                         password=users.get_password('admin'))
    Admin(browser).open_product_list()
    Admin(browser).add_product()
    product = products.get_product()
    NewProduct(browser).fill_product_name(product['name'], product['meta'])
    NewProduct(browser).fill_product_model(product['model'])
    NewProduct(browser).save_new_product()


@allure.title("Тест: удаление товара")
def test_delete_product(browser, url):
    browser.get(url=url+'admin')
    Admin(browser).login(username=users.get_username('admin'),
                         password=users.get_password('admin'))
    Admin(browser).open_product_list()
    Admin(browser).delete_product()


@allure.title("Тест: регистрация нового пользователя")
def test_register_new_user(browser, url):
    browser.get(url=url+'index.php?route=account/register')
    user = users.get_new_user()
    NewUser(browser).fill_personal_details(firstname=user['firstname'],
                                           lastname=user['lastname'],
                                           email=user['email'],
                                           telephone=user['telephone'])
    NewUser(browser).fill_password_fields(password=user['password'])
    NewUser(browser).submit()


@allure.title("Тест: выбор валюты")
def test_change_currency(browser, url):
    browser.get(url=url)
    CurrencyBox(browser).open_currency_box()
    usd = CurrencyBox(browser).usd
    gbp = CurrencyBox(browser).gbp
    eur = CurrencyBox(browser).eur
