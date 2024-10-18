# Схемы для ролей
from pydantic import BaseModel


# Схема для создания роли
class RoleCreate(BaseModel):
    name: str

    # Настройка Pydantic для работы с SQLAlchemy ORM
    class Config:
        from_attributes = True
