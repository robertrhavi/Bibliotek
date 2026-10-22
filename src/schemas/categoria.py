from pydantic import BaseModel
from typing import Optional


class CategoriaBase(BaseModel):
    nome : str
    descricao : Optional[str] = None


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaUpdate(BaseModel):
    pass


class CategoriaResponse(CategoriaBase):
    pass