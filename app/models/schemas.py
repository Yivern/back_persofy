from pydantic import BaseModel


class Song(BaseModel):
    title: str
    url: str
    thumbnail: str | None = None
    duration: int | None = None


class SearchParams(BaseModel):
    query: str


class AudioStreamResponse(BaseModel):
    audio_url: str
