from sqlalchemy import event
from datetime import timedelta, datetime
from models.emprestimo import EmprestimoModel

@event.listens_for(EmprestimoModel, 'before_insert')
def calcular_data_emprestimo(mapper, conn, target : EmprestimoModel):
    if not target.data_emprestimo:
        target.data_emprestimo = datetime.now()
    if not target.data_devolucao_prevista:
        target.data_devolucao_prevista = target.data_emprestimo + timedelta(days=14)
