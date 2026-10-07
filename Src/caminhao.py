from veiculo import Veiculo

class caminhao(Veiculo):
    def __init__(self, placa, marca, modelo, ano, km_rodados, consumo_medio, tipo_combustivel, status, eixos):
        super().__init__( placa, marca, modelo, "caminhão", ano, km_rodados, consumo_medio, tipo_combustivel , status)
        self.eixos = eixos

    @property
    def eixos(self):
        return self._eixos

    @eixos.setter
    def eixos(self, eixos):
        if eixos in("simples","duplos", "triplos"):
            self._eixos = eixos
        else:
            raise ValueError(f"Tipo de eixo inexistente")


c = caminhao("ABC1D23", "Volvo", "FH", 2015, 80000, 3.5, "Disponivel", "duplos")
print(c.eixos, c.marca, c.consumo_medio, c.ano, c.modelo, c.km_rodados)    