from veiculo import Veiculo

class caminhao(Veiculo):
    def __init__(self, placa, marca, modelo, ano, km_rodados, consumo_medio, tipo_combustivel,tamanho_tanque_combustivel , status, eixos):
        super().__init__( placa, marca, modelo, "CAMINHAO", ano, km_rodados, consumo_medio, tipo_combustivel, tamanho_tanque_combustivel, status)
        self.eixos = eixos

    categoria_exigida = "C"

    def __str__(self):
        return super().__str__() + f"\n Eixos: {self.eixos}"

    def to_dict(self):
        d = super().to_dict()
        d["eixos"] = self.eixos
        return d

    @classmethod
    def from_dict(cls,d):
        return cls(d["placa"], d["marca"], d["modelo"], d["ano"], d["km_rodados"],d["consumo_medio"], d["tipo_combustivel"],
                   d["tamanho_tanque_combustivel"], d["status"], d["eixos"])

    @property
    def eixos(self):
        return self._eixos

    @eixos.setter
    def eixos(self, eixos):
        eixos = eixos.strip().upper()
        if eixos in("SIMPLES","DUPLOS", "TRIPLOS"):
            self._eixos = eixos
        else:
            raise ValueError(f"Tipo de eixo inexistente")

