#general
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton, 
InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='бросить кубик')]
],
                        resize_keyboard=True,
                        input_field_placeholder="Выберете пункт меню")


git_button = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="Мой Git Hub", url = 'https://github.com/Rom667')]])