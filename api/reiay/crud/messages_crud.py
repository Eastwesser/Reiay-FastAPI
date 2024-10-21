from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from core.models import Message


async def search_messages(
        session: AsyncSession,
        query: str,
) -> Sequence[Message]:
    stmt = select(Message).where(Message.content.ilike(f"%{query}%"))
    result = await session.execute(stmt)
    return result.scalars().all()
