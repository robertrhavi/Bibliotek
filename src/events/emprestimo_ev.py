from datetime import datetime, timedelta
from sqlalchemy import event
from models.emprestimo import EmprestimoModel


@event.listens_for(EmprestimoModel, "before_insert")
def calcular_datas_emprestimo(mapper, conn, target: EmprestimoModel):
    if not target.data_emprestimo:
        target.data_emprestimo = datetime.now()
    if not target.data_devolucao_prevista:
        target.data_devolucao_prevista = target.data_emprestimo + timedelta(days=14)