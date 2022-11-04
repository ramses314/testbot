from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, KeyboardButton, ReplyKeyboardMarkup



async def send_phone(message : types.Message):
    but_1 = KeyboardButton('👉🏼 Поделиться контактом 👈🏼', request_contact=True)
    markup = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    markup.add(but_1)
    await message.answer('☎️ Теперь поделись контактом (нажми на кнопку ниже)', reply_markup=markup)


async def send_check(message : types.Message, text):
    markup = InlineKeyboardMarkup()
    but1 = InlineKeyboardButton('Вернуться к имени', callback_data="check_name")
    but2 = InlineKeyboardButton('почте', callback_data="check_email")
    but3 = InlineKeyboardButton('телефону', callback_data="check_phone")
    but4 = InlineKeyboardButton('дате рождения', callback_data="check_birth")
    but5 = InlineKeyboardButton('Все верно', callback_data="check_ok")
    but6 = InlineKeyboardButton('Отменить', callback_data="check_stop")
    markup.row(but5).row(but1, but2).row(but3, but4).row(but6)

    await message.answer(text="\n".join(text), reply_markup=markup, parse_mode=ParseMode.MARKDOWN)

