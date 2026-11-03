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
├── testes/
|   └── teste.py│   
│   
│
├── services/
│   └── relatorios.json
│
├── docs/
├── .gitignore
└── readme


settings.json

```

## - Comandos do Sistema de Gerenciamento de frota:

#Criação do motorista
#m1 = motorista("Nome", Numero da Cnh, idade, CPF, tipo da CNH)
#Tipos de Carteiras de Motorista
#   #CARTEIRAS = {
#    #"A":  {"A"},
#    #"B":  {"B"},
#    #"C":  {"B", "C"},
#    #"AB": {"A", "B"},
#    #"AC": {"A", "B", "C"},
#    #"AD": {"A", "B", "C", "D"},
#    #"AE": {"A", "B", "C", "D", "E"},
# m1 = motorista("Ana", "11111111111", 30, "12345678901", "B")

# Comando para salvar o motorista
# adicionar_motorista(nome do motorista)
# adicionar_motorista(m1)

# Criação dos tipos de veiculo
# --Carro
# "c1" = carro("Placa", Marca, Modelo, Ano, kilometragem, tipodecombustivel, tamanhodotanque,"Status inicial = Disponivel", numdeportas, kmda ultima revisão)
# c1 = carro("ABC1D23", "BYD", "Uno", 2015, 30000, 12, "Gasolina", 50, "Disponivel", 4, 29000)

# --Moto
# "m1" = moto("Placa", Marca, Modelo, Ano, kilometragem, tipodecombustivel, tamanhodotanque, "Status inicial = Disponivel", cilindradas,km da ultima revisão)
# moto1 = moto("MOT1A23", "Honda", "CG 160", 2022, 12000, 40, "Gasolina", 14, "Disponivel", 160, 10500)

# --Caminhao
# "caminhao1" = caminhao("Placa", Marca, Modelo, Ano, kilometragem, tipodecombustivel, tamanhodotanque,"Status inicial = Disponivel", tipo de eixos, km da ultima revisão)
# cam1 = caminhao("CAM2B34", "Volvo", "FH 540", 2020, 250000, 3, "Diesel", 600, "Disponivel", 3, 245000)

# Comando para adicionar veiculo
# "Cadastrar veiculo adicionar_veiculo(Nomeveiculo)"
# adicionar_veiculo(c1)
# adicionar_veiculo(moto1)
# adicionar_veiculo(cam1)

# Salvar veiculos
# salvar_veiculos()

# Criar viagens
# v1 = Viagem(motorista designado, carro designado, local de partidda, local de chegada, quantidade de km, km inicial)
# v1 = Viagem(motorista1, carro1, "João Cabral", "São José", 500, 0)

# Comando para inciar viagem
# v1.iniciar_viagem()

# Comando para parar a viagem para abastecimento
# v1.parar_viagem("Abastecimento, litros = quantidade, valor_litro_combustivel = preço do litro")
# v1.parar_viagem("abastecimento", litros=20, valor_litro_combustivel=6.0)
# v1.retornar_viagem("abastecimento")

# Comando para parar viagem em caso de manuntenção
# v1.parar_viagem("manutencao, tipo_manuntencao = "Tipo da manuntenção")
# v1.parar_viagem("manutencao", tipo_manutencao="Troca de Pneu", valor_manutencao=700)
# v1.retornar_viagem("manutencao")

# Comando para concluir viagem
# v1.concluir_viagem(Informa os km_percorridos) 
# v1.concluir_viagem(480)                        

# Comando para ver os relatorios de viagens
# print(numero_da_viagem.relatorio())
# print(v1.relatorio())

# Comando para salvar e atualizar os status dos veiculos, motoristas e viagens
# salvar_veiculos()
# salvar_motoristas()
# salvar_viagens()
```
