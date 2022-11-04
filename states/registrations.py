from aiogram.dispatcher.filters.state import State, StatesGroup

# classes for the state machine

class Registrations(StatesGroup):
    name = State()
    email = State()
    phone = State()
    birth = State()
    end = State()

