from sqlalchemy import String, DateTime, func, ForeignKey 
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, TYPE_CHECKING
from datetime import datetime, date
from database import Base
if TYPE_CHECKING:
    from livro import LivroModel
    from emprestimo import EmprestimoModel
    

class ExemplarModel(Base):
    __tablename__ = "exemplares"
    __table_args__ = {"schema" : "bibliotek"}

    id : Mapped[int] = mapped_column(primary_key=True)
    livro_id : Mapped[int] = mapped_column(ForeignKey("bibliotek.livros.id"))
    codigo_patrimonio : Mapped[str] = mapped_column(String(50), unique=True, index=True)
    status : Mapped[str] = mapped_column(String(30))

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
            DateTime, server_default=func.now(), onupdate=func.now()
        )
    emprestimos: Mapped[list["EmprestimoModel"]] = relationship(back_populates="exemplar")
    livro: Mapped["LivroModel"] = relationship(back_populates="exemplares")