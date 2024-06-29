# cash_register_handler.py

import random
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, Message
from cash_register_states import CashRegisterStates

router = Router()

@router.callback_query(F.data == "cash_register")
async def cash_register_start(callback: CallbackQuery, state: FSMContext):
    await state.set_state(CashRegisterStates.place)
    await callback.message.answer("Место:")

@router.message(CashRegisterStates.place)
async def cash_register_place(message: Message, state: FSMContext):
    await state.update_data(place=message.text)
    await state.set_state(CashRegisterStates.issues)
    await message.answer("Выдает:")

@router.message(CashRegisterStates.issues)
async def cash_register_issues(message: Message, state: FSMContext):
    await state.update_data(issues=message.text)
    await state.set_state(CashRegisterStates.accepts)
    await message.answer("Принимает:")

@router.message(CashRegisterStates.accepts)
async def cash_register_accepts(message: Message, state: FSMContext):
    await state.update_data(accepts=message.text)
    await state.set_state(CashRegisterStates.amount)
    await message.answer("Сумма:")

@router.message(CashRegisterStates.amount)
async def cash_register_amount(message: Message, state: FSMContext):
    await state.update_data(amount=message.text)
    await state.set_state(CashRegisterStates.code)
    code = f"{random.randint(10, 99)}-{random.randint(1000, 9999)}"
    await state.update_data(code=code)
    await state.set_state(CashRegisterStates.has_recount)
    await message.answer(f"Код: {code}\nЕсть пересчет? (да/нет)")

@router.message(CashRegisterStates.has_recount)
async def cash_register_has_recount(message: Message, state: FSMContext):
    await state.update_data(has_recount=message.text.lower() in ["да", "yes", "y"])
    data = await state.get_data()
    summary = (
        f"Место: {data['place']}\n"
        f"Выдает: {data['issues']}\n"
        f"Принимает: {data['accepts']}\n"
        f"Сумма: {data['amount']}\n"
        f"Код: {data['code']}\n"
        f"Есть пересчет: {'Да' if data['has_recount'] else 'Нет'}"
    )
    await message.answer(f"Итоговая заявка:\n{summary}")
    await state.clear()
