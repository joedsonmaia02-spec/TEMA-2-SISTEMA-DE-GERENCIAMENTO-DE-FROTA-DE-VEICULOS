from pessoa import Pessoa

class motorista(Pessoa):
    def __init__(self, nome, cpf , idade, numero_cnh, tipo_cnh):
        super().__init__(nome,cpf, idade)
        self.numero_cnh = numero_cnh
        self.tipo_cnh = tipo_cnh

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
    