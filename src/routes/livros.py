from fastapi import APIRouter, HTTPException, status
from database import SessionDep
from controllers.livro import cnt_livro
from schemas.livro import LivroCreate, LivroUpdate, LivroResponse

router = APIRouter()


@router.post("/", response_model=LivroResponse, status_code=status.HTTP_201_CREATED)
def criar_livro(dados: LivroCreate, db: SessionDep):
    return cnt_livro.create(db, obj_in=dados)


@router.get("/", response_model=list[LivroResponse])
def listar_livros(db: SessionDep, skip: int = 0, limit: int = 100):
    return cnt_livro.get_multi(db, skip=skip, limit=limit)


@router.get("/{livro_id}", response_model=LivroResponse)
def buscar_livro(livro_id: int, db: SessionDep):
    livro = cnt_livro.get_by_id(db, id=livro_id)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado.")
    return livro


@router.put("/{livro_id}", response_model=LivroResponse)
def atualizar_livro(livro_id: int, dados: LivroUpdate, db: SessionDep):
    livro = cnt_livro.get_by_id(db, id=livro_id)
    if not livro:
        raise HTTPException(status_code=404, detail="Livro não encontrado.")
    return cnt_livro.update(db, db_obj=livro, obj_in=dados)


@router.delete("/{livro_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_livro(livro_id: int, db: SessionDep):
    sucesso = cnt_livro.delete(db, id=livro_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Livro não encontrado.")