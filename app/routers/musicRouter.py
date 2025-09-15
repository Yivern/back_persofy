from fastapi import APIRouter, Depends
from typing import List
from app.security.api_key import require_api_key
from app.models.schemas import Song, AudioStreamResponse
from app.services.musicService import MusicService


router = APIRouter()


@router.get("/search", response_model = List[Song], dependencies = [Depends(require_api_key)])
async def searchMusic(query: str):
    """
    Busca canciones con el mismo nombre o parecido.
    """
    return await MusicService.search(query)


@router.get("/stream", response_model = AudioStreamResponse)
async def getMusic(query: str):
    """
    A partir de un link de youtube, retorna el streaming de audio.
    """
    return await MusicService.get_audio_stream(query)
