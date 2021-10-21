from src.validacao_exception import ValidacaoException
from src.model.funcionario import Funcionario
from src.service.reajuste.validacao_interface import ValidacaoReajusteInterface


class ValidacaoPercentualReajuste(ValidacaoReajusteInterface):
    def validar(self, funcionario: Funcionario, aumento: float) -> None:
        salario_atual = funcionario.get_salario()
        percentual_reajuste = aumento/salario_atual
        if percentual_reajuste > 0.4:
            raise ValidacaoException('Reajuste do salario nao pode ser superior a 40%!')
