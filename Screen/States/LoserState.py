from typing import List
from random import choice, randint
from Config.Folder import Folder
from Jogo.ControllerJogo import ControllerJogo
from Screen.States.AbstractState import AbstractState
from Screen.Views.LoserView import LoserView
from Screen.Views.PlayingView import PlayingView
from Config.Enums import States
from Config.TelaJogo import TelaJogo
from pygame.event import Event
from Jogo.Jogo import Jogo
from Sounds.MusicHandler import MusicHandler


class LoserState(AbstractState):
    __STATE = States.LOSER
    folder = Folder()
    path = folder.create_sounds_path(['musics', 'lose'])
    __MUSIC_PATH_BASE = path + 'lose_music_{}.mp3'

    def __init__(self) -> None:
        view = PlayingView()
        self.__loser_view = LoserView()
        self.__jogoOptions = ControllerJogo()
        self.__music = MusicHandler()
        self.__RUNNING = False
        super().__init__(view, LoserState.__STATE)

    def run(self, events: List[Event]) -> States:
        if not self.__RUNNING:
            self.__RUNNING = True
            music = self.__get_random_loser_music()
            self.__music.play_music_once(music)
            self.__jogo: Jogo = self.__jogoOptions.current_game()

        next_state = self.__loser_view.run(events)
        return next_state

    def desenhar(self, tela: TelaJogo) -> None:
        if not self.__RUNNING:
            self.__RUNNING = True
            music = self.__get_random_loser_music()
            self.__music.play_music_once(music)
            self.__jogo: Jogo = self.__jogoOptions.current_game()

        self.view.desenhar(tela)
        self.__jogo.desenhar(tela)
        self.__loser_view.desenhar(tela)

    def __get_random_loser_music(self) -> str:
        end = randint(1, 10)
        return LoserState.__MUSIC_PATH_BASE.format(end)
