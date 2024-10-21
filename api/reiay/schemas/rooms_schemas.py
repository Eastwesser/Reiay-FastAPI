from pydantic import BaseModel


class RoomCreate(BaseModel):
    name: str
    is_voice_chat: bool = False

    class Config:
        from_attributes = True


class RoomOut(BaseModel):
    id: int
    name: str
    is_voice_chat: bool

    class Config:
        from_attributes = True
