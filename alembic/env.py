import asyncio
import os
import sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy.ext.asyncio import create_async_engine

# Добавляем корневую директорию проекта в sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from core.db_helper import Base, DATABASE_URL

# Создаем асинхронный движок подключения к базе данных
connectable = create_async_engine(DATABASE_URL, echo=True)

# Настройка логирования
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata


def run_migrations_offline():
    """Запуск миграций в оффлайн-режиме"""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Запуск миграций в онлайн-режиме"""
    async with connectable.connect() as connection:
        await connection.run_sync(
            context.configure, connection=connection, target_metadata=target_metadata
        )
        async with connection.begin():
            await context.run_migrations()


# Основной блок выполнения миграций
if context.is_offline_mode():
    run_migrations_offline()
else:
    try:
        asyncio.run(run_migrations_online())
    except Exception as e:
        print(f"Ошибка при выполнении миграций: {e}")
