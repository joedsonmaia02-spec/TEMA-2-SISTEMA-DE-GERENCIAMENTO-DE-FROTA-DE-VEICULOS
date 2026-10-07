from viagem import Viagem


class Manutencao:
    def __init__(self, viagem: Viagem, tipo_manutencao, valor_manutencao):
        self.viagem = viagem
        self.tipo_manutencao = tipo_manutencao
        self.valor_manutencao = valor_manutencao

    @property
    def tipo_manutencao(self):
        return self._tipo

    @tipo_manutencao.setter
    def descricao(self, tipo_manutencao):
        if len[tipo_manutencao] == 0:
            raise ValueError("A descrição da manutenção não pode ser vazia")
        self._tipo_manutencao = tipo_manutencao

    @property
    def valor_manutencao(self):
        return self._valor_manutencao

    @valor_manutencao.setter
    def valor_manutencao(self, valor):
        if valor < 0:
            raise ValueError(f"{valor} não é um valor válido")
        self._valor_manutencao = valor