from dataclasses import dataclass

from contextos_de_negocio.alimentacao.dominio.entidades.alimento import Alimento
from contextos_de_negocio.alimentacao.dominio.objetos_de_valor import (
    Caloria,
    Carboidrato,
    Proteina,
    Gordura,
)


@dataclass
class AlimentoAgregado:
    alimento: Alimento

    @classmethod
    def criar_alimento(
        cls,
        nome: str,
        marca: str,
        descricao: str,
        caloria: float,
        carboidrato: float,
        proteina: float,
        gordura: float,
        unidade_de_medida: str,
        peso: float,
    ):
        alimento = Alimento(
            nome=nome,
            marca=marca,
            descricao=descricao,
            caloria=Caloria(caloria),
            carboidrato=Carboidrato(carboidrato),
            proteina=Proteina(proteina),
            gordura=Gordura(gordura),
            unidade_de_medida=unidade_de_medida,
            peso=peso,
        )

        return cls(alimento=alimento)

    @property
    def macronutrientes(self):
        return {
            "caloria": self.alimento.caloria,
            "carboidrato": self.alimento.carboidrato,
            "proteina": self.alimento.proteina,
            "gordura": self.alimento.gordura,
        }

    @property
    def calcular_caloria(self):
        return (
            self.alimento.carboidrato * 4
            + self.alimento.proteina * 4
            + self.alimento.gordura * 9
        )
