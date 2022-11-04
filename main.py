from aiogram import executor

from handlers.users.script_form import fill_form_on_site
from loader import dp

import asyncio
import aioschedule

# the main file of the bot launch


"""
 Function for simultaneous operation of telegram bot and script
responsible for cyclic connection to the site (every 10 minutes). Made using the 
aioschedule library, and the selenium automation tool is passed to this function.
"""
async def scheduler():
    aioschedule.every(600).seconds.do(fill_form_on_site)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)

async def on_startup(_):
    asyncio.create_task(scheduler())

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)



