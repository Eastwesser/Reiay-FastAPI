from pydantic import BaseModel


# Схема для создания роли
class RoleCreate(BaseModel):
    name: str

    class Config:
        from_attributes = True
