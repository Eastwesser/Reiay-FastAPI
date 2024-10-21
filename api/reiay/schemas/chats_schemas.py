from pydantic import BaseModel


class ChatCreate(BaseModel):
    name: str

    class Config:
        from_attributes = True


class ChatOut(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True
