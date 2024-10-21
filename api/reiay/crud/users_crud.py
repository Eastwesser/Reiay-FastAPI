from typing import (
    Optional,
    Sequence,
)

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from api.reiay.schemas.users_schemas import (
    UserCreate,
    UserUpdate,
)
from api.core.models import User


# CREATE
async def create_user(
        session: AsyncSession,
        user: UserCreate,
) -> User:
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
    return await session.get(User, username)


async def get_all_users(
        session: AsyncSession,
) -> Sequence[User]:
    stmt = select(User)
    result = await session.execute(stmt)
    return result.scalars().all()


# UPDATE
async def update_user(
        session: AsyncSession,
        user_id: int,
        user_update: UserUpdate,
) -> Optional[User]:
    user: Optional[User] = await session.get(User, user_id)

    if not user:
        return None

    for key, value in user_update.model_dump(exclude_unset=True).items():
        setattr(user, key, value)

    await session.commit()
    await session.refresh(user)
    return user


# DELETE
async def delete_donut(
        session: AsyncSession,
        username: str,
) -> User:
    user: Optional[User] = await session.get(User, username)
    await session.delete(user)
    await session.commit()
    return user
