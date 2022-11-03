import random
from random import randint

import psycopg2

print(222)

try:
    connection = psycopg2.connect(
        host = "127.0.0.1",
        user = "postgres",
        password = "gtx97",
        database = "postgres"
    )

    cursor = connection.cursor()

    print(555)

    with connection.cursor() as cur:
        cur.execute(
            'CREATE TABLE IF NOT EXISTS bot_list '
            '(id SERIAL PRIMARY KEY,'
            'chat_id VARCHAR(50),'
            'name VARCHAR(50),'
            'lastname VARCHAR(50),'
            'email VARCHAR(70),'
            'phone VARCHAR(50),'
            'birth VARCHAR(15)'
            ');'
        )

        print(777)

        cur.execute(
            'CREATE TABLE IF NOT EXISTS bot_list_archive '
            '(id SERIAL PRIMARY KEY,'
            'chat_id VARCHAR(15),'
            'name VARCHAR(50),'
            'lastname VARCHAR(50),'
            'email VARCHAR(70),'
            'phone VARCHAR(50),'
            'birth VARCHAR(15)'
            ');'
        )
        connection.commit()

        print(666)

except Exception as _ex:
    pass

finally:
    pass
    # if connection:
    #     connection.close()
        # print('[INFO] PostgreSQL closed')

