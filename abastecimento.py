from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from viagem import Viagem

class Abastecimento:
    def __init__(self, viagem: "Viagem", litros, valor_litro_combustivel):
        self.viagem = viagem 
        self.valor_litro_combustivel = valor_litro_combustivel
        self.litros = litros
    
    @property
    def tipo_combustivel(self):
        return self.viagem.veiculo.tipo_combustivel

    @property
    def litros(self):
        return self._litros

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
       
        