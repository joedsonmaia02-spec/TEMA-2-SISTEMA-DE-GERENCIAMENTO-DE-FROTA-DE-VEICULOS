from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .viagem import Viagem
#Classe manutenção, contendo os atributos próprios como o tipo e o valor
class Manutencao:
    def __init__(self, viagem: "Viagem", tipo_manutencao, valor_manutencao):
        self.viagem = viagem
        self.tipo_manutencao = tipo_manutencao
        self.valor_manutencao = valor_manutencao
    #converter manutenção em dicionario, para a posterior colocação no relatorios.json
    def to_dict(self):
        return {
            "tipo_manutencao": self.tipo_manutencao,
            "valor_manutencao": self.valor_manutencao,
        }
    
    @property
    def tipo_manutencao(self):
        return self._tipo_manutencao
    #Setter para apontar o campo de tipo_mautenção vazio
    @tipo_manutencao.setter
    def tipo_manutencao(self, tipo_manutencao):
        if not tipo_manutencao.strip():
            raise ValueError("O tipo da manutenção não pode ser vazio")
        self._tipo_manutencao = tipo_manutencao

    @property
    def valor_manutencao(self):
        return self._valor_manutencao
    #Setter para a verificação se a manutenção for valor menor ou igual a zero
    @valor_manutencao.setter
    def valor_manutencao(self, valor):
        if valor <= 0:
            raise ValueError(f"{valor} não é um valor válido")
        self._valor_manutencao = valor