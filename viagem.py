
from motorista import Motorista
from veiculo import Veiculo
from abastecimento import Abastecimento
from manutencao import Manutencao

class Viagem:
    def __init__(self, motorista:Motorista, veiculo:Veiculo, origem, destino, distancia_total, distancia_percorrida):
        self.motorista = motorista
        self.veiculo = veiculo
        self.origem = origem
        self.destino = destino
        self.distancia_total = distancia_total
        self.distancia_percorrida = distancia_percorrida
        self.abastecimentos = []
        self.manutencoes = []

    @property 
    def distancia_total(self):
        return self._distancia_total

    @distancia_total.setter
    def distancia_total(self, valor):
        if valor <= 0:
            raise ValueError(f"{valor} Essa não é uma distância válida")
        self._distancia_total = valor

    @property
    def distancia_percorrida(self):
        return self._distancia_percorrida

    @distancia_percorrida.setter
    def distancia_percorrida(self, distancia_per):
        if distancia_per <0:
            raise ValueError("Distância não é Válida")    
        self._distancia_percorrida = distancia_per

    @property
    def qnt_abastecimentos(self):
        return len(self.abastecimentos)

    @property
    def qnt_manutencoes(self):
        return len(self.manutencoes)

    #def litros_estimados_restantes(self):  Talvez entrará no código final
       # distancia_restante = self.distancia_total - self.distancia_percorrida
        #return distancia_restante / self.veiculo.consumo_medio

    def iniciar_viagem(self):
        if self.veiculo.status == "Disponivel":
            self.veiculo.status = "Viagem em curso"
        else:
            raise ValueError(f"{self.veiculo.status} Veiculo Indisponivel")
        
    def parar_viagem(self, motivo, litros=None, valor_litro_combustivel=None, tipo_manutencao=None, valor_manutencao=None):
        if self.veiculo.status != "Viagem em curso":
            raise ValueError("Veiculo não está em viagem")
        
        if motivo == "abastecimento":
            if litros is None or valor_litro_combustivel is None:
                raise ValueError("Informe os litros e o valor do litro")
            abastecimento = Abastecimento(self, litros, valor_litro_combustivel)
            self.abastecimentos.append(abastecimento)

        elif motivo == "manutencao":
            if tipo_manutencao is None or valor_manutencao is None:
                raise ValueError("Informe o tipo da manutenção junto ao valor")
            manutencao = Manutencao(self, tipo_manutencao, valor_manutencao)
            self.manutencoes.append(manutencao)
            self.veiculo.manutencoes.append(manutencao)

        else:
            raise ValueError(f"Motivo inválido: {motivo}")
        self.veiculo.status = f"Veiculo em {motivo}"
            

    def retornar_viagem(self, motivo):
        if self.veiculo.status == f"Veiculo em {motivo}":
            self.veiculo.status = "Viagem em curso"
        else:
            raise ValueError(f"Veiculo não está parado")

    def concluir_viagem(self):
        if self.veiculo.status == "Viagem em curso":
            self.veiculo.status = "Disponivel"
        else:
            raise ValueError("Veiculo não está em trajeto")