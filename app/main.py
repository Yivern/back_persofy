from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Config
from app.configs.config import Config

# Routes
from app.routers import musicRouter


app = FastAPI(
    title = "persofy",
    version = Config.version,
    docs_url = f"/api/persofy/v{ Config.version }/docs",
    redoc_url = f"/api/persofy/v{ Config.version }/redoc",
    openapi_url = f"/api/persofy/v{ Config.version }/openapi.json"
)


# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health():
    return {"status": "ok"}


app.include_router(
    musicRouter.router, prefix = f"/api/persofy/v{Config.version}", tags = ["meta"], responses = {404: {"description": "Not Found"}})
