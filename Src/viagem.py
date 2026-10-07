
from motorista import Motorista
from veiculo import Veiculo
from abastecimento import Abastecimento
from manutencao import Manutencao

class Viagem:
    def __init__(self, motorista:Motorista, veiculo:Veiculo, origem, destino, distancia_total,qnt_abastecimentos, qnt_manutencoes, tipo_manutencao):
        self.motorista = motorista
        self.veiculo = veiculo
        self.origem = origem
        self.destino = destino
        self.distancia_total = distancia_total
        self.qnt_abastecimentos = qnt_abastecimentos#vai ser implantado
        self.qnt_manutencoes = qnt_manutencoes #vai ser implantado
        self.tipo_manutencao = tipo_manutencao
        

    @property 
    def distancia_total(self):
        return self._distancia_total

    @distancia_total.setter
    def distancia_total(self, valor):
        if valor <= 0:
         raise ValueError(f"{valor} Essa não é uma distância válida")
        else:
            self.distancia_total = valor

    def iniciar_viagem(self):
        if self.veiculo.status == "Disponivel":
            self.veiculo.status = "Viagem em curso"
        else:
            raise ValueError(f"{self.veiculo.status} Veiculo Indisponivel")
        
    def parar_viagem(self, motivo, litros=None, valor_litro_combustivel=None, tipo_manutencao=None, valor_manutencao=None):
        if self.veiculo.status == "Viagem em curso":
            self.veiculo.status = f"Veiculo em {motivo}"
        else:
            raise ValueError("Veiculo não está em viagem")
        
        if motivo == "abastecimento":
            if litros is None or valor_litro_combustivel is None:
                raise ValueError("Informe os litros e o valor do litro")
            abastecimento = Abastecimento(self, litros, valor_litro_combustivel)

        elif motivo == "manutencao":
            if tipo_manutencao is None:
                raise ValueError("Informe o tipo da manutenção junto ao valor")
            manutencao = Manutencao(self, tipo_manutencao, valor_manutencao)
            

    def retormar_viagem(self, motivo):
        if self.veiculo.status == f"Veiculo em {motivo}":
            self.veiculo.status = "Viagem em curso"
        else:
            raise ValueError(f"Veiculo não está parado")

    def concluir_viagem(self):
        if self.veiculo.status == "Viagem em curso":
            self.veiculo.status = "Disponivel"
        else:
            raise ValueError("Veiculo não está em trajeto")