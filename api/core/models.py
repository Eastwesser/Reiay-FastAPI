from sqlalchemy import String, ForeignKey, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column

from api.core.db_helper import Base


class Chat(Base):
    __tablename__ = 'chats'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))

    messages: Mapped[list["Message"]] = relationship("Message", back_populates="chat")
    room: Mapped["Room"] = relationship("Room", back_populates="chats")


class Message(Base):
    __tablename__ = 'messages'
    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(String)
    chat_id: Mapped[int] = mapped_column(ForeignKey("chats.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    chat: Mapped["Chat"] = relationship("Chat", back_populates="messages")
    user: Mapped["User"] = relationship("User", back_populates="messages")


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    hashed_password: Mapped[str] = mapped_column(String)

    messages: Mapped[list["Message"]] = relationship("Message", back_populates="user")
    roles: Mapped[list["Role"]] = relationship("Role", secondary="user_roles", back_populates="users")


class Role(Base):
    __tablename__ = 'roles'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)

    users: Mapped[list["User"]] = relationship("User", secondary="user_roles", back_populates="roles")


# Ассоциативная таблица для связи many-to-many между User и Role
class UserRole(Base):
    __tablename__ = 'user_roles'
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), primary_key=True)


class Room(Base):
    __tablename__ = 'rooms'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, unique=True)
    is_voice_chat: Mapped[bool] = mapped_column(Boolean, default=False)

    chats: Mapped[list["Chat"]] = relationship("Chat", back_populates="room")
