from pydantic import BaseModel


class RoleCreate(BaseModel):
    name: str

    class Config:
        from_attributes = True
