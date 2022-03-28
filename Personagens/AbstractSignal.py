from abc import ABC, abstractmethod
from Personagens.AbstractPersonagem import AbstractPersonagem


class AbstractSignal(ABC):
    @property
    @abstractmethod
    def signal_range(self) -> int:
        pass

    @property
    @abstractmethod
    def source_position(self) -> tuple:
        pass

    @property
    @abstractmethod
    def sender(self) -> AbstractPersonagem:
        pass