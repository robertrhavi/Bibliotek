from fastapi import APIRouter, HTTPException, status
from database import SessionDep
from controllers.usuario import cnt_usuario
from schemas.usuario import UsuarioCreate, UsuarioUpdate, UsuarioResponse

router = APIRouter()


@router.post("/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def criar_usuario(dados: UsuarioCreate, db: SessionDep):
    return cnt_usuario.create(db, obj_in=dados)


@router.get("/", response_model=list[UsuarioResponse])
def listar_usuarios(db: SessionDep, skip: int = 0, limit: int = 100):
    return cnt_usuario.get_multi(db, skip=skip, limit=limit)


@router.get("/{usuario_id}", response_model=UsuarioResponse)
def buscar_usuario(usuario_id: int, db: SessionDep):
    usuario = cnt_usuario.get_by_id(db, id=usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return usuario


@router.put("/{usuario_id}", response_model=UsuarioResponse)
def atualizar_usuario(usuario_id: int, dados: UsuarioUpdate, db: SessionDep):
    usuario = cnt_usuario.get_by_id(db, id=usuario_id)
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")
    return cnt_usuario.update(db, db_obj=usuario, obj_in=dados)


@router.delete("/{usuario_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_usuario(usuario_id: int, db: SessionDep):
    sucesso = cnt_usuario.delete(db, id=usuario_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Usuário não encontrado.")