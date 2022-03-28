from typing import List, Tuple
from pygame import Rect, Surface, event
from Config.Folder import Folder
from Config.TelaJogo import TelaJogo
from Jogo.ControllerJogo import ControllerJogo
from Screen.Components.Buttons import Button, MenuButton, MusicImageButton, SaveButton
from Screen.Components.Text import Text
from Utils.Folder import import_single_sprite
from Config.Enums import States
from Screen.Views.AbstractView import AbstractView


class PauseView(AbstractView):
    __STATE = States.PLAYING
    folder = Folder()
    __IMAGE_PATH = folder.create_assets_path(['Telas'], 'FundoPause.jfif')
    __POS = (575, 375)
    __SIZE = (550, 450)
    __SIZE_SOM = (60, 60)
    __IMAGE_LOADED = False
    __IMAGE: Surface = None

    def __init__(self) -> None:
        rect = Rect(PauseView.__POS, PauseView.__SIZE)
        rect.center = rect.topleft
        position = rect.topleft
        self.__dao = ControllerJogo()
        self.__RUNNING = False
        super().__init__(PauseView.__STATE, position, PauseView.__SIZE)

        if not PauseView.__IMAGE_LOADED:
            PauseView.__IMAGE = import_single_sprite(PauseView.__IMAGE_PATH, self._views_size)
            PauseView.__IMAGE_LOADED = True

        self.__image = PauseView.__IMAGE
        self.__rect = self.__image.get_rect(topleft=self._position)

        self.__buttons: List[Button] = [
            MenuButton('CONTINUE', (575, 320), States.SAME),
            SaveButton('SAVE', (575, 390), States.SAME),
            MenuButton('LEAVE', (575, 460), States.RESET),
            MusicImageButton((760, 185), PauseView.__SIZE_SOM, (60, 60), States.SAME)
        ]
        self.__texts: List[Text] = []
        self.__temp_text: List[List[Text, int]] = []

    @property
    def image(self) -> Surface:
        return self.__image

    @property
    def rect(self) -> Rect:
        return self.__rect

    def desenhar(self, tela: TelaJogo) -> None:
        if not self.__RUNNING:
            self.__RUNNING = True
            save_name = self.__dao.current_game_save
            self.__texts.append(Text((575, 200), 30, f'Current Game: {save_name}'))

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

    def unpause(self) -> bool:
        continue_button = self.__buttons[0]
        if continue_button.clicked:
            return True
        else:
            return False

    def run(self, events: List[event.Event]) -> States:
        save_button = self.__buttons[1]
        if save_button.clicked:
            text = Text((575, 530), 25, 'Saving')
            self.__temp_text.append([text, 40])

        for button in self.__buttons:
            button.hover()
            button.run(events)

            next_state = button.get_state()
            if next_state != States.SAME:
                return next_state
        return States.SAME
