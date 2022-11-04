import psycopg2
from data.config import *


async def save_for_list(chat_id, name, lastname, email, phone, birth):
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    cursor = connection.cursor()
    with connection.cursor() as cur:
        cur.execute(f"INSERT INTO bot_list (chat_id, name, lastname, email, phone, birth) VALUES ('{chat_id}', '{name}', '{lastname}', "
                    f"'{email}', '{phone}', '{birth}');")
        connection.commit()



async def delete_from_list(chat_id):
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    cursor = connection.cursor()
    with connection.cursor() as cur:
        cur.execute(f"DELETE FROM bot_list WHERE chat_id = '{chat_id}';")
        connection.commit()



async def show_list():
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name
    )
    cursor = connection.cursor()
    try:
        with connection.cursor() as cur:
            cur.execute(f"SELECT * FROM bot_list;")
            a = cur.fetchall()
            return a
    except:
        return 'empty'

