import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_login = os.getenv('DB_LOGIN')
db_pass = os.getenv('DB_PASS')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')

engine = create_engine(
    f'postgresql+asyncpg://{db_login}:{db_pass}@{db_host}/{db_name}'
)
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)
Base = declarative_base()


# Зависимость для получения сессии базы данных
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
