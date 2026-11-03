#Classe Pessoa, que inclue atributos bbásicos que serão herdados para motorista:  nome, cpf e idade
class Pessoa:
    def __init__(self,nome,cpf,idade,):
        self.nome = nome
        self.cpf = cpf
        self.idade = idade

    def to_dict(self):
        return{
            "nome": self.nome,
            "cpf": self.cpf,
            "idade": self.idade,
        }

    @classmethod
    def from_dict(cls,d):
        return cls(d["nome"], d["cpf"], ["idade"])

    @property
    def nome(self):
        return self._nome
    #Verificação de nome, no caso se o campo estiver  em branco
    @nome.setter
    def nome(self, nome):
        if len(nome) > 0:
            self._nome = nome
        else:
            raise ValueError(f"{nome} é um nome inválido")

    @property
    def cpf(self):
        return self._cpf
    #Verificação do cpf com base nos caracteres que incluem ou não as pontuações como - ou .
    @cpf.setter
    def cpf(self, cpf):
        if len(cpf) >= 11 and len(cpf) <= 14:
            self._cpf= cpf
        else:
            raise ValueError(f"{cpf} não é um CPF válido")

    @property
    def idade(self):
        return self._idade

    #Verificação de idade do motorista, que deve se maior que 18 anos
    @idade.setter
    def idade(self, idade):
        idade = int(idade)
        if idade >= 18:
            self._idade = idade
        else:
            raise ValueError(f"{idade} é uma Idade é inválida ")