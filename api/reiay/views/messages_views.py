from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.reiay.crud.messages_crud import search_messages
from api.reiay.schemas.messages_schemas import MessageCreate, MessageOut
from api.core.db_helper import get_db

router = APIRouter()


@router.post("/messages/", response_model=MessageOut)
async def create_message_endpoint(message: MessageCreate, db: AsyncSession = Depends(get_db)):
    return await search_messages(db, message.content)


@router.get("/messages/", response_model=list[MessageOut])
async def search_messages_endpoint(query: str, db: AsyncSession = Depends(get_db)):
    return await search_messages(db, query)
