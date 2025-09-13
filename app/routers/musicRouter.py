from fastapi import APIRouter, Depends
from typing import List
from app.security.api_key import require_api_key
from app.models.schemas import SearchParams, Song
from app.services.musicService import MusicService


router = APIRouter()


@router.get("/search", response_model = List[Song], dependencies = [Depends(require_api_key)])
async def searchMusic(query: str):
    """
    Busca canciones con el mismo nombre o parecido.
    Return: Una lista de canciones desde la mas reproducida.
    """
    return await MusicService.search(query)
