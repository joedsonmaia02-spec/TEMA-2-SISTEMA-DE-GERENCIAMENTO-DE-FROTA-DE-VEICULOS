from datetime import datetime
from .config import SETTINGS

class Veiculo:
    def __init__(self, placa, marca, modelo, tipo, ano, km_rodados, consumo_medio, tipo_combustivel , tamanho_tanque_combustivel, status, km_ultima_revisao ):
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
        self.abastecimentos = []
        self.km_com_consumo = 0
        self.litros_consumidos = 0
        self.km_ultima_revisao = km_ultima_revisao

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

    #Modelo de como o código ficará salvo no veiculos.json, pegando tudo de principal que o veiculo possui.

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
            "km_ultima_revisao": self.km_ultima_revisao,
        }

    def carregar_consumo(self, d):
        self.km_ultima_revisao = d.get("km_ultima_revisao", 0)
        self.km_com_consumo = d.get("km_com_consumo", 0)
        self.litros_consumidos = d.get("litros_consumidos", 0)

    @property
    def categoria_exigida(self):
        try:
            return SETTINGS["categoria_minima_cnh"][self.tipo.upper()]
        except KeyError:
            raise ValueError(f"Tipo {self.tipo} não existe categoria dessa CNH no settings.json")

    @property
    def faixa_consumo(self):
        f = SETTINGS["faixa_consumo_km_l"][self.tipo.upper()]
        return f["min"], f["max"]

    @property
    def consumo_fora_do_padrao(self):
        minimo, maximo = self.faixa_consumo
        return not (minimo <= self.consumo_medio <= maximo)

    def registrar_consumo(self, km, litros):
        """Chamado ao concluir uma viagem com abastecimento."""
        self.km_com_consumo += km
        self.litros_consumidos += litros
        self.consumo_medio = self.km_com_consumo / self.litros_consumidos

    #verificação da revisão por kilometro limite
    @property
    def precisa_revisao(self):
        return self.km_rodados - self.km_ultima_revisao >= SETTINGS["limite_km_revisao"]

    @property
    def placa(self):
        return self._placa

    #Se a placa tiver menos que 7 caracteres ou for maior que 8, entrará em erro devido que não atende ao padrão mercosul
    @placa.setter 
    def placa(self, placa):
        if len(placa) < 7 or len(placa) > 8:
            raise ValueError(f"{placa} não atende aos requisitos obrigatórios")
        else:
            self._placa = placa

    @property
    def marca(self):
        return self._marca

    #Se a entrada da marca não tiver caractere algum será inválida
    @marca.setter 
    def marca(self, marca):
        if len(marca) == 0:
          raise ValueError(f"{marca} é uma marca inválida")
        self._marca = marca

    @property
    def modelo(self):
        return self._modelo

    #Se a entrada do modelo não tiver caractere algum será inválido
    @modelo.setter 
    def modelo(self, modelo):
        if len(modelo) == 0:
            raise ValueError(f"{modelo} é um modelo inválido")
        else:
            self._modelo = modelo

    @property
    def tipo(self):
        return self._tipo

    #Se a entrada para o tipo de veiculo não for carro,moto ou caminhao, o sistema vai apontar a falha na seleção do tipo
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

    #Se a entrada para o ano do veiculo for maior que o ano atual e menor que a data limite (1930), 
    # o sistema apresentará erro devido a idade do veiculo ou erro de digitação
    @ano.setter
    def ano(self, ano):
        ano =int(ano)
        if ano < 1930 or ano > datetime.now().year:
            raise ValueError(f"{ano} é um ano inválido" )
        self._ano = ano

    @property
    def km_rodados(self):
        return self._km_rodados
    #Setter do km_rodados que não podem ser inferiores a 0
    @km_rodados.setter
    def km_rodados(self, km_rodados):
        if km_rodados < 0:
            raise ValueError(f"{km_rodados} é um número inválido")
        else:
            self._km_rodados = km_rodados

    @property
    def consumo_medio(self):
        return self._consumo_medio
    #Setter do consumo medio que não pode ser inferior ou igual a 0, pois não há veiculo assim
    @consumo_medio.setter
    def consumo_medio(self, consumo_medio):
        if consumo_medio <= 0:
            raise ValueError(f"{consumo_medio} consumo médio não pode ser inferior ou igual a 0")
        else:
            self._consumo_medio = consumo_medio

    @property
    def tipo_combustivel(self):
        return self._tipo_combustivel

    #Setter do tipo de combustivel, com 3 opções que sempre vão para a padronização com o .upper()
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

    #Setter de verificação do tanque de combustivel que não deve ser menor ou igual a 0
    @tamanho_tanque_combustivel.setter 
    def tamanho_tanque_combustivel(self, valor):
        if valor <= 0:
            raise ValueError(f"{valor} não é um tamanho válido do tanque de combustível")
        self._tamanho_tanque_combustivel = valor

    #Validar se o veiculo possui o status atual como livre e se não precisa da manutenção preventiva
    def validar_alocacao(self):
        if self.status != "Disponivel":
            raise ValueError(f"Veículo {self.placa} indisponível (status: {self.status})")
        if self.precisa_revisao:
            raise ValueError(f"Veículo {self.placa} precisa de revisão preventiva")

    #Verificação dos status e validação do veiculo quanto a disponibilidadde

    STATUS_VALIDOS = {
        "Disponivel",
        "Viagem em curso",
        "Veiculo em abastecimento",
        "Veiculo em manutencao",
        "Em manutencao",
        "Inativo",
    }
        
    @property
    def status(self):
        return self._status
    #Setter para a verificação dos status disponiveis do veiculo
    @status.setter
    def status(self, status):
        if status not in self.STATUS_VALIDOS:
            raise ValueError(f"{status} não é um status válido")
        self._status = status

    @property
    def qnt_manutencoes(self):
        return len(self.manutencoes)
