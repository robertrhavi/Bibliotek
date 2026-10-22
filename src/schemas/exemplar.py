from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class ExemplarBase(BaseModel):
    livro_id: int
    codigo_patrimonio: str
    status: str = "disponivel"


class ExemplarCreate(ExemplarBase):
    pass


class ExemplarUpdate(BaseModel):
    status: Optional[str] = None


class ExemplarResponse(ExemplarBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)