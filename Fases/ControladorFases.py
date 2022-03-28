from typing import List
from Fases.DungeonFase import DungeonFase
from Personagens.Jogador import Jogador
from Fases.AbstractFase import AbstractFase


class ControladorFases():
    def __init__(self, jogador: Jogador) -> None:
        self.__fases = []
        self.__fases.append(DungeonFase(jogador))
        self.__current_fase: AbstractFase = None

    @property
    def fases(self) -> List[AbstractFase]:
        return self.__fases

    def set_fases(self, fases: List[AbstractFase]) -> None:
        self.__fases = fases

    @property
    def current_fase(self) -> AbstractFase:
        return self.__current_fase

    @current_fase.setter
    def current_fase(self, fase: AbstractFase) -> None:
        if isinstance(fase, AbstractFase):
            self.__current_fase = fase

    def proxima_fase(self) -> AbstractFase:
        if len(self.__fases) > 0:
            self.__current_fase = self.__fases.pop(0)
            return self.__current_fase
        else:
            return None
