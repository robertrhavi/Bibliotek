
from sqlalchemy import Integer, String, DateTime, func, Date
from sqlalchemy import mapped_column, relationship, Mapped
from datetime import date,datetime
from database import Base 
from typing import List
from typing import Optional
class AutorModel(Base):
    __tablename__ = 'autores'
    __table_args__ = {'schema': 'bibliotek'}

    id : Mapped[int] = mapped_column(primary_key=True)
    nome : Mapped[str] = mapped_column(String(150))
    biografia : Mapped[Optional[str]]

    data_nascimento : Mapped[Optional[date]]= mapped_column(Date)
    nacionalidade : Mapped[Optional[str]] = mapped_column(String(100))
    
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate=func.now())
