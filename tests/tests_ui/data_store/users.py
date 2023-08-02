import random


correct_emails = ['model@mail2.ua', 'model@mail5.ru', 'model@yandex.com']

wrong_emails = ['model@1', 'model@3', 'mail4.ua', 'model@m']


def get_correct_email():
    return random.choice(correct_emails)


def get_wrong_email():
    return random.choice(wrong_emails)
