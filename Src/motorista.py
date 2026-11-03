from .pessoa import Pessoa

#Classe motorista, que herda de pessoas as informações básicas e adiciona o numero e o tipo da cnh e 
# a situação atual do motorista que inicialmente deve ser "disponivel"
class Motorista(Pessoa):
    def __init__(self, nome, cpf , idade, numero_cnh, tipo_cnh):
        super().__init__(nome,cpf, idade)
        self.numero_cnh = numero_cnh
        self.tipo_cnh = tipo_cnh
        self._ocupado = False
    #Transformação para dicionario do numero e tipo da cnh e o status do motorista
    def to_dict(self):
        d = super().to_dict()
        d["numero_cnh"]= self.numero_cnh
        d["tipo_cnh"]= self.tipo_cnh
        d["ocupado"] = self._ocupado
        return d
    
    @classmethod
    def from_dict(cls, d):
      e = cls(d["nome"],d["cpf"],d["idade"],d["numero_cnh"], d["tipo_cnh"])
      e._ocupado = d.get("ocupado", False)
      return e
    #Tipos de carteira de motorista para a validação da existencia da carteira
    # quanto para o nivel dos veiculos que o motorista pode conduzir
    CARTEIRAS = {
        "A":  {"A"},
        "B":  {"B"},
        "C":  {"B", "C"},
        "AB": {"A", "B"},
        "AC": {"A", "B", "C"},
        "AD": {"A", "B", "C", "D"},
        "AE": {"A", "B", "C", "D", "E"},
        }
      
    def __str__(self):
        return(
        f"Nome: {self.nome}\n"
        f"CPF: {self.cpf}\n"
        f"Idade: {self.idade}\n"
        f"CNH: {self.numero_cnh}\n"
        f"Categoria: {self.tipo_cnh}\n"
        f"Situação: {self._ocupado}"
        )

    @property 
    def numero_cnh(self):
        return self._numero_cnh
    #Verificação do numero da cnh quanto a quantidade básica (11) de caracteres
    @numero_cnh.setter
    def numero_cnh(self, numero_cnh):
        if len(numero_cnh) < 11 or len(numero_cnh) > 11:
            raise ValueError(f"{numero_cnh} número de registro da CNH inválido")
        self._numero_cnh = numero_cnh

    @property
    def tipo_cnh(self):
        return self._tipo_cnh
    #Setter que verifica o tipo de cnh do motorista
    @tipo_cnh.setter 
    def tipo_cnh(self, tipo_cnh):
        tipo_cnh = tipo_cnh.upper()
        if tipo_cnh not in self.CARTEIRAS:
            raise ValueError(f"{tipo_cnh} não é um tipo de CNH")
        self._tipo_cnh = tipo_cnh
    #Função que verifica se o motorista pode dirigir o veiculo designado a ele
    def pode_conduzir(self, categoria_exigida):
        return categoria_exigida in self.CARTEIRAS[self._tipo_cnh]

    @property
    def ocupado(self):
        return self._ocupado 
    #Função de ocupar o motorista para as viagens
    def ocupar(self):
        if self._ocupado:
            raise ValueError(f"{self.nome} já está em outra viagem")
        self._ocupado = True
    #Função de liberar o motorista se esse estiver indisponivel
    def liberar(self):
        self._ocupado = False