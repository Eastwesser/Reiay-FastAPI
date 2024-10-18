from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api_v1.crud.roles import create_role, get_all_roles
from api_v1.schemas.role import RoleCreate
from core.database.db_configs import get_db

router = APIRouter()


# Создание новой роли
@router.post("/roles/")
async def create_role_endpoint(role: RoleCreate, db: AsyncSession = Depends(get_db)):
    return await create_role(db, role)


# Получение списка всех ролей
@router.get("/roles/")
async def get_roles(db: AsyncSession = Depends(get_db)):
    return await get_all_roles(db)
