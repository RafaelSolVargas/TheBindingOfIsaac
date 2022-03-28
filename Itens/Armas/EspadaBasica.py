from Itens.Armas.AbstractArma import AbstractArma


class EspadaBasica(AbstractArma):
    __DANO = 3
    __ALCANCE = 18

    def __init__(self) -> None:
        self.__dano = EspadaBasica.__DANO
        self.__alcance = EspadaBasica.__ALCANCE

    @property
    def dano(self) -> int:
        return self.__dano

    @property
    def alcance(self) -> int:
        return self.__alcance
