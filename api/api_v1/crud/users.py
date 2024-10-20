from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Optional, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select


from api.api_v1.schemas.user import UserCreate
from api.core.models.chat import User


async def create_user(
        session: AsyncSession,
        user: UserCreate,
) -> User:
    """Создание нового пользователя."""
    db_user = User(**user.model_dump())
    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    return db_user


async def get_user_by_username(
        session: AsyncSession,
        username: str,
) -> User:
    """Получение пользователя по имени."""
    stmt = select(User).filter(User.username == username)
    result = await db.execute(stmt)
    return result.scalar_one_or_none()


async def update_user(db: AsyncSession, user_id: int, new_data: UserCreate) -> User:
    """Обновление данных пользователя."""
    user = await db.get(User, user_id)
    if user:
        user.username = new_data.username
        user.hashed_password = new_data.hashed_password
        await db.commit()
        await db.refresh(user)
        return user
    return None
