from aiogram import types
from aiogram.dispatcher import FSMContext

from db.function_db import save_for_list
from keyboards.kb_form import *
from loader import dp
from states.registrations import Registrations


@dp.message_handler(state=Registrations.name)
async def form_ask_email(message: types.Message, state:FSMContext):

    string = message.text.split(' ')

    if len(string) != 2:
        await message.answer('Здесь что-то не так 🤔\nВведите имя и фамиилию через пробел')
        await form_ask_email(message)
    else:
        async with state.proxy() as data:
            string = message.text.split(' ')
            data['name'] = string[0]
            data['lastname'] = string[1]

        await message.answer('📨 Укажи свою почту\nНапример: forwork314@gmail.com')
        await Registrations.next()


@dp.message_handler(state=Registrations.email)
async def form_ask_phone(message: types.Message, state:FSMContext):

    string = message.text

    if len(string.split('@')) != 2 or len(string.split('.')) != 2 or len(string.split(' ')) > 1:
        await message.answer('Здесь что-то не так🤔\nПроверьте правильность написания')
        await form_ask_phone(message)
    else:
        async with state.proxy() as data:
            data['email'] = message.text

        await send_phone(message)
        await Registrations.next()



@dp.message_handler(content_types=['contact'], state=Registrations.phone)
async def form_ask_date_of_birth(message: types.Message, state:FSMContext):

    async with state.proxy() as data:
        data['phone'] = message.contact.phone_number

    await message.answer('📅 Укажите дату рождения в формате "YYYY-MM-DD"')
    await Registrations.next()


@dp.message_handler(state=Registrations.birth)
async def form_check(message: types.Message, state:FSMContext):

    string = message.text.split('-')

    date_of_birth = []
    for i in string:
        if i.startswith('0'):
            i = i[1:]
        date_of_birth.append(i)
    date = '-'.join(date_of_birth)

    flag = False

    for i in string:
        try:
            int(i)
        except Exception as ex:
            print(ex)
            flag = True



    if len(string[0]) != 4 or len(string[1]) != 2 or len(string[2]) != 2 or flag:
        await message.answer('Что-то здесь не так🤔\nПроверьте правильность формата "YYYY-MM-DD"')
    else:
        async with state.proxy() as data:
            data['birth'] = date
            name = data['name']
            lastname = data['lastname']
            email = data['email']
            phone = data['phone']
            birth = data['birth']

        text = [
            "*Проверьте верность введенных данных*\n",
            f"👤 {name} {lastname}, {message.text}",
            f"Телефон:️ {phone}",
            f"Почта: {email}",
            # "*Проверьте верность введенных данных* ☝🏼"
        ]

        await send_check(message, text)
        await Registrations.next()


@dp.callback_query_handler(state=Registrations.end)
async def form_check_results(callback: types.CallbackQuery, state: FSMContext):

    key = callback.data.split('_')[1]

    if key == 'ok':
        async with state.proxy() as data:
            name = data['name']
            lastname = data['lastname']
            email = data['email']
            phone = data['phone']
            birth = data['birth']
        await callback.message.edit_text('Данные успешно отправлены 🤝\n'
                                         'После заполнения формы, мы уведомим вас')
        await save_for_list(callback.message.chat.id, name, lastname, email, phone, birth)
        await state.finish()
    elif key =='name':
        await callback.message.edit_text('Введите свое Имя и Фамилию через пробел\nНапример, Владимир Агутин', reply_markup=None)
        await Registrations.name.set()
    elif key == 'email':
        await callback.message.edit_text("Укажи свою почту\nНапример: forwork314@gmail.com", reply_markup=None)
        await Registrations.email.set()
    elif key == 'phone':
        await callback.message.delete()
        await send_phone(callback.message)
        await Registrations.phone.set()
    elif key == "birth":
        await callback.message.edit_text('Укажите дату рождения в формате "YYYY-MM-DD', reply_markup=None)
        await Registrations.birth.set()
    elif key == "stop":
        await callback.message.edit_text('Заявка отменена')
        await state.finish()

