from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

# from loader import db

jobs = ['Реферат',
        'Курсовая работа',
        'Дипломная работа',
        'Речь для выступления',
        'Презентация',
        'Контрольная работа',
        'Лабораторная работа',
        'Эссе',
        'Ответы на билеты',
        'Сочинение',
        'Рецензия',
        'Диссертация'
        ]


# TODO: add rows and columns
def categories_markup():
    markup = InlineKeyboardMarkup()

    for job in jobs:
        inline_btn = InlineKeyboardButton(job, callback_data=job)
        markup.add(inline_btn)

    return markup
