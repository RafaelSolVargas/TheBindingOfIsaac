from Objetos.AbstractObjeto import AbstractObjeto
from Config.TelaJogo import TelaJogo


class ObjetoInvisivel(AbstractObjeto):
    def __init__(self, posicao: tuple, tamanho: tuple, transpassavel: bool, bloqueia_visao: bool) -> None:
        super().__init__(posicao, tamanho, transpassavel, bloqueia_visao)

    def desenhar(self, tela: TelaJogo) -> None:
        return
