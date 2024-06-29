# keyboards.py

from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, WebAppInfo

def start_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Актуальный курс", callback_data="current_rate")
    builder.button(text="Касса", web_app=WebAppInfo(url="https://yourdomain.com/webapp"))
    builder.adjust(1)
    return builder.as_markup()

