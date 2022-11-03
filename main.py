from aiogram import executor

from handlers.users.script_form import fill_form_on_site
from loader import dp
import handlers # middlewares, filters,
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands

import asyncio
import aioschedule

async def on_startup(dispatcher):
    pass
    # # Устанавливаем дефолтные команды
    # await set_default_commands(dispatcher)
    #
    # # Уведомляет про запуск
    # await on_startup_notify(dispatcher)



async def scheduler():
    aioschedule.every(100).seconds.do(fill_form_on_site)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def on_startup(_):
    asyncio.create_task(scheduler())


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)



