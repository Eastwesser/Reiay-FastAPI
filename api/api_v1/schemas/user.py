# Схемы для пользователей
from pydantic import BaseModel


# Схема для создания пользователя
class UserCreate(BaseModel):
    username: str
    password: str


# Схема для вывода информации о пользователе
class UserOut(BaseModel):
    id: int
    username: str

    # Настройка Pydantic для работы с SQLAlchemy ORM
    class Config:
        from_attributes = True
