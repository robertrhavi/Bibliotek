from typing import Any
from datetime import datetime
from sqlalchemy.orm import Session
from models.emprestimo import EmprestimoModel
from schemas.emprestimo import EmprestimoCreate, EmprestimoUpdate
from crud_controllers.crud_base import CRUD
from controllers.usuario import cnt_usuario
from controllers.exemplar import cnt_exemplar


class EmprestimoCRUD(CRUD[EmprestimoModel, EmprestimoCreate, EmprestimoUpdate]):

    def create(
        self, db: Session, obj_in: EmprestimoCreate | dict[str, Any]
    ) -> EmprestimoModel:
        if isinstance(obj_in, dict):
            dados = obj_in
        else:
            dados = obj_in.model_dump()

        # Valida utilizador
        usuario = cnt_usuario.get_by_id(db, id=dados["usuario_id"])
        if not usuario:
            raise ValueError("Utilizador não encontrado.")

        agora = datetime.now()
        if usuario.locked and usuario.locked > agora:
            data_str = usuario.locked.strftime("%d/%m/%Y")
            raise ValueError(f"Utilizador suspenso até {data_str}.")

        # Valida exemplar
        exemplar = cnt_exemplar.get_by_id(db, id=dados["exemplar_id"])
        if not exemplar:
            raise ValueError("Exemplar não encontrado.")

        if exemplar.status != "disponivel":
            raise ValueError("Exemplar não está disponível.")

        # Marca exemplar como emprestado
        exemplar.status = "emprestado"

        # O evento before_insert vai preencher as datas automaticamente
        return super().create(db, obj_in=dados)


cnt_emprestimo = EmprestimoCRUD(EmprestimoModel)