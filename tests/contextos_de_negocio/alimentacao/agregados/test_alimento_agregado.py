from contextos_de_negocio.alimentacao.agregados.alimento import AlimentoAgregado
from contextos_de_negocio.alimentacao.entidades.alimento import Alimento


def test_cadastrar_alimento():
    assert AlimentoAgregado.criar_alimento(
        nome="Arroz",
        marca="Tio João",
        descricao="Arroz branco",
        calorias=121.7,
        carboidratos=25.2,
        proteinas=2.5,
        gorduras=0.3,
        unidade_de_medida="g",
        peso=100,
    ) == Alimento(
        nome="Arroz",
        marca="Tio João",
        descricao="Arroz branco",
        calorias=121.7,
        carboidratos=25.2,
        proteinas=2.5,
        gorduras=0.3,
        unidade_de_medida="g",
        peso=100,
    )
