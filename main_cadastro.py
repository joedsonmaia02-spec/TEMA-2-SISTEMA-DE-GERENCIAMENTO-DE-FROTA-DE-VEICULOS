import json
from pathlib import Path
from moto import moto
from carro import carro
from caminhao import caminhao
from pessoa import Pessoa
from motorista import Motorista

veiculos = {}

CLASSES_VEICULO = {"moto": moto, "carro": carro, "caminhao": caminhao}
ARQUIVO_VEICULOS = Path("veiculos.json")


def adicionar_veiculo(veiculo):
    veiculos[veiculo.placa] = veiculo


def buscar_veiculo(placa):
    return(veiculos.get(placa))


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
        dados = json.load(f)
    for placa, d in dados.items():
        classe = CLASSES_VEICULO[d["tipo"]]
        veiculos[placa] = classe.from_dict(d)


Motoristas = {}

arquivo_Motorista = Path("Motoristas.json")

def adicionar_motorista(motorista):
    Motoristas[motorista.cpf] = motorista

def buscar_motorista(cpf):
    return Motoristas.get(cpf)

def salvar_motoristas():
    with arquivo_Motorista.open("w", encoding="utf-8") as f:
        json.dump(
            {cpf: m.to_dict() for cpf, m in Motoristas.items()},
            f, ensure_ascii=False, indent=4
        )


def carregar_motoristas():
    Motoristas.clear()

    if not arquivo_Motorista.exists():
        return
    with arquivo_Motorista.open(encoding="utf-8") as f:
        conteudo = f.read().strip()
    if not conteudo:
        return
    dados = json.loads(conteudo)
    for cpf, d in dados.items():
        Motoristas[cpf] = Motorista.from_dict(d)