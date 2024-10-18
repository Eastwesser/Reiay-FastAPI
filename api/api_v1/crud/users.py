from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from api_v1.schemas.user import UserCreate
from core.models.chat import User


async def create_user(db: AsyncSession, user: UserCreate) -> User:
    """Создание нового пользователя."""
    db_user = User(username=user.username, hashed_password=user.hashed_password)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


async def get_user_by_username(db: AsyncSession, username: str) -> User:
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
