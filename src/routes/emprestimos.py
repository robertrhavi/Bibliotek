from fastapi import APIRouter, HTTPException, status
from database import SessionDep
from controllers.emprestimo import cnt_emprestimo
from services.emprestimo_svc import EmprestimoService
from schemas.emprestimo import EmprestimoCreate, EmprestimoUpdate, EmprestimoResponse

router = APIRouter()


@router.post("/", response_model=EmprestimoResponse, status_code=status.HTTP_201_CREATED)
def criar_emprestimo(dados: EmprestimoCreate, db: SessionDep):
    try:
        return cnt_emprestimo.create(db, obj_in=dados)
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.post("/{emprestimo_id}/devolver", response_model=EmprestimoResponse)
def devolver_emprestimo(emprestimo_id: int, db: SessionDep):
    # Chama diretamente a camada de serviço dedicada
    return EmprestimoService.registrar_devolucao(db=db, emprestimo_id=emprestimo_id)


@router.get("/", response_model=list[EmprestimoResponse])
def listar_emprestimos(db: SessionDep, skip: int = 0, limit: int = 100):
    return cnt_emprestimo.get_multi(db, skip=skip, limit=limit)


@router.get("/{emprestimo_id}", response_model=EmprestimoResponse)
def buscar_emprestimo(emprestimo_id: int, db: SessionDep):
    emprestimo = cnt_emprestimo.get_by_id(db, id=emprestimo_id)
    if not emprestimo:
        raise HTTPException(status_code=404, detail="Empréstimo não encontrado.")
    return emprestimo


@router.put("/{emprestimo_id}", response_model=EmprestimoResponse)
def atualizar_emprestimo(emprestimo_id: int, dados: EmprestimoUpdate, db: SessionDep):
    emprestimo = cnt_emprestimo.get_by_id(db, id=emprestimo_id)
    if not emprestimo:
        raise HTTPException(status_code=404, detail="Empréstimo não encontrado.")
    return cnt_emprestimo.update(db, db_obj=emprestimo, obj_in=dados)


@router.delete("/{emprestimo_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_emprestimo(emprestimo_id: int, db: SessionDep):
    sucesso = cnt_emprestimo.delete(db, id=emprestimo_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Empréstimo não encontrado.")