from fastapi import FastAPI, HTTPException # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
import os
from fastapi.openapi.utils import get_openapi # type: ignore
from datetime import datetime, date

# Inicialização do FastAPI
app = FastAPI()

# Middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", summary="Endpoint inicial", description="Verifica se a API está online.")
def home():
    return {"description": "Bem vindo a API"}

if __name__ == "__main__":
    import uvicorn
    host = os.getenv("API_HOST", "0.0.0.0")
    port = int(os.getenv("API_PORT", 7090))
    reload = os.getenv("API_RELOAD", "true").lower() == "true"
    uvicorn.run(
        "app:app",
        host=host,
        port=port,
        reload=reload
    )