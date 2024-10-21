import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

# Получаем настройки базы данных из переменных окружения
db_login = os.getenv('DB_LOGIN')
db_pass = os.getenv('DB_PASS')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

# URL для подключения к базе данных PostgreSQL
DATABASE_URL = f'postgresql+asyncpg://{db_login}:{db_pass}@{db_host}/{db_name}'

# Создание асинхронного движка для подключения к базе данных
engine = create_async_engine(DATABASE_URL, echo=True)

# Создание базовой модели для SQLAlchemy
Base = declarative_base()


# Класс для работы с сессиями базы данных
class DatabaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(url, echo=echo)
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
        )

    # Функция-зависимость для работы с сессиями
    async def session_dependency(self):
        async with self.session_factory() as session:
            yield session


# Инициализация DatabaseHelper
db_helper = DatabaseHelper(
    url=DATABASE_URL,
    echo=True,
)


# Зависимость для FastAPI для получения сессии базы данных
async def get_db():
    async for session in db_helper.session_dependency():
        yield session
