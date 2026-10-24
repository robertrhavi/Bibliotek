
from fastapi import APIRouter, HTTPException, status
from database import SessionDep
from crud_controllers.crud import crud_autor 
from schemas.autor import AutorCreate, AutorUpdate, AutorResponse

router = APIRouter()

@router.post("/", response_model=AutorResponse, status_code=status.HTTP_201_CREATED)
def criar_autor(dados: AutorCreate, db: SessionDep):
    return crud_autor.create(db, obj_in=dados)


@router.get("/", response_model=list[AutorResponse])
def listar_autores(db: SessionDep, skip: int = 0, limit: int = 100):
    return crud_autor.get_multi(db, skip=skip, limit=limit)


@router.get("/{autor_id}", response_model=AutorResponse)
def buscar_autor(autor_id: int, db: SessionDep):
    autor = crud_autor.get_by_id(db, id=autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor não encontrado.")
    return autor


@router.put("/{autor_id}", response_model=AutorResponse)
def atualizar_autor(autor_id: int, dados: AutorUpdate, db: SessionDep):
    autor = crud_autor.get_by_id(db, id=autor_id)
    if not autor:
        raise HTTPException(status_code=404, detail="Autor não encontrado.")
    return crud_autor.update(db, db_obj=autor, obj_in=dados)


@router.delete("/{autor_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_autor(autor_id: int, db: SessionDep):
    sucesso = crud_autor.delete(db, id=autor_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Autor não encontrado.")