from pydantic import BaseModel


class Song(BaseModel):
    id: str
    title: str
    url: str
    thumbnail: str | None = None
    duration: int | None = None


class SearchParams(BaseModel):
    query: str


class AudioStreamResponse(BaseModel):
    stream_url: str
    duration: int
