class Veiculo:
    categoria_exigida = None
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
        self.manutencoes = []

    def __str__(self):
        return (
                f"Placa: {self.placa}\n"
                f"Marca: {self.marca}\n"
                f"Modelo: {self.modelo}\n"
                f"Ano: {self.ano}\n"
                f"KM rodados: {self.km_rodados}\n"
                f"Consumo_Medio: {self.consumo_medio}\n"
                f"Status: {self.status}"
        )

    def to_dict(self):
        return {
            "placa": self.placa,
            "marca": self.marca,
            "modelo": self.modelo,
            "tipo": self.tipo,
            "ano": self.ano,
            "km_rodados": self.km_rodados,
            "consumo_medio": self.consumo_medio,
            "tipo_combustivel": self.tipo_combustivel,
            "tamanho_tanque_combustivel": self.tamanho_tanque_combustivel,
            "status": self._status,
        }

    @classmethod
    def from_dict(cls,d):
        return cls(d["placa"],d["marca"],d["modelo"],d["tipo"],d["ano"],d["km_rodados"],d["consumo_medio"],d["tipo_combustivel"],d["tamanho_tanque_combustivel"],d["status"])


    @property
    def placa(self):
        return self._placa

    @placa.setter 
    def placa(self, placa):
        if len(placa) < 7 or len(placa) > 8:
            raise ValueError(f"{placa} não atende aos requisitos obrigatórios")
        else:
            self._placa = placa

    @property
    def marca(self):
        return self._marca

    @marca.setter 
    def marca(self, marca):
        if len(marca) == 0:
          raise ValueError(f"{marca} é uma marca inválida")
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo


    @modelo.setter 
    def modelo(self, modelo):
        if len(modelo) == 0:
            raise ValueError(f"{modelo} é um modelo inválido")
        else:
            self._modelo = modelo

    @property
    def tipo(self):
        return self._tipo

    @tipo.setter
    def tipo(self,tipo):
        if len(tipo) == 0:
            raise ValueError("Digite um tipo de veículos existentes: Carro, Caminhao e Moto ")
        elif tipo.upper() == "CARRO" or tipo.upper() == "CAMINHAO" or tipo.upper() == "MOTO":
            self._tipo= tipo
        else:
            raise ValueError(f"{tipo} não é um dos tipos de veículos existentes")
        
    @property
    def ano(self):
        return self._ano

    @ano.setter
    def ano(self, ano):
        ano =int(ano)
        if ano < 1930 or ano > 2026:
            raise ValueError(f"{ano} é um ano inválido" )
        self._ano = ano

    @property
    def km_rodados(self):
        return self._km_rodados
    
    @km_rodados.setter
    def km_rodados(self, km_rodados):
        if km_rodados < 0:
            raise ValueError(f"{km_rodados} é um número inválido")
        else:
            self._km_rodados = km_rodados

    @property
    def consumo_medio(self):
        return self._consumo_medio

    @consumo_medio.setter
    def consumo_medio(self, consumo_medio):
        if consumo_medio <= 0:
            raise ValueError(f"{consumo_medio} consumo médio não pode ser inferior ou igual a 0")
        else:
            self._consumo_medio = consumo_medio

    @property
    def tipo_combustivel(self):
        return self._tipo_combustivel

    @tipo_combustivel.setter
    def tipo_combustivel(self, tipo_combustivel):
        tipo = tipo_combustivel.strip().upper()
        if tipo in ("DIESEL", "ETANOL", "GASOLINA"):
            self._tipo_combustivel = tipo
        else:
            raise ValueError(f"{tipo_combustivel} não é um tipo de combustível")

    @property
    def tamanho_tanque_combustivel(self):
        return self._tamanho_tanque_combustivel
    
    @tamanho_tanque_combustivel.setter 
    def tamanho_tanque_combustivel(self, valor):
        if valor <= 0:
            raise ValueError(f"{valor} não é um tamanho válido do tanque de combustível")
        self._tamanho_tanque_combustivel = valor

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def qnt_manutencoes(self):
        return len(self.manutencoes)
