from typing import Sequence, Type, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from api.core.models import Chat


async def create_chat(
        session: AsyncSession,
        chat_name: str,
) -> Chat:
    chat = Chat(name=chat_name)
    session.add(chat)
    await session.commit()
    await session.refresh(chat)
    return chat


async def get_chat_by_id(
        session: AsyncSession,
        chat_id: int,
) -> Optional[Type[Chat]]:
    return await session.get(Chat, chat_id)


async def get_all_chats(
        session: AsyncSession,
) -> Sequence[Chat]:
    stmt = select(Chat)
    result = await session.execute(stmt)
    return result.scalars().all()


async def delete_chat(
        session: AsyncSession,
        chat_id: int,
) -> bool:
    chat = await session.get(Chat, chat_id)
    if chat:
        await session.delete(chat)
        await session.commit()
        return True
    return False
