class Pessoa:
    def __init__(self,nome,cpf,idade,):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, nome):
        if len(nome) > 0:
            self.nome = nome
        else:
            raise ValueError(f"{nome} é um nome inválido")

    @property
    def cpf(self):
        return self.cpf

    @cpf.setter
    def cpf(self, cpf):
        if len(cpf) >= 11 and len(cpf) <= 14:
            self.cpf= cpf
        else:
            raise ValueError(f"{cpf} não é um CPF válido")

    @property
    def idade(self):
        return self.idade

    @idade.setter
    def idade(self, idade):
        if idade >= "18":
            self.idade = idade
        else:
            raise ValueError(f"{idade} é uma Idade é inválida ")