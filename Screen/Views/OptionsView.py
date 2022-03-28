from Config.Folder import Folder
from Screen.Components.Text import DifficultyText, Text
from typing import List
from pygame import Rect, Surface, event
from pygame import Rect, Surface
from Config.TelaJogo import TelaJogo
from Utils.Folder import import_single_sprite
from Config.Enums import States
from Screen.Components.Buttons import Button, ButtonDificil, ButtonFacil, ButtonMedio, MenuButton, MusicButton
from Screen.Views.AbstractView import AbstractView


class OptionsView(AbstractView):
    __STATE = States.MENU
    folder = Folder()
    __IMAGE_PATH = folder.create_assets_path(['Telas'], '3.1.jpg')
    __IMAGE_LOADED = False
    __IMAGE: Surface = None

    def __init__(self) -> None:
        super().__init__(OptionsView.__STATE)

        if not OptionsView.__IMAGE_LOADED:
            OptionsView.__IMAGE = import_single_sprite(OptionsView.__IMAGE_PATH, self._views_size)
            OptionsView.__IMAGE_LOADED = True

        self.__image = OptionsView.__IMAGE
        self.__rect = self.__image.get_rect(topleft=self._position)

        self.__BTN_POS = [
            (self._views_size[0]*4/10, self._views_size[1]/2 - 100),
            (self._views_size[0]*4/10, self._views_size[1]/2 - 25),
            (self._views_size[0]*4/10, self._views_size[1]/2 + 50),
            (self._views_size[0]*6/10, self._views_size[1]/2 + 25),
            (self._views_size[0]*6/10, self._views_size[1]/2 - 90)
        ]

        self.__buttons: List[Button] = [
            ButtonFacil('Easy', self.__BTN_POS[0], States.SAME),
            ButtonMedio('Normal', self.__BTN_POS[1], States.SAME),
            ButtonDificil('Hard', self.__BTN_POS[2], States.SAME),
            MenuButton('Return', self.__BTN_POS[3], States.MENU),
            MusicButton(self.__BTN_POS[4], States.SAME)]

        self.__TEXT_POS = [
            (self._views_size[0]/2, 100),
            (self._views_size[0]*4/10, self._views_size[1]/2 - 150)
        ]
        self.__texts: List[Text] = [
            Text(self.__TEXT_POS[0], 60, 'Options'),
            DifficultyText(self.__TEXT_POS[1], 30)
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
        for text in self.__texts:
            text.desenhar(tela)

    def run(self, events: List[event.Event]) -> States:
        for button in self.__buttons:
            button.hover()
            button.run(events)
            state = button.get_state()

            if state != States.SAME:
                return state
        return States.SAME
