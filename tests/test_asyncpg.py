import asyncio

import asyncpg


async def main():
    # Подключение к базе данных
    conn = await asyncpg.connect(
        user='postgres',
        password='reiay2024',
        database='reiay',
        host='localhost'
    )

    # Создание таблицы
    await conn.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id serial PRIMARY KEY,
            name text,
            dob date
        )
    ''')

    # Вставка данных
    await conn.execute('''
        INSERT INTO users(name, dob) VALUES($1, $2)
    ''', 'Alice', '1990-01-01')

    # Получение данных
    row = await conn.fetchrow('SELECT * FROM users WHERE name = $1', 'Alice')
    print(row)  # Вывод: Record(id=1, name='Alice', dob=datetime.date(1990, 1, 1))

    # Закрытие соединения
    await conn.close()


# Запуск асинхронной функции
asyncio.run(main())
