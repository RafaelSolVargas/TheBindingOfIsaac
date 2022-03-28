from Config.Folder import Folder
from Screen.Components.Text import Text
from typing import List
from pygame import Rect, Surface, event
from pygame import Rect, Surface
from Config.TelaJogo import TelaJogo
from Utils.Folder import import_single_sprite
from Config.Enums import States
from Screen.Components.Buttons import Button, MenuButton, InputText
from Jogo.ControllerJogo import ControllerJogo
from Screen.Views.AbstractView import AbstractView


class NewGameView(AbstractView):
    __STATE = States.NEW
    folder = Folder()
    __IMAGE_PATH = folder.create_assets_path(['Telas'], '3.1.jpg')
    __IMAGE_LOADED = False
    __IMAGE: Surface = None

    def __init__(self) -> None:
        super().__init__(NewGameView.__STATE)
        self.__FORCE_RUN = False
        self.__NEXT_STATE = None
        self.__jogoOptions = ControllerJogo()

        if not NewGameView.__IMAGE_LOADED:
            NewGameView.__IMAGE = import_single_sprite(NewGameView.__IMAGE_PATH, self._views_size)
            NewGameView.__IMAGE_LOADED = True

        self.__image = NewGameView.__IMAGE
        self.__rect = self.__image.get_rect(topleft=self._position)

        self.__BTN_POS = [
            (self._views_size[0]/2, self._views_size[1]/2 - 25),
            (self._views_size[0]/2, self._views_size[1]/2 + 50),
            (self._views_size[0]*55/100, self._views_size[1]/2 - 100)]
        self.__buttons: List[Button] = [
            MenuButton('START', self.__BTN_POS[0], States.CREATE_NEW),
            MenuButton('RETURN', self.__BTN_POS[1], States.PLAY),
            InputText(self.__BTN_POS[2], 'Save1')
        ]

        self.__TEXT_POS = [
            (self._views_size[0]/2, 100),
            (self._views_size[0]*45/100, self._views_size[1]/2 - 100),
        ]
        self.__texts: List[Text] = [
            Text(self.__TEXT_POS[0], 60, 'New Game'),
            Text(self.__TEXT_POS[1], 25, 'Save Name:')]
        self.__temp_text: List[List[Text, int]] = []

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

        for index, [text, duration] in enumerate(self.__temp_text):
            if duration > 0:
                self.__temp_text[index][1] -= 1
                duration -= 1
                text.desenhar(tela)
            else:
                self.__temp_text.remove([text, duration])

    def run(self, events: List[event.Event]) -> States:
        for button in self.__buttons:
            button.run(events)

        start_button = self.__buttons[0]
        if start_button.clicked and not self.__FORCE_RUN:
            text = Text((575, 530), 35, 'Loading New Game...')
            self.__temp_text.append([text, 40])
            input_text = self.__buttons[2].text
            self.__jogoOptions.new_game_name = input_text
            self.__FORCE_RUN = True
            self.__NEXT_STATE = start_button.next_state
            return States.SAME

        for button in self.__buttons:
            button.hover()
            state = button.get_state()

            if self.__FORCE_RUN:
                return self.__NEXT_STATE

            if state != States.SAME:
                return state
        return States.SAME
