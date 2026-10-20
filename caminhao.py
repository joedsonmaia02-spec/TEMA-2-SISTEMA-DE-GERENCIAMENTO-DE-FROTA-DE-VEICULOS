from veiculo import Veiculo

class caminhao(Veiculo):
    def __init__(self, placa, marca, modelo, ano, km_rodados, consumo_medio, tipo_combustivel,tamanho_tanque_combustivel , status, eixos):
        super().__init__( placa, marca, modelo, "caminhão", ano, km_rodados, consumo_medio, tipo_combustivel, tamanho_tanque_combustivel, status)
        self.eixos = eixos

    def __str__(self):
        return super().__str__() + f"\n Eixos: {self.eixos}"

    def to_dict(self):
        d = super().to_dict()
        d["eixos"] = self.eixos
        return d

    @classmethod
    def from_dict(cls,d):
        return cls(d["eixos"])

    @property
    def eixos(self):
        return self._eixos

    @eixos.setter
    def eixos(self, eixos):
        if eixos in("simples","duplos", "triplos"):
            self._eixos = eixos
        else:
            raise ValueError(f"Tipo de eixo inexistente")

