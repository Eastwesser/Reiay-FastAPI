from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_reiay.crud.roles_crud import create_role, get_all_roles
from api.api_reiay.schemas.roles_schemas import RoleCreate
from core.db_helper import get_db

router = APIRouter()


# Создание новой роли
@router.post("/roles/")
async def create_role_endpoint(role: RoleCreate, db: AsyncSession = Depends(get_db)):
    return await create_role(db, role)


# Получение списка всех ролей
@router.get("/roles/")
async def get_roles(db: AsyncSession = Depends(get_db)):
    return await get_all_roles(db)
