from typing import Generic, TypeVar, Optional, Sequence, Any
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.orm import Session
from database import Base

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class CRUD(Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model : type[ModelType]):
        self.model = model


    def get_by_id(self, db : Session, id : Any) -> Optional[ModelType]:
        """Busca um registro pelo ID."""
        return db.get(self.model, id)


    def get_multi(
        self, db: Session, skip: int = 0, limit: int = 100
    ) -> Sequence[ModelType]:
        """Lista registros com suporte a paginação."""
        stmt = select(self.model).offset(skip).limit(limit)
        return db.scalars(stmt).all()


    def create(
            self, db : Session, obj_in : CreateSchemaType | dict[str, any]
    ) -> ModelType:
        if isinstance(obj_in, dict):
            obj_in_data = obj_in
        else:
            obj_in_data = obj_in.model_dump()
        db_obj = self.model(**obj_in_data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    
    def update(
                self, db : Session, db_obj : ModelType, obj_in : UpdateSchemaType | dict[str, Any]
            ) -> ModelType:
        
        if(isinstance(obj_in, dict)):
            update_data=obj_in
        else:
            update_data = obj_in.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            if hasattr(db_obj, field):
                setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj


    def delete(self, db: Session, id: Any) -> bool:
        
        db_obj = self.get_by_id(db, id)
        if db_obj:
            db.delete(db_obj)
            db.commit()
            return True
        return False
