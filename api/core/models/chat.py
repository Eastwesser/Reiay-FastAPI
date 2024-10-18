# Модели для чатов и сообщений
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from core.database.db_configs import Base


class Chat(Base):
    __tablename__ = 'chats'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)


class Message(Base):
    __tablename__ = 'messages'
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(String)
    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    chat: Mapped["Chat"] = relationship(back_populates="messages")
    user: Mapped["User"] = relationship(back_populates="messages")


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    hashed_password: Mapped[str] = mapped_column(String)
    messages: Mapped[list["Message"]] = relationship("Message", back_populates="user")
