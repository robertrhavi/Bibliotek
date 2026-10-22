from datetime import datetime
from decimal import Decimal
from typing import Optional, TYPE_CHECKING
from sqlalchemy import String, DateTime, ForeignKey, Numeric, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

if TYPE_CHECKING:
    from models.exemplar import ExemplarModel
    from models.usuario import UsuariosModel


class EmprestimoModel(Base):
    __tablename__ = "emprestimos"
    __table_args__ = {"schema": "bibliotek"}

    id: Mapped[int] = mapped_column(primary_key=True)
    exemplar_id: Mapped[int] = mapped_column(ForeignKey("bibliotek.exemplares.id"))
    usuario_id: Mapped[int] = mapped_column(ForeignKey("bibliotek.usuarios.id"))

    data_emprestimo: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now()
    )
    data_devolucao_prevista: Mapped[datetime] = mapped_column(DateTime)
    
    data_devolucao_real: Mapped[Optional[datetime]] = mapped_column(DateTime)

    status: Mapped[str] = mapped_column(String(30))

    multa_valor: Mapped[Optional[Decimal]] = mapped_column(
        Numeric(10, 2), default=0.00
    )

    exemplar: Mapped["ExemplarModel"] = relationship(back_populates="emprestimos")
    usuario: Mapped["UsuariosModel"] = relationship(back_populates="emprestimos")

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )