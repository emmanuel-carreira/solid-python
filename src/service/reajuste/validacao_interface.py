from src.model.funcionario import Funcionario


class ValidacaoReajusteInterface:
    def validar(self, funcionario: Funcionario, aumento: float) -> None:
        pass
