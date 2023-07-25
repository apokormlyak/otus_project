import random

products = [
    {'name': 'name1', 'meta': 'meta1', 'model': 'model1'},
    {'name': 'name2', 'meta': 'meta2', 'model': 'model2'},
    {'name': 'name3', 'meta': 'meta3', 'model': 'model3'},
    {'name': 'name4', 'meta': 'meta4', 'model': 'model4'},
    {'name': 'name5', 'meta': 'meta5', 'model': 'model5'},
    {'name': 'name6', 'meta': 'meta6', 'model': 'model6'},
    {'name': 'name7', 'meta': 'meta7', 'model': 'model7'},
    {'name': 'name8', 'meta': 'meta8', 'model': 'model8'},
    {'name': 'name8', 'meta': 'meta9', 'model': 'model9'},
    {'name': 'name10', 'meta': 'meta10', 'model': 'model10'}
]


def get_product():
    return random.choice(products)
