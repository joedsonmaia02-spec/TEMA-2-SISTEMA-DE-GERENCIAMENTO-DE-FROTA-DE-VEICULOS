from .veiculo import Veiculo
#Classe carro, vai tribuir as caracteristas em comuns e principais dos carros, com o diferencial que é o quantidade de portas
class carro(Veiculo):
    def __init__(self, placa, marca, modelo, ano, km_rodados, consumo_medio, tipo_combustivel, tamanho_tanque_combustivel, status, qnt_portas, km_ultima_revisao):
        super().__init__( placa, marca, modelo, "CARRO", ano, km_rodados, consumo_medio, tipo_combustivel, tamanho_tanque_combustivel, status, km_ultima_revisao)
        self.qnt_portas = qnt_portas
    
    def __str__(self):
        return super().__str__() + f"\nQuantidade de Portas: {self.qnt_portas}"


    def to_dict(self):
        d = super().to_dict()
        d["qnt_portas"] = self.qnt_portas
        return d
    #Transformar de string para dicionario as caracteristicas dos carros, 
    # além de chamar a função carregar consumo que tem os principais atributos do abastecimento
    @classmethod
    def from_dict(cls, d):
        c = cls(d["placa"], d["marca"], d["modelo"], d["ano"], d["km_rodados"],
                d["consumo_medio"], d["tipo_combustivel"],d["tamanho_tanque_combustivel"], d["status"], d["qnt_portas"], d.get("km_ultima_revisao", 0))
        c.carregar_consumo(d)
        return c

    @property
    def qtd_portas(self):
        return self._qtd_portas
    #verificação da quantidade de portas do carro
    @qtd_portas.setter
    def qtd_portas(self, qtd_portas):
        if qtd_portas < 2 or qtd_portas > 4:
            raise ValueError(f"{qtd_portas} não é uma quantidade de portas válida")
        self._qtd_portas = qtd_portas



