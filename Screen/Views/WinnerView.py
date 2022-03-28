from Config.Folder import Folder
from Screen.Components.Buttons import MenuButton, Button
from Screen.Components.Text import Text
from typing import List
from pygame import Rect, Surface, event
from Config.TelaJogo import TelaJogo
from Utils.Folder import import_single_sprite
from Config.Enums import States
from Screen.Views.AbstractView import AbstractView


class WinnerView(AbstractView):
    __STATE = States.WINNER
    folder = Folder()
    __IMAGE_PATH = folder.create_assets_path(['Telas'], 'FundoPause.jfif')
    __IMAGE_LOADED = False
    __IMAGE: Surface = None
    __POS = (575, 375)
    __SIZE = (550, 450)

    def __init__(self) -> None:
        rect = Rect(WinnerView.__POS, WinnerView.__SIZE)
        rect.center = rect.topleft
        position = rect.topleft

        super().__init__(WinnerView.__STATE, position, WinnerView.__SIZE)

        if not WinnerView.__IMAGE_LOADED:
            WinnerView.__IMAGE = import_single_sprite(WinnerView.__IMAGE_PATH, self._views_size)
            WinnerView.__IMAGE_LOADED = True

        self.__image = WinnerView.__IMAGE
        self.__rect = self.__image.get_rect(topleft=self._position)

        self.__texts: List[Text] = [
            Text((575, 350), 45, 'You Win :3')
        ]
        self.__buttons: List[Button] = [
            MenuButton('LEAVE', (575, 480), States.RESET),
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
            button.hover()
            button.desenhar(tela)
        for text in self.__texts:
            text.desenhar(tela)

    def run(self, events: List[event.Event]) -> States:
        for button in self.__buttons:
            button.run(events)

        leave_button = self.__buttons[0]
        if leave_button.clicked:
            return leave_button.next_state
        else:
            return States.SAME
