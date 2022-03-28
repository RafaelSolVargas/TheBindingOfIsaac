from typing import List
from pygame import event
from Config.TelaJogo import TelaJogo
from Personagens.Jogador import Jogador
from Config.Opcoes import Opcoes
from Fases.ControladorFases import ControladorFases
from Fases.AbstractFase import AbstractFase
from Sounds.MusicHandler import MusicHandler


class Jogo:
    def __init__(self, save_name: str):
        self.__save_name = save_name
        self.__music = MusicHandler()
        self.__opcoes = Opcoes()
        self.__carregar_dados()
        self.__PLAYER_WON = False

    @property
    def save_name(self) -> str:
        return self.__save_name

    @save_name.setter
    def save_name(self, value: str) -> None:
        self.__save_name = value

    def player_has_lost(self) -> bool:
        return self.__fase_atual.player_has_lost()

    def player_has_won(self) -> bool:
        return self.__PLAYER_WON

    def run(self, events: List[event.Event]) -> None:
        self.__music.update()
        self.__fase_atual.run()

        if self.__fase_atual.player_has_won():
            proxima_fase = self.__controlador.proxima_fase()
            if proxima_fase != None:
                self.__fase_atual = proxima_fase
                self.__fase_atual.start()
            else:
                self.__PLAYER_WON = True

    def desenhar(self, tela: TelaJogo) -> None:
        self.__fase_atual.desenhar(tela)

    def __carregar_dados(self) -> None:
        self.__jogador = Jogador((0, 0), self.__opcoes.nome)
        self.__controlador = ControladorFases(self.__jogador)
        self.__fase_atual: AbstractFase = self.__controlador.proxima_fase()
        self.__fase_atual.start()

    @property
    def controlador(self) -> ControladorFases:
        return self.__controlador

    @controlador.setter
    def controlador(self, controlador: ControladorFases) -> None:
        self.__controlador = controlador
        self.__fase_atual = controlador.current_fase
