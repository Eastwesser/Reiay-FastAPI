from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.schemas.role import RoleCreate
from api.core.models.role import Role


async def create_role(db: AsyncSession, role: RoleCreate) -> Role:
    """Создание новой роли."""
    db_role = Role(name=role.name)
    db.add(db_role)
    await db.commit()
    await db.refresh(db_role)
    return db_role


async def get_all_roles(db: AsyncSession) -> Sequence[Role]:
    """Получение списка всех ролей."""
    stmt = select(Role)
    result = await db.execute(stmt)
    return result.scalars().all()
