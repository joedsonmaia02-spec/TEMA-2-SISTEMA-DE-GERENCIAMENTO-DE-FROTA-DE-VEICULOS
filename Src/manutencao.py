<<<<<<< HEAD
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from viagem import Viagem

class Manutencao:
    def __init__(self, viagem: "Viagem", tipo_manutencao, valor_manutencao):
=======
from viagem import Viagem


class Manutencao:
    def __init__(self, viagem: Viagem, tipo_manutencao, valor_manutencao):
>>>>>>> 9e7b941e00328633fa8441e9ccddf70b4a696d17
        self.viagem = viagem
        self.tipo_manutencao = tipo_manutencao
        self.valor_manutencao = valor_manutencao

    @property
    def tipo_manutencao(self):
<<<<<<< HEAD
        return self._tipo_manutencao

    @tipo_manutencao.setter
    def tipo_manutencao(self, tipo_manutencao):
        if not tipo_manutencao.strip():
            raise ValueError("O tipo da manutenção não pode ser vazio")
=======
        return self._tipo

    @tipo_manutencao.setter
    def descricao(self, tipo_manutencao):
        if len[tipo_manutencao] == 0:
            raise ValueError("A descrição da manutenção não pode ser vazia")
>>>>>>> 9e7b941e00328633fa8441e9ccddf70b4a696d17
        self._tipo_manutencao = tipo_manutencao

    @property
    def valor_manutencao(self):
        return self._valor_manutencao

    @valor_manutencao.setter
    def valor_manutencao(self, valor):
<<<<<<< HEAD
        if valor <= 0:
=======
        if valor < 0:
>>>>>>> 9e7b941e00328633fa8441e9ccddf70b4a696d17
            raise ValueError(f"{valor} não é um valor válido")
        self._valor_manutencao = valor