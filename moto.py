from veiculo import Veiculo

class moto(Veiculo):
    def __init__(self, placa, marca, modelo, ano, km_rodados, consumo_medio, tipo_combustivel, status, cilindradas):
        super().__init__( placa, marca, modelo, "moto", ano, km_rodados, consumo_medio,tipo_combustivel, status)
        self.cilindradas= cilindradas

    @property
    def cilindradas(self):
            return self._cilindradas

    @cilindradas.setter
    def cilindradas(self, cilindradas):
        if cilindradas <=0:
            raise ValueError(f"{cilindradas} não é uma quantidade válida de cilindradas")
        else:
            self._cilindradas = cilindradas

c = moto("ABC1D23", "Fiat", "Uno", 2015, 80000, 12.5, "Disponivel", 500)

print(c.cilindradas,c.marca,c.modelo)