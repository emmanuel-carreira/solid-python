from datetime import datetime, timedelta

from src.validacao_exception import ValidacaoException
from src.model.funcionario import Funcionario
from src.service.reajuste.validacao_interface import ValidacaoReajusteInterface


class ValidacaoPeriodicidadeEntreReajustes(ValidacaoReajusteInterface):
    def validar(self, funcionario: Funcionario, aumento: float) -> None:
        data_ultimo_reajuste = funcionario.get_data_ultimo_reajuste()
        data_atual = datetime.now()
        if data_ultimo_reajuste + timedelta(days=180) > data_atual:
            raise ValidacaoException('Intervalo entre reajustes deve ser de no mínimo 6 meses!')
