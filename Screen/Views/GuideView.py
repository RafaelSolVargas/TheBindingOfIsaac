from typing import List
from pygame import Rect, Surface, event
from pygame import Rect, Surface
from Config.Folder import Folder
from Config.TelaJogo import TelaJogo
from Utils.Folder import import_single_sprite
from Config.Enums import States
from Screen.Components.Buttons import Button, MenuButton
from Screen.Views.AbstractView import AbstractView


class GuideView(AbstractView):
    __STATE = States.MENU
    folder = Folder()
    __IMAGE_PATH = folder.create_assets_path(['Telas'], 'Guide.png')
    __IMAGE_LOADED = False
    __IMAGE: Surface = None

    def __init__(self) -> None:
        super().__init__(GuideView.__STATE)

        if not GuideView.__IMAGE_LOADED:
            GuideView.__IMAGE = import_single_sprite(GuideView.__IMAGE_PATH, self._views_size)
            GuideView.__IMAGE_LOADED = True

        self.__image = GuideView.__IMAGE
        self.__rect = self.__image.get_rect(topleft=self._position)

        self.__BTN_POS = [
            (self._views_size[0]*19/100, self._views_size[1]*11/100),
        ]

        self.__buttons: List[Button] = [
            MenuButton('Return', self.__BTN_POS[0], States.MENU)
        ]

    @property
    def image(self) -> Surface:
        return self.__image

    @property
    def rect(self) -> Rect:
        return self.__rect

    def desenhar(self, tela: TelaJogo) -> None:
        super().desenhar(tela)
        for button in self.__buttons:
            button.desenhar(tela)

    def run(self, events: List[event.Event]) -> States:
        for button in self.__buttons:
            button.hover()
            button.run(events)
            state = button.get_state()

            if state != States.SAME:
                return state
        return States.SAME
