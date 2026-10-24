from datetime import date, datetime
from typing import Optional, TYPE_CHECKING
from sqlalchemy import String, Date, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

if TYPE_CHECKING:
    from models.livro_autor import LivroAutorModel
    from models.livro import LivroModel


class AutorModel(Base):
    __tablename__ = "autores"
    __table_args__ = {"schema": "bibliotek"}

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str] = mapped_column(String(150))
    biografia: Mapped[Optional[str]]
    data_nascimento: Mapped[Optional[date]] = mapped_column(Date)
    nacionalidade: Mapped[Optional[str]] = mapped_column(String(100))

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )

    # Relacionamento N:N Direto com LivroModel via Tabela Pivô
    livros: Mapped[list["LivroModel"]] = relationship(
        secondary="bibliotek.livro_autor",
        back_populates="autores"
    )

    # Relacionamento com o Modelo Intermediário (se precisar acessar metadados do vínculo)
    livro_autores: Mapped[list["LivroAutorModel"]] = relationship(
        back_populates="autor"
    )