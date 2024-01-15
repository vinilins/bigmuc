from dataclasses import dataclass
from typing import List

from contextos_de_negocio.alimentacao.dominio.entidades import Alimento
from contextos_de_negocio.alimentacao.dominio.objetos_de_valor import NomeRefeicao


@dataclass
class Refeicao:
    nome: NomeRefeicao
    alimentos: List[Alimento]
