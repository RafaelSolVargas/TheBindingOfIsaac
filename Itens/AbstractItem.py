from abc import ABC, abstractmethod
from pygame import Rect, Surface
from Personagens.Status import Status


class AbstractItem(ABC):
    @abstractmethod
    def modificar_status(self, status: Status) -> None:
        pass

    @abstractmethod
    def check_aplicado(self) -> bool:
        pass

    @property
    @abstractmethod
    def image(self) -> Surface:
        pass

    @property
    @abstractmethod
    def rect(self) -> Rect:
        pass

    @property
    @abstractmethod
    def posicao(self) -> None:
        pass

    @property
    @abstractmethod
    def sound_path(self) -> str:
        pass
