from fastapi import Depends
from requests import Session

from main import get_db
from api.routers.users import router


class RoleCreate:
    pass


class Role:
    pass


@router.post("/roles/")
def create_role(role: RoleCreate, db: Session = Depends(get_db)):
    db_role = Role(name=role.name)
    db.add(db_role)
    db.commit()
    return db_role
