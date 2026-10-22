from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict
from schemas.editora import EditoraResponse
from schemas.categoria import CategoriaResponse


class LivroBase(BaseModel):
    titulo: str
    isbn: Optional[str] = None
    ano_publicacao: Optional[int] = None
    editora_id: int
    categoria_id: int


class LivroCreate(LivroBase):
    autores_ids: list[int] = [] 


class LivroUpdate(BaseModel):
    titulo: Optional[str] = None
    isbn: Optional[str] = None
    ano_publicacao: Optional[int] = None
    editora_id: Optional[int] = None
    categoria_id: Optional[int] = None


class LivroResponse(LivroBase):
    id: int
    created_at: datetime
    updated_at: datetime
    editora: Optional[EditoraResponse] = None
    categoria: Optional[CategoriaResponse] = None

    model_config = ConfigDict(from_attributes=True)