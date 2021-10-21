from src.validacao_exception import ValidacaoException
from src.model.cargo import Cargo
from src.model.funcionario import Funcionario


class PromocaoReajuste:
    def promover(self, funcionario: Funcionario, meta_batida: bool):
        cargo_atual = funcionario.get_cargo()
        if Cargo.GERENTE == cargo_atual:
            raise ValidacaoException('Gerentes não podem ser promovidos!')

        if not meta_batida:
            raise ValidacaoException('Funcionário não bateu a meta!')

        novo_cargo = cargo_atual.sucessor()
        funcionario.promover(novo_cargo)
