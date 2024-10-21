from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.api_reiay.crud.users_crud import create_user, get_user_by_username, update_user
from api.api_reiay.schemas.users_schemas import UserOut, UserCreate
from core.db_helper import get_db
from api.security.bcrypt import verify_password

router = APIRouter()


# Регистрация пользователя
@router.post("/register", response_model=UserOut)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    existing_user = await get_user_by_username(db, user.username)
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already registered")

    new_user = await create_user(db, user)
    return new_user


# Вход пользователя
@router.post("/login")
async def login_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    db_user = await get_user_by_username(db, user.username)
    if not db_user or not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"message": "Login successful"}


# Обновление данных пользователя
@router.put("/users/{user_id}", response_model=UserOut)
async def update_user_endpoint(user_id: int, user: UserCreate, db: AsyncSession = Depends(get_db)):
    updated_user = await update_user(db, user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user
