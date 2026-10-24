from fastapi import APIRouter, HTTPException, status
from database import SessionDep
from controllers.editora import cnt_editora
from schemas.editora import EditoraCreate, EditoraUpdate, EditoraResponse

router = APIRouter()


@router.post("/", response_model=EditoraResponse, status_code=status.HTTP_201_CREATED)
def criar_editora(dados: EditoraCreate, db: SessionDep):
    return cnt_editora.create(db, obj_in=dados)


@router.get("/", response_model=list[EditoraResponse])
def listar_editoras(db: SessionDep, skip: int = 0, limit: int = 100):
    return cnt_editora.get_multi(db, skip=skip, limit=limit)


@router.get("/{editora_id}", response_model=EditoraResponse)
def buscar_editora(editora_id: int, db: SessionDep):
    editora = cnt_editora.get_by_id(db, id=editora_id)
    if not editora:
        raise HTTPException(status_code=404, detail="Editora não encontrada.")
    return editora


@router.put("/{editora_id}", response_model=EditoraResponse)
def atualizar_editora(editora_id: int, dados: EditoraUpdate, db: SessionDep):
    editora = cnt_editora.get_by_id(db, id=editora_id)
    if not editora:
        raise HTTPException(status_code=404, detail="Editora não encontrada.")
    return cnt_editora.update(db, db_obj=editora, obj_in=dados)


@router.delete("/{editora_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_editora(editora_id: int, db: SessionDep):
    sucesso = cnt_editora.delete(db, id=editora_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Editora não encontrada.")