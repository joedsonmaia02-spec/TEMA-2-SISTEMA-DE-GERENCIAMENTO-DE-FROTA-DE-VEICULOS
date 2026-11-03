import json
from pathlib import Path

_CAMINHO = Path(__file__).parent.parent / "Data" / "settings.json"
#Responsável por ler o settings.py e deixar disponivel para as areas do projeto que possuem a utilização das regras de negocio
def carregar_settings():
    try:
        with open(_CAMINHO, encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Configurações não encontradas: {_CAMINHO}")

SETTINGS = carregar_settings()