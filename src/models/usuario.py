from datetime import datetime
from typing import Annotated, Optional, TYPE_CHECKING
from sqlalchemy import String, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

str30 = Annotated[str, mapped_column(String(30))]

if TYPE_CHECKING:
    from models.emprestimo import EmprestimoModel
class UsuariosModel(Base):
    __tablename__ = "usuarios"
    __table_args__ = {"schema": "bibliotek"}

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(150))

    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    senha_hash: Mapped[str] = mapped_column(String(255))

    telefone: Mapped[Optional[str30]] = mapped_column(index=True)
    tipo_usuario: Mapped[str30]
    status: Mapped[str30]

    locked: Mapped[Optional[datetime]] = mapped_column(DateTime, nullable=True)

    emprestimos: Mapped[list["EmprestimoModel"]] = relationship(back_populates="usuario")

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )