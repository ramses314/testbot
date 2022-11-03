from aiogram.dispatcher.filters.state import State, StatesGroup

class Registrations(StatesGroup):
    name = State()
    email = State()
    phone = State()
    birth = State()
    end = State()

class  AlertUsers(StatesGroup):
    begin = State