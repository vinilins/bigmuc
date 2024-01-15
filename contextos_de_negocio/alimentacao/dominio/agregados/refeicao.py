from dataclasses import dataclass
from typing import List, Optional

from contextos_de_negocio.alimentacao.dominio.entidades import Refeicao, Alimento
from contextos_de_negocio.alimentacao.dominio.objetos_de_valor import (
    NomeRefeicao,
    Macronutriente,
)


@dataclass
class RefeicaoAgregado:
    refeicao: Refeicao

    @classmethod
    def criar_refeicao(cls, nome: NomeRefeicao, alimentos: Optional[List[Alimento]]):
        alimentos = [alimento for alimento in alimentos]
        refeicao = Refeicao(nome=nome, alimentos=alimentos)

        return cls(refeicao=refeicao)

    def adicionar_alimento(self, alimento: Alimento):
        self.refeicao.alimentos.append(alimento)

    def remover_alimento(self, alimento: Alimento):
        self.refeicao.alimentos.remove(alimento)

    def obter_macronutrientes(self):
        return {
            "calorias": self._obter_calorias(),
            "carboidratos": self._obter_carboidratos(),
            "proteinas": self._obter_proteinas(),
            "gorduras": self._obter_gorduras(),
        }

    def calcular_macronutrientes(self):
        return {
            "calorias": self._calcular_calorias(),
            "carboidratos": self._obter_carboidratos(),
            "proteinas": self._obter_proteinas(),
            "gorduras": self._obter_gorduras(),
        }

    def __soma_macro(self, macro: Macronutriente):
        macronutriente = macro.value
        soma_macro = sum(
            [getattr(alimento, macronutriente) for alimento in self.refeicao.alimentos]
        )
        return round(soma_macro, 2)

    def _calcular_calorias(self):
        return (
            self._obter_carboidratos() * 4
            + self._obter_proteinas() * 4
            + self._obter_gorduras() * 9
        )

    def _obter_calorias(self):
        return self.__soma_macro(Macronutriente.CALORIA)

    def _obter_carboidratos(self):
        return self.__soma_macro(Macronutriente.CARBOIDRATO)

    def _obter_proteinas(self):
        return self.__soma_macro(Macronutriente.PROTEINA)

    def _obter_gorduras(self):
        return self.__soma_macro(Macronutriente.GORDURA)

    def __eq__(self, other):
        return self.refeicao.nome == other.refeicao.nome and all(
            alimento in other.refeicao.alimentos for alimento in self.refeicao.alimentos
        )
