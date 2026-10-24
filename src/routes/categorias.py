from fastapi import APIRouter, HTTPException, status
from database import SessionDep
from controllers.categoria import cnt_categoria
from schemas.categoria import CategoriaBase, CategoriaCreate, CategoriaUpdate,  CategoriaResponse

router = APIRouter()

@router.post("/", response_model=CategoriaResponse, status_code=status.HTTP_201_CREATED)
def criar_categoria(dados : CategoriaCreate, db : SessionDep):
    return cnt_categoria.create(db, obj_in=dados)

@router.get("/", response_model=list[CategoriaResponse])
def listar_categorias(db : SessionDep, skip : int = 0, limit : int = 100):
    return cnt_categoria.get_multi(db, skip, limit)

@router.get("/{categoria_id}", response_model=CategoriaResponse)
def buscar_categoria(categoria_id : int, db : SessionDep):
    categoria = cnt_categoria.get_by_id(db, id=categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return categoria

@router.put("/{categoria_id}", response_model=CategoriaResponse)
def atualizar_categoria(categoria_id : int, dados : CategoriaUpdate, db : SessionDep):
    categoria = cnt_categoria.get_by_id(db, id=categoria_id)
    if not categoria:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    return cnt_categoria.update(db, db_ob=categoria, obj_in=dados)


@router.delete("/{categoria_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_categoria(categoria_id: int, db: SessionDep):
    sucesso = cnt_categoria.delete(db, id=categoria_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Categoria não encontrada.")