from pessoa import Pessoa

class Motorista(Pessoa):
    def __init__(self, nome, cpf , idade, numero_cnh, tipo_cnh):
        super().__init__(nome,cpf, idade)
        self.numero_cnh = numero_cnh
        self.tipo_cnh = tipo_cnh
        self._ocupado = False

<<<<<<< HEAD

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
        if tipo_cnh not in self.CARTEIRAS:
            raise ValueError(f"{tipo_cnh} não é um tipo de CNH")
        self._tipo_cnh = tipo_cnh

    def pode_conduzir(self, categoria_exigida):
        return categoria_exigida in self.CARTEIRAS[self._tipo_cnh]

    @property
    def ocupado(self):
        return self._ocupado 

    def ocupar(self):
        if self._ocupado:
            raise ValueError(f"{self.nome} já está em outra viagem")
        self._ocupado = True

    def liberar(self):
        self._ocupado = False
=======
    @property 
    def numero_cnh(self):
        return self.numero_cnh

    @numero_cnh.setter
    def numero_cnh(self, numero_cnh):
        if len(numero_cnh) < 11 or len(numero_cnh) > 11:
            raise ValueError(f"{numero_cnh} número de registro da CNH inválido")
        else:
            self.numero_cnh = numero_cnh

    @property
    def tipo_cnh(self):
        return self.tipo_cnh

    @tipo_cnh.setter 
    def tipo_cnh(self, tipo_cnh):
        if tipo_cnh not in("A","B","C","AB","AC","AD","AE"):
            raise ValueError(f"{tipo_cnh} não é um tipo de CNH")
    
>>>>>>> 9e7b941e00328633fa8441e9ccddf70b4a696d17
