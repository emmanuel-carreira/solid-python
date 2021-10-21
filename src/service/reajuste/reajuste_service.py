from typing import List

from src.model.funcionario import Funcionario
from src.service.reajuste.validacao_interface import ValidacaoReajusteInterface


class ReajusteService:
    def __init__(self, validacoes: List[ValidacaoReajusteInterface]) -> None:
        self.validacoes = validacoes

    def reajustar_salario(self, funcionario: Funcionario, aumento: float) -> None:
        for validacao in self.validacoes:
            validacao.validar(funcionario, aumento)

        salario_reajustado = funcionario.get_salario() + aumento
        funcionario.atualizar_salario(salario_reajustado)
