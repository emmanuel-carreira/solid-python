from enum import Enum


class Cargo(Enum):
	ASSISTENTE = 1
	ANALISTA = 2
	ESPECIALISTA = 3
	GERENTE = 4

	def sucessor(self):
		valor = self.value
		if valor + 1 > 4:
			return Cargo(valor)
		return Cargo(valor+1)
