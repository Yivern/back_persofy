from fastapi import HTTPException, status
import yt_dlp

# Models
from app.models.schemas import SearchParams, Song

# Config
from app.configs.config import Config


class MusicService:
    """
    Podemos crear clases aprovechando la POO de python y los metodos (@staticmethod),
    llamamos metodos cuando necesitemos esa logica y listo.
    """
    @staticmethod
    async def search(query: str):
        """
        Metodo para busqueda de musica.
        """
        try:
            with yt_dlp.YoutubeDL(Config.yt_options) as ydl:
                info = ydl.extract_info(f"ytsearch5: {query}", download = False)
                results = []

                for entry in info.get("entries", []):
                    results.append({
                        "title": entry.get("title"),
                        "url": entry.get("url"),
                        "thumbnail": entry.get("thumbnail"),
                        "duration": entry.get("duration")
                    })

            return results

        except HTTPException as e:
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = f"Error en la peticion a YT: { e }"
            )

        except Exception as e:
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = f"Error { e }"
            )
