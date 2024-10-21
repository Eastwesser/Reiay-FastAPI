from pydantic import BaseModel


class MessageCreate(BaseModel):
    content: str
    chat_id: int
    user_id: int

    class Config:
        from_attributes = True


class MessageOut(BaseModel):
    id: int
    content: str
    chat_id: int
    user_id: int

    class Config:
        from_attributes = True
