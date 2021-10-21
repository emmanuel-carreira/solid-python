from src.model.cargo import Cargo
from src.model.dados_pessoais import DadosPessoais


class Terceirizado:
    def __init__(self, nome: str, cpf: str, cargo: Cargo, salario: float, empresa: str) -> None:
        self.dados_pessoais = DadosPessoais(nome, cpf, cargo, salario)
        self.empresa = empresa

    def get_empresa(self) -> str:
        return self.empresa

    def set_empresa(self, empresa: str) -> None:
        return self.empresa

    def get_nome(self) -> str:
        return self.nome

    def get_cpf(self) -> str:
        return self.cpf

    def get_cargo(self) -> Cargo:
        return self.cargo

    def get_salario(self) -> float:
        return self.salario