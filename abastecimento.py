from typing import TYPE_CHECKING
from datetime import date
#evitar importação circular
if TYPE_CHECKING:
    from .viagem import Viagem

#Adiçaõ da classe "Abastecimento" com as categorias valores de valor por litro, litros e a data do abastecimento, 
# armazenando cada abastecimento  

class Abastecimento:
    def __init__(self, viagem: "Viagem", litros, valor_litro_combustivel, data = None):
        self.viagem = viagem 
        self.valor_litro_combustivel = valor_litro_combustivel
        self.litros = litros
        self.data = data or date.today()
    
    @property
    def tipo_combustivel(self):
        return self.viagem.veiculo.tipo_combustivel

    @property
    def litros(self):
        return self._litros
    #Setter para evitar que litros esteja colocado como negativo ou nulo 
    # e que o valor inicial não pode ser maior que o tanque de gasolina do veiculo
    @litros.setter
    def litros(self,litros):
        if litros <= 0:
            raise ValueError(f"{litros} não é um valor real")
        elif litros > self.viagem.veiculo.tamanho_tanque_combustivel:
            raise ValueError(f"{litros} A quantidade de litros não deve ser superior ao tamanho do tanque")
        self._litros = litros
       
    @property
    def custo_total(self):
        return self.litros*self.valor_litro_combustivel
    
    #converte as informações para um dicionario para ser compativel com o json
    def to_dict(self):
        return {
            "data": self.data.isoformat(),
            "tipo_combustivel": self.tipo_combustivel,
            "litros": self.litros,
            "valor_litro_combustivel": self.valor_litro_combustivel,
            "custo_total": self.custo_total,
        }
       
        