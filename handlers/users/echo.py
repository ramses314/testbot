from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import CommandStart, CommandHelp

from loader import dp
from states.registrations import Registrations


"""
A central file with handlers that respond 
to keywords and commands (start, help, etc.)
"""


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\n"
                         f"Чтобы заполнить форму обратной связи 👉🏼 /form")


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку")
    await message.answer("\n".join(text))


@dp.message_handler(commands='form', state=None)
async def start_form(message : types.Message):
    await message.answer('👤 Введите свое имя и фамилию через пробел\nНапример: Сергей Немчинский')
    await Registrations.name.set()


@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\n"
                         f"Чтобы заполнить форму обратной связи 👉🏼 /form")


@dp.message_handler(commands='stop_form', state="*")
async def start_form(message : types.Message, state:FSMContext):
    await message.answer('Отменено заполнение формы')
    await state.finish()


# Echo handler, where ALL messages with the specified status fly to
@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    await message.answer('Вы отправляете неверные данные, можете остановить заполнение формы 👉🏼/stop_form')
