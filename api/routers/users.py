from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from api.database.db_configs import get_db
from api.models.chat import User
from api.schemas.user import UserCreate, UserOut
from api.security.bcrypt import hash_password, verify_password

router = APIRouter()


# Регистрация пользователя
@router.post("/register", response_model=UserOut)
def register_user(user: UserCreate, db: Session = Depends(get_db)):
    # Проверка существования пользователя
    existing_user = db.query(User).filter(User.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    # Создание нового пользователя
    db_user = User(username=user.username, hashed_password=hash_password(user.password))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# Вход пользователя
@router.post("/login")
def login_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.username == user.username).first()

    # Проверка существования пользователя и правильности пароля
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    return {"message": "Login successful"}


# Обновление данных пользователя
@router.put("/users/{user_id}", response_model=UserOut)
def update_user(user_id: int, user: UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")

    # Обновление данных пользователя
    if user.username:
        db_user.username = user.username

    if user.password:
        db_user.hashed_password = hash_password(user.password)  # Хеширование нового пароля

    db.commit()
    db.refresh(db_user)

    return db_user
