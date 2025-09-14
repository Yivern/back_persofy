from fastapi import HTTPException, status
from pprint import pp as pprint
import yt_dlp

# Config
from app.configs.config import Config


class MusicService:
    """
    Servicio de manejo de musica.
    """

    @staticmethod
    async def search(query: str):
        """
        Metodo para busqueda de musica.
        """
        try:
            with yt_dlp.YoutubeDL(Config.yt_options) as ydl:
                info = ydl.extract_info(f"ytsearch10: {query}", download = False)
                results = []

                for entry in info.get("entries", []):
                    results.append({
                        "title": entry.get("title"),
                        "url": entry.get("url"),
                        "thumbnail": max(entry['thumbnails'], key=lambda t: t['width'])['url'],
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


    @staticmethod
    async def get_audio_stream(url: str):
        try:
            with yt_dlp.YoutubeDL(Config.yt_options) as ydl:
                info = ydl.extract_info(url, download = False)

                stream_url = info.get('url')

                if not stream_url:

                    if info.get('formats'):
                        stream_url = info['formats'][0].get('url')

                if not stream_url:
                    raise HTTPException(
                        status_code = status.HTTP_404_NOT_FOUND,
                        detail = "No se pudo encontrar una URL de stream válida."
                    )

                song_data = {
                    "title": info.get('title', 'Título desconocido'),
                    "stream_url": stream_url,
                }

                return song_data

        except yt_dlp.utils.DownloadError as e:
            print(f"yt-dlp error: {e}")
            raise HTTPException(
                status_code = status.HTTP_400_BAD_REQUEST,
                detail = "La URL no es válida o el video no está disponible."
            )
        except Exception as e:
            print(f"Error inesperado al obtener audio: {e}")
            raise HTTPException(
                status_code = status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail = "Ocurrió un error en el servidor al procesar la solicitud."
            )
