from typing import Optional, Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from api.api_v1.schemas.user import UserCreate
from api.core.models.chat import User


# CREATE
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


# READ
async def get_user_by_username(
        session: AsyncSession,
        username: str,
) -> Optional[User]:
    """Получение пользователя по имени."""
    return await session.get(User, username)


async def get_all_users(session: AsyncSession) -> Sequence[User]:
    stmt = select(User)
    result = await session.execute(stmt)
    return result.scalars().all()


# UPDATE
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


# DELETE

async def delete_donut(
        session: AsyncSession,
        username: str,
) -> User:
    # Fetch the existing donut from the database.
    user: Optional[User] = await session.get(User, username)

    await session.delete(user)
    await session.commit()
    return user
