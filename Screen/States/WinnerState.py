from random import randint
from typing import List
from Config.Folder import Folder
from Jogo.ControllerJogo import ControllerJogo
from Screen.States.AbstractState import AbstractState
from Screen.Views.PlayingView import PlayingView
from Config.Enums import States
from Config.TelaJogo import TelaJogo
from pygame.event import Event
from Jogo.Jogo import Jogo
from Screen.Views.WinnerView import WinnerView
from Sounds.MusicHandler import MusicHandler


class WinnerState(AbstractState):
    __STATE = States.WINNER
    folder = Folder()
    path = folder.create_sounds_path(['musics', 'win'])
    __MUSIC_PATH_BASE = path + 'win_music_{}.mp3'

    def __init__(self) -> None:
        view = PlayingView()
        self.__winner_view = WinnerView()
        self.__jogoOptions = ControllerJogo()
        self.__music = MusicHandler()
        self.__RUNNING = False
        super().__init__(view, WinnerState.__STATE)

    def run(self, events: List[Event]) -> States:
        if not self.__RUNNING:
            self.__RUNNING = True
            music = self.__get_random_winner_music()
            self.__music.play_music_once(music)
            self.__jogo: Jogo = self.__jogoOptions.current_game()

        next_state = self.__winner_view.run(events)
        return next_state

    def desenhar(self, tela: TelaJogo) -> None:
        if not self.__RUNNING:
            self.__RUNNING = True
            music = self.__get_random_winner_music()
            self.__music.play_music_once(music)
            self.__jogo: Jogo = self.__jogoOptions.current_game()

        self.view.desenhar(tela)
        self.__jogo.desenhar(tela)
        self.__winner_view.desenhar(tela)

    def __get_random_winner_music(self) -> str:
        end = randint(1, 2)
        return WinnerState.__MUSIC_PATH_BASE.format(end)
