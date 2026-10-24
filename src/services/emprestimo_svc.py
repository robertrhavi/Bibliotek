from datetime import datetime, timedelta
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.emprestimo import EmprestimoModel

FATOR_SUSPENSAO = 3


class EmprestimoService:

    @staticmethod
    def registrar_devolucao(db: Session, emprestimo_id: int) -> EmprestimoModel:
        emprestimo = db.get(EmprestimoModel, emprestimo_id)

        if not emprestimo:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Empréstimo não encontrado.",
            )

        if emprestimo.data_devolucao_real is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Este empréstimo já foi encerrado.",
            )

        agora = datetime.now()
        emprestimo.data_devolucao_real = agora

        # 1. Cálculo de atraso e acumulação de suspensão no utilizador
        if agora > emprestimo.data_devolucao_prevista:
            dias_atraso = (
                agora.date() - emprestimo.data_devolucao_prevista.date()
            ).days

            if dias_atraso > 0:
                dias_suspensao = dias_atraso * FATOR_SUSPENSAO
                usuario = emprestimo.usuario

                # Acumula a partir da data de bloqueio atual ou a partir de 'agora'
                inicio_bloqueio = max(agora, usuario.locked or agora)
                usuario.locked = inicio_bloqueio + timedelta(days=dias_suspensao)

                emprestimo.status = "concluido_com_atraso"
            else:
                emprestimo.status = "concluido"
        else:
            emprestimo.status = "concluido"

        # 2. Liberta o exemplar associado
        if emprestimo.exemplar:
            emprestimo.exemplar.status = "disponivel"

        db.commit()
        db.refresh(emprestimo)
        return emprestimo