from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class Song(BaseModel):
    title: str
    url: str
    thumbnail: str | None = None
    duration: int | None = None


class SearchParams(BaseModel):
    query: str
