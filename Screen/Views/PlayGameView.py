from Config.Folder import Folder
from Screen.Components.Text import Text
from typing import List
from pygame import Rect, Surface
from Config.TelaJogo import TelaJogo
from pygame import Rect, Surface, event
from Utils.Folder import import_single_sprite
from Config.Enums import States
from Screen.Components.Buttons import Button, MenuButton
from Screen.Views.AbstractView import AbstractView


class PlayGameView(AbstractView):
    __STATE = States.PLAY
    folder = Folder()
    __IMAGE_PATH = folder.create_assets_path(['Telas'], '3.1.jpg')
    __IMAGE_LOADED = False
    __IMAGE: Surface = None

    def __init__(self) -> None:
        super().__init__(PlayGameView.__STATE)

        if not PlayGameView.__IMAGE_LOADED:
            PlayGameView.__IMAGE = import_single_sprite(PlayGameView.__IMAGE_PATH, self._views_size)
            PlayGameView.__IMAGE_LOADED = True

        self.__image = PlayGameView.__IMAGE
        self.__rect = self.__image.get_rect(topleft=self._position)

        self.__BTN_POS = [
            (self._views_size[0]/2, self._views_size[1]/2 - 100),
            (self._views_size[0]/2, self._views_size[1]/2 - 25),
            (self._views_size[0]/2, self._views_size[1]/2 + 50)]
        self.__buttons: List[Button] = [
            MenuButton('NEW', self.__BTN_POS[0], States.NEW),
            MenuButton('LOAD', self.__BTN_POS[1], States.LOAD),
            MenuButton('RETURN', self.__BTN_POS[2], States.MENU)]

        self.__TEXT_POS = [
            (self._views_size[0]/2, 100)]
        self.__texts: List[Text] = [
            Text(self.__TEXT_POS[0], 60, 'The Binding Of Isaac')]

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
