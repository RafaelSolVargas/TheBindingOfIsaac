from typing import List
from pygame import Rect, Surface, event
from Config.Folder import Folder
from Config.TelaJogo import TelaJogo
from Utils.Folder import import_single_sprite
from Config.Enums import States
from Screen.Views.AbstractView import AbstractView


class PlayingView(AbstractView):
    __STATE = States.PLAYING
    folder = Folder()
    __IMAGE_PATH = folder.create_assets_path(['Telas'], '3.1.jpg')
    __IMAGE_LOADED = False
    __IMAGE: Surface = None

    def __init__(self) -> None:
        super().__init__(PlayingView.__STATE)

        if not PlayingView.__IMAGE_LOADED:
            PlayingView.__IMAGE = import_single_sprite(PlayingView.__IMAGE_PATH, self._views_size)
            PlayingView.__IMAGE_LOADED = True

        self.__image = PlayingView.__IMAGE
        self.__rect = self.__image.get_rect(topleft=self._position)

    @property
    def image(self) -> Surface:
        return self.__image

    @property
    def rect(self) -> Rect:
        return self.__rect

    def desenhar(self, tela: TelaJogo) -> None:
        super().desenhar(tela)

    def run(self, events: List[event.Event]) -> States:
        return States.SAME
