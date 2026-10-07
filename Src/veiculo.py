class Veiculo:
    def __init__(self, placa, marca, modelo, tipo, ano, km_rodados, consumo_medio, tipo_combustivel , tamanho_tanque_combustivel, status ):
        self.placa = placa
        self.marca = marca
        self.modelo = modelo
        self.tipo = tipo
        self.ano = ano
        self.km_rodados = km_rodados
        self.consumo_medio = consumo_medio
        self.tipo_combustivel = tipo_combustivel
        self.tamanho_tanque_combustivel = tamanho_tanque_combustivel
        self.status = status

    @property
    def placa(self):
        return self._placa

    @placa.setter 
    def placa(self, placa):
        if len(placa) < 7 or len(placa) > 7:
            raise Exception(f"{placa} não atende aos requisitos obrigatórios")
        else:
            self._placa = placa

    @property
    def marca(self):
        return self._marca

    @marca.setter 
    def marca(self, marca):
        if len(marca) == 0:
            print(f"{marca} é uma marca inválida")
        else:
            self._marca = marca

    @property
    def modelo(self):
        return self._modelo


    @modelo.setter 
    def modelo(self, modelo):
        if len(modelo) == 0:
            print(f"{modelo} é um modelo inválido")
        else:
            self._modelo = modelo

    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, ano):
        if ano < 1930 or ano > 2026:
            print(f"{ano} é um ano inválido" )
        else:
            self._ano = ano

    @property
    def km_rodados(self):
        return self._km_rodados
    
    @km_rodados.setter
    def km_rodados(self, km_rodados):
        if km_rodados < 0:
            print(f"{km_rodados} é um número inválido")
        else:
            self._km_rodados = km_rodados

    @property
    def consumo_medio(self):
        return self._consumo_medio

    @consumo_medio.setter
    def consumo_medio(self, consumo_medio):
        if consumo_medio < 0:
            print(f"{consumo_medio} consumo médio não pode ser inferior a 0")
        else:
            self._consumo_medio = consumo_medio

    @property
    def tipo_combustivel(self):
        return self._tipo_combustivel

    @tipo_combustivel.setter
    def tipo_combustivel(self, tipo_combustivel):
        if tipo_combustivel in ("Diesel", "Etanol", "Gasolina"):
            self._tipo_combustivel = tipo_combustivel
        else:
            raise ValueError(f"{tipo_combustivel} não é um tipo de combustível")

    @property
    def tamanho_tanque_combustivel(self):
        return self.tamanho_tanque_combustivel
    
    @tamanho_tanque_combustivel.setter 
    def tamanho_tanque_combustivel(self, tamanho_tanque_combustivel):
        if tamanho_tanque_combustivel <0 :
            raise ValueError(f"{self.tamanho_tanque_combustivel} não é um tamanho válido do tanque de combustível")
        else:
            self.tamanho_tanque_combustivel = self.tamanho_tanque_combustivel

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        status = "Disponivel"
        self._status = status


