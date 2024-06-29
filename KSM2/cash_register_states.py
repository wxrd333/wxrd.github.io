# cash_register_states.py

from aiogram.fsm.state import State, StatesGroup

class CashRegisterStates(StatesGroup):
    place = State()
    issues = State()
    accepts = State()
    amount = State()
    code = State()
    has_recount = State()
