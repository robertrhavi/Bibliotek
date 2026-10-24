from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from database import Base

if TYPE_CHECKING:
    from models.autor import AutorModel
    from models.livro import LivroModel


class LivroAutorModel(Base):
    __tablename__ = "livro_autor"
    __table_args__ = {"schema": "bibliotek"}

    livro_id: Mapped[int] = mapped_column(
        ForeignKey("bibliotek.livros.id"), primary_key=True
    )
    autor_id: Mapped[int] = mapped_column(
        ForeignKey("bibliotek.autores.id"), primary_key=True
    )

    livro: Mapped["LivroModel"] = relationship(back_populates="livro_autores")
    autor: Mapped["AutorModel"] = relationship(back_populates="livro_autores")