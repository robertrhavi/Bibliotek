from fastapi import APIRouter, HTTPException, status
from database import SessionDep
from controllers.exemplar import cnt_exemplar
from schemas.exemplar import ExemplarCreate, ExemplarUpdate, ExemplarResponse

router = APIRouter()


@router.post("/", response_model=ExemplarResponse, status_code=status.HTTP_201_CREATED)
def criar_exemplar(dados: ExemplarCreate, db: SessionDep):
    return cnt_exemplar.create(db, obj_in=dados)


@router.get("/", response_model=list[ExemplarResponse])
def listar_exemplares(db: SessionDep, skip: int = 0, limit: int = 100):
    return cnt_exemplar.get_multi(db, skip=skip, limit=limit)


@router.get("/{exemplar_id}", response_model=ExemplarResponse)
def buscar_exemplar(exemplar_id: int, db: SessionDep):
    exemplar = cnt_exemplar.get_by_id(db, id=exemplar_id)
    if not exemplar:
        raise HTTPException(status_code=404, detail="Exemplar não encontrado.")
    return exemplar


@router.put("/{exemplar_id}", response_model=ExemplarResponse)
def atualizar_exemplar(exemplar_id: int, dados: ExemplarUpdate, db: SessionDep):
    exemplar = cnt_exemplar.get_by_id(db, id=exemplar_id)
    if not exemplar:
        raise HTTPException(status_code=404, detail="Exemplar não encontrado.")
    return cnt_exemplar.update(db, db_obj=exemplar, obj_in=dados)


@router.delete("/{exemplar_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_exemplar(exemplar_id: int, db: SessionDep):
    sucesso = cnt_exemplar.delete(db, id=exemplar_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Exemplar não encontrado.")