import random

USERNAME = 'bn_opencart'
PASSWORD = 'test'
ADMIN_USERNAME = 'user'
ADMIN_PASSWORD = 'bitnami'

users = [
    {'firstname': 'name1', 'lastname': 'meta1', 'email': 'model@1',
     'phone': 'phone1', 'password': 'password1'},
    {'firstname': 'name2', 'lastname': 'meta2', 'email': 'model@mail2.ua',
     'phone': 'phone2', 'password': 'password2'},
    {'firstname': 'name3', 'lastname': 'meta3', 'email': 'model@3',
     'phone': 'phone3', 'password': 'password3'},
    {'firstname': 'name4', 'lastname': 'meta4', 'email': 'mail4.ua',
     'phone': 'phone4', 'password': 'password4'},
    {'firstname': 'name5', 'lastname': 'meta5', 'email': 'model@mail5.ua',
     'phone': 'phone5', 'password': 'password5'},
    {'firstname': 'name6', 'lastname': 'meta6', 'email': 'model@m',
     'phone': 'phone6', 'password': 'password6'},
]


def get_new_user():
    return random.choice(users)


def get_username(user=None):
    if user == 'admin':
        return ADMIN_USERNAME
    else:
        return USERNAME


def get_password(user=None):
    if user == 'admin':
        return ADMIN_PASSWORD
    else:
        return PASSWORD
