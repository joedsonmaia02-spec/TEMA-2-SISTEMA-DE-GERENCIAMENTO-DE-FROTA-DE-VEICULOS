from .veiculo import Veiculo
#Class moto com o atributo próprio Cilindradas
class moto(Veiculo):
    def __init__(self, placa, marca, modelo, ano, km_rodados, consumo_medio, tipo_combustivel, tamanho_tanque_combustivel, status, cilindradas, km_ultima_revisao):
        super().__init__( placa, marca, modelo, "MOTO", ano, km_rodados, consumo_medio,tipo_combustivel, tamanho_tanque_combustivel, status, km_ultima_revisao)
        self.cilindradas= cilindradas

    def __str__(self):
        return super().__str__() + f"\nCilindradas: {self.cilindradas}"
    #Conversão do atributo cilindradas para dicionario
    def to_dict(self):
         d = super().to_dict()  
         d["cilindradas"] = self.cilindradas
         return d

    @classmethod
    def from_dict(cls, d):
        m = cls(d["placa"],d["marca"],d["modelo"],d["ano"],d["km_rodados"],d["consumo_medio"],d["tipo_combustivel"],
                d["tamanho_tanque_combustivel"],d["status"],d["cilindradas"], d.get("km_ultima_revisao", 0))
        m.carregar_consumo(d)
        return m

    @property
    def cilindradas(self):
            return self._cilindradas
    #Setter para a verificação da quantidade de cilindradas, se for inferior ou igual a 0
    @cilindradas.setter
    def cilindradas(self, cilindradas):
        if cilindradas <=0:
            raise ValueError(f"{cilindradas} não é uma quantidade válida de cilindradas")
        else:
            self._cilindradas = cilindradas
