# start_handler.py

from aiogram import Router, F
from aiogram.types import Message
from keyboards import start_keyboard

router = Router()

@router.message(F.text == "/start")
async def start_command(message: Message):
    await message.answer("Привет! Выберите действие:", reply_markup=start_keyboard())
