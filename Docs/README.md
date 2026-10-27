# TEMA-2-SISTEMA-DE-GERENCIAMENTO-DE-FROTA-DE-VEICULOS

## - Descrição do Projeto

O Sistema de Gerenciamento de frota de veículos, permite o controle sobre os elementos participantes do frete, com informações sobre a situação do veículo, o motorista designado e a situação atual da viagem. Contém um registro com informações dos veículos que a empresa possui, além do monitoramento da chegada e saída, status ao longo do trajeto (manutenção, abastecimento) e gera estatísticas de desempenho.


## - Objetivo

O sistema tem como objetivo ser uma ferramenta de controle para gerenciar frotas de veículos de empresas de transporte, otimizando o acesso a informações sobre as condições em que se encontram os veículos e viabilizando um controle preciso sobre a frota, reduzindo custos operacionais e tempo de resposta. 

# - Estrutura Planejada de Classes

```

frota/
├── main.py
│
├── src/
│   ├── __init__.py
│   ├── pessoa.py
│   ├── motorista.py
│   ├── veiculo.py
│   ├── carro.py
│   ├── moto.py
│   ├── caminhao.py
│   ├── viagem.py
│   ├── manutencao.py
|   ├── relatorios.py
│   └── abastecimento.py
|
│
├── data/
│   ├── veiculos.json
│   └── motoristas.json
│
├── repositories/
│   ├── __init__.py
│   ├── base.py
│   └── json_repository.py
│
├── services/
│   └── relatorios.json
│
├── docs/
├── .gitignore
└── readme


settings.json

```
