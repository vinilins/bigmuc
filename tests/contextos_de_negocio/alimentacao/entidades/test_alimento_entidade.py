from contextos_de_negocio.alimentacao.entidades.alimento import Alimento


def test_criar_alimento():
    arroz = Alimento(
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

    assert isinstance(arroz, Alimento)
    assert arroz.nome == "Arroz"
    assert arroz.marca == "Tio João"
    assert arroz.descricao == "Arroz branco"
    assert arroz.calorias == 121.7
    assert arroz.carboidratos == 25.2
    assert arroz.proteinas == 2.5
    assert arroz.gorduras == 0.3
    assert arroz.unidade_de_medida == "g"
    assert arroz.peso == 100
