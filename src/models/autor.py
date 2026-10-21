
from sqlalchemy import Integer, String, DateTime, func
from sqlalchemy import mapped_column, relationship, Mapped
from datetime import datetime
from database import Base 
from typing import List
from typing import Optional
class AutorModel(Base):
    __tablename__ = 'autores'
    __table_args__ = {'schema': 'bibliotek'}

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nome : Mapped[str] = mapped_column(String(150), nullable=False)
    biografia : Mapped[Optional[str]] = mapped_column(nullable=True)

    data_nascimento : Mapped[Optional[date]]= mapped_column(Date)
    nacionalidade : Mapped[Optional[str]] = mapped_column(String(100))
    created_at : Mapped[datetime]= mapped_column(DateTime, default=func.now())
    updated_at : Mapped[datetime] = mapped_column(DateTime, default=func.now, onupdate=func.now())
