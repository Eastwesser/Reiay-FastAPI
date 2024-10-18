from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database.db_configs import Base
from core.models.chat import Message


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String, unique=True)
    hashed_password: Mapped[str] = mapped_column(String)
    messages: Mapped[list["Message"]] = relationship("Message", back_populates="user")
