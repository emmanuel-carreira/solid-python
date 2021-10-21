from datetime import datetime

from src.model.cargo import Cargo
from src.model.dados_pessoais import DadosPessoais


class Funcionario:
    def __init__(self, nome: str, cpf: str, cargo: Cargo, salario: float) -> None:
        self.dados_pessoais = DadosPessoais(nome, cpf, cargo, salario)

    def atualizar_salario(self, novo_salario: float):
        self.dados_pessoais.set_salario(novo_salario)
        self.data_ultimo_reajuste = datetime.now()

    def promover(self, novo_cargo: Cargo) -> None:
        self.dados_pessoais.set_cargo(novo_cargo)

    def get_nome(self) -> str:
        return self.nome

    def get_cpf(self) -> str:
        return self.cpf

    def get_cargo(self) -> Cargo:
        return self.cargo

    def get_salario(self) -> float:
        return self.salario

    def get_data_ultimo_reajuste(self) -> datetime:
        return self.data_ultimo_reajuste
