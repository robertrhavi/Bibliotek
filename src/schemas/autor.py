from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class AutorBase(BaseModel):
    nome: str
    biografia: Optional[str] = None
    data_nascimento: Optional[date] = None
    nacionalidade: Optional[str] = None


class AutorCreate(AutorBase):
    pass


class AutorUpdate(BaseModel):
    nome: Optional[str] = None
    biografia: Optional[str] = None
    data_nascimento: Optional[date] = None
    nacionalidade: Optional[str] = None


class AutorResponse(AutorBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)