from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, ConfigDict, computed_field


class EmprestimoBase(BaseModel):
    exemplar_id: int
    usuario_id: int


class EmprestimoCreate(EmprestimoBase):
    pass 


class EmprestimoUpdate(BaseModel):
    exemplar_id: Optional[int] = None
    usuario_id: Optional[int] = None
    data_devolucao_prevista: Optional[datetime] = None
    data_devolucao_real: Optional[datetime] = None
    status: Optional[str] = None
    multa_valor: Optional[Decimal] = None


class EmprestimoDevolucao(BaseModel):
    pass 

class EmprestimoResponse(EmprestimoBase):
    id: int
    data_emprestimo: datetime
    data_devolucao_prevista: datetime
    data_devolucao_real: Optional[datetime] = None
    status: str
    multa_valor: Optional[Decimal] = Decimal("0.00")
    created_at: datetime
    updated_at: datetime

    @computed_field
    def foi_devolvido(self) -> bool:
        return self.data_devolucao_real is not None

    @computed_field
    def dias_atraso(self) -> int:
        if self.data_devolucao_real:
            data_fim = self.data_devolucao_real
        else:
            data_fim = datetime.now()

        if data_fim > self.data_devolucao_prevista:
            return max(0, (data_fim.date() - self.data_devolucao_prevista.date()).days)
        return 0

    model_config = ConfigDict(from_attributes=True)