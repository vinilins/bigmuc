from dataclasses import dataclass


@dataclass
class Alimento:
    nome: str
    marca: str
    descricao: str
    calorias: float
    carboidratos: float
    proteinas: float
    gorduras: float
    unidade_de_medida: str
    peso: float
