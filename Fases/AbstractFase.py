from abc import ABC, abstractmethod
from typing import List
from Personagens.Jogador import Jogador
from Config.TelaJogo import TelaJogo
from Mapas.AbstractMapa import AbstractMapa
from Personagens.HUD import HUD
from Sounds.MusicHandler import MusicHandler


class AbstractFase(ABC):
    def __init__(self, jogador: Jogador) -> None:
        self.__jogador: Jogador = jogador
        self.__hud = HUD(self.__jogador.status, self.__jogador.escudo, self.__jogador.arma)
        self.__music = MusicHandler()

        self.__PLAYER_WON = False
        self.__MAX_DELAY_CHANGE_MAP = 100
        self.__CURRENT_DELAY_CHANGE_MAP = 0

    def _set_maps_lists(self, mapas: List[AbstractMapa]) -> None:
        self.__maps_list: List[AbstractMapa] = mapas
        self.__current_map: AbstractMapa = self.__maps_list[0]
        self.__current_map_index = 0
        self.__current_map.load()

    @property
    def mapas(self) -> List[AbstractMapa]:
        return self.__maps_list

    @mapas.setter
    def mapas(self, mapas: List[AbstractMapa]) -> None:
        self.__maps_list = mapas
        self.__current_map = self.__maps_list[self.__current_map_index]
        self.__current_map.load()

    @property
    def current_map_index(self) -> int:
        return self.__current_map_index

    @current_map_index.setter
    def current_map_index(self, map_index) -> None:
        self.__current_map_index = map_index
        self.__current_map = self.__maps_list[self.__current_map_index]
        self.__current_map.load()

    def run(self) -> None:
        self.__update()
        self.__current_map.animate()
        self.__jogador.processar_inputs()
        self.__current_map.mover_inimigos()
        self.__current_map.lidar_ataques()
        self.__current_map.update()

    def player_has_won(self) -> bool:
        return self.__PLAYER_WON

    def player_has_lost(self) -> bool:
        if self.__jogador.morreu:
            return True
        else:
            return False

    def start(self):
        self.__jogador.mapa = self.__current_map
        self.__music.play_music(self.__current_map.background_music_path)

    def desenhar(self, tela: TelaJogo) -> None:
        self.__current_map.desenhar(tela)
        self.__hud.desenhar(tela)

    def __update(self):
        if self.__CURRENT_DELAY_CHANGE_MAP > 0:
            self.__CURRENT_DELAY_CHANGE_MAP -= 1

        if self.__current_map.go_next_map:
            if self.__current_map_index == len(self.__maps_list) - 1:
                self.__PLAYER_WON = True
            elif self.__CURRENT_DELAY_CHANGE_MAP == 0:
                self.__set_next_map()

        if self.__current_map.go_previous_map:
            if self.__current_map_index != 0 and self.__CURRENT_DELAY_CHANGE_MAP == 0:
                self.__set_previous_map()

    def __set_previous_map(self):
        previous_map = self.__maps_list[self.__current_map_index - 1]
        self.__current_map = previous_map
        self.__current_map_index -= 1
        self.__current_map.change_player_position_returning_map()
        self.__jogador.mapa = self.__current_map
        self.__CURRENT_DELAY_CHANGE_MAP = self.__MAX_DELAY_CHANGE_MAP
        self.__music.play_music(self.__current_map.background_music_path)

    def __set_next_map(self):
        next_map = self.__maps_list[self.__current_map_index + 1]
        self.__current_map = next_map
        self.__current_map_index += 1
        self.__current_map.load()
        self.__current_map.change_player_position_entering_map()
        self.__jogador.mapa = self.__current_map
        self.__CURRENT_DELAY_CHANGE_MAP = self.__MAX_DELAY_CHANGE_MAP
        self.__music.play_music(self.__current_map.background_music_path)

    @property
    def jogador(self) -> Jogador:
        return self.__jogador

    @jogador.setter
    def jogador(self, jogador: Jogador) -> None:
        if isinstance(jogador, Jogador):
            self.__jogador = jogador
            self.__hud = HUD(self.__jogador.status, self.__jogador.escudo, self.__jogador.arma)

    @property
    def current_map(self) -> AbstractMapa:
        return self.__current_map

    @property
    def _set_mapa(self, mapa: AbstractMapa) -> None:
        if isinstance(mapa, AbstractMapa):
            self.__current_map = mapa
