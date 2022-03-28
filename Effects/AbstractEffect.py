from abc import ABC, abstractmethod


class AbstractEffect(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def has_ended(self) -> bool:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @property
    @abstractmethod
    def rect(self) -> None:
        pass

    @property
    @abstractmethod
    def image(self) -> None:
        pass
