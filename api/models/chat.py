from datetime import datetime
from symtable import Symbol

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, BigInteger, MetaData
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import relationship, Mapped, mapped_column

from main import Base

url = f'postgresql+asyncpg://{dbconfigs.db_login}:{dbconfigs.db_pass}@{dbconfigs.db_host}/{dbconfigs.db_name}'
engine = create_async_engine(url, echo=True)
user_metadata = MetaData()
async_session = async_sessionmaker(engine, class_=AsyncSession)


class Chat(Base):
    __tablename__ = 'chats'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)


class Message(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
    chat_id = Column(Integer, ForeignKey("chats.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    chat = relationship("Chat")
    user = relationship("User")


class User(Base):
    __tablename__ = 'users'
    pk_id: Mapped[int] = mapped_column(primary_key=True)
    tg_id: Mapped[BigInteger] = mapped_column(BigInteger)
    symbol_name: Mapped[str] = mapped_column(String)
    sheet_id: Mapped[BigInteger] = mapped_column(BigInteger, nullable=True)
    symbol_id: Mapped[int] = mapped_column(ForeignKey("symbols.user_id"))
    symbol: Mapped["Symbol"] = relationship(back_populates="user")

    async def connectdb(self):
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)
