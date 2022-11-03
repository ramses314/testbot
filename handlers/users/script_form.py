from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from selenium import webdriver
from db.function_db import show_list, delete_from_list

from loader import bot
import time



async def fill_form_on_site():

    users = await show_list()

    if users:
        for i in users:
            url = "https://b24-iu5stq.bitrix24.site/backend_test/"
            driver = webdriver.Chrome(executable_path="/home/ramses/Рабочий стол/test-bot-form/chrome_driver/chromedriver")

            try:
                driver.get(url=url)
                time.sleep(0.5)

                # ЗАПОЛНЕНИЕ ИМЕНИ
                name_input = driver.find_element(by=By.NAME, value="name")
                name_input.clear()
                name_input.send_keys(f'{i[2]}')
                # ЗАПОЛНЕНИЕ ФАМИЛИИ
                name_input = driver.find_element(by=By.NAME, value="lastname")
                name_input.clear()
                name_input.send_keys(f'{i[3]}')
                time.sleep(0.5)
                # ОТПРАВКА НА СЛЕДУЮЩУУ СТРАНИЦУ
                driver.find_element(by=By.CLASS_NAME, value="b24-form-btn").click()
                time.sleep(1)

                # ЗАПОЛНЕНИЕ ПОЧТЫ
                name_input = driver.find_element(by=By.NAME, value="email")
                name_input.clear()
                name_input.send_keys(f'{i[4]}')
                # ЗАПОЛНЕНИЕ ТЕЛЕФОНА
                name_input = driver.find_element(by=By.NAME, value="phone")
                name_input.clear()
                name_input.send_keys(f'{i[5]}')
                # ОТПРАВКА НА СЛЕДУЮЩУЮ СТРАНИЦУ
                driver.find_element(by=By.XPATH, value='/html/body/main/div/section/div/div/div/div/div/div/div/div/div[2]/form/div[3]/div[2]/button').click()
                time.sleep(0.5)

                # ЗАПОЛНЕНИЕ ДАТЫ РОЖДЕНИЯ
                driver.find_element(by=By.CLASS_NAME, value='b24-form-control').click()
                time.sleep(0.5)
                birth = i[6].split('-')

                # МЕСЯЦ
                select = Select(driver.find_element(by=By.XPATH, value='/html/body/main/div/section/div/div/div/div/div/div/div/div/div[2]/form/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/header/div/div[1]/select'))
                # select by visible text
                # select.select_by_visible_text('Февраль')
                # select by value
                select.select_by_value(f'{int(birth[1])-1}')

                # ГОД
                select = Select(driver.find_element(by=By.XPATH, value='/html/body/main/div/section/div/div/div/div/div/div/div/div/div[2]/form/div[2]/div/div/div/div/div[2]/div/div[2]/div/div/header/div/div[2]/select'))
                select.select_by_visible_text(f'{birth[0]}')
                time.sleep(1)

                # ДЕНЬ
                driver.find_element(by=By.CSS_SELECTOR, value=f"[data-id='{i[6]}']").click()
                time.sleep(2)

                # ОТПРАВЛЯЕМ ФОРМУ
                driver.find_element(by=By.XPATH, value="/html/body/main/div/section/div/div/div/div/div/div/div/div/div[2]/form/div[4]/div[2]/button").click()
                time.sleep(2)

                # ДЕЛАЕМ СКРИНШОТ И СОХРАНЯЕМ В КАТАЛОГЕ
                path = f'media/{time.strftime("%Y-%m-%d_%H_%M")}_{i[1]}.jpg'
                driver.save_screenshot(path)
                time.sleep(1)

                await bot.send_photo(chat_id=i[1], photo="AgACAgIAAxkBAAIEWWNju8u_43M52z-tUf3yfn7308NqAAJawDEb1jggSzn8AQIVi6FhAQADAgADeAADKgQ", caption='Ваша форма успешно заполнена')

            except Exception as ex:
                print(ex)
                await bot.send_message(chat_id=i[1], text='❗️Ваша форма не была заполнена, вероятно вы указали несуществующую почту или дату рождения'
                                                          '\nПопробуйте еще раз 👉🏼 /form')
            finally:
                # УДАЛЯЕМ ПОЛЬЗОВАТЕЛЯ ИЗ ОЧЕРЕДИ
                await delete_from_list(i[1])
                driver.close()
                driver.quit()
