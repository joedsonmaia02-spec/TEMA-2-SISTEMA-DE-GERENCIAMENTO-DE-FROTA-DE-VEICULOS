from veiculo import Veiculo

class carro(Veiculo):
    def __init__(self, placa, marca, modelo, ano, km_rodados, consumo_medio, tipo_combustivel, status, qnt_portas):
        super().__init__( placa, marca, modelo, "carro", ano, km_rodados, consumo_medio, tipo_combustivel, status)
        self.qnt_portas = qnt_portas

    @property
    def qtd_portas(self):
        return self._qtd_portas

    @qtd_portas.setter
    def qtd_portas(self, qtd_portas):
        if qtd_portas < 2 or qtd_portas > 5:
            raise ValueError(f"{qtd_portas} não é uma quantidade de portas válida")
        self._qtd_portas = qtd_portas

c = carro("ABC1D23", "Fiat", "Uno", 2015, 80000, 12.5, "Disponivel", 4)

print(c.marca, c.placa, c.modelo, c.tipo)