from veiculo import Veiculo

class carro(Veiculo):
    def __init__(self, placa, marca, modelo, ano, km_rodados, consumo_medio, tipo_combustivel, tamanho_tanque_combustivel, status, qnt_portas):
        super().__init__( placa, marca, modelo, "carro", ano, km_rodados, consumo_medio, tipo_combustivel, tamanho_tanque_combustivel, status)
        self.qnt_portas = qnt_portas

    def __str__(self):
        return super().__str__() + f"\nQuantidade de Portas: {self.qnt_portas}"

    def to_dict(self):
        d = super().to_dict()
        d["qnt_portas"] = self.qnt_portas
        return d

    @classmethod
    def from_dict(cls,d):
        return cls(d["qnt_portas"])

    @property
    def qtd_portas(self):
        return self._qtd_portas

    @qtd_portas.setter
    def qtd_portas(self, qtd_portas):
        if qtd_portas < 2 or qtd_portas > 5:
            raise ValueError(f"{qtd_portas} não é uma quantidade de portas válida")
        self._qtd_portas = qtd_portas



