from .motorista import Motorista
from .veiculo import Veiculo
from .abastecimento import Abastecimento
from .manutencao import Manutencao
from datetime import datetime

class Viagem:
    def __init__(self, motorista:Motorista, veiculo:Veiculo, origem, destino, distancia_total, distancia_percorrida):
        self.id = None
        self.data_inicio = datetime.now().strftime("%Y-%m-%d %H:%M")
        self.motorista = motorista
        self.veiculo = veiculo
        self.origem = origem
        self.destino = destino
        self.distancia_total = distancia_total
        self.distancia_percorrida = distancia_percorrida
        self.abastecimentos = []
        self.manutencoes = []
        self.associar_motorista_veiculo(motorista)

    #Verifica se o motorista pode conduzir o veiculo, se ele está ocupado ou não e se a a carteira de motorista dele permite dirigir tal veiculo
    def associar_motorista_veiculo(self, motorista):
        self.veiculo.validar_alocacao()
        if motorista.ocupado:
            raise ValueError(f"{motorista.nome} não está disponível")
        if not motorista.pode_conduzir(self.veiculo.categoria_exigida):
            raise ValueError(
            f"{motorista.nome} (CNH {motorista.tipo_cnh}) não pode conduzir "
            f"{self.veiculo.tipo}: exige categoria {self.veiculo.categoria_exigida}")
        self.motorista= motorista

    @property 
    def distancia_total(self):
        return self._distancia_total
    #Setter da Distância total da viagem não pode ser menor ou igual a 0
    @distancia_total.setter
    def distancia_total(self, valor):
        if valor <= 0:
            raise ValueError(f"{valor} Essa não é uma distância válida")
        self._distancia_total = valor

    @property
    def distancia_percorrida(self):
        return self._distancia_percorrida
    #Setter da disntancia percorrida não pode ser negativo
    @distancia_percorrida.setter
    def distancia_percorrida(self, distancia_per):
        if distancia_per <0:
            raise ValueError("Distância não é Válida")    
        self._distancia_percorrida = distancia_per

    @property
    def qnt_abastecimentos(self):
        return len(self.abastecimentos)

    @property
    def qnt_manutencoes(self):
        return len(self.manutencoes)
    
    @property
    def total_litros(self):
        return sum(r.litros for r in self.abastecimentos)

    @property
    def custo_combustivel(self):
        return sum(r.custo_total for r in self.abastecimentos)

    @property
    def custo_manutencao(self):
        return sum(r.valor_manutencao for r in self.manutencoes)

    @property
    def custo_total(self):
        return self.custo_combustivel + self.custo_manutencao

    @property
    def consumo_viagem(self):
        if self.total_litros == 0 or self.distancia_percorrida == 0:
            return None
        return self.distancia_percorrida / self.total_litros
    
    @property
    def consumo_fora_do_padrao(self):
        consumo = self.consumo_viagem
        if consumo is None:
            return None
        minimo, maximo = self.veiculo.faixa_consumo
        return not (minimo <= consumo <= maximo)

    #Método para o inicio da viagem
    def iniciar_viagem(self):
        self.veiculo.validar_alocacao()
        self.motorista.ocupar()
        self.veiculo.status = "Viagem em curso"

    #Método para parar a viagem devido a abastecimentos ou manutenções e guardar as informações desses
    def parar_viagem(self, motivo, litros=None, valor_litro_combustivel=None,
                     tipo_manutencao=None, valor_manutencao=None):
        if self.veiculo.status != "Viagem em curso":
            raise ValueError("Veiculo não está em viagem")

        if motivo == "abastecimento":
            if litros is None or valor_litro_combustivel is None:
                raise ValueError("Informe os litros e o valor do litro")
            abastecimento = Abastecimento(self, litros, valor_litro_combustivel)
            self.abastecimentos.append(abastecimento)
            self.veiculo.abastecimentos.append(abastecimento)

        elif motivo == "manutencao":
            if tipo_manutencao is None:
                raise ValueError("Informe o tipo da manutenção")
            manutencao = Manutencao(self, tipo_manutencao, valor_manutencao)
            self.manutencoes.append(manutencao)
            self.veiculo.manutencoes.append(manutencao)

        else:
            raise ValueError(f"Motivo inválido: {motivo}")

        self.veiculo.status = f"Veiculo em {motivo}"

    #Método para retornar para a viagem apos uma parada 
    def retornar_viagem(self, motivo):
        if self.veiculo.status == f"Veiculo em {motivo}":
            self.veiculo.status = "Viagem em curso"
        else:
            raise ValueError("Veiculo não está parado")
    #Método para a conclusão da viagem registrando o consumo e kilometros rodados e liberando o motorista e o veiculo
    def concluir_viagem(self, distancia_percorrida=None):
        if self.veiculo.status != "Viagem em curso":
            raise ValueError("Veiculo não está em trajeto")
        if distancia_percorrida is not None:
            self.distancia_percorrida = distancia_percorrida
        self.veiculo.km_rodados += self.distancia_percorrida
        if self.consumo_viagem is not None:
            self.veiculo.registrar_consumo(self.distancia_percorrida, self.total_litros)
        self.motorista.liberar()
        self.veiculo.status = "Disponivel"
    #Metodo para a criação do relatorio em arquivo .json pegando todas as informações da viagem e
    #agrupando tudo em um mesmo lugar no relatorio.json
    def relatorio(self):
        linhas = [
            "=" * 40,
            f"Motorista: {self.motorista.nome} (CNH {self.motorista.tipo_cnh})",
            f"Veículo: {self.veiculo.placa} - {self.veiculo.marca} {self.veiculo.modelo}",
            f"Trajeto: {self.origem} -> {self.destino}",
            f"Distância total: {self.distancia_total} km",
            f"Distância percorrida: {self.distancia_percorrida} km",
            "-" * 40,
            f"Abastecimentos: {self.qnt_abastecimentos} ({self.total_litros:.1f} L)",
        ]
        for r in self.abastecimentos:
            linhas.append(f"  {r.data} | {r.tipo_combustivel} | {r.litros} L | R$ {r.custo_total:.2f}")

        linhas.append(f"Manutenções: {self.qnt_manutencoes}")
        for r in self.manutencoes:
            linhas.append(f"  {r.tipo_manutencao} R$ {r.valor_manutencao:.2f}")

        linhas.append("-" * 40)
        linhas.append(f"Custo combustível: R$ {self.custo_combustivel:.2f}")
        linhas.append(f"Custo manutenção: R$ {self.custo_manutencao:.2f}")
        linhas.append(f"Custo total: R$ {self.custo_total:.2f}")
        #Verificação do consumo se está fora da curva adequada com base na faixa dita anteriormente
        consumo = self.consumo_viagem
        if consumo is None:
            linhas.append("Consumo: sem dados suficientes (nenhum abastecimento ou distância)")
        else:
            minimo, maximo = self.veiculo.faixa_consumo
            situacao = "FORA DO PADRÃO" if self.consumo_fora_do_padrao else "dentro do padrão"
            linhas.append(f"Consumo: {consumo:.2f} km/l ({situacao}, faixa {minimo} a {maximo})")
        linhas.append("=" * 40)
        return "\n".join(linhas)

    def to_dict(self):
        return{
            "id": self.id,
            "data_inicio": self.data_inicio,
            "motorista": self.motorista.nome,
            "cpf_motorista": self.motorista.cpf,
            "cnh": self.motorista.tipo_cnh,
            "placa_veiculo": self.veiculo.placa,
            "veiculo": f"{self.veiculo.marca} {self.veiculo.modelo}",
            "origem": self.origem,
            "destino": self.destino,
            "distancia_total": self.distancia_total,
            "distancia_percorrida": self.distancia_percorrida,
            "abastecimentos": [r.to_dict() for r in self.abastecimentos],
            "manutencoes": [r.to_dict() for r in self.manutencoes],
            "total_litros": self.total_litros,
            "custo_combustivel": self.custo_combustivel,
            "custo_manutencao": self.custo_manutencao,
            "custo_total": self.custo_total,
            "consumo_km_l": self.consumo_viagem,
            "consumo_fora_do_padrao": self.consumo_fora_do_padrao,
        }