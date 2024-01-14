from contextos_de_negocio.alimentacao.entidades.alimento import Alimento


class AlimentoAgregado:
    @classmethod
    def criar_alimento(
        cls,
        nome: str,
        marca: str,
        descricao: str,
        calorias: float,
        carboidratos: float,
        proteinas: float,
        gorduras: float,
        unidade_de_medida: str,
        peso: float,
    ):
        return Alimento(
            nome=nome,
            marca=marca,
            descricao=descricao,
            calorias=calorias,
            carboidratos=carboidratos,
            proteinas=proteinas,
            gorduras=gorduras,
            unidade_de_medida=unidade_de_medida,
            peso=peso,
        )
