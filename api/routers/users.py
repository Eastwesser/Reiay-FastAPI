from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from api.database.db_configs import get_db
from api.models.user import User
from api.schemas.user import UserCreate, UserOut

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
