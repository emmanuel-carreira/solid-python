from src.model.cargo import Cargo


class DadosPessoais:
    def __init__(self, nome: str, cpf: str, cargo: Cargo, salario: float) -> None:
        self.nome = nome
        self.cpf = cpf
        self.cargo = cargo
        self.salario = salario

    def get_nome(self) -> str:
        return self.nome

    def get_cpf(self) -> str:
        return self.cpf

    def get_cargo(self) -> Cargo:
        return self.cargo

    def get_salario(self) -> str:
        return self.salario

    def set_cargo(self, cargo: Cargo) -> None:
        self.cargo = cargo

    def set_salario(self, salario: float) -> None:
        self.salario = salario
