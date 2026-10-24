from typing import Any
from sqlalchemy import select
from sqlalchemy.orm import Session
from crud_controllers.crud_base import CRUD
from models.livro import LivroModel
from models.autor import AutorModel
from schemas.livro import LivroCreate, LivroUpdate


class LivroCRUD(CRUD[LivroModel, LivroCreate, LivroUpdate]):

    def create(
        self, db: Session, obj_in: LivroCreate | dict[str, Any]
    ) -> LivroModel:
        if isinstance(obj_in, dict):
            dados = obj_in.copy()
        else:
            dados = obj_in.model_dump()

        autores_ids: list[int] = dados.pop("autores_ids", [])

        autores = []
        if autores_ids:
            stmt = select(AutorModel).where(AutorModel.id.in_(autores_ids))
            autores = list(db.scalars(stmt).all())

            if len(autores) != len(autores_ids):
                raise ValueError("Um ou mais IDs de autores fornecidos são inválidos.")

        db_obj = self.model(**dados)
        db_obj.autores = autores  

        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj


cnt_livro = LivroCRUD(LivroModel)