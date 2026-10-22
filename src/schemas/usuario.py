from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict, EmailStr, computed_field


class UsuarioBase(BaseModel):
    nome: str
    email: EmailStr
    telefone: Optional[str] = None
    tipo_usuario: str
    status: str = "ativo"


class UsuarioCreate(UsuarioBase):
    senha: str  # Senha em texto puro enviada na criacao


class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    telefone: Optional[str] = None
    tipo_usuario: Optional[str] = None
    status: Optional[str] = None
    senha: Optional[str] = None


class UsuarioResponse(UsuarioBase):
    id: int
    locked: Optional[datetime] = None
    created_at: datetime
    updated_at: datetime

    @computed_field
    def esta_suspenso(self) -> bool:
        if self.locked is None:
            return False
        return self.locked > datetime.now()

    model_config = ConfigDict(from_attributes=True)