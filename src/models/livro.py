from datetime import datetime
from typing import Optional, TYPE_CHECKING
from sqlalchemy import String, DateTime, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base
if TYPE_CHECKING:
    from editora import EditoraModel
    from categorias import CategoriaModel

class LivroModel(Base):
    __tablename__ = "livros"
    __table_args__ = {"schema": "bibliotek"}

    id: Mapped[int] = mapped_column(primary_key=True)
    titulo: Mapped[str] = mapped_column(String(255))
    isbn: Mapped[Optional[str]] = mapped_column(String(20), unique=True, index=True)
    ano_publicacao: Mapped[Optional[int]]

    editora_id: Mapped[int] = mapped_column(ForeignKey("bibliotek.editoras.id"))
    categoria_id: Mapped[int] = mapped_column(ForeignKey("bibliotek.categorias.id"))

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )

    editora: Mapped["EditoraModel"] = relationship(back_populates="livros")
    categoria: Mapped["CategoriaModel"] = relationship(back_populates="livros")