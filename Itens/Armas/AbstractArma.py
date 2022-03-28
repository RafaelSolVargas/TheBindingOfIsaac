from abc import ABC, abstractmethod


class AbstractArma(ABC):
    def __init__(self) -> None:
        pass

    @property
    @abstractmethod
    def dano(self) -> int:
        return self.__dano

    @property
    @abstractmethod
    def alcance(self) -> int:
        return self.__alcance
