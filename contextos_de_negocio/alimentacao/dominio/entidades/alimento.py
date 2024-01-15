from dataclasses import dataclass
from typing import Optional

from contextos_de_negocio.alimentacao.dominio.objetos_de_valor import (
    Caloria,
    Carboidrato,
    Proteina,
    Gordura,
)


@dataclass
class Alimento:
    nome: str
    caloria: Caloria
    carboidrato: Carboidrato
    proteina: Proteina
    gordura: Gordura
    unidade_de_medida: str
    peso: float
    descricao: Optional[str] = None
    marca: Optional[str] = None

    def __eq__(self, other):
        return (
            self.nome == other.nome
            and self.caloria == other.caloria
            and self.carboidrato == other.carboidrato
            and self.proteina == other.proteina
            and self.gordura == other.gordura
            and self.marca == other.marca
        )
