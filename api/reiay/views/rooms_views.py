from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.reiay.crud.rooms_crud import create_room, get_all_rooms, get_room_by_id, delete_room
from api.reiay.schemas.rooms_schemas import RoomCreate, RoomOut
from api.core.db_helper import get_db

router = APIRouter()


@router.post("/rooms/", response_model=RoomOut)
async def create_room_endpoint(room: RoomCreate, db: AsyncSession = Depends(get_db)):
    return await create_room(db, room.name, room.is_voice_chat)


@router.get("/rooms/", response_model=list[RoomOut])
async def get_all_rooms_endpoint(db: AsyncSession = Depends(get_db)):
    return await get_all_rooms(db)


@router.get("/rooms/{room_id}", response_model=RoomOut)
async def get_room_by_id_endpoint(room_id: int, db: AsyncSession = Depends(get_db)):
    room = await get_room_by_id(db, room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room


@router.delete("/rooms/{room_id}")
async def delete_room_endpoint(room_id: int, db: AsyncSession = Depends(get_db)):
    success = await delete_room(db, room_id)
    if not success:
        raise HTTPException(status_code=404, detail="Room not found")
    return {"message": "Room deleted"}
