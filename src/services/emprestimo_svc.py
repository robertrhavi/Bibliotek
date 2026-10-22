from datetime import datetime, timedelta
from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from models.emprestimo import EmprestimoModel
from models.usuario import UsuariosModel

FATOR_SUSPENSAO = 3  

class EmprestimoService:
    @staticmethod
    def registrar_devolucao(db: Session, emprestimo_id: int) -> EmprestimoModel:
        emprestimo = db.get(EmprestimoModel, emprestimo_id)
        if not emprestimo or emprestimo.data_devolucao_real is not None:
            raise HTTPException(status_code=400, detail="Empréstimo inválido ou já encerrado.")

        agora = datetime.now()
        emprestimo.data_devolucao_real = agora

        # 1. Verifica se houve atraso
        if agora > emprestimo.data_devolucao_prevista:
            dias_atraso = (agora.date() - emprestimo.data_devolucao_prevista.date()).days

            if dias_atraso > 0:
                dias_suspensao = dias_atraso * FATOR_SUSPENSAO
                usuario = db.get(UsuariosModel, emprestimo.usuario_id)

                # Se o usuário já tinha uma suspensão ativa, acumula a partir do final dela
                inicio_bloqueio = max(agora, usuario.locked or agora)
                usuario.locked = inicio_bloqueio + timedelta(days=dias_suspensao)
                
                emprestimo.status = "concluido_com_atraso"
            else:
                emprestimo.status = "concluido"
        else:
            emprestimo.status = "concluido"

        # 2. Libera o exemplar
        emprestimo.exemplar.status = "disponivel"

        db.commit()
        db.refresh(emprestimo)
        return emprestimo