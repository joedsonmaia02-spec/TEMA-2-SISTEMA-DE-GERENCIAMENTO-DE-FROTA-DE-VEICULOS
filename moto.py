from veiculo import Veiculo

class moto(Veiculo):
    def __init__(self, placa, marca, modelo, ano, km_rodados, consumo_medio, tipo_combustivel, tamanho_tanque_combustivel, status, cilindradas):
        super().__init__( placa, marca, modelo, "moto", ano, km_rodados, consumo_medio,tipo_combustivel, tamanho_tanque_combustivel, status)
        self.cilindradas= cilindradas

    def __str__(self):
        return super().__str__() + f"\nCilindradas: {self.cilindradas}"

    def to_dict(self):
         d = super().to_dict()  
         d["cilindradas"] = self.cilindradas
         return d

    @classmethod
    def from_dict(cls, d):
        return cls(d["placa"],d["marca"],d["modelo"],d["ano"],d["km_rodados"],d["consumo_medio"],d["tipo_combustivel"],d["tamanho_tanque_combustivel"],d["status"],d["cilindradas"])

    @property
    def cilindradas(self):
            return self._cilindradas

    @cilindradas.setter
    def cilindradas(self, cilindradas):
        if cilindradas <=0:
            raise ValueError(f"{cilindradas} não é uma quantidade válida de cilindradas")
        else:
            self._cilindradas = cilindradas
