from fastapi import FastAPI, HTTPException, Path, Body
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import Annotated
app = FastAPI(description="API pra gerenciamento de biblitoecas")

livrarias = []
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_headers=["*"],
    allow_credentials=True,
    allow_methods=["*"],
)
class Biblioteca(BaseModel):
    id : Annotated[int, Field(gt=0, lt=1000)]
    nome : Annotated[str, Field(max_length=100, min_length=5)]

    

libs = {
    1 : Biblioteca(id=1, nome='COTUCA'),
    2 : Biblioteca(id=2, nome='COTIL')
}


@app.get("/health", tags=["Health"])
async def server():
    return {'status' : 'ok' }

@app.get('/libs/{lib_id}', tags=['GetLibrary'])
async def get_libraries(lib_id : Annotated[int | None, Path(gt=0, lt=1000)]):
    lib = libs.get(lib_id)
    if lib is None:
        raise HTTPException(
            status_code=404,
            detail="Library not found."
        )
    return lib

@app.put('/libs/update/{lib_id}', tags=["UpdateLibrary"])
async def update_library(lib_id : Annotated[int | None, Path(gt=0, lt=1000)], lib : Annotated[Biblioteca, Body()]):
    up_lib = libs.get(lib_id)
    if up_lib is None:
        raise HTTPException(
            status_code=404,
            detail="Library not found."
        )
    if lib.id != lib_id:
        raise HTTPException(
            status_code=400,
            detail="ID in URL does not match ID in body."
        )
        
    libs[lib_id] = lib
    return lib