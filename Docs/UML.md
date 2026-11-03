```mermaid
classDiagram
    class Veiculo {
        -placa: str
        -marca: str
        -modelo: str
        -tipo: str
        -ano: int
        -km: float
        -consumo_medio: float
        -status: StatusVeiculo
        +calcular_consumo() float
        +abastecer(abastecimento) void
        +registrar_manutencao(manutencao) void
        +concluir_manutencao() void
        +__str__() str
        +__eq__(outro) bool
        +__lt__(outro) bool
        +__iter__() Iterator
    }

    class Carro {
        -num_portas: int
        +calcular_consumo() float
    }

    class Moto {
        -cilindrada: int
        +calcular_consumo() float
    }

    class Caminhao {
        -capacidade_carga: float
        +calcular_consumo() float
    }

    class Pessoa {
        -nome: str
        -cpf: str
        - idade: str
    }

    class Motorista {
        -categoria_cnh: CategoriaCNH
        -disponivel: bool
        +ocupado: bool
    }

    class Viagem {
        -motorista: Motorista
        -veiculo: Veiculo
        -associar_motorista_veiculo
        -origem: str
        -destino: str
        -distancia: float
        -data_saida: date
        -data_entrada: date
        +iniciar(data_saida) void
        +finalizar(data_entrada) void
        +duracao() timedelta
    }

    class Manutencao {
        -veiculo: Veiculo
        -data: date
        -tipo: TipoManutencao
        -descricao: str
        -custo: float
    }

    class Abastecimento {
        -veiculo: Veiculo
        -data: date
        -tipo_combustivel: TipoCombustivel
        -litros: float
        -valor_litro: float
    }

    class JsonRepository

    Veiculo <|-- Carro
    Veiculo <|-- Moto
    Veiculo <|-- Caminhao
    Pessoa <|-- Motorista

    RepositorioBase <|.. JsonRepository

    Viagem --> Motorista : motorista designado
    Viagem --> Veiculo : veiculo designado
    Manutencao --> Veiculo
    Manutencao ..> EstrategiaCustoManutencao : usa
    Abastecimento --> Veiculo
    Veiculo --> StatusVeiculo
```
