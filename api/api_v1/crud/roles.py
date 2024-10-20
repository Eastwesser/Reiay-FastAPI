from typing import Sequence

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_v1.schemas.role import RoleCreate
from api.core.models.role import Role


async def create_role(
        session: AsyncSession,
        role: RoleCreate,
) -> Role:
    db_role = Role(**role.model_dump())
    session.add(db_role)
    await session.commit()
    await session.refresh(db_role)
    return db_role


async def get_all_roles(
        session: AsyncSession,
) -> Sequence[Role]:
    stmt = select(Role)
    result = await session.execute(stmt)
    return result.scalars().all()
