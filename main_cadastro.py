import json
from pathlib import Path
from .moto import moto
from .carro import carro
from .caminhao import caminhao
from .pessoa import Pessoa
from .motorista import Motorista

PASTA_DADOS = Path(__file__).parent.parent / "Data"

#Sessão que adiciona, faz a busca, carrega e salva os veiculos no veiculos.json com formato de dicionario
veiculos = {}

CLASSES_VEICULO = {"MOTO": moto, "CARRO": carro, "CAMINHAO": caminhao}
ARQUIVO_VEICULOS = PASTA_DADOS / "veiculos.json"

#Escolhe o veiculo com base na placa (Atributo que torna ele único)
def adicionar_veiculo(veiculo):
    veiculos[veiculo.placa] = veiculo

def buscar_veiculo(placa):
    return(veiculos.get(placa.strip().upper()))

def salvar_veiculos():
    with ARQUIVO_VEICULOS.open("w", encoding="utf-8") as f:
        json.dump(
        {placa: v.to_dict() for placa, v in veiculos.items()},
            f, ensure_ascii=False, indent=4,
            )

def carregar_veiculos():
    veiculos.clear()
    if not ARQUIVO_VEICULOS.exists(): 
        return
    with ARQUIVO_VEICULOS.open(encoding="utf-8") as f:
        conteudo = f.read().strip()
        if not conteudo:
            return 
        dados = json.loads(conteudo)
    for placa, d in dados.items():
        classe = CLASSES_VEICULO[d["tipo"].upper()]
        veiculos[placa] = classe.from_dict(d)

#Sessão que adiciona,busca e salva motoristas em formato de dicionario no Motoristas.json
Motoristas = {}

ARQUIVO_MOTORISTAS = PASTA_DADOS / "Motoristas.json"
#Adiciona o Motorista com base no numero da CPF (Tornar ele único)
def adicionar_motorista(motorista):
    Motoristas[motorista.cpf] = motorista

def buscar_motorista(cpf):
    return Motoristas.get(cpf)

def salvar_motoristas():
    with ARQUIVO_MOTORISTAS.open("w", encoding="utf-8") as f:
        json.dump(
            {cpf: m.to_dict() for cpf, m in Motoristas.items()},
            f, ensure_ascii=False, indent=4
        )

def carregar_motoristas():
    Motoristas.clear()

    if not ARQUIVO_MOTORISTAS.exists():
        return
    with ARQUIVO_MOTORISTAS.open(encoding="utf-8") as f:
        conteudo = f.read().strip()
    if not conteudo:
        return
    dados = json.loads(conteudo)
    for cpf, d in dados.items():
        Motoristas[cpf] = Motorista.from_dict(d)

viagens = []

ARQUIVO_VIAGENS = PASTA_DADOS / "Relatorios.json"

def adicionar_viagem(viagem):
    viagens.append(viagem)

def carregar_historico_viagens():
    if not ARQUIVO_VIAGENS.exists():
        return {}
    conteudo = ARQUIVO_VIAGENS.read_text(encoding="utf-8").strip()
    if not conteudo:
        return {}
    dados = json.loads(conteudo)
    if isinstance(dados, list):
        return {}
    return dados

def salvar_viagens():
    historico = carregar_historico_viagens()
    proximo = len(historico) + 1
    for v in viagens:
        v.id = f"V{proximo:04d}"
        historico[v.id] = v.to_dict()
        proximo += 1
    with ARQUIVO_VIAGENS.open("w", encoding="utf-8") as f:
        json.dump(historico, f, ensure_ascii=False, indent=4)
    viagens.clear()