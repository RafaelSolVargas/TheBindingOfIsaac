from typing import List
from pygame import Rect, Surface, event
from Config.Folder import Folder
from Config.TelaJogo import TelaJogo
from Utils.Folder import import_single_sprite
from Config.Enums import States
from Screen.Views.AbstractView import AbstractView


class StaticView(AbstractView):
    __STATE = States.STATIC
    folder = Folder()
    __IMAGE_PATH = folder.create_assets_path(['Telas'], '3.1.jpg')
    __IMAGE_LOADED = False
    __IMAGE: Surface = None

    def __init__(self) -> None:
        super().__init__(StaticView.__STATE)

        if not StaticView.__IMAGE_LOADED:
            StaticView.__IMAGE = import_single_sprite(StaticView.__IMAGE_PATH, self._views_size)
            StaticView.__IMAGE_LOADED = True

        self.__image = StaticView.__IMAGE
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
