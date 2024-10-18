# Роуты для пользователей

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from api.database.db_configs import get_db
from api.models.chat import User
from api.schemas.user import UserCreate, UserOut
from api.security.bcrypt import hash_password

router = APIRouter()


@router.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(username=user.username, hashed_password=user.hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.post("/login")
def login_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful"}


@router.put("/users/{user_id}")
async def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.username = user.username
        db_user.hashed_password = hash_password(user.password)
        db.commit()
        db.refresh(db_user)
        return db_user
    raise HTTPException(status_code=404, detail="User not found")
