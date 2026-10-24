from fastapi import FastAPI, HTTPException, Path, Body
from fastapi.middleware.cors import CORSMiddleware
from routes import api_router
from events import emprestimo_ev
import models

app = FastAPI(description="API pra gerenciamento de biblitoecas")


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_headers=["*"],
    allow_credentials=True,
    allow_methods=["*"],
)

app.include_router(api_router)

@app.get("/health", tags=["Health"])
async def server():
    return {'status' : 'ok' }

