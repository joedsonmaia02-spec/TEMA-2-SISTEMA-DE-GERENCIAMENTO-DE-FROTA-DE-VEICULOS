from pessoa import Pessoa

class Motorista(Pessoa):
    def __init__(self, nome, cpf , idade, numero_cnh, tipo_cnh):
        super().__init__(nome,cpf, idade)
        self.numero_cnh = numero_cnh
        self.tipo_cnh = tipo_cnh

    def to_dict(self):
        d = super().to_dict()
        d["numero_cnh"]= self.numero_cnh
        d["tipo_cnh"]= self.tipo_cnh
        return d
        
    @classmethod
    def from_dict(cls, d):
      return cls(d["nome"],d["cpf"],d["idade"],d["numero_cnh"], d["tipo_cnh"])  

    def __str__(self):
        return(
        f"Nome: {self.nome}\n"
        f"CPF: {self.cpf}\n"
        f"Idade: {self.idade}\n"
        f"CNH: {self.numero_cnh}\n"
        f"Categoria: {self.tipo_cnh}"
    )

    @property 
    def numero_cnh(self):
        return self._numero_cnh

    @numero_cnh.setter
    def numero_cnh(self, numero_cnh):
        if len(numero_cnh) < 11 or len(numero_cnh) > 11:
            raise ValueError(f"{numero_cnh} número de registro da CNH inválido")
        self._numero_cnh = numero_cnh

    @property
    def tipo_cnh(self):
        return self._tipo_cnh

    @tipo_cnh.setter 
    def tipo_cnh(self, tipo_cnh):
        tipo_cnh = tipo_cnh.upper()
        if tipo_cnh not in("A","B","C","AB","AC","AD","AE"):
            raise ValueError(f"{tipo_cnh} não é um tipo de CNH")
        self._tipo_cnh = tipo_cnh
    