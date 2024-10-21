from typing import Sequence, Optional

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from api.core.models import Room


# Создание комнаты
async def create_room(
        session: AsyncSession,
        room_name: str,
        is_voice_chat: bool = False
) -> Room:
    room = Room(name=room_name, is_voice_chat=is_voice_chat)
    session.add(room)
    await session.commit()
    await session.refresh(room)
    return room


# Получение всех комнат
async def get_all_rooms(session: AsyncSession) -> Sequence[Room]:
    stmt = select(Room)
    result = await session.execute(stmt)
    return result.scalars().all()


# Получение комнаты по ID
async def get_room_by_id(session: AsyncSession, room_id: int) -> Optional[Room]:
    return await session.get(Room, room_id)


# Удаление комнаты
async def delete_room(session: AsyncSession, room_id: int) -> bool:
    room = await session.get(Room, room_id)
    if room:
        await session.delete(room)
        await session.commit()
        return True
    return False
