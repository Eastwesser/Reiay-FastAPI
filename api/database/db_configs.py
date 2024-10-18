import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

# Получение параметров из окружения
db_login = os.getenv('DB_LOGIN')
db_pass = os.getenv('DB_PASS')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

# URL для подключения к базе данных PostgreSQL
DATABASE_URL = f'postgresql+asyncpg://{db_login}:{db_pass}@{db_host}/{db_name}'

# Базовая модель для SQLAlchemy
Base = declarative_base()

# Создание асинхронного движка
engine = create_async_engine(DATABASE_URL, echo=True)


class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        # Создание асинхронного движка
        self.engine = create_async_engine(url, echo=echo)
        # Создание асинхронной фабрики сессий
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False
        )

    # Зависимость для предоставления сессий в FastAPI
    async def session_dependency(self):
        async with self.session_factory() as session:
            yield session


# Инициализация DatabaseHelper с использованием настроек базы данных
db_helper = DatabaseHelper(
    url=DATABASE_URL,
    echo=True  # Можно изменить на False для отключения вывода SQL запросов
)


# Пример использования: сессия будет использоваться как зависимость
async def get_db():
    async for session in db_helper.session_dependency():
        yield session
