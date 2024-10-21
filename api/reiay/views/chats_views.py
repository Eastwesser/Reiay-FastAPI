from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.reiay.crud.chats_crud import create_chat, get_all_chats, get_chat_by_id, delete_chat
from api.reiay.schemas.chats_schemas import ChatCreate, ChatOut
from api.core.db_helper import get_db

router = APIRouter()


@router.post("/chats/", response_model=ChatOut)
async def create_chat_endpoint(chat: ChatCreate, db: AsyncSession = Depends(get_db)):
    return await create_chat(db, chat.name)


@router.get("/chats/", response_model=list[ChatOut])
async def get_all_chats_endpoint(db: AsyncSession = Depends(get_db)):
    return await get_all_chats(db)


@router.get("/chats/{chat_id}", response_model=ChatOut)
async def get_chat_by_id_endpoint(chat_id: int, db: AsyncSession = Depends(get_db)):
    chat = await get_chat_by_id(db, chat_id)
    if not chat:
        raise HTTPException(status_code=404, detail="Chat not found")
    return chat


@router.delete("/chats/{chat_id}")
async def delete_chat_endpoint(chat_id: int, db: AsyncSession = Depends(get_db)):
    success = await delete_chat(db, chat_id)
    if not success:
        raise HTTPException(status_code=404, detail="Chat not found")
    return {"message": "Chat deleted"}
