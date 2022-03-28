from abc import ABC, abstractmethod
from Config.TelaJogo import TelaJogo
from Utils.Hitbox import Hitbox


class AbstractObjeto(ABC):
    def __init__(self, posicao: tuple, tamanho: tuple, transpassavel=False, bloqueia_visao=True) -> None:
        self.__transpassavel = transpassavel
        self.__bloqueia_visao = bloqueia_visao
        self.__hitbox = Hitbox(posicao=posicao, tamanho=tamanho)

    @property
    def transpassavel(self) -> bool:
        return self.__transpassavel

    @transpassavel.setter
    def transpassavel(self, value):
        if type(value) == bool:
            self.__transpassavel = value

    @property
    def bloqueia_visao(self) -> bool:
        return self.__bloqueia_visao

    @bloqueia_visao.setter
    def bloqueia_visao(self, value):
        if type(value) == bool:
            self.__bloqueia_visao = value

    @property
    def hitbox(self) -> Hitbox:
        return self.__hitbox

    @abstractmethod
    def desenhar(self, tela: TelaJogo) -> None:
        pass
