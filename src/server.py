from fastapi import FastAPI
from fastapi.middleware import CORSMiddleware
from routes import api_router
app = FastAPI(description="API pra gerenciamento de biblitoecas")
app.add_middleware(
    CORSMiddleware,
    allow_origin=['*'],
    allow_headers=["*"],
    allow_credentials=True,
    allow_methods=["*"],
)

app.include_router(api_router)
@app.get("/health", tags=["Health"])
async def server():
    return {'status' : 'ok' }
