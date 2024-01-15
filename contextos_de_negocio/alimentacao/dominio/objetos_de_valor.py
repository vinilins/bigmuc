from dataclasses import dataclass
from enum import StrEnum


class Macronutriente(StrEnum):
    CALORIA = "caloria"
    CARBOIDRATO = "carboidrato"
    PROTEINA = "proteina"
    GORDURA = "gordura"


class NomeRefeicao(StrEnum):
    CAFE_DA_MANHA = "Café da manhã"
    LANCHE_DA_MANHA = "Lanche da manhã"
    ALMOCO = "Almoço"
    LANCHE_DA_TARDE = "Lanche da tarde"
    JANTAR = "Jantar"
    CEIA = "Ceia"


@dataclass
class FloatComUmaCasaDecimal(float):
    def __new__(cls, valor):
        return super().__new__(cls, round(valor, 1))


class Carboidrato(FloatComUmaCasaDecimal):
    pass


class Proteina(FloatComUmaCasaDecimal):
    pass


class Gordura(FloatComUmaCasaDecimal):
    pass


class Caloria(FloatComUmaCasaDecimal):
    pass


class Peso(FloatComUmaCasaDecimal):
    pass
