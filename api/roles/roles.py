from api.models.role import Role
from api.schemas.role import RoleCreate
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.database.db_configs import get_db

router = APIRouter()


@router.post("/roles/")
async def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    db_role = Role(name=role.name)
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


# Можно добавить дополнительную логику для получения всех ролей
@router.get("/roles/")
async def get_roles(db: Session = Depends(get_db)):
    roles = db.query(Role).all()
    return roles
