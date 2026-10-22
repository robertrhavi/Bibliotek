from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class EditoraBase(BaseModel):
    nome: str
    site: Optional[str] = None


class EditoraCreate(EditoraBase):
    pass


class EditoraUpdate(BaseModel):
    nome: Optional[str] = None
    site: Optional[str] = None


class EditoraResponse(EditoraBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)